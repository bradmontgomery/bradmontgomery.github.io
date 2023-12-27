---
date: '2023-12-27 22:37:02.626926+00:00'
title: Welp, I built a static site generator
draft: false
tags:
- python
- web
- tools
- software
slug: welp-i-built-a-static-site-generator
description: 'Hello new website.'
markup: md
url: /blog/welp-i-built-a-static-site-generator/
aliases:
- /blog/2023/37/27/welp-i-built-a-static-site-generator/

---

## New Website?

I've been meaning to shift my personal site to a static site for quite a while. I fully indented to use something like
[hugo](https://gohugo.io/) or even [Pelican](https://getpelican.com/) which I formerly used to manage the
[mempy.org](https://mempy.org) website. Earlier this year, I archived my
[django-blargg](https://github.com/bradmontgomery/django-blargg) repo, and so with a little extra time around the
holidays I decided to finally make this happen.

I really wanted to use Hugo. I've used it before, it's got a great feature-set and tons of support. BUT! I had a few
requirements for my new site:

1. [Cool URIs don't change](https://www.w3.org/Provider/Style/URI). I really really though I could do this with hugo,
   and I 100% beleive it's possible, but I just pounded my head against this forever. Eventually I ditched hugo because
   of this requirement (and the fact that I had some markdown + some rst + some html content).
2. I really want to just use markdown. Most of my content was already there, and with a little extra throw-away code I
   mostly converted everythign to markdown.
3. I really don't want to think too hard. I write so infrequently hugo's giant feature-set was just a bit much.


*I know python. I know jinja. I know how I want to organize my content.*


## New Wheel.

**Well crap**. [I've reinvented a static site generator](https://github.com/bradmontgomery/bradmontgomery.github.io/pull/1).
Right now, the feature set is pretty small (just want I wanted). Features include:

- Two commands for managing content:
    - `python site.py new` to generate a template for new articles
    - `python site.py build` to build the site.
- support for [CommonMark](https://commonmark.org/) thanks to [markdown-it-py](https://github.com/executablebooks/markdown-it-py)
- Easy (for me) template customization thanks to [jinja](https://jinja.palletsprojects.com/en/3.1.x/)
- A very simple UI -- because I didn't want to think about this righ now, but it'll probably change. Thanks [kevquirk/simple.css](https://github.com/kevquirk/simple.css)


If you're interested, take a look at the single python module here: [https://github.com/bradmontgomery/bradmontgomery.github.io/blob/main/site.py](https://github.com/bradmontgomery/bradmontgomery.github.io/blob/main/site.py).

This isn't really indented to be shipped, but if there's interest I could turn it into a library. I probably should. Maybe. We'll see.

