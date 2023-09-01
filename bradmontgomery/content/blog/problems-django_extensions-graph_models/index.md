---
date: '2013-11-15T20:14:01.470801+00:00'
title: problems with django_extension's graph_models?
draft: false
tags:
- django
- django_extensions
- python
slug: problems-django_extensions-graph_models
description: <p>I recently ran in...
markup: html
url: /blog/problems-django_extensions-graph_models/
aliases:
- /blog/2013/11/15/problems-django_extensions-graph_models/

---

<p>I recently ran into an issue when trying to generate an image of my project's models using <a href="https://github.com/django-extensions/django-extensions"><code>django_extension</code></a>'s <code>graph_models</code> command. Unfortunately,  googling for the error didn't turn up any solutions, so I'm dumping some info here (just in case!).</p>

<h2>some background</h2>
<p>For the record, I was using django_extensions, version 1.2.5 (the latest release as of this post), and Django 1.4.2 (yeah... it's old)</p>

<p>Running the following command:</p><pre>$ ./manage.py graph_models my_app &gt; my_models.dot</pre>

<p>Gave me the following error</p><pre><code>Traceback (most recent call last):
  File "./manage.py", line 10, in <module>
    execute_from_command_line(sys.argv)
  File "/home/vagrant/.virtualenvs/my_app/local/lib/python2.7/site-packages/django/core/management/__init__.py", line 443, in execute_from_command_line
    utility.execute()
  File "/home/vagrant/.virtualenvs/my_app/local/lib/python2.7/site-packages/django/core/management/__init__.py", line 382, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/home/vagrant/.virtualenvs/my_app/local/lib/python2.7/site-packages/django/core/management/base.py", line 196, in run_from_argv
    self.execute(*args, **options.__dict__)
  File "/home/vagrant/.virtualenvs/my_app/local/lib/python2.7/site-packages/django/core/management/base.py", line 232, in execute
    output = self.handle(*args, **options)
  File "/home/vagrant/.virtualenvs/my_app/local/lib/python2.7/site-packages/django_extensions/management/commands/graph_models.py", line 72, in handle
    dotdata = generate_dot(args, cli_options=cli_options, **options)
  File "/home/vagrant/.virtualenvs/my_app/local/lib/python2.7/site-packages/django_extensions/management/modelviz.py", line 168, in generate_dot
    if field == pk:
  File "/home/vagrant/.virtualenvs/my_app/local/lib/python2.7/site-packages/django/db/models/fields/__init__.py", line 128, in __cmp__
    return cmp(self.creation_counter, other.creation_counter)
AttributeError: 'NoneType' object has no attribute 'creation_counter'</code></pre>

<h2>The problem?</h2>
<p>I'm not entirely sure, but <a href="https://github.com/django-extensions/django-extensions/issues/402">it seems related to this issue</a>.</p>

<h2>The solution</h2><p><em>Rather, the solution that worked for me</em> (YMMV): Uninstall your current version:</p>
<pre>pip uninstall django-extensions</pre>

<p>Then install the current development version from github:</p>
<pre>pip install -e git+https://github.com/django-extensions/django-extensions.git#egg=django_extensions</pre>

<p>Hope that helps someone else!</p>