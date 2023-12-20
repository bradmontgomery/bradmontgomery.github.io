---
date: '2006-09-06T21:29:00+00:00'
title: OpenCV on Mac OS X
draft: false
tags:
- OpenCV
- Programming
slug: opencv-on-mac-os-x
description: ''
markup: md
url: /blog/opencv-on-mac-os-x/
aliases:
- /blog/2006/09/06/opencv-on-mac-os-x/

---

I finally got arount to compiling [OpenCV](http://opencvlibrary.sourceforge.net/) on my G4 Mac mini. While there is a lot of good information online as to how to do this, there were a few final steps that took me a while to either figure out or find. Apparently using OpenCV on OS X is still a new thing...  
  
First of all, follow the directions here at the [Mac OS X OpenCV Port Wiki](http://opencvlibrary.sourceforge.net/Mac_OS_X_OpenCV_Port). (Note the two different configure options for Fink and MacPorts/DarwinPorts)  
Then, after typing "sudo make install", the include files should be in **/usr/local/include/opencv**, while the dynamic libraries should be in **/usr/local/lib**.  
  
So, the last thing to do is let your shell know about the libraries, and pkgconfig. Since I use bash, I added this to my .bashrc file.  

```
export LD_LIBRARY_PATH=/usr/local/lib  
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
```
  
And so... things seem to work.  
  
Many thanks go to those who've done a lot of work to get OpenCV on OS X!  
<http://opencvlibrary.sourceforge.net/MarkAsbach>  
<http://www.christophseibert.de/weblog/en/it/computer-vision/tools/opencv-mac.html>  
<http://lestang.org/article45.html>![](https://blogger.googleusercontent.com/tracker/4123748873183487963-3997551314779282905?l=bradmontgomery.blogspot.com)