---
date: '2007-01-05T21:13:00+00:00'
title: Migrating PHP scripts to MySQL from PostgreSQL
draft: false
tags:
- Programming
- mysql
- php
- postgresql
slug: migrating-php-scripts-to-mysql-from-postgresql
description: ''
markup: md
url: /blog/migrating-php-scripts-to-mysql-from-postgresql/
aliases:
- /blog/2007/01/05/migrating-php-scripts-to-mysql-from-postgresql/

---

I've recently had to work on a project where I needed toconvert some very basic [PHP](http://php.net) code thataccessed a [postgresql](http://www.postgresql.org/)database so that it would work with [mysql](http://mysql.com/). For the most part, this has beenfairly simple thanks to [rpl](http://freshmeat.net/projects/rpl/). Many of PHP'sdatabase functions have very similar names, so I simply use rpl toconvert the existing code. Here's a simple bashscript that I put together to convert some of my postgresqlfunctions to mysql:



```

#!/bin/bash
if [ ! -n "$1" ]
then
   echo "Usage: `basename $0` "
  exit 1;
fi

X=$1

echo "---- Relacing pg_ with mysql_ in $X"

rpl -R -x'.php' 'pg_pconnect' 'mysql_pconnect' $X
rpl -R -x'.php' 'pg_connect' 'mysql_connect' $X
rpl -R -x'.php' 'pg_query' 'mysql_query' $X
rpl -R -x'.php' 'pg_fetch_row' 'mysq_fetch_row' $X
rpl -R -x'.php' 'pg_fetch_assoc' 'mysq_fetch_assoc' $X
rpl -R -x'.php' 'pg_close' 'mysq_close' $X
rpl -R -x'.php' 'pg_num_rows' 'mysq_num_rows' $X
rpl -R -x'.php' 'pg_numrows' 'mysq_num_rows' $X
rpl -R -x'.php' 'pg_last_error' 'mysql_error' $X

```

Just in case your curious about converting from postgresql or
mysql to sqlite, I've compiled the following table 
of analogous functions from [php.net](http://php.net):



| PostgreSQL | MySQL | SQLite |
| --- | --- | --- |
| pg\_connect | mysql\_connect | sqlite\_open // open or create database |
| pg\_query | mysql\_query | sqlite\_query |
| pg\_fetch\_row | mysql\_fetch\_row | sqlite\_fetch\_array (ordinal and associative) |
| pg\_fetch\_assoc | mysql\_fetch\_assoc |
| pg\_close | mysql\_close | sqlite\_close |
| pg\_num\_rows or pg\_numrows | mysql\_num\_rows | sqlite\_num\_rows |

  


