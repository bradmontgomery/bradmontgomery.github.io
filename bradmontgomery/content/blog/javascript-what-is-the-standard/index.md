---
date: '2007-02-27T21:06:00+00:00'
title: 'Javascript: What is the standard?'
draft: false
tags:
- Javascript
- Programming
- web
slug: javascript-what-is-the-standard
description: I've recently been w...
markup: html
url: /blog/javascript-what-is-the-standard/
aliases:
- /blog/2007/02/27/javascript-what-is-the-standard/

---

I've recently been writing a little javascript, and I needed to chage the value of some text inside an html/xhtml element.  It seems there are several ways to do this, but evey browser may or may not support the same method for doing it (big surprise, here) I'm not sure what is considered the "standard" way.  Here's a little script that I use to help me decide which browsers support which methods for altering text within an html/xhtml element:<br /><pre><br />&lt;html&gt;<br />&lt;head&gt;&lt;title&gt;blah&lt;/title&gt;<br />&lt;script language="JavaScript"&gt;<br />&lt;!-- Hide code from older browsers<br />function loader() {<br />  pp = document.getElementsByTagName("p")<br />  pp[0].innerText = ".innerText DOES work!"<br />  pp[1].style.content = ".style.content DOES work!"<br />  pp[2].innerhtml    = ".innerhtml DOES work!"<br />  pp[3].childNodes[0].nodeValue = ".childNodes[0].nodeValue DOES work!"<br />}<br />// End hiding--&gt;<br />&lt;/script&gt;<br />&lt;/head&gt;<br /><br />&lt;body onload="loader()"&gt;<br />&lt;h1&gt;Changing text with javascript&lt;/h1&gt;<br />&lt;p&gt; .innerText DOES NOT work.&lt;/p&gt;<br /><br />&lt;p&gt; .style.content DOES NOT work.&lt;/p&gt;<br />&lt;p&gt; .innerhtml DOES NOT work.&lt;/p&gt;<br />&lt;p&gt; .childNodes[0].nodeValue DOES NOT work.&lt;/p&gt;<br />&lt;/body&gt;<br /><br />&lt;/html&gt;</pre><br />(Thanks to the users of <a href="http://www.codingforums.com/showthread.php?t=34717<br />">codingforums.com</a>, especially Roy Gardiner, whose code from which this script was adapted.)<div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/4123748873183487963-7998488112426396151?l=bradmontgomery.blogspot.com' alt='' /></div>