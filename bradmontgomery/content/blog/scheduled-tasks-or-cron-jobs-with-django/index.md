---
date: '2009-02-20T10:15:00+00:00'
title: Scheduled Tasks (or cron jobs) with Django
draft: false
tags:
- Python
- cron
- django
- web
slug: scheduled-tasks-or-cron-jobs-with-django
description: ''
markup: md
url: /blog/scheduled-tasks-or-cron-jobs-with-django/
aliases:
- /blog/2009/02/20/scheduled-tasks-or-cron-jobs-with-django/

---

This is my take on setting up cron jobs for the apps in a Django project. It is based on my own convention, and it solves my initial problems where I want to perform some action on all of my Django apps at a periodic interval (currently this is a once-a-day task).  
  
In order for this to work, I create a *cron.py* module for all of my INSTALLED\_APPS. This module **must** contain a *run* method. Other than that, it can work just like any other python module (using django's internals as necessary).  
  
For example, if you had an app called utils (possibly located at mysite/utils/), and if you just wanted to delete all sessions with old expire\_dates, your *cron.py* (which you would put in mysite/utils/cron.py) might look something like this:  

```
from datetime import datetime  
from django.contrib.sessions.models import Session  
  
def delete\_old\_sessions():  
    Session.objects.filter(expire_date__lt=datetime.now()).delete()  
  
def run():  
    delete_old_sessions()  

```
  
Now, the meat of this solution checks for the cron.py module in all of the apps in mysite.settings.INSTALLED\_APPS, and invokes its run() method. I've also named this module *cron.py*, but this gets stored in Django's project directory (e.g. mysite)... the same directory where your *settings.py* is located.  

```
#!/usr/bin/env python  
"""  
Project-wide Cron Job... A Command-line Django Script.  
  
This script gets scheduled and run by cron (or whatever).  
It then calls the `run` method of each app's cron module,   
if it exists (should be `appname/cron.py`)  
  
This script should be invoked after setting the   
DJANGO\_SETTINGS\_MODULE environment variable.  
  
You chould do this in a BASH script as follows:  
 export DJANGO\_SETTINGS\_MODULE=mysite.settings  
 python /path/to/mysite/cron.py  
"""  
from django.conf import settings  
  
def my\_import(name):  
    '''  
 \_\_import\_\_ helper function to import modules inside packages  
 e.g.: where name is something like 'package.module.mod\_i\_want',  
 would return mod\_i\_want  
   
 See: http://www.python.org/doc/2.5.2/lib/built-in-funcs.html  
 '''  
    mod = \_\_import\_\_(name)  
    components = name.split('.')  
    for comp in components[1:]:  
        mod = getattr(mod, comp)  
    return mod  
  
def run():  
    for app in settings.INSTALLED_APPS:  
        if not app.startswith('django'):  
            output_info = '%s.cron'%app  
            ## Dynamically import a module called 'cron'  
            ## from each INSTALLED\_APP (if it exists)  
            try:  
                cron_mod = my_import(app+'.cron')  
                output_info += '... FOUND'  
                print output_info  
                ## 3. Execute the cron's run method (if it exists)  
                if hasattr(cron_mod, 'run'):  
                    #print '---> calling run()'  
                    cron_mod.run()  
            except ImportError:  
                # ignore packages that don't have a cron module  
                output_info += '... SKIPPED'  
                print output_info  
  
if __name__ == "\_\_main\_\_":  
    run()  

```
  
  
The final piece of this puzzle lies in the BASH script used to invoke the above python module. It makes sure the appropriate environment variables are set and then it invokes the above module. I also store this in my django project directory (as cron.sh), and I use cron to schedule it to run.  

```
#!/bin/bash  
# This is a Django, Project-specific Cron script.  
# Separate Projects would need a copy of this script   
# with appropriate Settings export statments.  
  
PYTHONPATH="${PYTHONPATH}:/path/to/django/project/directory"  
export PYTHONPATH  
export DJANGO\_SETTINGS\_MODULE=mysite.settings  
  
python/path/to/django/project/directory/mysite/cron.py  

```
  
  
Using cron, you'd schudule this to run every morning at 6am by editing your crontab and adding the following:  

```
#m h dom mon dow command  
  0   6    *        *      *     /path/to/django/project/directory/cron.sh  

```
  
  
That's it. This has been working for me, but there is at least one major pitfall: All of your app's cron tasks get run at the same time. This works well if your apps need to do something once a day (which has been my requirement), but this probably won't work well if you have some apps that need to run tasks at differing times.  
  
There are also other solutions to this (none of which I've tried). There's a snippet at <http://www.djangosnippets.org/snippets/1126/> which looks interesting. Then there's the [django-cron](http://code.google.com/p/django-cron/) app which seems to be fairly flexible in how it works, and it doesn't require cron (so this is a plus if you cant set a crontab or if you're on Windows!)  
  
Thanks in advance for any feedback... suggestions are always welcome!![](https://blogger.googleusercontent.com/tracker/4123748873183487963-7714347806734835776?l=bradmontgomery.blogspot.com)