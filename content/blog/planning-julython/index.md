---
date: '2012-07-02T02:36:24+00:00'
title: planning julython
draft: false
tags: []
slug: planning-julython
description: ''
markup: md
url: /blog/planning-julython/
aliases:
- /blog/2012/07/02/planning-julython/

---

A few days ago I saw [@jtauber](https://twitter.com/#!/jtauber) tweet
something about [julython](http://www.julython.org/). Essentially it's a game
that *encourages* you give a pet python project a little extra love during the
month of July.


For me (and probably several others), this is a little push to spend some time
on projects that otherwise get neglected because there are **more pressing**
things to do. So, without further ado, here's what I'd like to accomplish this
month (in order of importance!):


1. [python-github3](https://github.com/copitux/python-github3): I ran across
this a couple of weeks ago (yeah, I got bit by not keeping up with the news
regarding
[v2 of the github api](https://github.com/blog/1160-github-api-v2-end-of-life))
and I offered to add support for events
([Issue #15](https://github.com/copitux/python-github3/issues/15)). So that's
what I'm doing first.


2. django-coffers: I keep up with my finances in spreadsheet that's modeled
after a checkbook register, and every time time I open it a little piece of me
dies. Granted, I'm a little OCD about tracking my spending, and I've long wanted
to build a web app that makes this easier to do. Around December 2010, I
started working on a django app and had even planned to turn it into a public
service (<http://fullcoffers.com>), but got *sidetracked* by an
[even cooler idea](http://workforpie.com/). A lot of the intial work is done,
so I'm going to bring it up to date and open-source it. Then I'm going to
doogfood the crap out of it so I can bury the spreadsheet once and for all!


3. [elasticdict](https://github.com/bradmontgomery/elasticdict): I don't
really even know where this came from, but one day I thought, "What if a
python dict pushed it's data out to
[elasticsearch](http://www.elasticsearch.org/)?" So, I started hacking
that together, but didn't really get very far. I'd like to play with this a bit
more and see what happens. I don't really have a use case for this, and I think
it only makes sense for a small subset of features offered by elasticsearch,
but I'll play with it untill my curiosity is sated (or until it explodes).


In addition, I'd like to get some of my local friends to join me, and see if
we can help [Memphis, TN](http://www.julython.org/location/memphis-tn/) get
some sort of showing on the leaderboard. There's a rather
[small group of pythonistas](http://mempy.org/) in the area, but I think we
can do enough to get noticed ;)

  



**UPDATE:** Out of the blue I needed to use an older project of mine ([image-crawler](https://bitbucket.org/bkmontgomery/image-crawler/)), so I've decided to give it an update as well. These changes will involve PEP8 improvements and the use of [requests](http://pypi.python.org/pypi/requests/). These will be some quick fixes, so I've decided to do them first!

