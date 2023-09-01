---
date: '2006-12-31T21:17:00+00:00'
title: Building a Debian-Based Webserver
draft: false
tags:
- Linux
slug: building-a-debian-based-webserver
description: Well, my server was ...
markup: html
url: /blog/building-a-debian-based-webserver/
aliases:
- /blog/2006/12/31/building-a-debian-based-webserver/

---

Well, my server was recently compromised and used to perform a UPD flood Denial of Service attack (or so my <a href="http://www.1and1.com/?k_id=7289629">provider</a> claimed), so I&rsquo;ve had to rebuild my server from scratch.  Now, this seems like a daunting task, but it has actually been quite easy.  I started out with a minimal Debian Linux system, and after a few apt-get install commands, and a few hours of uploading backups, I&rsquo;m up and running again.<br /><br />How&rsquo;d I do it?  Well, i just set up my apt-sources:<br /><br /><pre>### debian<br /># stable<br />deb http://http.us.debian.org/debian stable main contrib non-free<br />deb http://non-us.debian.org/debian-non-US stable/non-US main contrib non-free<br />deb http://security.debian.org stable/updates main contrib non-free<br /># testing<br />deb http://http.us.debian.org/debian testing main contrib non-free<br /># unstable<br />deb http://http.us.debian.org/debian unstable main contrib non-free<br />### dotdeb<br />deb http://packages.dotdeb.org stable all<br />deb-src http://packages.dotdeb.org stable all</pre><br />Then I ran the following apt-get commands:<br /><pre>apt-get update<br />apt-get upgrade<br />apt-get install libperl5.8<br />apt-get install postgresql<br />apt-get install libapache2-mod-php4<br />apt-get install php4-pgsql<br />apt-get install gd<br />apt-get install php4-cli</pre><br />And I&rsquo;m all set! (yeah... I&rsquo;ve still got a few PHP4 sites, and I grabbed the <a href="http://php.net/gd">PHP GD library</a> and the <a href="http://php.net/features.commandline">PHP command-line Interface</a>).  Notice that I updated my apt sources before I started installing packages... this is kind of important!  I also knew that I needed some perl libraries before installing <a href="http://www.postgresql.org/">Postgresql</a> (my preferred database)  All in all, things went fairly well.  The worst part of (re)building  this server was uploading my backups!  (AND I CANNOT EXPRESS THE IMPORTANCE OF BACKUPS!)<div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/4123748873183487963-2188106155647904337?l=bradmontgomery.blogspot.com' alt='' /></div>