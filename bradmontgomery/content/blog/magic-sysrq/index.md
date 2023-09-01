---
date: '2007-02-09T21:07:00+00:00'
title: magic SysRq
draft: false
tags:
- Linux
- Programming
slug: magic-sysrq
description: Occasionally I goof ...
markup: html
url: /blog/magic-sysrq/
aliases:
- /blog/2007/02/09/magic-sysrq/

---

Occasionally I goof up.  Yes, as much as I hate to admit it, it's true.  However, thanks to <a href="http://liquidweather.net/howto/index.php?id=97">this handy tutorial on liquidweather.net</a>, I've learned about some nifty ways to kill things in linux.<br /><br />In addition to the traditional ways to kill a process, this tutorial lists some magic SysRq key combinations that--if enabled in your kernel--can provide a nice option to just pulling the plug...<br /><ul><li>Alt+SysRq+K - Kills all processes (SIGKILL / kill -9)</li><br /><li>Alt+SysRq+E - Terminates all processes (SIGTERM / kill -15)</li><br /><li>Alt+SysRq+I - Interrupts all processes (SIGINT / kill -2)</li><br /><li>Alt+SysRq+U - Force unmount and remount of all filesystems readonly</li><br /><li>Alt+SysRq+S - Syncs all disks</li><br /><li>Alt+SysRq+B - Reboots</li></ul><br />(Note to self, and any other developers:  When using a language without built-in garbage collection, don't forget to free up memory when you're done!)<div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/4123748873183487963-2326695535330074466?l=bradmontgomery.blogspot.com' alt='' /></div>