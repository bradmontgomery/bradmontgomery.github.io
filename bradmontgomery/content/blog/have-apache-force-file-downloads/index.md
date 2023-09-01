---
date: '2009-05-01T14:27:00+00:00'
title: Have Apache Force File Downloads
draft: false
tags:
- apache
- django
- web
slug: have-apache-force-file-downloads
description: I have a Django app ...
markup: html
url: /blog/have-apache-force-file-downloads/
aliases:
- /blog/2009/05/01/have-apache-force-file-downloads/

---

I have a Django app that lets users upload files.  Any kind of file. It's nice that Apache will let me force file downloads based on the files extension.  <br /><div class="highlight" ><pre><span style="color: #062873; font-weight: bold">&lt;LocationMatch</span> <span style="color: #4070a0">&quot;\.(gz|tar|pdf|docx|doc|xls|xlsx|bz2|zip)$&quot;</span><span style="color: #062873; font-weight: bold">&gt;</span><br />    <span style="color: #007020">SetHandler</span> <span style="color: #007020; font-weight: bold">None</span><br />    <span style="color: #007020">Header</span> set Content-Disposition attachment<br /><span style="color: #062873; font-weight: bold">&lt;/LocationMatch&gt;</span><br /></pre></div><br />So, in my HTML/templates: all I have to do is this:<br /><div class="highlight" ><pre><span style="color: #062873; font-weight: bold">&lt;a</span> <span style="color: #4070a0">href=&quot;SomFile.docx&quot;</span><span style="color: #062873; font-weight: bold">&gt;</span>Some File<span style="color: #062873; font-weight: bold">&lt;/a&gt;</span><br /></pre></div><div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/4123748873183487963-9046149690255549987?l=bradmontgomery.blogspot.com' alt='' /></div>