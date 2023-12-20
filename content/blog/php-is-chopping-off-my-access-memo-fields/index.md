---
date: '2008-07-30T15:29:00+00:00'
title: PHP is chopping off my Access Memo Fields
draft: false
tags: []
slug: php-is-chopping-off-my-access-memo-fields
description: ''
markup: md
url: /blog/php-is-chopping-off-my-access-memo-fields/
aliases:
- /blog/2008/07/30/php-is-chopping-off-my-access-memo-fields/

---

I've got a few simple web forms that use PHP to read and write to an Access database (running on IIS), and I just spent the last few hours frantically trying to figure out why some of my Memo fields were being truncated around 4000 characters.   
  
I know Memo fields "should" be able to contain up to 65536 characters, and I could verify this by inserting data directly into the database. However, when querying the database through PHP (using odbc), I could only retrieve 4000 characters.  
  
The culprit? A tiny little setting called odbc.defaultlrl! (lrl = long read length). This can be changed in php.ini, or you can use ini\_set to modify this setting directly in your php script:  

```
<?php  
ini_set('odbc.defaultlrl', 65536);  
?>  

```
  
I found this info on the discussion for the [odbc\_longreadlen](http://us3.php.net/manual/en/function.odbc-longreadlen.php) function.![](https://blogger.googleusercontent.com/tracker/4123748873183487963-6208247461343887893?l=bradmontgomery.blogspot.com)