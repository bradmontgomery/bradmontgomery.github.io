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
description: I run a dual-boot Ub...
markup: html
url: /blog/ubuntu-audio-yes-windows-xp-no/
aliases:
- /blog/2009/12/13/ubuntu-audio-yes-windows-xp-no/

---

I run a dual-boot Ubuntu64<a href="#one">[1]</a> and Windows XP system.  The windows partition really exists for a <a href="http://en.wikipedia.org/wiki/Unreal_Tournament_2004">single purpose</a>, and I occasionally just reboot the machine, choose the XP partition from the Grub menu, and all is well.<br /><br />However, a few weeks ago, I upgraded Ubuntu, but when I rebooted the machine and chose the XP partition, I noticed the sound<a href="#two">[2]</a> stopped working. What!?  The audio worked fine in ubuntu!<br /><br />The Secret: <b>I had to <em>completely power down the machine</em> before booting into Windows.</b>  Then, audio works just fine.  <br /><br />Unfortunately, I didn't discover this until I'd re-installed the windows drivers (which didn't work), reformatted/reinstalled windows and all drivers (which only worked because I powered down in the process), <a href="http://www.howtogeek.com/howto/ubuntu/reinstall-ubuntu-grub-bootloader-after-windows-wipes-it-out/">fixed my grub boot loader</a>, and incorrectly assumed the problem was fixed until I booted back into Ubuntu and back into Windows only to find that the problem remained.<br /><br />Sheesh. So, if this has happened to you, I'm sure you've found the myriad article on how to get sound working in Linux... which for me, has always worked just fine.<br /><br /><a name="one">[1]</a> Output of <b>uname -a</b>:<pre>Linux homeserver 2.6.31-16-generic #53-Ubuntu SMP Tue Dec 8 04:02:15 UTC 2009 x86_64 GNU/Linux</pre><a name="two">[2]</a> A Soundblaster Audigy LS. Output of <b>lspci</b>:<pre>02:02.0 Multimedia audio controller: Creative Labs CA0106 Soundblaster</pre><div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/4123748873183487963-8164638269643552852?l=bradmontgomery.blogspot.com' alt='' /></div>