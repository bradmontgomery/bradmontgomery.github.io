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
description: ''
markup: md
url: /blog/mercurial-installation-woes-on-mac-os-x/
aliases:
- /blog/2009/09/30/mercurial-installation-woes-on-mac-os-x/

---

I started using mercurial around version 1.2, and I'm pretty sure I used the Mac OS X installer (from <http://mercurial.berkwood.com/>) to install 1.2.1. This placed hg in /Library/Frameworks/Python.framework/Versions/Current/bin/.  
  
Now, I've decided to upgrade to 1.3.1, and I again grab the Mac OS X installer (again from <http://mercurial.berkwood.com/>), which installs hg in /usr/local/bin/.  
  
Ok, but my path is set up so that the older version is used by default... Is there a preferred way to remove the older version of mercurial?  
  
I just renamed the file: /Library/Frameworks/Python.framework/Versions/Current/bin/hg to hg-1.2.1, and source'd my .profile so that the new version (/usr/local/bin/hg) gets used instead.  
  
This does not seem like a good way to upgrade. :(  
  
*this is all relevant to Mac OS X 10.5.8*