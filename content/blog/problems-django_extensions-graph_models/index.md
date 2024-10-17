---
date: '2013-11-15T20:14:01.470801+00:00'
title: problems with django_extension's graph_models?
draft: false
tags:
- django
- django_extensions
- python
slug: problems-django_extensions-graph_models
description: ''
markup: md
url: /blog/problems-django_extensions-graph_models/
aliases:
- /blog/2013/11/15/problems-django_extensions-graph_models/

---

I recently ran into an issue when trying to generate an image of my project's models using [`django_extension`](https://github.com/django-extensions/django-extensions)'s `graph_models` command. Unfortunately, googling for the error didn't turn up any solutions, so I'm dumping some info here (just in case!).


some background
---------------


For the record, I was using django\_extensions, version 1.2.5 (the latest release as of this post), and Django 1.4.2 (yeah... it's old)


Running the following command:


```
$ ./manage.py graph_models my_app > my_models.dot
```

Gave me the following error


```
Traceback (most recent call last):
  File "./manage.py", line 10, in 
 execute\_from\_command\_line(sys.argv)
 File "/home/vagrant/.virtualenvs/my\_app/local/lib/python2.7/site-packages/django/core/management/\_\_init\_\_.py", line 443, in execute\_from\_command\_line
 utility.execute()
 File "/home/vagrant/.virtualenvs/my\_app/local/lib/python2.7/site-packages/django/core/management/\_\_init\_\_.py", line 382, in execute
 self.fetch\_command(subcommand).run\_from\_argv(self.argv)
 File "/home/vagrant/.virtualenvs/my\_app/local/lib/python2.7/site-packages/django/core/management/base.py", line 196, in run\_from\_argv
 self.execute(\*args, \*\*options.\_\_dict\_\_)
 File "/home/vagrant/.virtualenvs/my\_app/local/lib/python2.7/site-packages/django/core/management/base.py", line 232, in execute
 output = self.handle(\*args, \*\*options)
 File "/home/vagrant/.virtualenvs/my\_app/local/lib/python2.7/site-packages/django\_extensions/management/commands/graph\_models.py", line 72, in handle
 dotdata = generate\_dot(args, cli\_options=cli\_options, \*\*options)
 File "/home/vagrant/.virtualenvs/my\_app/local/lib/python2.7/site-packages/django\_extensions/management/modelviz.py", line 168, in generate\_dot
 if field == pk:
 File "/home/vagrant/.virtualenvs/my\_app/local/lib/python2.7/site-packages/django/db/models/fields/\_\_init\_\_.py", line 128, in \_\_cmp\_\_
 return cmp(self.creation\_counter, other.creation\_counter)
AttributeError: 'NoneType' object has no attribute 'creation\_counter'
```

The problem?
------------


I'm not entirely sure, but [it seems related to this issue](https://github.com/django-extensions/django-extensions/issues/402).


The solution
------------

*Rather, the solution that worked for me* (YMMV): Uninstall your current version:



```
pip uninstall django-extensions
```

Then install the current development version from github:



```
pip install -e git+https://github.com/django-extensions/django-extensions.git#egg=django_extensions
```

Hope that helps someone else!

