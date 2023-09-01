---
date: '2007-05-16T20:57:00+00:00'
title: Hello Torque, again.
draft: false
tags:
- Games
- Programming
slug: hello-torque-again
description: Well, I've just begu...
markup: html
url: /blog/hello-torque-again/
aliases:
- /blog/2007/05/16/hello-torque-again/

---

Well, I've just begun to dig into the <a href="http://www.garagegames.com/products/torque/tge/">Torque Game Engine</a> again, but this time, I'm building it on a Linux box. Once I downloaded the Linux source, it took me a while to figure out how to get it compiled.  TGE's configuration is a little different than the typical "./configure and make" process.<br /><br />First of all, I tried to make sure I had all of the development tools necessary to build TGE, including <b>nasm</b>, <b>libogg</b>, <b>libvorbis</b>, and <b>libtheora</b> along with any <package>-dev versions of many packages.   Then, once you unzip the source you need to issue the following command to set up your configuration:<pre>make -f mk/configure.mk</pre>This will display the current build configuration and it will tell you if it's valid or not.  To get a valid configuration on my system, I used the following configuration:<br /><br /><pre>make -f m/configure.mk OS=LINUX COMPILER=GCC4 BUILD=DEBUG \<br />DIR.OBJ=/home/brad/TorqueGameEngineSDK-Linux-1-5-0/build</pre><br />Notice that I had to use an absolute path for the (optional) object Directory.  At first, I just used "DIR.OBJ=build", which resulted in some compiler errors. Anyway, this placed all the object files in a directory called "build.GCC4.DEBUG"<br /><br />The next change I had to make was in an actual source file. Apparently, GCC didn't like some things... I'm not going to post any details, but I did eventually get it working, so <a href="http://bradmontgomery.net/show.php?page=contact">contact me</a> if you're interested.<br /><br />Good Luck!<div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/4123748873183487963-6044072354529285854?l=bradmontgomery.blogspot.com' alt='' /></div>