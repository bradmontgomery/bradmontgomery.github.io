---
date: '2008-07-30T15:29:00+00:00'
title: PHP is chopping off my Access Memo Fields
draft: false
tags: []
slug: php-is-chopping-off-my-access-memo-fields
description: I've got a few simpl...
markup: html
url: /blog/php-is-chopping-off-my-access-memo-fields/
aliases:
- /blog/2008/07/30/php-is-chopping-off-my-access-memo-fields/

---

I've got a few simple web forms that use PHP to read and write to an Access database (running on IIS), and I just spent the last few hours frantically trying to figure out why some of my Memo fields were being truncated around 4000 characters.  <br /><br />I know Memo fields "should" be able to contain up to 65536 characters, and I could verify this by inserting data directly into the database.  However, when querying the database through PHP (using odbc), I could only retrieve 4000 characters.<br /><br />The culprit?  A tiny little setting called <span style="font-weight: bold; font-size: xx-large;">odbc.defaultlrl</span>! (lrl = long read length).  This can be changed in php.ini, or you can use ini_set to modify this setting directly in your php script:<br /><pre>&lt;?php<br />ini_set(&#39;odbc.defaultlrl&#39;, 65536);<br />?&gt;<br /></pre><br />I found this info on the discussion for the <a href="http://us3.php.net/manual/en/function.odbc-longreadlen.php">odbc_longreadlen</a> function.<div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/4123748873183487963-6208247461343887893?l=bradmontgomery.blogspot.com' alt='' /></div>