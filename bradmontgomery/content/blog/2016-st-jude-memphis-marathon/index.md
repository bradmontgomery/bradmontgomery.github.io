---
date: '2016-12-10T22:42:04.055160+00:00'
title: 2016 St Jude Memphis Marathon
draft: false
tags: []
slug: 2016-st-jude-memphis-marathon
description: It's been exactly on...
markup: md
url: /blog/2016-st-jude-memphis-marathon/
aliases:
- /blog/2016/12/10/2016-st-jude-memphis-marathon/

---

It's been exactly one week since I participated in the St. Jude Memphis Marathon, and I wanted to take a moment to say *thank you* to everyone who helped me get so close to my fundraising goal.  Together, we raised $1435 of $1500, and I'm really happy about that (although, [you can still give up 'till January](http://heroes.stjude.org/bkmontgomery)!).

As for the race, well... I'm glad I ran it. This year, I've run a 50k, a 50-miler, and this marathon. Unfortunately the marathon was my least favorite of the three.  Don't get me wrong: I love this race, and I love what it stands for. It's just the first race that I've had real issues with cramping. Basically, here's how it broke down:

- Mile 1 - 10: Yeah, I'm feeling great! I'm gonna crush this thing.
- Mile 11-17: Hrmm, I may have started off too fast. I'm suddenly feeling a little tired.
- Miles 18-26:  _i am nothing but cramps, please stop running_.

This is first race where I just wanted to stop. I guess this happens to everyone, and it's no fun.  I'm not even sure what I did wrong, and I've been pretty consistent with training & nutrition for the past few months. Head over to [Garmin Connect](https://connect.garmin.com/modern/activity/1470476516) and you can see where things fall apart.  I did however, set nearly a 15-minute PR with this, by finishing in just over four hours: 4:14. So there's that.

Oh well. _C'est la vie_.

Perhaps I can beat the 4-hour mark next year.

## And now for some geeky stuff

A couple days after the race (once my legs stopped hurting), I went looking for the race results, and I realized they would be pretty easy feed into a python script and generate some interesting aggregate stats. So, this happened:

<script src="https://gist.github.com/bradmontgomery/5ee44fdf280b87c9b62da79ef43e118b.js"></script>

I posted this to a Facebook group, and my friend [Von](http://www.liftheavyrunlong.com/von/) thought it'd be fun to see this kind of data for the entire history of the race. So, I grabbed as many of the data files as I could and started analyzing them.  You can can check out [this spreadsheet](https://docs.google.com/spreadsheets/d/15nSFo_WKVWTufqSwoTxWbe2013KVXTqk7gE2Pj-JEbg/edit?usp=sharing) with some cool data like, _average pace_, _average finish time_, and _male/female participation_ numbers. And if you're interested, the [code to analyze this stuff is on github](https://github.com/bradmontgomery/st-jude-marathon).

Here's a a few charts to whet your appetite:

<iframe width="600" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/15nSFo_WKVWTufqSwoTxWbe2013KVXTqk7gE2Pj-JEbg/pubchart?oid=676261128&amp;format=interactive"></iframe>

<iframe width="600" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/15nSFo_WKVWTufqSwoTxWbe2013KVXTqk7gE2Pj-JEbg/pubchart?oid=994886875&amp;format=interactive"></iframe>

Unfortunately, I couldn't get Google Sheets to recognize things like `9:50` and `4:44:17` as durations nor could I get them to plot those values. So I ended up converting pace and finish times to seconds. Still, it's interesting stuff.