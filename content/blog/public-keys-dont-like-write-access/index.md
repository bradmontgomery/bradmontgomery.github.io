---
date: '2009-03-25T15:20:00+00:00'
title: Public Keys don't like write access!
draft: false
tags:
- Backup
- Linux
slug: public-keys-dont-like-write-access
description: ''
markup: md
url: /blog/public-keys-dont-like-write-access/
aliases:
- /blog/2009/03/25/public-keys-dont-like-write-access/

---

The first part of my [Automatic Backups with cron, tar, and SSH](http://bradmontgomery.blogspot.com/2007/01/automatic-backups-with-cron-tar-and-ssh.html) details how to set up remote login (sans passwords) using RSA public key.  
  
Apparently this doesn't work if your home directory allows groups or others write access. So if used *ssh-keygen -t rsa* to generate a public key which you added to a remote host (under *.ssh/authorized\_keys*), but ssh is still prompting you for a password, try setting your home directory's permissions to something like 0755 (or remove write permissions from other and groups)!![](https://blogger.googleusercontent.com/tracker/4123748873183487963-5225263534188052703?l=bradmontgomery.blogspot.com)