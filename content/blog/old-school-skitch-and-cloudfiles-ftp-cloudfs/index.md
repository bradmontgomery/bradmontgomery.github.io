---
date: '2014-01-28T14:55:24.172398+00:00'
title: Old-school Skitch and CloudFiles with ftp-cloudfs
draft: false
tags:
- cloudfiles
- ftpcloudfs
- python
- rackspace
- skitch
slug: old-school-skitch-and-cloudfiles-ftp-cloudfs
description: ''
url: /blog/old-school-skitch-and-cloudfiles-ftp-cloudfs/
aliases:
- /blog/2014/01/28/old-school-skitch-and-cloudfiles-ftp-cloudfs/

---

I'm an unabashed fan of Skitch . The old one (pre-Evernote acquisition). A lot of folks have written about how to acquire this and how they use it. Until recently, I just used the built-in *SFTP* support to upload files to a Rackspace CloudServer .

Lately however, I've been trying to limit the amount of stuff I have on servers that I have to maintain. One way I've been doing that is to push everything that looks like a *static website* into CloudFiles .

So the question is, "**How do I make the old Skitch work with CloudFiles?**" It's a little bit of work, but not too terribly bad. Here's how I made it happen. It's a little python-centric (which is OK by me, because I'm a python developer).

1. Create a virtualenv . We're going to install an open-source python library. I named my virtualenv, ftp-cloudfs.
2. Run pip install ftp-cloudfs.
3. Now, you can run the following command: ftpcloudfs -a https://auth.api.rackspacecloud.com/v1.0

This will run a local FTP server which will transparently push files up to CloudFiles. Now you need to configure Skitch (screenshot) .

1. Access Skitch's Preferences
2. Click on the Share tab.
3. Add an FTP Account Type.
4. Your Server should be 127.0.0.1
5. The port is 2021 (the default for ftp-cloudfs, though you can change this)
6. Use your Rackspace username.
7. Your password should be your rackspace cloud API Key (find or create this in your Account Settings .
8. The Directory will be the name of your CloudFiles container, and plus any subdirectory structure that you have. For example, I have a container named static, and I want my uploaded files to appear to be in an uploads directory. So, Skitch's Directory setting should be static/uploads.
9. Finally, add your CloudFiles Container's target domain as Skitch's Base URL. I'm assuming that you created a container to use as a *Static Website*. This look something like *http://some-really-long-hash.something.rackcdn.com/uploads*

If you've done everything correctly so far, you should be able to Skitch and upload to CloudFiles. Keep in mind, though, that you'll have to make sure the ftpcloudfs command (from above) is running every time you want to upload an image. There are ways to do this automatically (see this SO question ), but I've just left the command running in a Terminal window.

Be sure to take a look at ftpcloudfs --help to see what else is available in this nifty app. Enjoy!
