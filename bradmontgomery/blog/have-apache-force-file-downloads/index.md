---
date: '2009-05-01T14:27:00+00:00'
title: Have Apache Force File Downloads
draft: false
tags:
- apache
- django
- web
slug: have-apache-force-file-downloads
description: ''
markup: md
url: /blog/have-apache-force-file-downloads/
aliases:
- /blog/2009/05/01/have-apache-force-file-downloads/

---

I have a Django app that lets users upload files. Any kind of file. It's nice that Apache will let me force file downloads based on the files extension.   

```
<LocationMatch "\.(gz|tar|pdf|docx|doc|xls|xlsx|bz2|zip)$">  
    SetHandler None  
    Header set Content-Disposition attachment  
</LocationMatch>  

```
  
So, in my HTML/templates: all I have to do is this:  

```
<a href="SomFile.docx">Some File</a>  

```
![](https://blogger.googleusercontent.com/tracker/4123748873183487963-9046149690255549987?l=bradmontgomery.blogspot.com)