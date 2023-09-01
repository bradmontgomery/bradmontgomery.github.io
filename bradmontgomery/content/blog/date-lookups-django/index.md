---
date: '2015-10-10T19:27:40.047401+00:00'
title: Date lookups in Django
draft: false
tags:
- database
- django
- lookups
- orm
- postgres
- python
slug: date-lookups-django
description: <p>A while ago I <a ...
markup: html
url: /blog/date-lookups-django/
aliases:
- /blog/2015/10/10/date-lookups-django/

---

<p>A while ago I <a href="https://twitter.com/bkmontgomery/status/615665645594632192">tweeted</a>
out something that I've wanted to see in Django for a very long time, yet have
never really taken the time to investigate or implement it:</p>

<blockquote class="twitter-tweet" lang="en"><p lang="en" dir="ltr">I wish <a href="https://twitter.com/hashtag/django?src=hash">#django</a> had this: &#10;&#10;M.objects.filter(datetimefield__date=<a href="http://t.co/MVFXsN4Ivk">http://t.co/MVFXsN4Ivk</a>(2015, 6, 29))&#10;&#10;Has that ever been attempted?</p>&mdash; Brad Montgomery (@bkmontgomery) <a href="https://twitter.com/bkmontgomery/status/615665645594632192">June 29, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>


<p>Django's ORM has a <a href="https://docs.djangoproject.com/en/1.8/topics/db/queries/#field-lookups">
very rich set of field lookups</a>, but at present, it doesn't support an exact
date lookup. At least not with the syntax I would expect. Luckily, that tweet
got some very handy responses, so let's do a bit of exploring.</p>


<p>Assume we have the following model. For the now, the only field we care about
is the <code>created</code> field.</p>

<pre><code class="python">from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)</code></pre>


<p>Again, what I <em>wish</em> we could do is an exact date lookup using a
<code>__date</code> lookup. If you try that:</p>

<pre><code class="python">from datetime import date
Item.objects.filter(created__date=date(2015, 10, 1))</code></pre>

<p>Well, you get an exception.</p>
<pre>FieldError: Unsupported lookup 'date' for AutoCreatedField or join on the field not permitted.</pre>

<p>Fear not, there are a handful of ways to acheive the same results. One way
is to use the date-based lookups that django already provides. Such as
<code>__day</code>, <code>__month</code>, and <code>__year</code>. </p>

<pre><code class="python">dt = date(2015, 10, 1)
Item.objects.filter(
    created__day=dt.day, 
    created__month=dt.month, 
    created__year=dt.year
)</code></pre>

<p>That's a technique I've used quite a lot in the past. It's fairly verbose,
yet it's pretty readable. Another technique is to use the <code>__range</code>
lookup. You can use a datetime object's
<a href="https://docs.python.org/3.4/library/datetime.html#datetime.date.replace">replace method</a>
to set minimum and maximum values for the time-related attributes (and the
<a href="https://docs.python.org/3.4/library/datetime.html#datetime-objects">docs for datetime objects</a>
list these values).</p>

<pre><code class="python"># Create a datetime object spanning a full day
dt = datetime.now()
start = dt.replace(hour=0, minute=0, second=0, microsecond=0)
end = dt.replace(hour=23, minute=59, second=59, microsecond=999999)

# Query for objects that fall within that day.
Item.objects.filter(created__range=(start, end))</code></pre>


<p>One neat suggestion came from <a href="https://twitter.com/jasonamyers">Jason Myers</a>
notes that you can use the <code>__contains</code> lookup with dates:</p>

<pre><code class="python">Item.objects.filter(created__contains=date(2015, 10, 1))</code></pre>


<p>Another from <a href="https://twitter.com/joshourisman">Josh Ourisman</a> takes
advantage of the fact that dates are really just strings (at least in postgres):</p>

<pre><code class="python">Item.objects.filter(created__startswith='2015-10-01')</code></pre>

<p><a href="https://twitter.com/j00bar">Joshua Ginsberg</a> suggested using a
custom database function prior to filtering. So, in the spirit of learning new
things available in Django 1.8, I did just that. With a
<a href="https://docs.djangoproject.com/en/1.8/ref/models/expressions/#func-expressions">
Func() expression</a>.</p>


<p>In PostgreSQL, you could run the following query to view the date store
on an Item:</p>

<pre><code class="sql">select created from items limit 1;
&gt;  2015-10-01 12:37:23.620442+00</code></pre>

<p>It turns out, PostgreSQL has a handy
<a href="http://www.postgresql.org/docs/9.4/static/functions-datetime.html)">
<code>date</code> function</a> that gives us just the date part of a datetime string.</p>

<pre><code class="sql">select date(created) from items limit 1;
&gt;  2015-10-01</code></pre>

<p><code>Func()</code> expressions (using in conjunction with <code>F()</code>
expressions and the <code>aggregate</code> method will let us call postgres's
date function from python!</p>

<pre><code class="python">from django.db.models import Func, F

# Note, this is PostgreSQL-specific.
# Build a queryset annotated with the date portion of the `created` datetime.
queryset = Item.objects.annotate(
  created_date=Func(F('created'), function='DATE')
)

# Now, we can query agains that annotation:
items = queryset.filter(created_date=date(2015, 10, 1))  # What we want!

</code></pre>

<p>Pretty Cool!</p>

<p>So there you have a number of ways to do date-based lookups in Django. These
will probably get you where you want to go most of the time.</p>

<p><strong>But wait! There's more!</strong> It turns out, you can build your
own lookups. The <a href="https://docs.djangoproject.com/en/1.8/ref/models/lookups/">Lookup API reference</a>
was introduced in Django 1.7, yet I've not dabbled with it. Stay Tuned, because
in my next post, I'll see just how hard it is to implement that <code>__date</code>
lookup (if nothing else gets in my way over the next few days).</p>
