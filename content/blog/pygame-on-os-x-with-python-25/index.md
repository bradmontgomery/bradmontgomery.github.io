---
date: '2007-09-23T20:38:00+00:00'
title: Pygame on OS X with python 2.5
draft: false
tags:
- OS
- Python
- X
slug: pygame-on-os-x-with-python-25
description: ''
markup: md
url: /blog/pygame-on-os-x-with-python-25/
aliases:
- /blog/2007/09/23/pygame-on-os-x-with-python-25/

---

I've used Pygame on Mac OS X in the past, but my installation recently stopped working for some reason, so I decided to grab the binaries and re-install. After checking out the [Pythonmac](http://pythonmac.org/packages/) list, I was a little disappointed to see that there were only Pygame binaries for [Python 2.4](http://pythonmac.org/packages/py24-fat/index.html). Below is a list of software that I installed (in the necessary order) to get pygame working with Python 2.5 on OS X. All of these (except Python 2.5.1) I got from [pythonmac.org/packages](http://pythonmac.org/packages/py25-fat/index.html).  
  
2. [Python 2.5.1](http://www.python.org/ftp/python/2.5.1/python-2.5.1-macosx.dmg) - from the [Python download page](http://www.python.org/download/).
  
4. [PIL 1.16 - Python Image Library](http://pythonmac.org/packages/py25-fat/dmg/PIL-1.1.6-py2.5-macosx10.4-2007-05-18.dmg).
  
6. [NumPy 1.0.3.1](http://pythonmac.org/packages/py25-fat/dmg/numpy-1.0.3.1-py2.5-macosx10.4-2007-08-27.dmg).
  
8. [Numeric 24.2](http://pythonmac.org/packages/py25-fat/dmg/Numeric-24.2-py2.5-macosx10.4.dmg).
  
10. [numarray 1.5.2](http://pythonmac.org/packages/py25-fat/dmg/numarray-1.5.2-py2.5-macosx10.4-2007-01-30.dmg).
  
12. [PyObjC 1.4](http://pythonmac.org/packages/py25-fat/mpkg/pyobjc-1.4-py2.5-macosx10.4.mpkg.zip).
  
14. [wxPython 2.9.3.0](http://pythonmac.org/packages/py25-fat/dmg/wxPython2.8-osx-unicode-2.8.3.0-universal10.4-py2.5.dmg) (just in case)

  
  
Finally, I grabbed the Pygame 1.7.1 source from [pygame.org/download.shtml](http://pygame.org/download.shtml).  
   
Installation for most of the prerequisite packages went smoothly, since they all include OS X Installers. While pygame requires Numeric, I went ahead and installed NumPy and numarray, just in case.  
  
The only real problem came when installing PyObjC. After installing, I opened a python interpreter to test it out by typing "import Foundation" (as it says to do in the [PyObjC Tutorial](http://pyobjc.sourceforge.net/doc/tutorial.php). This let to the following error:
```
  
dyld: Symbol not found: __cg_jpeg_resync_to_restart  
Referenced from: /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ImageIO.framework/Versions/A/ImageIO  
Expected in: /sw/lib/libJPEG.dylib
```
  
  
Apparently, if you've installed anything using Fink, the PyObjC installer gets confused when trying to choose to which libraries to link. For me, libjpeg was the culprit... hence the error above. To make sure PyObjC works with Apple's ImageIO, I edited my ~/.profile and commented out any lines that set a DYLD\_LIBRARY\_PATH environment variable (just place a # in front of the line). For me, this looked like this:  

```
#DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:/usr/local/lib:/sw/lib:/usr/lib  
#export DYLD_LIBRARY_PATH
```
  
This prevents any conflicts when linking against libraries installed by fink (which are stored in /sw) and possibly duplicate system libraries. After doing this, I re-ran the PyObjC installer, and everything worked perfectly. Now, I built the Pygame source, and my simple Pygame applications will run.   
  
**So what's next?** Notice there's no mention of PyOpenGL above, so any Pygame applications that use PyOpenGL won't work Until you [Install PyOpenGL](http://bradmontgomery.blogspot.com/2007/10/pyopengl-on-os-x.html)  
  
**Download this Pygame Package:** <http://bradmontgomery.net/files/pygame-1.7.1release-py2.5.1-macosx10.4.dmg>![](https://blogger.googleusercontent.com/tracker/4123748873183487963-543717478932761428?l=bradmontgomery.blogspot.com)