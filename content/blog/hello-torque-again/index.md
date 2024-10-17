---
date: '2007-05-16T20:57:00+00:00'
title: Hello Torque, again.
draft: false
tags:
- Games
- Programming
slug: hello-torque-again
description: ''
markup: md
url: /blog/hello-torque-again/
aliases:
- /blog/2007/05/16/hello-torque-again/

---

Well, I've just begun to dig into the [Torque Game Engine](http://www.garagegames.com/products/torque/tge/) again, but this time, I'm building it on a Linux box. Once I downloaded the Linux source, it took me a while to figure out how to get it compiled. TGE's configuration is a little different than the typical "./configure and make" process.  
  
First of all, I tried to make sure I had all of the development tools necessary to build TGE, including **nasm**, **libogg**, **libvorbis**, and **libtheora** along with any -dev versions of many packages. Then, once you unzip the source you need to issue the following command to set up your configuration:
```
make -f mk/configure.mk
```
This will display the current build configuration and it will tell you if it's valid or not. To get a valid configuration on my system, I used the following configuration:  
  

```
make -f m/configure.mk OS=LINUX COMPILER=GCC4 BUILD=DEBUG \  
DIR.OBJ=/home/brad/TorqueGameEngineSDK-Linux-1-5-0/build
```
  
Notice that I had to use an absolute path for the (optional) object Directory. At first, I just used "DIR.OBJ=build", which resulted in some compiler errors. Anyway, this placed all the object files in a directory called "build.GCC4.DEBUG"  
  
The next change I had to make was in an actual source file. Apparently, GCC didn't like some things... I'm not going to post any details, but I did eventually get it working, so [contact me](http://bradmontgomery.net/show.php?page=contact) if you're interested.  
  
Good Luck!