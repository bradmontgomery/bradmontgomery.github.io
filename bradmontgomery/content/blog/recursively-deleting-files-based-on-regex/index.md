---
date: '2008-09-09T06:20:00+00:00'
title: Recursively deleting files (based on regex)
draft: false
tags: []
slug: recursively-deleting-files-based-on-regex
description: While we're on the t...
markup: html
url: /blog/recursively-deleting-files-based-on-regex/
aliases:
- /blog/2008/09/09/recursively-deleting-files-based-on-regex/

---

While we're on the topic... (the topic being recursively doing stuff to files), I often want to delete all the files in a hierachy of directories that match a regular expression (or regex).<br /><br />The typical scenario for this is, "I want to delete all of my compiled python files."<br /><br />Here's how I do it:<pre>find ./ -type f -name "*.pyc" -exec rm {} \;</pre><em>find ./ -type f -name "*.pyc"</em> should find all files ending in .pyc under the <em>current directory</em>.  Once they've been found, the <em>-exec rm {} \;</em> will remove them.<div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/4123748873183487963-6785752564543884991?l=bradmontgomery.blogspot.com' alt='' /></div>