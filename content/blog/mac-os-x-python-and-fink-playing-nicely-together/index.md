---
date: '2008-06-25T08:29:00+00:00'
title: 'Mac OS X, Python, and Fink: Playing Nicely Together'
draft: false
tags:
- Fink
- Mac
- OS
- Python
- X
slug: mac-os-x-python-and-fink-playing-nicely-together
description: ''
markup: md
url: /blog/mac-os-x-python-and-fink-playing-nicely-together/
aliases:
- /blog/2008/06/25/mac-os-x-python-and-fink-playing-nicely-together/

---

Since upgrading to Leopard, I've been using Mac's default install of Python (which is 2.5.1). For the most part it's worked well for me, namely because I've installed additionaly packages either using Mac installers or through easy\_install. I recently needed to install python-ldap which didn't work using easy\_install. So, I turned to [Fink](http://finkproject.org/).  
  
Unfortunately, Fink wanted to install it's own version of python (2.5.2) as well. (I say unfortunately only because I now how two separate python installations, which I think is a bit redundant.) So, the problem is this: How do I make the Mac's System python play nicely with any python modules I install through Fink?  
  
My solution to this problem is to add the Fink python's site-packages directory to my PYTHONPATH. I do this by setting an environment variable in my *.profile* file located in my home directory. I added the following:  

```
  
PYTHONPATH="${PYTHONPATH}:/sw/lib/python2.5/site-packages"  
export PYTHONPATH
```
  
Now, when I run the python interpreter, I can import packages that were installed the Mac way, or through Fink. Hopefully, this won't give me any problems.