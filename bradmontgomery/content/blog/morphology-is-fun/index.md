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
description: ''
markup: md
url: /blog/morphology-is-fun/
aliases:
- /blog/2009/01/04/morphology-is-fun/

---

[Morphological operations](http://en.wikipedia.org/wiki/Morphological_image_processing) are
very common in image processing. The two most basic of these are Erosion and Dilations, and from these,
additional morphological operations can be performed. While there is an
[abundance](http://www.ph.tn.tudelft.nl/Courses/FIP/noframes/fip-Morpholo.html) of
[literature](http://www-viz.tamu.edu/faculty/parke/ends489f00/notes/sec1_9.html) on the
topic of [morphology](http://www.dspguide.com/ch25/4.htm), I often like to view concrete
examples of the operations.


So, I've [published a few images](http://files.bradmontgomery.net/morphology/index.html)
that illustrate the output of 1-to-5 iterations of various morphological operations
--erosion, dilation, opening, closing, gradient, top hat, and black hat--with various
structuring elements--rectangle, cross, and ellipse.


The code to reproduce these images was written using OpenCV, and is freely
available at <https://gist.github.com/bradmontgomery/5096641>


