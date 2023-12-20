---
date: '2010-02-25T15:40:00+00:00'
title: 'Building PIL on OS X: Snow Leopard'
draft: false
tags:
- Mac
- OS
- PIL
- Python
- X
- homebrew
- virtualenv
slug: building-pil-on-os-x-snow-leopard
description: ''
markup: md
url: /blog/building-pil-on-os-x-snow-leopard/
aliases:
- /blog/2010/02/25/building-pil-on-os-x-snow-leopard/

---

There are [several](http://jetfar.com/libjpeg-and-python-imaging-pil-on-snow-leopard/) [places](http://stackoverflow.com/questions/1438270/installing-python-imaging-library-pil-on-snow-leopard-with-updated-python-2-6-2) [online](http://proteus-tech.com/blog/cwt/install-pil-in-snow-leopard/) that discuss problems installing PIL on Mac OS X Snow Leopard  
  
This is how I got it to work.  
  
2. Install lib jpeg using [homebrew](http://github.com/mxcl/homebrew) (which is super-aweseome!) 
```
brew intall jpeg
```
.This installs the library into 
```
/usr/local/Cellar/jpeg/7
```
  
4. Install [libfreetype](http://www.freetype.org/) the old-fashioned way (./configure, make, sudo make install). I used *freetype-2.1.10.pre-20050511*.
  
6. Download, unpack PIL (I used [Imaging-1.1.6](http://effbot.org/downloads/Imaging-1.1.6.tar.gz)). I had to make the following changes to setup.py
```
FREETYPE_ROOT = "/usr/local"  
JPEG_ROOT = ("/usr/local/Cellar/jpeg/7/lib", "/usr/local/Cellar/jpeg/7/include")
```
  
8. Then, build PIL:
```
python setup.py build_ext -i
```
  
10. If the build works without any errors, you can run the tests:
```
python selftest.py
```
 which should yield the following: **57 tests passed.**
  
12. (optional) I like to use virtualenv, so I activate that: 
```
workon myproject
```
  
14. Install PIL:
```
python setup.py install
```
  

At this point, code like the following works for me:
```
import Image  
im = Image.open("/path/to/pretty/picture.jpg")  
im.show()
```
![](https://blogger.googleusercontent.com/tracker/4123748873183487963-3675678730344892934?l=bradmontgomery.blogspot.com)