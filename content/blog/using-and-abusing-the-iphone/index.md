---
date: '2007-07-04T20:47:00+00:00'
title: Using (and Abusing) the iPhone
draft: false
tags:
- iPhone
slug: using-and-abusing-the-iphone
description: ''
markup: md
url: /blog/using-and-abusing-the-iphone/
aliases:
- /blog/2007/07/04/using-and-abusing-the-iphone/

---

OK... so for part 2 of my iPhone saga:  
We went to visit some family today, and of course I took my iPhone. For the most part, I've really tested out the camera today. I'm no guru, but I'm very happy with how quickly the iPhone takes pictures. Since my girls are now 4 and 2, this is a very important feature!! I've also got an HP Photosmart M527, and my non-scientific opinion is that the iPhone takes photos about as twice as fast as my HP. (Of course, it's a 2-megapixel camera vs. a 6-megapixel camera)  
  
Just to give you an idea, here's a picture of my youngest daughter: [![](http://bradmontgomery.net/files/iPhone/iphone_photo_thumb.png)](http://bradmontgomery.net/files/iPhone/iphone_photo.jpg)  
  
I convinced my wife (OK, so she offered :)) to drive home from out festivities today, so I could play with the iPhone in the car. While in town, I had no problems browsing the web or checking my email using the EDGE connection. However, once we got out of town, there were several locations where I had no network connection (this is rural NE Arkansas...)  
  
Another thing that I've noticed is that there are a **LOT** of unsecured wireless networks... but that's for another blog!   
  
**As for typing on the iPhone**, I'm fairly impressed with it's ability to suggest and correct misspelled words. Now, I don't really think that I have large fingers, but I very frequently misspelled words using the iPhone. However, the iPhone "guessed" what I wanted about 80% of the time! Things like "sxgppl" were correctly identified as "school" (As as side note, I'd guesstimate that I touch type somewhere around 60wpm with 90% accuracy, if anyone cares)So, when typing on the iPhone, I found myself just ignoring what I typed in hopes that the phone could figure it out. Overall, I'm impressed.  
  
Now that I'm home, the geek in me is dieing to portscan this thing! So here goes! First a basic portmap with nmap:  

```
  
nmap 192.168.0.11  
  
Starting Nmap 4.20 ( http://insecure.org ) at 2007-07-04 19:41 CDT  
All 1697 scanned ports on 192.168.0.11 are closed  

```
  
Interesting enough... let's see what OS nmap thinks is running on this thing:  

```
  
sudo nmap -O 192.168.0.11  
  
Starting Nmap 4.20 ( http://insecure.org ) at 2007-07-04 19:43 CDT  
Warning:  OS detection for 192.168.0.11 will be MUCH less reliable because we did not find at least 1 open and 1 closed TCP port  
All 1697 scanned ports on 192.168.0.11 are closed  
MAC Address: 00:1B:63:E1:ED:D8 (Unknown)  
Device type: general purpose  
Running: Apple Mac OS X 10.3.X|10.4.X|10.5.X, FreeBSD 4.x  
OS details: Applie Mac OS X 10.3.9 - 10.4.7, Apple Mac OS X 10.4.8 (Tiger), OS X Server 10.5 (Leopard) pre-release build 9A284, FreeBSD 4.10-RELEASE (x86)  
Network Distance: 1 hop  
  
OS detection performed. Please report any incorrect results at http://insecure.org/nmap/submit/ .  
Nmap finished: 1 IP address (1 host up) scanned in 16.991 seconds
```
  
  
So, while I'm not really a security professional, and I know these are very basic scans, it seems like there's no blatantly obvious security gaps in the iPhone (through its wifi connection anyway). If anybody has any more advanced nmap scans they'd like to see performed, just let me know.