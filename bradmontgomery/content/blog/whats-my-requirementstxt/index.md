---
date: '2017-05-14T16:19:03.519517+00:00'
title: What's in my requirements.txt
draft: false
tags:
- programming
- python
- unix
slug: whats-my-requirementstxt
description: It's Sunday, and tom...
markup: md
url: /blog/whats-my-requirementstxt/
aliases:
- /blog/2017/05/14/whats-my-requirementstxt/

---

It's Sunday, and tomorrow is our scheduled [monthly python meetup in Memphis](http://www.mempy.org/), and it's one of those month's where I've been busy and I haven't done a good job of finding a speaker.  So, that mean's I've got to pull something together at the last minute. While racking my brain for a quick-and-easy topic, I thought, "I wonder what python packages I'm using most?"

So, I ran this nifty monstrosity of a command, and here's the results. I also tweeted it out:

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">find . -name &quot;requirements*txt&quot; -exec cat {} \; | awk -F &quot;==&quot; &#39;{ print $1 }&#39; | sort | uniq -c | sort -rn | head -n 20</p>&mdash; Brad Montgomery (@bkmontgomery) <a href="https://twitter.com/bkmontgomery/status/863777050594869248">May 14, 2017</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<pre><code>$ find . -name "requirements*txt" -exec cat {} \; | awk -F "==" '{ print $1 }' | \
 sort | uniq -c | sort -rn | head -n 20
  23 ipython
  17 Django
  15 psycopg2
  11 requests
  11 pytz
  11 gunicorn
   9 ipdb
   9 django-extensions
   9 django-debug-toolbar
   8 six
   8 python-dateutil
   8 Pygments
   8 Jinja2
   7 tablib
   7 pandas
   7 docker-py
   7 Pillow
   7 MarkupSafe
   7 Flask
   7</code></pre>

It's really not that surprising, since I do a lot of work with Django, and I use a fair number of the same dependencies everywhere. If course, this is only for projects that I still have in my home directly, which is a fair representation of the last couple year's worth of work.

Let's break that command down a little, though:

## find

I'll admit that I always forget how find works. Luckily [this developerworks article is really good](https://www.ibm.com/developerworks/aix/library/au-unix-find.html). I should probably book mark that.

I wanted to find all my `requirements.txt` files, even those that I may have named `requirements_dev.txt` or `requirements_prod.txt`. Usually all my projects _just_ have a `requirements.txt`. This command will cat any matchign files.

    find . -name "requirements*txt" -exec cat {} \; 

## awk

I then pipe that result into awk. I'm 99% sure most of my requirements files pin versions exectly, so the following awk command will take something like `Django==1.9.1` and keep the `Django` part.

    awk -F "==" '{ print $1 }'

## sort & uniq

Then, sort the results, use `uniq -c` to count them, then sort again numerically (`-n`) in reverse order (`-r`):

    sort | uniq -c | sort -rn


## head

... and keep the top 20 results.

    head -n

Apparently I also just have  blank line in many of my requirements file.  ¯\_(ツ)_/¯

Anyway, hope you've enjoyed this little snippet. Run it on your projects and see what you get!

----

**Update:** [@jackdied](https://twitter.com/jackdied) says you should use tail!

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr"><a href="https://twitter.com/bkmontgomery">@bkmontgomery</a> Drop the reverse on the sort and use tail!</p>&mdash; Jack Diederich (@jackdied) <a href="https://twitter.com/jackdied/status/863781949520961537">May 14, 2017</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>