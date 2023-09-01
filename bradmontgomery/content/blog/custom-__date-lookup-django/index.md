---
date: '2015-10-18T20:40:37.236361+00:00'
title: A custom __date lookup for Django
draft: false
tags:
- database
- django
- lookups
- orm
- postgres
- python
slug: custom-__date-lookup-django
description: <p class="callout wa...
markup: html
url: /blog/custom-__date-lookup-django/
aliases:
- /blog/2015/10/18/custom-__date-lookup-django/

---

<p class="callout warning">
&#9888; Django 1.9 now includes a <a href="https://docs.djangoproject.com/en/1.9/ref/models/querysets/#date">built-in __date lookup</a>. If possible, you should use that instead of the code below, which doesn't support timezones.
</p>

<p>In my post <a href="/blog/date-lookups-django/">last week on date lookups</a>,
I ended with a promise to take a look at building a
<a href="https://docs.djangoproject.com/en/1.8/howto/custom-lookups/">custom
django lookup</a> (namely, a <code>__date</code> lookup). Django includes
a basic <code>Lookup</code> class, and to build your own lookup expressions,
all you really need to do is:

<ol>
<li>Subclass <code>django.db.models.Lookup</code></li>
<li>define a <code>lookup_name</code> attribute</li>
<li>write the <code>as_sql</code> method to define how your database should
handle building the query</li>
</ol>

<p>As promised, here's a quick example. Assume we have the following model (silly,
but simple) model. For illustration purposes, it has both a <code>DateField</code>
and a <code>DateTimeField</code>. We'll build our lookup, so that it works with
both fields.</p>

<pre><code class="python">from django.db import models

class Meeting(models.Model):
    date = models.DateField()
    scheduled = models.DateTimeField()</code></pre>

<p><strong>Step 1:</strong> Let's build the lookup, which I'm going to
creatively name, <code>DateLookup</code>.

<pre><code class="python">from django.db.models import Lookup

class DateLookup(Lookup):
    """A custom lookup, that lets you query DateField and DateTimeFields by a date"""

    lookup_name = 'date'  # This enables us to use __date='2015-10-18' in a query

    def as_sql(self, compiler, connection):
        # The left-hand-side (lhs) in the query's WHERE clause. It consists
        # of your app name and field name. e.g. '"myapp"."scheduled"'
        # In this case, the left-hand-side has no params.
        lhs, lhs_params = self.process_lhs(compiler, connection)

        # The right-hand-side (rhs) + its params will define the input used
        # in the query's WHERE clause. At this point, the rhs_params will
        # be a datetime object, e.g.: datetime(2015, 10, 18, 0, 0, tzinfo=<UTC>)
        rhs, rhs_params = self.process_rhs(compiler, connection)

        # Both PostgreSQL and MySQL have a DATE function that lets us query
        # by date. The where clause in the generated SQL will look something
        # like, WHERE DATE(scheduled) = '2015-10-18'
        params = lhs_params + rhs_params
        return 'DATE(%s) = %s' % (lhs, rhs), params</code></pre>


<p><strong>Step 2:</strong> Register it with the appropriate model field(s).
In this case, both the <code>DateField</code> and <code>DateTimeField</code>.</p>

<p>The Django docs include an important note about registering custom lookups:</p>

<pre><code class="python">from django.db.models.fields import DateField, DateTimeField

DateField.register_lookup(DateLookup)
DateTimeField.register_lookup(DateLookup)</code></pre>

<blockquote>
You will need to ensure that this registration happens before you try to
create any querysets using it. You could place the implementation in a
models.py file, or register the lookup in the ready() method of an AppConfig.
</blockquote>

<p>Now, open a django shell, and you can run a query like the following, which
queries against a date field. This should give you all the Meetings where
<code>date = datetime.date(2015, 10, 18)</code>:</p>
<pre><code class="python">Meeting.objects.filter(date__date='2015-10-18')</code></pre>
<p>Or, you can do the following, which queries agains a datetime field, which
should give you all the meetings where the <code>scheduled</code> column
includes 2015-10-18.</p>
<pre><code class="python">Meeting.objects.filter(scheduled__date='2015-10-18')</code></pre>

<p>There's more to custom lookups in Django, and I highly recommend reading
through the <a href="https://docs.djangoproject.com/en/1.8/howto/custom-lookups/">
custom lookups documentation</a> because it also includes a really great
example, as well.</p>

<p><em>Note: All the code in this post was written using Python 3.4 and Django 1.8.</em></p>