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
description: ''
markup: md
url: /blog/pygraphviz-on-os-x-sl-with-virtualenv/
aliases:
- /blog/2010/07/14/pygraphviz-on-os-x-sl-with-virtualenv/

---

There's this cool project called [django-extensions](http://github.com/django-extensions/) that (among other things) adds a lot of commands to django's `manage.py` offerings. One of which is `./manage.py graph_models [appname]` which will generate a nice graph displaying the relationships among all of your Models. This comand needs pyGraphViz, though, and I was a little disappointed when i discovered I couldn't install pyGraphViz with `pip install pygraphviz`. (ok, a lot disappointed).   
  
I eventually got this working, and here's how:  
  
* First, install the development snapshot of GraphViz: <http://graphviz.org/Download_macos.php> (I used graphviz-2.27.20100713.0445.pkg)
  
* Next, download the pygraphviz source code from <http://networkx.lanl.gov/pygraphviz/download.html>. (Again, I got pygraphviz-0.99.1/ )
  
* Here's the fun part. You need to edit pygraphviz's setup.py file (located at pygraphviz-0.99.1/setup.py for me). Find the following two lines of code:
```
  
library_path=None  
include_path=None
```
  
And change them to
```
  
library_path='/usr/local/lib/graphviz/'  
include_path='/usr/local/include/graphviz/'
```
  
You also might want to verify that the above directories exist.
  
* Now, active your virtualenv (workon <whatever\_your\_virtualenv\_is\_named>)
  
* Finally, just run `python setup.py install`
  

  
  
That's it! This installed pygraphviz in my activated virtualenv, and I can now use `./manage.py graph_models` to my heart's desire.  
  
I should mention that I'm using [distribute](http://pypi.python.org/pypi/distribute) (and it may be safe to assume that if you're using virtualenv, you're probably also using distribute).