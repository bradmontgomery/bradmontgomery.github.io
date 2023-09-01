---
date: '2007-02-08T21:09:00+00:00'
title: wifit - an iwconfig tool
draft: false
tags:
- Linux
- networking
- wifi
slug: wifit-an-iwconfig-tool
description: I've recently instal...
markup: html
url: /blog/wifit-an-iwconfig-tool/
aliases:
- /blog/2007/02/08/wifit-an-iwconfig-tool/

---

I've recently installed <a href="http://www.mepis.org/">Mepis Linux</a> on a couple of laptops (a Compaq Presario 2195US and a Dell Latitude D610, both of which use <a href="http://ndiswrapper.sourceforge.net/">NdisWrapper</a> for wifi drivers).I'm fairly mobile, so I needed a way to quickly change my wireless settings.  I wrote this simple bash script to let me do that, and I thought I'd just share it.<br /><pre><br />#!/bin/bash<br /><br />## wifit - the wifi tool<br />## This is a script that accepts a wifi-enabled interface, <br />## essid, and an optional ascii key for a wifi network connection<br /><br />if [ $# -lt 2 ] || [ $# -gt 3 ] ; then <br /> echo "wifit - the wifi tool"<br /> echo "-------------------------------------------------"<br /> echo "Usage: wifit <interface> <essid> [Optional: <key>]"<br /> echo " Example: wifit wlan0 somenet "<br /> echo " Example: wifit wlan0 somenet mypassword "<br /> echo "-------------------------------------------------"<br />else<br /> echo "Setting up wifi connection for "<br /> echo "Interface $1, ESSID: $2..."<br /><br /> iwconfig $1 essid $2<br /> iwlist $1 scan<br /> iwconfig $1 mode Managed<br /> if [ -n $3 ] ; then<br />  iwconfig $1 key restricted s:$3<br /> else<br />  iwconfig $1 key open<br />  iwconfig ap any<br /> fi<br /> iwconfig commit<br /> dhclient<br />fi</pre>  <br />To use this, just copy and paste the code above into a file named wifit (or wifit.sh, or whatever you want).  You'll then need to make that file executable using chmod:<pre>chmod a+x wifit.sh</pre>Then, simply call the script (possibly using sudo) passing  it any arguments you need:<pre>sudo ./wifit wlan0 somenetwork</pre><br />Alternatively, you could place this file in your /usr/local/bin or /usr/bin directories so that it would be included in your PATH.  If you find this useful, or if you decide to add to is, feel free to <a href="http://bradmontgomery.net/show.php?page=contact">Contact Me</a>!<br /><br />Enjoy.<div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/4123748873183487963-2958546588737408191?l=bradmontgomery.blogspot.com' alt='' /></div>