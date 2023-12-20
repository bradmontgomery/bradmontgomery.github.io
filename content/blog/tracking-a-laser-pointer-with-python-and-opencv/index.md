---
date: '2008-01-24T13:13:00+00:00'
title: Tracking a Laser pointer with Python and OpenCV
draft: false
tags:
- opencv
- python
slug: tracking-a-laser-pointer-with-python-and-opencv
description: ''
markup: md
url: /blog/tracking-a-laser-pointer-with-python-and-opencv/
aliases:
- /blog/2008/01/24/tracking-a-laser-pointer-with-python-and-opencv/

---

A recent thread on the OpenCV mailing list (entitled: "Tracking laser dots")
discussed techniques that could be used to track the dot from a laser pointer.
This sounded like something fun, so I finally got around to trying it out.
Essentially this could be done acheived by the following algorithm:


1. Grab the video frame.
2. Convert the video frame to the HSV color space.
3. Split the frame into individual components (separate images for H, S, and V).
4. Apply a threshold to each compenent (hopefully keeping just the dot from
 the laser). It was originally suggested that just the Hue component be used
 to search for the laser's dot, but I actually got several false positives
 doing this. Therefore, using Value in addition to Hue gave me a more
 reliable result. I can see where finding good threshold values for all 3
 components would be a good approach in some situations.
5. Finally, perform an AND operation on the 3 images (which "should" cut down
 on false positives)


I should note that my testing was performed using a red laser pointer and a
large white sheet of paper in an well-lit office. Since I was only tracking the
dot on the paper, this turned out to be a fairly easy task to accomplish.
Finding good threshold values in other situations would be much more difficult.


Update: This code is now on Github:
<https://github.com/bradmontgomery/python-laser-tracker>


