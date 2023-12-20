---
date: '2009-12-13T14:57:00+00:00'
title: Ubuntu Audio, YES! Windows XP, NO.
draft: false
tags:
- Hardware
- Linux
- Ubuntu
- audio
slug: ubuntu-audio-yes-windows-xp-no
description: ''
markup: md
url: /blog/ubuntu-audio-yes-windows-xp-no/
aliases:
- /blog/2009/12/13/ubuntu-audio-yes-windows-xp-no/

---

I run a dual-boot Ubuntu64[[1]](#one) and Windows XP system. The windows partition really exists for a [single purpose](http://en.wikipedia.org/wiki/Unreal_Tournament_2004), and I occasionally just reboot the machine, choose the XP partition from the Grub menu, and all is well.  
  
However, a few weeks ago, I upgraded Ubuntu, but when I rebooted the machine and chose the XP partition, I noticed the sound[[2]](#two) stopped working. What!? The audio worked fine in ubuntu!  
  
The Secret: **I had to *completely power down the machine* before booting into Windows.** Then, audio works just fine.   
  
Unfortunately, I didn't discover this until I'd re-installed the windows drivers (which didn't work), reformatted/reinstalled windows and all drivers (which only worked because I powered down in the process), [fixed my grub boot loader](http://www.howtogeek.com/howto/ubuntu/reinstall-ubuntu-grub-bootloader-after-windows-wipes-it-out/), and incorrectly assumed the problem was fixed until I booted back into Ubuntu and back into Windows only to find that the problem remained.  
  
Sheesh. So, if this has happened to you, I'm sure you've found the myriad article on how to get sound working in Linux... which for me, has always worked just fine.  
  
[1] Output of **uname -a**:
```
Linux homeserver 2.6.31-16-generic #53-Ubuntu SMP Tue Dec 8 04:02:15 UTC 2009 x86_64 GNU/Linux
```
[2] A Soundblaster Audigy LS. Output of **lspci**:
```
02:02.0 Multimedia audio controller: Creative Labs CA0106 Soundblaster
```
![](https://blogger.googleusercontent.com/tracker/4123748873183487963-8164638269643552852?l=bradmontgomery.blogspot.com)