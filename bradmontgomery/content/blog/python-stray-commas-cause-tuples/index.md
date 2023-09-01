---
date: '2010-10-15T11:26:00+00:00'
title: 'Python: stray commas cause tuples?'
draft: false
tags:
- Python
slug: python-stray-commas-cause-tuples
description: As I try to debug a ...
markup: html
url: /blog/python-stray-commas-cause-tuples/
aliases:
- /blog/2010/10/15/python-stray-commas-cause-tuples/

---

As I try to debug a strange problem in a Django view, I notice a stray comma after a dictionary definition. So I jump over to a python shell, and guess what?  Ending a literal dict with a comma creates a tuple.  <br /><div class="highlight" ><pre><span style="color: #c65d09; font-weight: bold">&gt;&gt;&gt; </span>d <span style="color: #666666">=</span> {<span style="color: #40a070">1</span>:<span style="color: #4070a0">&#39;foo&#39;</span>},<br /><span style="color: #c65d09; font-weight: bold">&gt;&gt;&gt; </span><span style="color: #007020">type</span>(d)<br /><span style="color: #808080">&lt;type &#39;tuple&#39;&gt;</span><br /><span style="color: #808080"></span><span style="color: #c65d09; font-weight: bold">&gt;&gt;&gt; </span>d<br /><span style="color: #808080">({1: &#39;foo&#39;},)</span><br /><span style="color: #808080"></span><span style="color: #c65d09; font-weight: bold">&gt;&gt;&gt; </span><br /></pre></div><div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/4123748873183487963-5282351448916778629?l=bradmontgomery.blogspot.com' alt='' /></div>