---
date: '2010-03-25T15:21:00+00:00'
title: Dealing with Unicode and ASCII using Python
draft: false
tags:
- ascii
- python
- unicode
slug: dealing-with-unicode-and-ascii-using-python
description: <p>Dealing with Char...
markup: html
url: /blog/dealing-with-unicode-and-ascii-using-python/
aliases:
- /blog/2010/03/25/dealing-with-unicode-and-ascii-using-python/

---

<p>Dealing with Character Encodings is (sometimes) hard.  It's especially confusing for those who've never done it before.  Converting text from unicode to ascii can be tricky. </p><p>A lot of times, I'll import some data from a text file, and I just want to convert everything to ASCII and ignore anything that's not ascii (like MS Word's smart quotes).  Luckily, this is fairly easy:<br></p><div class="highlight"><pre>mystring <span style="color: #666666" _mce_style="color: #666666;">=</span> mystring<span style="color: #666666" _mce_style="color: #666666;">.</span>decode(<span style="color: #4070a0" _mce_style="color: #4070a0;">'ascii'</span>, <span style="color: #4070a0" _mce_style="color: #4070a0;">'ignore'</span>)</pre></div><p>There's tons of great Python resources (and code!) for all your character encoding needs. In no particular order, here are a few I've found:<br></p><ul><li><a href="http://www.pyzine.com/Issue008/Section_Articles/article_Encodings.html" _mce_href="http://www.pyzine.com/Issue008/Section_Articles/article_Encodings.html">A Crash Course in Character Encoding</a></li><li><a href="http://diveintopython.org/xml_processing/unicode.html" _mce_href="http://diveintopython.org/xml_processing/unicode.html">Dive Into Python's Chapter on Unicode</a></li><li><a href="http://www.crummy.com/software/BeautifulSoup/" _mce_href="http://www.crummy.com/software/BeautifulSoup/">Beautiful Soup</a> gives you <a href="http://www.crummy.com/software/BeautifulSoup/documentation.html#Beautiful Soup Gives You Unicode, Dammit" _mce_href="http://www.crummy.com/software/BeautifulSoup/documentation.html#Beautiful Soup Gives You Unicode, Dammit">Unicode, Dammit</a> and there's the companion: <a href="http://www.crummy.com/cgi-bin/msm/map.cgi/ASCII,+Dammit" _mce_href="http://www.crummy.com/cgi-bin/msm/map.cgi/ASCII,+Dammit">ASCII, Dammit</a></li><li>There's also <a href="http://effbot.python-hosting.com/file/stuff/sandbox/text/unaccent.py" _mce_href="http://effbot.python-hosting.com/file/stuff/sandbox/text/unaccent.py">unaccent.py</a>, which seems to convert various unicode characters to their ascii equivalent.</li></ul><p>There's probably more, but most of these have helped me get the job done.</p>