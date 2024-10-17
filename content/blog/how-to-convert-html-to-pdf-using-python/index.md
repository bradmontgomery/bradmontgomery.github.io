---
date: '2008-12-17T19:37:00+00:00'
title: How to convert HTML to PDF using Python.
draft: false
tags:
- PDF
- Python
- web
slug: how-to-convert-html-to-pdf-using-python
description: ''
markup: md
url: /blog/how-to-convert-html-to-pdf-using-python/
aliases:
- /blog/2008/12/17/how-to-convert-html-to-pdf-using-python/

---

I'm building web-based, data-driven apps using [Django](http://www.djangoproject.com/). Eventually (or unfortunately), I will need to generate some reports that are printer-friendly. Logically, [PDF](http://en.wikipedia.org/wiki/Portable_Document_Format) is the format for such files... so how am I going to convert my xHTML and CSS to a nice-looking PDF document?  
  
The [Django Book](http://www.djangobook.com/) has a whole chapter dedicated to [Generating Non-HTML Content](http://www.djangobook.com/en/1.0/chapter11/). They seem to to be fond of [ReportLab ToolKit](http://www.reportlab.org/rl_toolkit.html). The caveat here, though, is that you need to know a bit about the internals of a PDF document. If you're familiar with this, the ReportLab toolkit seems to be the way to go! It has many features, and it seems to be a powerful PDF-generating tool.  
  
Unfortunately, I know nothing about PDF internals, but I do know quite a bit about HTML and CSS. That's why [xhtml2pdf.com](http://www.xhtml2pdf.com/) caught my attention. If it delivers on it's promises, it parses HTML and CSS and generates PDFs (imagine that)! There's also a handy Activestate recipe using it: [Recipe 572160: HTML/CSS to PDF converter](http://code.activestate.com/recipes/572160/).  
  
I'm definately going to check this (HTML2PDF.org) out... so expect an update on this!  
  
Any other suggestions?  
  
UPDATE: [xhtml2pdf](http://www.xhtml2pdf.com/) works well. There's also a great  
[post by Greg Newman](http://www.20seven.org/journal/2008/11/pdf-generation-with-pisa-in-django.html) outlining how it's used in django.