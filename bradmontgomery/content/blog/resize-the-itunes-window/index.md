---
date: '2010-01-14T09:47:00+00:00'
title: Resize the iTunes Window
draft: false
tags:
- Mac
- Programming
- applescript
- iTunes
slug: resize-the-itunes-window
description: My Macbook Pro is my...
markup: html
url: /blog/resize-the-itunes-window/
aliases:
- /blog/2010/01/14/resize-the-itunes-window/

---

My Macbook Pro is my main machine. At the office, I connect it to a 20" Cinema display. At home, I connect it to a 24" Samsung Monitory (Model 2494SW Glossy Black, which I really like, btw.)<br /><br />There's a down-side to all this, though.  I mostly just notice it with iTunes. When I'm working on the laptop without an external monitor, my iTunes window is larger than my screen :(   Unfortunately, clicking the Maximize  button doesn't do what I want (which is to make the window fit in the screen.  So here's a little Applescript to to fix it:<br /><br /><pre>tell application "iTunes"<br /> set the bounds of the first window to {50, 50, 1024, 640}<br />end tell</pre><br />The arguments are the distance from the top and left of the screen (both 50), the width of the iTunes window (1024) followed by its height (640). <br /><br />I just saved this in a file called <em>resize_itunes.scpt</em> and put it in my <em>Documents/Applescripts/</em> folder. I'm a big fan of <a href="http://www.blacktree.com/projects/quicksilver.html">Quicksilver</a>, so when I need to resize my iTunes window, I just activate Quicksilver (Ctrl+Spacebar), type in "resize" (which finds the applescript file), and then hit "enter" to run the script.  Easy.<div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/4123748873183487963-8179727769750930704?l=bradmontgomery.blogspot.com' alt='' /></div>