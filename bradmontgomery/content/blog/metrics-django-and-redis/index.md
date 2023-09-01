---
date: '2013-05-19T02:38:29.648285+00:00'
title: Metrics with Django and Redis
draft: false
tags:
- django
- django-redis-metrics
- metrics
- redis
slug: metrics-django-and-redis
description: ''
markup: md
url: /blog/metrics-django-and-redis/
aliases:
- /blog/2013/05/19/metrics-django-and-redis/

---

So, you've got a shiny new Django-powered site, and now you'd like to start
recording metrics. Perhaps you've read [The
Lean Startup](http://theleanstartup.com/), and you know you've got to know how people are using your
site in order to know what to improve. Perhaps you're just a data nerd and you
like to count things. Either way, there are ton's of ways to measure things
on your site.


You could use third-party applications like [Google Analytics](http://www.google.com/analytics/) or [Mixpanel](https://mixpanel.com/) to see how
people interact with your site. Then there are services like [New Relic](https://newrelic.com/) that give you amazing insights as to where your application is slow
or too memory hungry. All of these services are really good, and if you're building
a startup, you should be using them.


But sometimes, you need a little more flexibility when *counting things*.
That's the motivation behind [`django-redis-metrics`](https://github.com/bradmontgomery/django-redis-metrics). It's a simple, lightweight Django app that
lets you easily record metrics in your Django apps.


I use it on [Work for Pie](https://workforpie.com) to measure
things such as:


* User growth
* External API usage (e.g. how hard we're hitting the GitHub or StackOverflow APIs)
* User interaction (e.g. how frequently somone
 [follows a company](https://workforpie.com/companies/gallery/))


Once installed, it's fairly simple to start recording metrics. You can call
out to the `metric` function anywhere in your code, and that will
increment a counter every time the function is called.




```
from redis_metrics import metric

metric("thing-i-want-to-measure")
```

All data is stored in [Redis](http://redis.io/) (which is a great
data store for this kind of thing). and there are very
few dependencies. `django-redis-metrics` aims to be a fairly
minimalistic, and very simple to use out of the box.


If you need a simple way to measure arbitrary events in a Django app, please
give it a look.

