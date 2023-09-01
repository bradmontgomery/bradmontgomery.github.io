---
date: '2007-12-05T08:59:00+00:00'
title: Computing Correlation Coefficients in Python
draft: false
tags:
- Image
- Python
- numpy
- pil
slug: computing-correlation-coefficients-in-python
description: <p>A useful techniqu...
markup: html
url: /blog/computing-correlation-coefficients-in-python/
aliases:
- /blog/2007/12/05/computing-correlation-coefficients-in-python/

---

<p>A useful technique for matching objects in images is to compute the images'
Correlation Coefficients. Essentially, you take any image and compute the
correlation between it and another, smaller image containing ONLY the object
that you want to identify.  The resulting correlation image should contain
bright spots where there is a high correlation (or match) between the two
images.</p>

<p>Here's a simple python script to compute the correlation between two images:
<br /><a href="https://github.com/bradmontgomery/correlation">
https://github.com/bradmontgomery/correlation</a></p>

<p>It requires <a href="http://www.pythonware.com/products/pil/">PIL</a> and
<a href="http://www.numpy.org/">numpy</a>, and it's fairly inefficient, but
it's a simple, straightforward implementation.</p>