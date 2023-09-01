---
date: '2008-12-17T19:37:00+00:00'
title: How to convert HTML to PDF using Python.
draft: false
tags:
- PDF
- Python
- web
slug: how-to-convert-html-to-pdf-using-python
description: I'm building web-bas...
markup: html
url: /blog/how-to-convert-html-to-pdf-using-python/
aliases:
- /blog/2008/12/17/how-to-convert-html-to-pdf-using-python/

---

I'm building web-based, data-driven apps using <a href="http://www.djangoproject.com/">Django</a>.  Eventually (or unfortunately), I will need to generate some reports that are <span style="font-style:italic;">printer-friendly</span>.  Logically, <a href="http://en.wikipedia.org/wiki/Portable_Document_Format">PDF</a> is <span style="font-weight:bold;">the</span> format for such files... so how am I going to convert my xHTML and CSS to a nice-looking PDF document?<br /><br />The <a href="http://www.djangobook.com/">Django Book</a> has a whole chapter dedicated to <a href="http://www.djangobook.com/en/1.0/chapter11/">Generating Non-HTML Content</a>.  They seem to to be fond of <a href="http://www.reportlab.org/rl_toolkit.html">ReportLab ToolKit</a>.  The caveat here, though, is that you need to know a bit about the internals of a PDF document.  If you're familiar with this, the ReportLab toolkit seems to be the way to go!   It has many features, and it seems to be a powerful PDF-generating tool.<br /><br />Unfortunately, I know nothing about PDF internals, but I do know quite a bit about HTML and CSS.  That's why <a href="http://www.xhtml2pdf.com/">xhtml2pdf.com</a> caught my attention.  If it delivers on it's promises, it parses HTML and CSS and generates PDFs  (imagine that)!  There's also a handy Activestate recipe using it: <a href="http://code.activestate.com/recipes/572160/">Recipe 572160: HTML/CSS to PDF converter</a>.<br /><br />I'm definately going to check this (HTML2PDF.org) out... so expect an update on this!<br /><br />Any other suggestions?<br /><br />UPDATE: <a href="http://www.xhtml2pdf.com/">xhtml2pdf</a> works well.  There's also a great<br /><a href="http://www.20seven.org/journal/2008/11/pdf-generation-with-pisa-in-django.html">post by Greg Newman</a> outlining how it's used in django.<div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/4123748873183487963-7973631231608601676?l=bradmontgomery.blogspot.com' alt='' /></div>