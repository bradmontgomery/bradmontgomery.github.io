---
date: '2007-02-27T21:06:00+00:00'
title: 'Javascript: What is the standard?'
draft: false
tags:
- Javascript
- Programming
- web
slug: javascript-what-is-the-standard
description: ''
markup: md
url: /blog/javascript-what-is-the-standard/
aliases:
- /blog/2007/02/27/javascript-what-is-the-standard/

---

I've recently been writing a little javascript, and I needed to chage the value of some text inside an html/xhtml element. It seems there are several ways to do this, but evey browser may or may not support the same method for doing it (big surprise, here) I'm not sure what is considered the "standard" way. Here's a little script that I use to help me decide which browsers support which methods for altering text within an html/xhtml element:  

```
  
<html>  
<head><title>blah</title>  
<script language="JavaScript">  
<!-- Hide code from older browsers  
function loader() {  
  pp = document.getElementsByTagName("p")  
  pp[0].innerText = ".innerText DOES work!"  
  pp[1].style.content = ".style.content DOES work!"  
  pp[2].innerhtml    = ".innerhtml DOES work!"  
  pp[3].childNodes[0].nodeValue = ".childNodes[0].nodeValue DOES work!"  
}  
// End hiding-->  
</script>  
</head>  
  
<body onload="loader()">  
<h1>Changing text with javascript</h1>  
<p> .innerText DOES NOT work.</p>  
  
<p> .style.content DOES NOT work.</p>  
<p> .innerhtml DOES NOT work.</p>  
<p> .childNodes[0].nodeValue DOES NOT work.</p>  
</body>  
  
</html>
```
  
(Thanks to the users of [codingforums.com](http://www.codingforums.com/showthread.php?t=34717<br />), especially Roy Gardiner, whose code from which this script was adapted.)![](https://blogger.googleusercontent.com/tracker/4123748873183487963-7998488112426396151?l=bradmontgomery.blogspot.com)