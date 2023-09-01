---
date: '2008-09-05T19:10:00+00:00'
title: Recursively Renaming files
draft: false
tags:
- Linux
- Mac
- Programming
slug: recursively-renaming-files
description: My hosting provider ...
markup: html
url: /blog/recursively-renaming-files/
aliases:
- /blog/2008/09/05/recursively-renaming-files/

---

My hosting provider offers PHP4 and PHP5.  Unfortunately, all files ending in .php get interpreted by PHP4, while all files ending in .php5 get interpreted by PHP5.  So, how do I quickly change all of my files that end in .php to .php5?<br /><br />Do a google search for "recursively rename files", and you might run across this:<br /><br /><a href="http://seal-7.blogspot.com/2006/12/recursively-rename-files-with-regex-one.html">http://seal-7.blogspot.com/2006/12/recursively-rename-files-with-regex-one.html</a><br /><br />So, to accomplish my task, I use the following:<br /><br /><pre>find . -type f -print0 | xargs -0 rename 's/.php$/.php5/g'</pre><br /><br />Awesomeness.<div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/4123748873183487963-4179556125303523868?l=bradmontgomery.blogspot.com' alt='' /></div>