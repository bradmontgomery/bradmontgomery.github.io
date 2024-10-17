---
date: '2007-06-16T20:53:00+00:00'
title: Compiling Warzone 2100 on Mac OS X
draft: false
tags:
- Games
- OS
- X
slug: compiling-warzone-2100-on-mac-os-x
description: ''
markup: md
url: /blog/compiling-warzone-2100-on-mac-os-x/
aliases:
- /blog/2007/06/16/compiling-warzone-2100-on-mac-os-x/

---

I recently ran across [The Warzone 2100 Resurrection Project](http://wz2100.net/), and I thought to myself,"cool, I wonder if there's an OS X version..." So, I hit their [downloads](http://wz2100.net/downloads.html) page only to find the message: "(The MacOSX diskimage will follow soon)"  
  
So I thought, "oh well, I'll just grab the source code and compile it!" After about two hours of digging, I finally got it compiled, and here's how! (NOTE: I've got quite a bit of Unix stuff installed via [fink](http://finkproject.org/), so your mileage may vary)  
  
1. Here's the list of stuff I had to get/install/compile before I could even start on Warzone 2100: **cmake (to compile physfs)**, **physfs**, **a newer bison**, and **SDL\_net**
  
3. First I grab [cmake 2.4.6](http://cmake.org). Luckily, they have a [universal .dmg for Tiger](http://cmake.org/HTML/Download.html).
  
5. Next, I grab the source code for [physfs-1.1.1](http://icculus.org/physfs/) from their [download page](http://icculus.org/physfs/downloads/). At first I tried compiling the "Unix Way", but that didn't work, so I used cmake to generate an Xcode project (pretty cool!). From a terminal window, I cd into the physfs directory and type:  

```
cmake -G Xcode .
```
  
Then, after compiling physfs with Xcode, I copied the libraries to my /usr/local directories. Again from a Terminal:  

```
sudo cp libphysfs.* /usr/local/lib  
sudo cp physfs.h /usr/local/include
```
  
7. Next, I open up [fink commander](http://finkcommander.sourceforge.net/) and grab the newest version of bison from fink
  
9. Now I need [SDL\_net](http://www.libsdl.org/projects/SDL_net/). While the project offers a [Mac OS X Framework](http://www.libsdl.org/projects/SDL_net/release/SDL_net-1.2.6.dmg) and SDL\_net is available through fink... I grabbed the source anyway. It compiled just fine the Unix way:
```
  
./configure  
make  
sudo make install
```
  
This put all the libraries in /usr/local/lib and /usr/local/include
  
11. Finally, time to compile Warzone2100, so I grabbed the [source code](http://wz2100.net/downloads.html), which contains a handy-dandy file called COMPILE. I suggest you read it. To start of, I opened a terminal and cd'd into the warzone2100-2.0.6 directory and typed the following command:
```
./autogen.sh
```
  
Then, I typed the following to configure it using my fink libraries and headers:  

```
./configure --prefix=/Applications/Warzone2100-2.0.6 LDFLAGS=-L/sw/lib CPPFLAGS=-I/sw/include
```
   
This will also put the final binary in my /Applications Directory. So, the last to steps are to compile, and install:
```
make  
sudo make install
```
This did the trick for me.
  
13. Now that I got Warzone2100 compiled, I can open a terminal and type the following:  

```
/Applications/Warzone2100/bin/warzone2100 --fullscreen
```
  
And this "should" lauch the application!

Enjoy!