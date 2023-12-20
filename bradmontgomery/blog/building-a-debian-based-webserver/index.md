---
date: '2006-12-31T21:17:00+00:00'
title: Building a Debian-Based Webserver
draft: false
tags:
- Linux
slug: building-a-debian-based-webserver
description: ''
markup: md
url: /blog/building-a-debian-based-webserver/
aliases:
- /blog/2006/12/31/building-a-debian-based-webserver/

---

Well, my server was recently compromised and used to perform a UPD flood Denial of Service attack (or so my [provider](http://www.1and1.com/?k_id=7289629) claimed), so I’ve had to rebuild my server from scratch. Now, this seems like a daunting task, but it has actually been quite easy. I started out with a minimal Debian Linux system, and after a few apt-get install commands, and a few hours of uploading backups, I’m up and running again.  
  
How’d I do it? Well, i just set up my apt-sources:  
  

```
### debian  
# stable  
deb http://http.us.debian.org/debian stable main contrib non-free  
deb http://non-us.debian.org/debian-non-US stable/non-US main contrib non-free  
deb http://security.debian.org stable/updates main contrib non-free  
# testing  
deb http://http.us.debian.org/debian testing main contrib non-free  
# unstable  
deb http://http.us.debian.org/debian unstable main contrib non-free  
### dotdeb  
deb http://packages.dotdeb.org stable all  
deb-src http://packages.dotdeb.org stable all
```
  
Then I ran the following apt-get commands:  

```
apt-get update  
apt-get upgrade  
apt-get install libperl5.8  
apt-get install postgresql  
apt-get install libapache2-mod-php4  
apt-get install php4-pgsql  
apt-get install gd  
apt-get install php4-cli
```
  
And I’m all set! (yeah... I’ve still got a few PHP4 sites, and I grabbed the [PHP GD library](http://php.net/gd) and the [PHP command-line Interface](http://php.net/features.commandline)). Notice that I updated my apt sources before I started installing packages... this is kind of important! I also knew that I needed some perl libraries before installing [Postgresql](http://www.postgresql.org/) (my preferred database) All in all, things went fairly well. The worst part of (re)building this server was uploading my backups! (AND I CANNOT EXPRESS THE IMPORTANCE OF BACKUPS!)![](https://blogger.googleusercontent.com/tracker/4123748873183487963-2188106155647904337?l=bradmontgomery.blogspot.com)