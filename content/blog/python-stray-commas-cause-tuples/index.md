---
date: '2010-10-15T11:26:00+00:00'
title: 'Python: stray commas cause tuples?'
draft: false
tags:
- Python
slug: python-stray-commas-cause-tuples
description: ''
markup: md
url: /blog/python-stray-commas-cause-tuples/
aliases:
- /blog/2010/10/15/python-stray-commas-cause-tuples/

---

As I try to debug a strange problem in a Django view, I notice a stray comma after a dictionary definition. So I jump over to a python shell, and guess what? Ending a literal dict with a comma creates a tuple.   

```
>>> d = {1:'foo'},  
>>> type(d)  
<type 'tuple'>  
>>> d  
({1: 'foo'},)  
>>>   

```
