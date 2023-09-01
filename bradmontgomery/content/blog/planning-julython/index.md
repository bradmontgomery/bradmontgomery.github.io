---
date: '2012-07-02T02:36:24+00:00'
title: planning julython
draft: false
tags: []
slug: planning-julython
description: <p>A few days ago I ...
markup: html
url: /blog/planning-julython/
aliases:
- /blog/2012/07/02/planning-julython/

---

<p>A few days ago I saw <a class="reference external" href="https://twitter.com/#!/jtauber" _mce_href="https://twitter.com/#!/jtauber">@jtauber</a> tweet
something about <a class="reference external" href="http://www.julython.org/" _mce_href="http://www.julython.org/">julython</a>. Essentially it's a game
that <em>encourages</em> you give a pet python project a little extra love during the
month of July.</p>
<p>For me (and probably several others), this is a little push to spend some time
on projects that otherwise get neglected because there are <strong>more pressing</strong>
things to do. So, without further ado, here's what I'd like to accomplish this
month (in order of importance!):</p>
<p>1. <a class="reference external" href="https://github.com/copitux/python-github3" _mce_href="https://github.com/copitux/python-github3">python-github3</a>: I ran across
this a couple of weeks ago (yeah, I got bit by not keeping up with the news
regarding
<a class="reference external" href="https://github.com/blog/1160-github-api-v2-end-of-life" _mce_href="https://github.com/blog/1160-github-api-v2-end-of-life">v2 of the github api</a>)
and I offered to add support for events
(<a class="reference external" href="https://github.com/copitux/python-github3/issues/15" _mce_href="https://github.com/copitux/python-github3/issues/15">Issue #15</a>). So that's
what I'm doing first.</p>
<p>2. django-coffers: I keep up with my finances in spreadsheet that's modeled
after a checkbook register, and every time time I open it a little piece of me
dies. Granted, I'm a little OCD about tracking my spending, and I've long wanted
to build a web app that makes this easier to do. Around December 2010, I
started working on a django app and had even planned to turn it into a public
service (<a class="reference external" href="http://fullcoffers.com" _mce_href="http://fullcoffers.com">http://fullcoffers.com</a>), but got <em>sidetracked</em> by an
<a class="reference external" href="http://workforpie.com/" _mce_href="http://workforpie.com/">even cooler idea</a>. A lot of the intial work is done,
so I'm going to bring it up to date and open-source it. Then I'm going to
doogfood the crap out of it so I can bury the spreadsheet once and for all!</p>
<p>3. <a class="reference external" href="https://github.com/bradmontgomery/elasticdict" _mce_href="https://github.com/bradmontgomery/elasticdict">elasticdict</a>: I don't
really even know where this came from, but one day I thought, "What if a
python <cite>dict</cite> pushed it's data out to
<a class="reference external" href="http://www.elasticsearch.org/" _mce_href="http://www.elasticsearch.org/">elasticsearch</a>?"  So, I started hacking
that together, but didn't really get very far. I'd like to play with this a bit
more and see what happens. I don't really have a use case for this, and I think
it only makes sense for a small subset of features offered by elasticsearch,
but I'll play with it untill my curiosity is sated (or until it explodes).</p>
<p>In addition, I'd like to get some of my local friends to join me, and see if
we can help <a class="reference external" href="http://www.julython.org/location/memphis-tn/" _mce_href="http://www.julython.org/location/memphis-tn/">Memphis, TN</a> get
some sort of showing on the leaderboard. There's a rather
<a class="reference external" href="http://mempy.org/" _mce_href="http://mempy.org/">small group of pythonistas</a> in the area, but I think we
can do enough to get noticed ;)</p><p><br></p>

<p><strong>UPDATE:</strong> Out of the blue I needed to use an older project of mine (<a href="https://bitbucket.org/bkmontgomery/image-crawler/" _mce_href="https://bitbucket.org/bkmontgomery/image-crawler/">image-crawler</a>), so I've decided to give it an update as well. These changes will involve PEP8 improvements and the use of <a href="http://pypi.python.org/pypi/requests/" _mce_href="http://pypi.python.org/pypi/requests/">requests</a>. These will be some quick fixes, so I've decided to do them first!</p>