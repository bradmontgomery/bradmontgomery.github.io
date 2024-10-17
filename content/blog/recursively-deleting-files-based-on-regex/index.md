---
date: '2008-09-09T06:20:00+00:00'
title: Recursively deleting files (based on regex)
draft: false
tags: []
slug: recursively-deleting-files-based-on-regex
description: ''
markup: md
url: /blog/recursively-deleting-files-based-on-regex/
aliases:
- /blog/2008/09/09/recursively-deleting-files-based-on-regex/

---

While we're on the topic... (the topic being recursively doing stuff to files), I often want to delete all the files in a hierachy of directories that match a regular expression (or regex).  
  
The typical scenario for this is, "I want to delete all of my compiled python files."  
  
Here's how I do it:
```
find ./ -type f -name "*.pyc" -exec rm {} \;
```
*find ./ -type f -name "\*.pyc"* should find all files ending in .pyc under the *current directory*. Once they've been found, the *-exec rm {} \;* will remove them.