---
date: '2013-03-07T19:39:54.168594+00:00'
title: Calculate a Week Range for a Date
draft: false
tags:
- date
- isocalendar
- python
- range
slug: calculate-week-range-date
description: <p>Math with dates a...
markup: html
url: /blog/calculate-week-range-date/
aliases:
- /blog/2013/03/07/calculate-week-range-date/

---

<p>Math with dates and date ranges is often <em>fun &amp; enlightening</em>! As
a testament to the fun of calculating dates (particularly ranges of dates), I
present the following:</p>

<p>Given a date, how would you find the range of dates that describe the week
during which your original date lies? In other words, assume today is <em>March
7, 2013</em> (and it is... for now anyway). Can you answer these two questions:

<ol>
<li>What was last Sunday's date?</li>
<li>What will be the date on Saturday?</li>
</ol>

<p><em>NOTE: I'm assuming weeks start on Sunday and end on Saturday. I'm in the
US and that's how people in my area typically define a "week".</em></p>

<p>Here's some Python code that calculates this. (also available at
<a href="https://gist.github.com/bradmontgomery/5110985">https://gist.github.com/bradmontgomery/5110985</a>)</p>

<pre class="python"><code>from datetime import timedelta

def week_range(date):
    """Find the first/last day of the week for the given day.
    Assuming weeks start on Sunday and end on Saturday.

    Returns a tuple of ``(start_date, end_date)``.

    """
    # isocalendar calculates the year, week of the year, and day of the week.
    # dow is Mon = 1, Sat = 6, Sun = 7
    year, week, dow = date.isocalendar()

    # Find the first day of the week.
    if dow == 7:
        # Since we want to start with Sunday, let's test for that condition.
        start_date = date
    else:
        # Otherwise, subtract `dow` number days to get the first day
        start_date = date - timedelta(dow)

    # Now, add 6 for the last day of the week (i.e., count up to Saturday)
    end_date = start_date + timedelta(6)

    return (start_date, end_date)</code></pre>

<p>Now, playing with this in a python shell...</p>
<pre class="python"><code>&gt;&gt;&gt; from datetime import datetime
&gt;&gt;&gt; d = datetime(2013, 3, 7)
&gt;&gt;&gt; week_range(d)
(datetime.datetime(2013, 3, 3, 0, 0),
 datetime.datetime(2013, 3, 9, 0, 0))</code></pre>

<p>This is also useful if you've got a Django site, and you want to find
the Users that joined during a certain week:</p>

<pre class="python"><code>&gt;&gt;&gt; from django.contrib.auth.models import User
&gt;&gt;&gt; d = datetime(2013, 3, 7)
&gt;&gt;&gt; week = week_range(d)
&gt;&gt;&gt; User.objects.filter(date_joined__range=week)
[&lt;User ...&gt;, ...]</code></pre>

<p>Cool, huh. Check out the docs for <a href="http://docs.python.org/2/library/datetime.html#timedelta-objects"><code>timedelta</code></a> and
<a href="http://docs.python.org/2/library/datetime.html#datetime.date.isocalendar"><code>isocalendar</code></a> for more information.</p>
