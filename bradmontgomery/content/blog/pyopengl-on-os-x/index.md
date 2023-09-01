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
description: '<strong>Update: July...'
markup: html
url: /blog/pyopengl-on-os-x/
aliases:
- /blog/2007/10/16/pyopengl-on-os-x/

---

<strong>Update: July 7, 2010:</strong> For the past year or so I've been using <a href="http://pypi.python.org/pypi/virtualenv">virtualenv</a>, <a href="http://www.doughellmann.com/projects/virtualenvwrapper/">virtualenvwrapper</a>, and <a href="http://pip.openplans.org/">pip</a> to manage and install python packages, and I highly encourage everyone to use these tools!  It may take a bit to learn how to use these tools, but once you do, the rewards are great!  (especially when using 3rd party python libraries on Mac OS X).<br /><br />To install PyOpenGL using the aforementioned tools, you'd simply do the following.<br /><ul><li>Create a virtual environment for your OpenGL installation.  I'm naming it "gl":<pre>mkvirtualenv gl</pre></li><br /><li>Then use pip to install PyOpenGL: <pre>pip install pyopengl</pre></li></ul><br />That's all there is to it!  I grabbed the demo apps from <a href="http://pypi.python.org/pypi/PyOpenGL-Demo">http://pypi.python.org/pypi/PyOpenGL-Demo</a>, and verified that the gears.py script works, so this should get you started.<br /><br />I'm leaving the old post below, but again, check out virtualenv and pip.  You'll be happy that you did!<br /><hr/><br />I actually got this working quite a while ago, but for some reason I've gotten busy and never documented it.  In fact, installing PyOpenGL was almost so easy it's not even worth mentioning... Except... it was  so easy, so it's worth mentioning!<br /><br />Here are the steps to install PyOpenGL on Mac OS X (10.4.10):<br /><ol><br /><li> You'll need to get setuptools, and the easiest way to do that is with <a href="http://peak.telecommunity.com/DevCenter/EasyInstall">EasyInstall</a> (see <a href="http://peak.telecommunity.com/DevCenter/EasyInstall">http://peak.telecommunity.com/DevCenter/EasyInstall</a>).  You'll download the <b>ez_setup.py</b> file, and just run: <b>python ez_setup.py</b>.</li><br /><li>Download PyOpenGL from their <a href="http://sourceforge.net/project/showfiles.php?group_id=5988">download page</a>. (Side Note: I also grabbed the OpenGLContext). Now, once you untar/unzip it, you should have a PyOpenGL/ directory.  Just open a Terminal, cd into that directory, and run <b>python setup.py build</b>.  Once that is finished, run <b>python setup.py install</b></li><br /><li>Now, do the same for OpenGLContext...</li><br /></ol><div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/4123748873183487963-4096316648311915512?l=bradmontgomery.blogspot.com' alt='' /></div>