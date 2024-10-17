---
date: '2008-11-17T12:41:00+00:00'
title: Soup's On! And it IS Beautiful!
draft: false
tags:
- Programming
- Python
- web
slug: soups-on-and-it-is-beautiful
description: ''
markup: md
url: /blog/soups-on-and-it-is-beautiful/
aliases:
- /blog/2008/11/17/soups-on-and-it-is-beautiful/

---

Here's the problem: There's a BAJILLIION static html pages sitting out on a server, and I need to migrate all that content to a new Database-driven CMS. Additionally, I need to get rid of a lot of non-essential hard-coded presentational markup (like align="center" or font="whatever") and any inline styles that may exist... (you know, because external CSS is the way to go).  
  
I *could* spend hours and hours just copy-/pasting stuff... but meh. Enter [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/), [urllib](http://www.python.org/doc/2.5.2/lib/module-urllib.html), and [sqlite](http://www.python.org/doc/2.5.2/lib/module-sqlite3.html)... all glued together with [python](http://python.org).  
  
Now, for the most part, the content I want to scrape from these static html pages aIso contains links to the other pages I want to keep. So, here's what we can do, use urlllib to grab the content from the web server, use BeautifulSoup to extract all the values from href attributes in our "a" elements, and keep a list of these (checking to make sure they point to sites we want to keep).   
  
Then, I use BeautifulSoup to parse the page, keeping the bits that I want to keep. Lucky for me, the pages I'm particularly interested in have handy "InstanceBeginEditable" and "InstanceEndEditable" in comments (thanks Dreamweaver), so I just strip out everything before and after that, and parse what's left over. Of course, this sort of thing is going to be different for everybody, but luckily, parsing *X*HTML isn't that difficulty thanks to [BeautifulSoup's mostly-comprehensive documentation](http://www.crummy.com/software/BeautifulSoup/documentation.html).  
  
  
So, the part you've been waiting for... Download the Code, try it out, and leave me some feedback!  
<http://bradmontgomery.net/files/migrate_web.zip>  
  
[![Creative Commons License](http://i.creativecommons.org/l/by/3.0/us/80x15.png)](http://creativecommons.org/licenses/by/3.0/us/)  
migrate\_web.py by [Brad Montgomery](http://bradmontgomery.net/) is licensed under a [Creative Commons Attribution 3.0 United States License](http://creativecommons.org/licenses/by/3.0/us/).  
Based on a work at [bradmontgomery.net](http://bradmontgomery.net/files/migrate_web.py).