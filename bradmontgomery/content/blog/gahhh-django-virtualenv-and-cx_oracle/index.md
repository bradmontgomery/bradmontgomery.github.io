---
date: '2009-11-24T13:47:00+00:00'
title: Gahhh!! Django, virtualenv, and cx_Oracle
draft: false
tags:
- apache
- cx_oracle
- django
- virtualenv
slug: gahhh-django-virtualenv-and-cx_oracle
description: ''
markup: md
url: /blog/gahhh-django-virtualenv-and-cx_oracle/
aliases:
- /blog/2009/11/24/gahhh-django-virtualenv-and-cx_oracle/

---

UPDATE: Thanks in advance to the comments from [Graham Dumpleton](http://blog.dscpl.com.au/) whose comments below pointed me in the right direction!  
  
This was~~is~~ a plea for help.  
  
I've got django installed and configured with apache and virtualenv. I also have one particular app (named **myapp**) that queries an Oracle database directly (django is configured to use MySQL). All of the apps work, **except** for anything thatbrequires the **myapp** app... which includes the admin!  
  
Requesting any view that uses cx\_Oracle results in a cryptic error simiar to:  
  
**ViewDoesNotExist at /some/url/**  
*Could not import myproject.myapp.views. Error was: libclntsh.so.10.1: cannot open shared object file: No such file or directory*  
  
The full traceback follows:
```
Environment:  
  
Request Method: GET  
Request URL: http://mydomain.com/myapp/foo/  
Django Version: 1.1.1  
Python Version: 2.6.2  
Installed Applications:  
['django.contrib.auth',  
 'django.contrib.contenttypes',  
 'django.contrib.sessions',  
 'django.contrib.sites',  
 'django.contrib.admin',  
 'django.contrib.admindocs',  
 'django.contrib.flatpages',  
 'django_extensions',  
 'myproject.userprofile',  
 **'myproject.myapp',**  
  
 ... *snip*...  
  
 'myproject.utils']  
Installed Middleware:  
('django.middleware.gzip.GZipMiddleware',  
 'django.middleware.common.CommonMiddleware',  
 'django.contrib.sessions.middleware.SessionMiddleware',  
 'django.contrib.auth.middleware.AuthenticationMiddleware',  
 'django.middleware.doc.XViewMiddleware')  
  
  
Traceback:  
File "/home/django/.virtualenvs/myproject/lib/python2.6/site-packages/django/core/handlers/base.py" in get_response  
  83.                     request.path_info)  
File "/home/django/.virtualenvs/myproject/lib/python2.6/site-packages/django/core/urlresolvers.py" in resolve  
  218.                     sub_match = pattern.resolve(new_path)  
File "/home/django/.virtualenvs/myproject/lib/python2.6/site-packages/django/core/urlresolvers.py" in resolve  
  218.                     sub_match = pattern.resolve(new_path)  
File "/home/django/.virtualenvs/myproject/lib/python2.6/site-packages/django/core/urlresolvers.py" in resolve  
  125.             return self.callback, args, kwargs  
File "/home/django/.virtualenvs/myproject/lib/python2.6/site-packages/django/core/urlresolvers.py" in _get_callback  
  134.             raise ViewDoesNotExist, "Could not import %s. Error was: %s" % (mod_name, str(e))  
  
Exception Type: ViewDoesNotExist at /myapp/foo/  
Exception Value: Could not import myproject.myapp.views. Error was: libclntsh.so.10.1: cannot open shared object file: No such file or directory
```
  
  
The strange thing is that tests using cx\_Oracle run correctly (as does code typed into the interpreter via ./manage.py shell), so cx\_Oracle is installed correctly in the virtualenv. Orignally, I thought that apache was somehow misconfigured. The problem, however, is that Apache just doesn't know where to find the shared libraries for cx\_Oracle's C extension modules. On my system (Ubuntu), shared libraries are located in /usr/lib and /usr/local/lib .  
  
When building cx\_Oracle, you must include an environment variable for ORACLE\_HOME and update the LD\_LIBRARY\_PATH so that it also includes ORACLE\_HOME. While logged in as the *django* user, I updated .bashrc so that it includes the following:  

```
export ORACLE\_HOME=/home/django/oracle/instantclient_10_2  
export LD\_LIBRARY\_PATH=$ORACLE\_HOME:$LD_LIBRARY_PATH  

```
  
For me, all of the cx\_Oracle shared libraries are located in **/home/django/oracle/instantclient\_10\_2**. So, (with my virtualenv activated) I built, installed, and tested cx\_Oracle, and everything worked fine, because my user environment was set up so that these shared libraries are available.  
  
To make these available to Apache, I created **hard** links to all of the shared libraries from /usr/local/lib, and then ran ldconfig. Note that ldconfig ignores symbolic links!  

```
cd /usr/local/lib  
sudo ln /home/django/oracle/instantclient_10_2/libclntsh.so.10.1  
# also creating links to all other libs  
sudo ldconfig  

```
  
  
After restarting Apache, my django apps worked as expected. For the curious, my wsgi script and apache config follows.  
  
**My .wsgi script**  

```
import sys  
import site  
import os  
  
vepath = '/home/django/.virtualenvs/myproject/lib/python2.6/site-packages'  
prev_sys_path = list(sys.path)  
  
# add the site-packages of our virtualenv as a site dir  
site.addsitedir(vepath)  
  
# add the app's directory to the PYTHONPATH  
sys.path.append('/home/django/django\_projects/myproject\_root/myproject/')  
sys.path.append('/home/django/django\_projects/myproject\_root/')  
os.environ['PYTHON\_EGG\_CACHE'] = '/home/django/.python-eggs'  
  
new_sys_path = [p for p in sys.path if p not in prev_sys_path]  
for item in new_sys_path:   
    sys.path.remove(item)  
sys.path[:0] = new_sys_path  
  
from django.core.handlers.wsgi import WSGIHandler  
os.environ['DJANGO\_SETTINGS\_MODULE'] = 'myproject.settings'  
application = WSGIHandler()  

```
  
  
  
**The Pertinent part of the Apache Config, located within a VirtualHost Directive:**  

```
Alias /media/ /var/www/media/  
Alias /site\_media/ /var/www/static/  
  
# Run WSGI in Daemon Mode:  
WSGIDaemonProcess myproject user=www-data group=www-data threads=25  
WSGIProcessGroup myproject  
WSGIScriptAlias / /home/django/django\_projects/myproject\_root/apache\_mod\_wsgi\_conf/myproject.wsgi  

```
  
  
NOTE: Graham Dumpleton suggests four options to get around the original problem (and I paraphrase):  
1. *Rebuild cx\_Oracle setting the LD\_RUN\_PATH* - I tried this, but was unnsuccessful.
  
3. *Put the shared libraries in /usr/lib* - I hard linked to the libraries from /usr/local/lib. This is the solution that worked.
  
5. *Modify /etc/ld.conf so that it includes the path to the shared libraries* - I considered adding a file to /etc/ld.so.conf.d/ which would have included the path to my ORACLE\_HOME directory. However, the above options worked, so I went with that instead.
  
7. *Edit /etc/apache/envvars so that it includes the appropriate environment variables* - I also tried this approach, including the same environment variables that I added to my .bashrc, but this also did not work

  
  
Hope this helps someone else!![](https://blogger.googleusercontent.com/tracker/4123748873183487963-6881096023935249692?l=bradmontgomery.blogspot.com)