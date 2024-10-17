---
date: '2016-04-29T16:04:11.732863+00:00'
title: Let's convert a Word Doc to HTML
draft: false
tags:
- html
- pandoc
- python
- word
slug: lets-convert-word-doc-html
description: ''
markup: md
url: /blog/lets-convert-word-doc-html/
aliases:
- /blog/2016/04/29/lets-convert-word-doc-html/

---

## tl;dr

I wrote a python script to convert Word documents to mostly-clean html. Get it at [https://github.com/bradmontgomery/word2html](https://github.com/bradmontgomery/word2html).

## Ah, Microsoft Word...

That glorious business-class software used all-around the world. It's perfect for those long, legal documents consisting of nothing but headers, paragraphs, and bulleted lists. All of which we an easily convert into simple HTML, right. Right?

File > Save As > Web Page (.htm). Easy as... No wait, was that supposed to be File > Save As > Web Page, Filtered (.htm)? 

O.M.G. What is all this `MsoTitle` crap. Why are there so many inline styles for simple black & white text. Why are all of my bulleted lists paragraph tags!? Why oh why are we 20-years into having a world wide web, and the world's foremost business document software can't even generate a simple html page.

## Never fear there's hope.

Disclaimer: this is a quick and dirty hack. Check out my [word2html](https://github.com/bradmontgomery/word2html) script. With the magic of python, [pandoc](http://pandoc.org/), and [pytidylib](http://countergram.com/open-source/pytidylib/)/[html tidy](http://countergram.com/open-source/pytidylib/), doing this conversion isn't soooo bad.

The gist of the code looks something like this:

 import pypandoc
 from tidylib import tidy\_document

 output = pypandoc.convert(your\_filename, 'html')
 output, errors = tidy\_document(output)
 with open(output\_file, 'w') as f:
 f.write(output)

Grab the repo, install the requirements, and run the command:

 python convert.py MyGloriousDoc.docx

Happy converting your word docs to html. Long live the web!