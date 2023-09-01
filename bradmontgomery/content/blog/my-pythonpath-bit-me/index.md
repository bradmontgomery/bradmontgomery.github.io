---
date: '2009-06-30T14:23:00+00:00'
title: My PYTHONPATH bit me.
draft: false
tags:
- Python
- django
- web
slug: my-pythonpath-bit-me
description: I'd just finished th...
markup: html
url: /blog/my-pythonpath-bit-me/
aliases:
- /blog/2009/06/30/my-pythonpath-bit-me/

---

I'd just finished the first version of a new django app (<em>myapp</em>), and so I pushed it out to my development server.  All the new code was in place, so I ran <em>python manage.py syncdb</em>.  The result?<br /><br /><pre><br />Traceback (most recent call last):<br />  File "manage.py", line 11, in &lt;module&gt;<br />    execute_manager(settings)<br />  File "/usr/local/lib/python2.6/site-packages/django/core/management/__init__.py", line 340, in execute_manager<br />    <br />  File "/usr/local/lib/python2.6/site-packages/django/core/management/__init__.py", line 295, in execute<br />    <br />  File "/usr/local/lib/python2.6/site-packages/django/core/management/base.py", line 192, in run_from_argv<br />  File "/usr/local/lib/python2.6/site-packages/django/core/management/base.py", line 210, in execute<br />  File "/usr/local/lib/python2.6/site-packages/django/utils/translation/__init__.py", line 73, in activate<br />    <br />  File "/usr/local/lib/python2.6/site-packages/django/utils/translation/__init__.py", line 43, in delayed_loader<br />    <br />  File "/usr/local/lib/python2.6/site-packages/django/utils/translation/trans_real.py", line 209, in activate<br />  File "/usr/local/lib/python2.6/site-packages/django/utils/translation/trans_real.py", line 198, in translation<br />  File "/usr/local/lib/python2.6/site-packages/django/utils/translation/trans_real.py", line 181, in _fetch<br />AttributeError: 'module' object has no attribute 'myapp'<br /></pre><br /><br /><strong>What!?</strong>  I had all the correct files in place, and <em>myapp</em> was listed in my settings' INSTALLED_APPS.  I was confused.    As it turns out, my PYTHONPATH pointed to my production code (which is actually on the same system, configured for a separate virtual host).  So no, it couldn't find my new app because my path said to look in my production code.... :(<br /><br />So, I just temporarily reset my PYTHONPATH, ran my <em>python manage.py syncdb</em>, and I'm rolling for now...<div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/4123748873183487963-3810087032644746773?l=bradmontgomery.blogspot.com' alt='' /></div>