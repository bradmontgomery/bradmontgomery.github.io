---
date: '2007-01-03T21:15:00+00:00'
title: Blocking outgoing UDP traffic using iptables
draft: false
tags:
- Linux
- networking
slug: blocking-outgoing-udp-traffic-using-iptables
description: ''
markup: md
url: /blog/blocking-outgoing-udp-traffic-using-iptables/
aliases:
- /blog/2007/01/03/blocking-outgoing-udp-traffic-using-iptables/

---

Since rebuilding my server (after having it used to propogate a UDP flood DoS attack), I’ve been advised that I should set up iptables to block any unnecessary outbound UDP traffic. So, how do I do this?  
Well, the first thing I’ll do is update my apt repository, and install iptables using the following two commands:  

```
apt-get update  
apt-get install iptables
```
  
Now, the quick and dirty solution is to just add append a rule that blocks all outgoing UDP packets from my server. You can do this based on the systems IP addess. Assuming my server’s IP addess is 192.168.0.1, I would use the following rule:
```
iptables -A OUTPUT -s 192.168.0.1 -p udp -j DROP
```
  
Essentially, this rule says, match any outbound UDP packets whose source address (-s) is 192.168.0.1, and jump (-j) to the DROP chain. That will drop the packet. Now, just to be safe, I’ll add the same rool using my loopback address, as follows:
```
iptables -A OUTPUT -s 127.0.0.1 -p udp -j DROP
```
   
Now, let’s just hope that keeps me covered until I can find a little more advanced solution that will also write to a log when a packet gets dropped...  
  
**Resources:*** [netfilter’s documentation](http://www.netfilter.org/documentation/HOWTO/packet-filtering-HOWTO-7.html)
  
* [linuxquestions.org forums](http://www.linuxquestions.org/questions/showthread.php?t=385165)
  
* The manpage! (man iptables)
  

