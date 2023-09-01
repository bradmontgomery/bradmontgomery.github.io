---
date: '2010-03-25T15:21:00+00:00'
title: Dealing with Unicode and ASCII using Python
draft: false
tags:
- ascii
- python
- unicode
slug: dealing-with-unicode-and-ascii-using-python
description: ''
markup: md
url: /blog/dealing-with-unicode-and-ascii-using-python/
aliases:
- /blog/2010/03/25/dealing-with-unicode-and-ascii-using-python/

---

Dealing with Character Encodings is (sometimes) hard. It's especially confusing for those who've never done it before. Converting text from unicode to ascii can be tricky. 

A lot of times, I'll import some data from a text file, and I just want to convert everything to ASCII and ignore anything that's not ascii (like MS Word's smart quotes). Luckily, this is fairly easy:  



```
mystring = mystring.decode('ascii', 'ignore')
```
There's tons of great Python resources (and code!) for all your character encoding needs. In no particular order, here are a few I've found:  


* [A Crash Course in Character Encoding](http://www.pyzine.com/Issue008/Section_Articles/article_Encodings.html)
* [Dive Into Python's Chapter on Unicode](http://diveintopython.org/xml_processing/unicode.html)
* [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/) gives you [Unicode, Dammit](http://www.crummy.com/software/BeautifulSoup/documentation.html#Beautiful Soup Gives You Unicode, Dammit) and there's the companion: [ASCII, Dammit](http://www.crummy.com/cgi-bin/msm/map.cgi/ASCII,+Dammit)
* There's also [unaccent.py](http://effbot.python-hosting.com/file/stuff/sandbox/text/unaccent.py), which seems to convert various unicode characters to their ascii equivalent.

There's probably more, but most of these have helped me get the job done.

