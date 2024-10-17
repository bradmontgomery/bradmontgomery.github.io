---
date: '2008-02-15T18:26:00+00:00'
title: Shrinking Images with Python
draft: false
tags:
- Python
slug: shrinking-images-with-python
description: ''
markup: md
url: /blog/shrinking-images-with-python/
aliases:
- /blog/2008/02/15/shrinking-images-with-python/

---

My wife had a very large image, and she needed some smaller versions of it. Well, I thought I'd just fire up [The GIMP](http://gimp.org) and create a few shrunken versions, but by the time The GIMP loaded on my G4 Mac mini, I'd almost finished writing the python coded needed to do the task for me!  
  
Writing code is good!  

```
import Image  
from sys import argv  
  
def shrink(filename):  
    im = Image.open(filename)  
    w,h = im.size  
      
    # Create images that are 10%, 20%....90% of the original  
    sizes = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]  
      
    for s in sizes:  
        nw = int(w*s)  
        nh = int(h*s)  
        n = im.resize((nw, nh))  
        f = "%s_x_%s_%s"%(nw,nh,filename)  
        print "Saving %s"%(f)  
        n.save(f)  
          
if __name__ == "__main__":  
      
    if len(argv) == 2:  
        shrink(argv[1])  
    else:  
        print "USAGE: python shrink.py "
```
  
  
Download this code: <http://bradmontgomery.net/files/shrink.zip>