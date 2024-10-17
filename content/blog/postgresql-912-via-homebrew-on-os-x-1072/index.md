---
date: '2011-12-22T06:20:39+00:00'
title: PostgreSQL 9.1.2 via homebrew on OS X 10.7.2
draft: false
tags:
- django
- homebrew
- osx
- postgresql
- python
slug: postgresql-912-via-homebrew-on-os-x-1072
description: ''
markup: md
url: /blog/postgresql-912-via-homebrew-on-os-x-1072/
aliases:
- /blog/2011/12/22/postgresql-912-via-homebrew-on-os-x-1072/

---

I just picked up a snazzy new Macbook Air, and I'm working on setting up my development 
 environment(s). For the most part this has been fairly easy. I pull in my repos from 
 [github](https://github.com/bradmontgomery) and [bitbucket](https://bitbucket.org/bkmontgomery), 
 and I use [virtualenv](http://pypi.python.org/pypi/virtualenv) and [pip](http://www.pip-installer.org/)
 to organize all my python packages (mostly installing from 
 [requirements files](http://www.pip-installer.org/en/latest/requirements.html)). Most of the other 
 command-line tools get intalled with [homebrew](http://mxcl.github.com/homebrew/), and this time around I 
 decided to install PostgreSQL with homebrew.


I didn't keep track of all the steps I followed, but I'm pretty sure I just kept all the defaults 
 while installing. I set up a new database cluster with `initdb` and then I created a 
 local user (no password) and set up a database for one of my Django apps. But then I got this 
 error when running syncdb:



```
OperationalError: could not connect to server: Permission denied
    Is the server running locally and accepting
    connections on Unix domain socket "/var/pgsql_socket/.s.PGSQL.5432"?

```

That's odd. I did some digging and didn't really find much info that seem relevant 
 (though there is this ticket: <https://trac.macports.org/ticket/30125>).
 However, when I explicitly specified a `HOST` value in my django settings, things just started working.



```
DATABASES = { 
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'somedb',  
        'USER': 'someuser', 
        'PASSWORD': '', 
        'HOST': 'localhost',
        'PORT': '', 
    }   
}

```

I'm not quite sure what's going on here, or if this is a bug in PostgreSQL. Other than that little 
 snag, everything seems to be working swell.


Apparently reinstalling `psycopg2` also fixes this problem:


```
pip install -U psycopg2
```

Thanks to [@lukeman](https://twitter.com/lukeman) for the tip, and to [@dstufft](https://twitter.com/dstufft) who helped him!  
  
:)

