---
date: '2012-03-03T15:29:24+00:00'
title: Streaming Replication in PostgreSQL 9.1
draft: false
tags:
- database
- postgresql
slug: streaming-replication-in-postgresql-91
description: ''
markup: md
url: /blog/streaming-replication-in-postgresql-91/
aliases:
- /blog/2012/03/03/streaming-replication-in-postgresql-91/

---

Not long ago, I set up *synchronous*, streaming replication in PostgreSQL 9.1 in order to build a *Hot Standby* system. This is the story of that journey.


This post is mostly based on the [5-minute simple replication](http://wiki.postgresql.org/wiki/Binary_Replication_Tutorial#5_Minutes_to_Simple_Replication) tutorial from the PostgreSQL wiki, but with a few modifications and clarifications. There's also lots of good information in the [Streaming Replication wiki](http://wiki.postgresql.org/wiki/Streaming_Replication) from the PostgreSQL wiki.


For the remainder of this post, assume that you have a Master at 111.111.111.111 (host named `db0`) and a Standby at 222.222.222.222 (host named `db1`).


Configure the Master
--------------------


In `postgresql.conf`, you need to set the following:



```
listen_address = '*'
wal_level = hot_standby
max_wal_senders = 3
```

There is one caveat of running a hot standby system: if the standby crashes, the master will continue to wait for a response on every transaction. This is a Bad Thing. You should adequately monitor this so you know when it happens!


Now, in `pg_hba.conf`, you need to add this:



```
host replication all 222.222.222.222/32 trust
```

This gives your standby server permissions to connect to the master.


Configure the Standby
---------------------


Now, on the standby machine, edit `postgresql.conf` so that it includes:



```
hot_standby = on
```

Then, add a `recovery.conf` file. This ususally goes in PostgreSQL's data directory, which defaults to `/var/lib/postgresql/9.1/main` on Ubuntu. This file should contain:



```
standby_mode = 'on'
primary_conninfo = 'host=111.111.111.111 application_name=db1'
```

Data Transfer
-------------


Just to make sure the appropriate processes are running, verify that there's a `sender` process that will run on the master and a `receiver` process that will run on the standby. You can check for those with `ps -ef | grep sender` and `ps -ef | grep receiver`, respectively.


At this point, we've got to make sure the Standby contains an exact copy of the data from the Master. Shut down the PostgreSQL service on the master and standby (e.g. with a command such as `invoke-rc.d postgresql stop`). Then copy data files from the master to the standby. You must exclude any config files if you've put any there (we haven't in this tutorial) as well as the `pg_xlog` directory.:



```
rsync -av --exclude pg_xlog
    /var/lib/postgresql/9.1/main
    222.222.222.222:/var/lib/postgresql/9.1/main
```

Then, start the standby and the master (`invoke-rc.d postgresql start` on both systems).


Verify
------


Now it's time to test this setup. Log into the master (`ssh root@111.111.111.111`) and create a sample database:



```
$ su postgres
$ createdb sampledb
```

Now, access the postgresql command prompt:



```
$ psql -d sampledb
```

Create a simple table and populate it with some data:



```
CREATE table samples (
    id integer  PRIMARY KEY,
    name varchar(25),
    stuff text
);

INSERT into samples values (1, 'foo', 'lots of foo');
INSERT into samples values (2, 'bar', 'lots of bar');
INSERT into samples values (3, 'baz', 'lots of baz');
INSERT into samples values (4, 'bin', 'lots of bin');
```

Now, in another shell, log into your standby (`ssh root@222.222.222.222`), and fire up the `psql` prompt:



```
$ su postgres
$ psql -d sampledb

```

Look at a list of the tables:



```
sampledb=# \d
          List of relations
 Schema |  Name   | Type  |  Owner
--------+---------+-------+----------
 public | samples | table | postgres
(1 row)

```

Then query the `samples` table:



```
sampledb=# select * from samples;
 id | name |    stuff
----+------+-------------
  1 | foo  | lots of foo
  2 | bar  | lots of bar
  3 | baz  | lots of baz
  4 | bin  | lots of bin
(4 rows)

```

Now, try to insert some more data:



```
sampledb=# insert into samples values (5, 'asdf', 'more asdf');
ERROR:  cannot execute INSERT in a read-only transaction

```

Whoops! The standby server gives you *Read-Only* access to the data.


Checking the WAL Status
-----------------------


On the master, you can run the following command to see the current WAL write location:



```
SELECT pg_current_xlog_location();

```

Then on the standby, you can run:



```
SELECT pg_last_xlog_receive_location();

```

and:



```
SELECT pg_last_xlog_replay_location();

```

If you get the same values, then replication is up-to-date... otherwise there is some lag. We haven't set up synchronous replication, yet, so in a production environment (with a lot of data getting written to the database) it's possible the Standby would lag behind the master. If you *need* both systems to always be idendical, you can flip on *synchronous replication*.


Synchronous Replication
=======================


Enabling Synchronous Replaction just takes a couple of additional steps. Keep in mind though, that this *should only be done when there's little latency between the master and the standby*! That's because each query on the master will wait for a responce from the standby, which has to go over the network. I would only configure synchronous replication if both the master and standby are connected over a local (preferably private) network.


Ok, to make it happen, add the following to `postgresql.conf` on the Master:



```
synchronous_standby_names = 'db1'
```

Where the value here is a comma-separated list of your standby servers. You can have more than one, but only the first one will be used. If for some reason the first one dies, the second will become the standby.


Restart postgresql, then check out the status of your data synchronization (still on the master):



```
$ su posgresql
$ psql

```

Then run:



```
SELECT usename, application_name, client_addr, client_hostname, sync_state FROM pg_stat_replication;
```

You should see something like this:



```
usename   | application_name |  client_addr    | client_hostname | sync_state
----------+------------------+-----------------+-----------------+------------
 postgres | db1              | 222.222.222.222 |                 | sync

```

Now, just for fun, go back and insert a bunch of data in your master, then query on your standby machine. You should see the same results on both machines!


What Next?
==========


Now that you've got this set up, it's probably not a bad idea to read more about what's going on. The official PostgreSQL Docs make a good reference:


* [18.5. Write Ahead Log](http://www.postgresql.org/docs/9.1/interactive/runtime-config-wal.html)
* [18.6. Replication](http://www.postgresql.org/docs/9.1/interactive/runtime-config-replication.html)
* [25. High Availability, Load Balancing, and Replication](http://www.postgresql.org/docs/9.1/interactive/high-availability.html)
* Basically the whole [Server Administration Section](http://www.postgresql.org/docs/9.1/interactive/admin.html).


Enjoy!

