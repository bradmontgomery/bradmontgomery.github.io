---
date: '2012-06-11T16:44:51+00:00'
title: Building a Happy Potty
draft: false
tags:
- ios
- javascript
- mobile
- web
slug: building-a-happy-potty
description: ''
markup: md
url: /blog/building-a-happy-potty/
aliases:
- /blog/2012/06/11/building-a-happy-potty/

---

This past weekend, I particpated in Memphis's [48 Hour Launch](http://www.launchmemphis.com/2012/05/14/48-hour-launch-on-june-8-10/). It's a weekend-long event where anyone can
pitch a business or app idea on a Friday night, try to get enough
people to buy into the idea, and form your team. Then, you spend
the weekend building something, and on Sunday you get a chance to
showcase what you've accomplished.


I was fortunate enough to team up with a few friends (and some
new ones!) to build an intial version of [Happy
Potty](http://happypottyapp.com): A mobile app that helps you find a clean place to... go.
Check it out! It's not quite available yet, but once it is, we hope
you'll have fun using it. Once it's ready, we'll start talking
about it on twiter (via [@happypotty](https://twitter.com/happypotty)).


One of the neat things about an event like 48hr launch is that
you often get a chance to dive into a few unfamiliar tools. We'd
originally planned to build an iOS app, though few of us felt
comfortable enough with the toolset to risk having nothing to show
at the end of the weekend. So, we decided to build the app using
some familiar tools (HTML & JavaScript), while also diving into
a few new things.


PhoneGap
--------


I know it's nothing *new*, per se, but this was
completely new to me; I've not really done any mobile work, but
PhoneGap really does make prototyping a mobile app increadibly
easy. You get access to a lot of the device's internals, while
using tools that are second nature to any seasoned web
developer.


I'm sure there are some caveats here, but if you want a working
prototype for simple mobile app, definitely give [PhoneGap a
spin](http://phonegap.com/).


jQuery Mobile
-------------


I really like jQuery, and I've known of [jQuery
Mobile](http://jquerymobile.com/)'s existance for quite some time, but again, I'd never
played with it. I did run into a few quirks regarding the timing of
events (when is my code executing vs. jQuery mobile), but
all-in-all, this is a really nice toolchain.


There's also, [codiqa](http://codiqa.com/) which I'd totally pay for if I
spent much time at all building mobile apps. It's a really nice
drag & drop interface builder using jQuery mobile's
widgets.


Parse.com
---------


I can't remember where I first heard about Parse, but we almost
passed over it this weekend. I'm really glad we didn't. Parse gives
you a really flexible, easy-to-use online data persistance. We just
used the Javascript API, and in a few minutes (ok, I spent an hour
fooling around with it) we were pushing data out for people to
share.


Now, I can't comment on what it's like at scale, but it appears
that [some people like it](https://parse.com/testimonials), and their
[$0
basic plan](https://parse.com/plans) gives you quite a bit of leeway for development
& testing.


We weren't using Backbone.js on this project, but it appears
that Parse plays pretty nicely there, too.


Takeaway
--------


I'd always toyed around with the idea of getting into mobile app
development, but had never jumped headlong into the fray. I didn't
realize just how accessible these tools are to web developers.


If you spend your days in HTML & JavaScript land, and you're
curious about mobile app development, do yourself a favor and spend
a weekend playing with these tools. You'll have a working demo
before you know it!

