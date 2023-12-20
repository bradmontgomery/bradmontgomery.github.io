---
date: '2009-06-30T14:23:00+00:00'
title: My PYTHONPATH bit me.
draft: false
tags:
- Python
- django
- web
slug: my-pythonpath-bit-me
description: ''
markup: md
url: /blog/my-pythonpath-bit-me/
aliases:
- /blog/2009/06/30/my-pythonpath-bit-me/

---

I'd just finished the first version of a new django app (*myapp*), and so I pushed it out to my development server. All the new code was in place, so I ran *python manage.py syncdb*. The result?  
  

```
  
Traceback (most recent call last):  
  File "manage.py", line 11, in <module>  
    execute_manager(settings)  
  File "/usr/local/lib/python2.6/site-packages/django/core/management/__init__.py", line 340, in execute_manager  
      
  File "/usr/local/lib/python2.6/site-packages/django/core/management/__init__.py", line 295, in execute  
      
  File "/usr/local/lib/python2.6/site-packages/django/core/management/base.py", line 192, in run_from_argv  
  File "/usr/local/lib/python2.6/site-packages/django/core/management/base.py", line 210, in execute  
  File "/usr/local/lib/python2.6/site-packages/django/utils/translation/__init__.py", line 73, in activate  
      
  File "/usr/local/lib/python2.6/site-packages/django/utils/translation/__init__.py", line 43, in delayed_loader  
      
  File "/usr/local/lib/python2.6/site-packages/django/utils/translation/trans_real.py", line 209, in activate  
  File "/usr/local/lib/python2.6/site-packages/django/utils/translation/trans_real.py", line 198, in translation  
  File "/usr/local/lib/python2.6/site-packages/django/utils/translation/trans_real.py", line 181, in _fetch  
AttributeError: 'module' object has no attribute 'myapp'  

```
  
  
**What!?** I had all the correct files in place, and *myapp* was listed in my settings' INSTALLED\_APPS. I was confused. As it turns out, my PYTHONPATH pointed to my production code (which is actually on the same system, configured for a separate virtual host). So no, it couldn't find my new app because my path said to look in my production code.... :(  
  
So, I just temporarily reset my PYTHONPATH, ran my *python manage.py syncdb*, and I'm rolling for now...![](https://blogger.googleusercontent.com/tracker/4123748873183487963-3810087032644746773?l=bradmontgomery.blogspot.com)