---
date: '2007-02-09T21:07:00+00:00'
title: magic SysRq
draft: false
tags:
- Linux
- Programming
slug: magic-sysrq
description: ''
markup: md
url: /blog/magic-sysrq/
aliases:
- /blog/2007/02/09/magic-sysrq/

---

Occasionally I goof up. Yes, as much as I hate to admit it, it's true. However, thanks to [this handy tutorial on liquidweather.net](http://liquidweather.net/howto/index.php?id=97), I've learned about some nifty ways to kill things in linux.  
  
In addition to the traditional ways to kill a process, this tutorial lists some magic SysRq key combinations that--if enabled in your kernel--can provide a nice option to just pulling the plug...  
* Alt+SysRq+K - Kills all processes (SIGKILL / kill -9)
  
* Alt+SysRq+E - Terminates all processes (SIGTERM / kill -15)
  
* Alt+SysRq+I - Interrupts all processes (SIGINT / kill -2)
  
* Alt+SysRq+U - Force unmount and remount of all filesystems readonly
  
* Alt+SysRq+S - Syncs all disks
  
* Alt+SysRq+B - Reboots

  
(Note to self, and any other developers: When using a language without built-in garbage collection, don't forget to free up memory when you're done!)