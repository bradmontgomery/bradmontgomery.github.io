---
date: '2009-01-04T14:27:00+00:00'
title: Morphology is Fun!
draft: false
tags:
- Fun
- Image
- Programming
- morphology
- vision
slug: morphology-is-fun
description: <p><a href="http://e...
markup: html
url: /blog/morphology-is-fun/
aliases:
- /blog/2009/01/04/morphology-is-fun/

---

<p><a href="http://en.wikipedia.org/wiki/Morphological_image_processing">Morphological operations</a> are
very common in image processing. The two most basic of these are Erosion and Dilations, and from these,
additional morphological operations can be performed. While there is an
<a href="http://www.ph.tn.tudelft.nl/Courses/FIP/noframes/fip-Morpholo.html">abundance</a> of
<a href="http://www-viz.tamu.edu/faculty/parke/ends489f00/notes/sec1_9.html">literature</a> on the
topic of <a href="http://www.dspguide.com/ch25/4.htm">morphology</a>, I often like to view concrete
examples of the operations.</p>

<p>So, I've <a target="_blank" href="http://files.bradmontgomery.net/morphology/index.html">published a few images</a>
that illustrate the output of 1-to-5 iterations of various morphological operations
--erosion, dilation, opening, closing, gradient, top hat, and black hat--with various
structuring elements--rectangle, cross, and ellipse.</p>

<p>The code to reproduce these images was written using OpenCV, and is freely
available at <a href="https://gist.github.com/bradmontgomery/5096641">https://gist.github.com/bradmontgomery/5096641</a></p>

<script src="https://gist.github.com/bradmontgomery/5096641.js"></script>