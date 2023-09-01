---
date: '2011-01-24T15:56:59+00:00'
title: SiteSprint III - An update
draft: false
tags: []
slug: sitesprint-iii-an-update
description: ''
markup: md
url: /blog/sitesprint-iii-an-update/
aliases:
- /blog/2011/01/24/sitesprint-iii-an-update/

---

This post, a followup to [my previous post](/blog/sitesprint-iii-the-reclaimation/), is now about 2 months overdue. I have to admit, I'm glad I participated in [SiteSprint](http://sitesprint.info/), but I'm fairly disappointed in the amount of work that I accomplished. So, without further ado, here's the update on what happened.

Success!
--------

1. Set up a Django stack running nginx, gunicorn, postgresql
2. Set up [Mezzanine](http://github.com/stephenmcd/mezzanine)
3. Migrated my blog posts and comments from Blogger

For a weekend of work, this really wasn't too bad. I like Mezzanine for publishing, and I like being in control of my own content and web stack again.  I still have plans for integrating other apps for my own personal use, so having this stack available is worth a lot to me.

Failure
-------

These are the things that I *knew* would be most difficult to accomplish.

1. Design & Typography.
2. *Modern* HTML
3. Housecleaning - fixing imported blog posts

I really don't like the current design of this blog.  It's close to what I want, but not quite.  The [960](http://960.gs/) CSS framework comes bundled with Mezzanine, so I tried to use that.  I'm much more familiar with [Blueprint](http://www.blueprintcss.org/), and at some point, I'd like to completely revise the layout and design of this site using it.

I actually did spend quite a bit of time reading about typography (specifically [The Elements of Typographic Style Applied to the Web](http://webtypography.net/toc/ "Go to table of contents")). I think I learned quite a bit, but still just enough to know that for the most part, *I'm doing it wrong*. I'd like to remedy this, as typography is an incredibly important subject.

I'd also planned on using more modern markup for the layout of this site with elements such as <nav>, <header>, and <footer> for page layout and <article> for blog entries.  In addition, many of the entries imported from Blogger are littered with horrendous markup.  These posts really need to be cleaned up, especially since much of the code snippets are now completely unreadable.

So, as you can see, there's still a lot of work to be done, and I need to *buckle down* and get this stuff done.

