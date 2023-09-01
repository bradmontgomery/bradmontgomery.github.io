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
description: There are <a href="h...
markup: html
url: /blog/building-pil-on-os-x-snow-leopard/
aliases:
- /blog/2010/02/25/building-pil-on-os-x-snow-leopard/

---

There are <a href="http://jetfar.com/libjpeg-and-python-imaging-pil-on-snow-leopard/">several</a> <a href="http://stackoverflow.com/questions/1438270/installing-python-imaging-library-pil-on-snow-leopard-with-updated-python-2-6-2">places</a> <a href="http://proteus-tech.com/blog/cwt/install-pil-in-snow-leopard/">online</a> that discuss problems installing PIL on Mac OS X Snow Leopard<br /><br />This is  how I got it to work.<br /><ol><br /><li>Install lib jpeg using <a href="http://github.com/mxcl/homebrew">homebrew</a> (which is super-aweseome!) <pre>brew intall jpeg</pre>.This installs the library into <pre>/usr/local/Cellar/jpeg/7</pre></li><br /><li>Install <a href="http://www.freetype.org/">libfreetype</a> the old-fashioned way (./configure, make, sudo make install).  I used <em>freetype-2.1.10.pre-20050511</em>.</li><br /><li>Download, unpack PIL (I used <a href="http://effbot.org/downloads/Imaging-1.1.6.tar.gz">Imaging-1.1.6</a>). I had to make the following changes to setup.py<pre>FREETYPE_ROOT = "/usr/local"<br />JPEG_ROOT = ("/usr/local/Cellar/jpeg/7/lib", "/usr/local/Cellar/jpeg/7/include")</pre></li><br /><li>Then, build PIL:<pre>python setup.py build_ext -i</pre></li><br /><li>If the build works without any errors, you can run the tests:<pre>python selftest.py</pre> which should yield the following: <strong>57 tests passed.</strong></li><br /><li>(optional) I like to use virtualenv, so I activate that: <pre>workon myproject</pre></li><br /><li>Install PIL:<pre>python setup.py install</pre></li><br /></ol>At this point, code like the following works for me:<div class="highlight" ><pre><span style="color: #007020; font-weight: bold">import</span> <span style="color: #0e84b5; font-weight: bold">Image</span><br />im <span style="color: #666666">=</span> Image<span style="color: #666666">.</span>open(<span style="color: #4070a0">&quot;/path/to/pretty/picture.jpg&quot;</span>)<br />im<span style="color: #666666">.</span>show()</pre></div><div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/4123748873183487963-3675678730344892934?l=bradmontgomery.blogspot.com' alt='' /></div>