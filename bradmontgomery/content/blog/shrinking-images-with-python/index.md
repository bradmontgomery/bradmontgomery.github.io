---
date: '2008-02-15T18:26:00+00:00'
title: Shrinking Images with Python
draft: false
tags:
- Python
slug: shrinking-images-with-python
description: My wife had a very l...
markup: html
url: /blog/shrinking-images-with-python/
aliases:
- /blog/2008/02/15/shrinking-images-with-python/

---

My wife had a very large image, and she needed some smaller versions of it.  Well, I thought I'd just fire up <a href="http://gimp.org">The GIMP</a> and create a few shrunken versions, but by the time The GIMP loaded on my G4 Mac mini, I'd almost finished writing the python coded needed to do the task for me!<br /><br />Writing code is good!<br /><pre>import Image<br />from sys import argv<br /><br />def shrink(filename):<br />    im = Image.open(filename)<br />    w,h = im.size<br />    <br />    # Create images that are 10%, 20%....90% of the original<br />    sizes = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]<br />    <br />    for s in sizes:<br />        nw = int(w*s)<br />        nh = int(h*s)<br />        n = im.resize((nw, nh))<br />        f = "%s_x_%s_%s"%(nw,nh,filename)<br />        print "Saving %s"%(f)<br />        n.save(f)<br />        <br />if __name__ == "__main__":<br />    <br />    if len(argv) == 2:<br />        shrink(argv[1])<br />    else:<br />        print "USAGE: python shrink.py <imagefile>"</pre><br /><br />Download this code: <a href="http://bradmontgomery.net/files/shrink.zip">http://bradmontgomery.net/files/shrink.zip</a><div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/4123748873183487963-222154634554447484?l=bradmontgomery.blogspot.com' alt='' /></div>