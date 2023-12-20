---
date: '2007-10-16T20:17:00+00:00'
title: PyOpenGL on OS X
draft: false
tags:
- OS
- OpenGL
- Python
- X
slug: pyopengl-on-os-x
description: ''
markup: md
url: /blog/pyopengl-on-os-x/
aliases:
- /blog/2007/10/16/pyopengl-on-os-x/

---

**Update: July 7, 2010:** For the past year or so I've been using [virtualenv](http://pypi.python.org/pypi/virtualenv), [virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/), and [pip](http://pip.openplans.org/) to manage and install python packages, and I highly encourage everyone to use these tools! It may take a bit to learn how to use these tools, but once you do, the rewards are great! (especially when using 3rd party python libraries on Mac OS X).  
  
To install PyOpenGL using the aforementioned tools, you'd simply do the following.  
* Create a virtual environment for your OpenGL installation. I'm naming it "gl":
```
mkvirtualenv gl
```
  
* Then use pip to install PyOpenGL: 
```
pip install pyopengl
```

  
That's all there is to it! I grabbed the demo apps from <http://pypi.python.org/pypi/PyOpenGL-Demo>, and verified that the gears.py script works, so this should get you started.  
  
I'm leaving the old post below, but again, check out virtualenv and pip. You'll be happy that you did!  


---

  
I actually got this working quite a while ago, but for some reason I've gotten busy and never documented it. In fact, installing PyOpenGL was almost so easy it's not even worth mentioning... Except... it was so easy, so it's worth mentioning!  
  
Here are the steps to install PyOpenGL on Mac OS X (10.4.10):  
  
2. You'll need to get setuptools, and the easiest way to do that is with [EasyInstall](http://peak.telecommunity.com/DevCenter/EasyInstall) (see <http://peak.telecommunity.com/DevCenter/EasyInstall>). You'll download the **ez\_setup.py** file, and just run: **python ez\_setup.py**.
  
4. Download PyOpenGL from their [download page](http://sourceforge.net/project/showfiles.php?group_id=5988). (Side Note: I also grabbed the OpenGLContext). Now, once you untar/unzip it, you should have a PyOpenGL/ directory. Just open a Terminal, cd into that directory, and run **python setup.py build**. Once that is finished, run **python setup.py install**
  
6. Now, do the same for OpenGLContext...
  

![](https://blogger.googleusercontent.com/tracker/4123748873183487963-4096316648311915512?l=bradmontgomery.blogspot.com)