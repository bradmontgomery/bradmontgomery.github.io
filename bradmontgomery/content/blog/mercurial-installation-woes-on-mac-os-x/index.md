---
date: '2009-09-30T12:15:00+00:00'
title: Mercurial installation woes on Mac OS X
draft: false
tags:
- Mac
- OS
- Python
- X
- hg
- mercurial
slug: mercurial-installation-woes-on-mac-os-x
description: I started using merc...
markup: html
url: /blog/mercurial-installation-woes-on-mac-os-x/
aliases:
- /blog/2009/09/30/mercurial-installation-woes-on-mac-os-x/

---

I started using mercurial around version 1.2, and I'm pretty sure I used the Mac OS X installer (from <a href="http://mercurial.berkwood.com/">http://mercurial.berkwood.com/</a>) to install 1.2.1.  This placed hg in <span style="font-family: courier">/Library/Frameworks/Python.framework/Versions/Current/bin/</span>.<br /><br />Now, I've decided to upgrade to 1.3.1, and I again grab the Mac OS X installer (again from <a href="http://mercurial.berkwood.com/">http://mercurial.berkwood.com/</a>), which installs hg in <span style="font-family: courier">/usr/local/bin/</span>.<br /><br />Ok, but my path is set up so that the older version is used by default... Is there a preferred way to remove the older version of mercurial?<br /><br />I just renamed the file: <span style="font-family: courier">/Library/Frameworks/Python.framework/Versions/Current/bin/hg</span> to hg-1.2.1, and source'd my .profile so that the new version (<span style="font-family: courier">/usr/local/bin/hg</span>) gets used instead.<br /><br />This does not seem like a good way to upgrade.  :(<br /><br /><em>this is all relevant to Mac OS X 10.5.8</em><div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/4123748873183487963-3322153686297622685?l=bradmontgomery.blogspot.com' alt='' /></div>