---
date: '2007-02-08T21:09:00+00:00'
title: wifit - an iwconfig tool
draft: false
tags:
- Linux
- networking
- wifi
slug: wifit-an-iwconfig-tool
description: ''
markup: md
url: /blog/wifit-an-iwconfig-tool/
aliases:
- /blog/2007/02/08/wifit-an-iwconfig-tool/

---

I've recently installed [Mepis Linux](http://www.mepis.org/) on a couple of laptops (a Compaq Presario 2195US and a Dell Latitude D610, both of which use [NdisWrapper](http://ndiswrapper.sourceforge.net/) for wifi drivers).I'm fairly mobile, so I needed a way to quickly change my wireless settings. I wrote this simple bash script to let me do that, and I thought I'd just share it.  

```
  
#!/bin/bash  
  
## wifit - the wifi tool  
## This is a script that accepts a wifi-enabled interface,   
## essid, and an optional ascii key for a wifi network connection  
  
if [ $# -lt 2 ] || [ $# -gt 3 ] ; then   
 echo "wifit - the wifi tool"  
 echo "-------------------------------------------------"  
 echo "Usage: wifit   [Optional: ]"  
 echo " Example: wifit wlan0 somenet "  
 echo " Example: wifit wlan0 somenet mypassword "  
 echo "-------------------------------------------------"  
else  
 echo "Setting up wifi connection for "  
 echo "Interface $1, ESSID: $2..."  
  
 iwconfig $1 essid $2  
 iwlist $1 scan  
 iwconfig $1 mode Managed  
 if [ -n $3 ] ; then  
 iwconfig $1 key restricted s:$3  
 else  
 iwconfig $1 key open  
 iwconfig ap any  
 fi  
 iwconfig commit  
 dhclient  
fi
```
   
To use this, just copy and paste the code above into a file named wifit (or wifit.sh, or whatever you want). You'll then need to make that file executable using chmod:
```
chmod a+x wifit.sh
```
Then, simply call the script (possibly using sudo) passing it any arguments you need:
```
sudo ./wifit wlan0 somenetwork
```
  
Alternatively, you could place this file in your /usr/local/bin or /usr/bin directories so that it would be included in your PATH. If you find this useful, or if you decide to add to is, feel free to [Contact Me](http://bradmontgomery.net/show.php?page=contact)!  
  
Enjoy.