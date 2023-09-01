---
date: '2007-01-03T21:15:00+00:00'
title: Blocking outgoing UDP traffic using iptables
draft: false
tags:
- Linux
- networking
slug: blocking-outgoing-udp-traffic-using-iptables
description: Since rebuilding my ...
markup: html
url: /blog/blocking-outgoing-udp-traffic-using-iptables/
aliases:
- /blog/2007/01/03/blocking-outgoing-udp-traffic-using-iptables/

---

Since rebuilding my server (after having it used to propogate a UDP flood DoS attack), I&rsquo;ve been advised that I should set up iptables to block any unnecessary outbound UDP traffic.  So, how do I do this?<br />Well, the first thing I&rsquo;ll do is update my apt repository, and install iptables using the following two commands:<br /><pre>apt-get update<br />apt-get install iptables</pre><br />Now, the quick and dirty solution is to just add append a rule that blocks all outgoing UDP packets from my server. You can do this based on the systems IP addess.  Assuming my server&rsquo;s IP addess is 192.168.0.1, I would use the following rule:<pre>iptables -A OUTPUT -s 192.168.0.1 -p udp -j DROP</pre><br />Essentially, this rule says, match any outbound UDP packets whose source address (-s) is 192.168.0.1, and jump (-j) to the DROP chain.  That will drop the packet.  Now, just to be safe, I&rsquo;ll add the same rool using my loopback address, as follows:<pre>iptables -A OUTPUT -s 127.0.0.1 -p udp -j DROP</pre> <br />Now, let&rsquo;s just hope that keeps me covered until I can find a little more advanced solution that will also write to a log when a packet gets dropped...<br /><br /><b>Resources:</b><ul><li><a href="http://www.netfilter.org/documentation/HOWTO/packet-filtering-HOWTO-7.html">netfilter&rsquo;s documentation</a></li><br /><li><a href="http://www.linuxquestions.org/questions/showthread.php?t=385165">linuxquestions.org forums</a></li><br /><li>The manpage!  (man iptables)</li><br /></ul><div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/4123748873183487963-7802155410853194174?l=bradmontgomery.blogspot.com' alt='' /></div>