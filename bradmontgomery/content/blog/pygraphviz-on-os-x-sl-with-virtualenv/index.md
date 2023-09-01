---
date: '2010-07-14T22:14:00+00:00'
title: PyGraphviz on OS X (SL) with virtualenv
draft: false
tags:
- Mac
- OS
- Python
- X
- graphviz
- virtualenv
slug: pygraphviz-on-os-x-sl-with-virtualenv
description: There's this cool pr...
markup: html
url: /blog/pygraphviz-on-os-x-sl-with-virtualenv/
aliases:
- /blog/2010/07/14/pygraphviz-on-os-x-sl-with-virtualenv/

---

There's this cool project called <a href="http://github.com/django-extensions/">django-extensions</a> that (among other things) adds a lot of commands to django's <code>manage.py</code> offerings.  One of which is <code>./manage.py graph_models [appname]</code> which will generate a nice graph displaying the relationships among all of your Models.  This comand needs pyGraphViz, though, and I was a little disappointed when i discovered I couldn't install pyGraphViz with <code>pip install pygraphviz</code>. (ok, a lot disappointed). <br /><br />I eventually got this working, and here's how:<br /><ul><br /><li>First, install the development snapshot of GraphViz: <a href="http://graphviz.org/Download_macos.php">http://graphviz.org/Download_macos.php</a> (I used graphviz-2.27.20100713.0445.pkg)</li><br /><li>Next, download the pygraphviz source code from <a href="http://networkx.lanl.gov/pygraphviz/download.html">http://networkx.lanl.gov/pygraphviz/download.html</a>. (Again, I got pygraphviz-0.99.1/ )</li><br /><li>Here's the fun part.  You need to edit pygraphviz's setup.py file (located at pygraphviz-0.99.1/setup.py for me). Find the following two lines of code:<pre><br />library_path=None<br />include_path=None</pre><br />And change them to<pre><br />library_path='/usr/local/lib/graphviz/'<br />include_path='/usr/local/include/graphviz/'</pre><br />You also might want to verify that the above directories exist.</li><br /><li>Now, active your virtualenv (workon &lt;whatever_your_virtualenv_is_named&gt;)</li><br /><li>Finally, just run <code>python setup.py install</code></li><br /></ul><br /><br />That's it! This installed pygraphviz in my activated virtualenv, and I can now use <code>./manage.py graph_models</code> to my heart's desire.<br /><br />I should mention that I'm using <a href="http://pypi.python.org/pypi/distribute">distribute</a> (and it may be safe to assume that if you're using virtualenv, you're probably also using distribute).<div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/4123748873183487963-671214602676980877?l=bradmontgomery.blogspot.com' alt='' /></div>