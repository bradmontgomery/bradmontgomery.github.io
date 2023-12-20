---
date: '2007-01-10T21:10:00+00:00'
title: Automatic Backups with cron, tar, and SSH
draft: false
tags:
- Backup
- Linux
- OS
- X
slug: automatic-backups-with-cron-tar-and-ssh
description: ''
markup: md
url: /blog/automatic-backups-with-cron-tar-and-ssh/
aliases:
- /blog/2007/01/10/automatic-backups-with-cron-tar-and-ssh/

---

Everyone knows that backups are important, but how many of us regularly back up our own websites, blogs, or whatever? Well, I've put together a relatively simple way for my Mac to log into my Linux-based webserver, archive some content, and download it for me. All of this is done Automatically, too!  
  
The first thing I had to do, was set up my home machine (a Mac, but any Unix-based system should work, too) so that it could log into a remote host without requiring me to type a password. This is accomplished by generating a public key, which I can store on my webserver. To do this, I opened a Terminal, and typed the following:
```
ssh-keygen -t rsa
```
 This generated the following output, and I accepted all default values... even the empty passphrase. This is important, because I don't want to type anything to log into my server!
```
  
Generating public/private rsa key pair.  
Enter file in which to save the key (/home/brad/.ssh/id_rsa):  
Enter passphrase (empty for no passphrase):   
Enter same passphrase again:   
Your identification has been saved in /home/brad/.ssh/id_rsa.  
Your public key has been saved in /home/brad/.ssh/id_rsa.pub.
```
  
  
Now, I need to store the public key (id\_rsa.pub) on my webserver. Again, from my Terminal (in my home directory), I issue the following command to log into my webserver (Note that you'd need to change the following command to fit your needs).  

```
cat .ssh/id_rsa.pub | ssh myusername@mywebserver.com 'cat >> .ssh/authorized_keys'
```
  
I'll need to type my password here, but after executing this command, I should be able to ssh into my remote server without ever typing my password again!  
  
Now that I've accomplished that, I need to write some simple bash scripts that will archive my web content. **On my Webserver:** For simplicity sake, let's save this in our home directory in a file named www.sh. Inside that file we put the following shell script, which uses tar to archive my web directory and then calls bzip2 to compress the tar file. Upon execution, I should have a file with a name similar to 2007-01-10.tar.bz2. Notice that you could also modify this script to invoke mysql\_dump or pg\_dump if you needed to backup a database as well!   

```
  
#!/bin/bash  
DATE=`date +%F`  # Grab the date  
TARFILE=$DATE-www.tar # Use it to create a filename  
tar -cf $TARFILE public_html  
bzip2 $TARFILE # compress the tarfile
```
  
  
Now that I have a script that will archive my content, I need to schedule a cron job to run it on a regular basis. I can use the following command to view my cron jobs
```
crontab -l
```
And, to edit my cron jobs, I just use:
```
crontab -e
```
This will open your system's default editor (vi for me), where we need to add the information that tells cron when to run our www.sh script. I added the following: 
```
30 1 * * * ~/www.sh
```
This tells cron to run my backup script every morning at 1:30am (system time). See [wikipedia](http://en.wikipedia.org/wiki/Cron) for more info on cron.  
  
Almost done! I've now got my webserver generating automatic nightly backups, but how can I transfer them to my local machine? Well, we'll make use of our newly generated public key to do this! First I need to write another simple bash script that will use scp to copy the backup that I generated on the server.**On my local machine**, I create a file called transfer.sh, which contains the following:  

```
#!/bin/bash  
DATE=`date +%F` # Grab the date  
# I'm downloading file with this name  
FILE=$DATE-www.tar.bz2   
  
# put the file on my local Desktop  
scp myusername@mywebserver.com:~/$FILE ~/Desktop  
  
# delete the file from the server  
ssh myusername@mywebserver.com rm -f ~/$FILE  

```
  
Now all I have to do is schedule a cron job on my local machine, and I've got an automatic website backup! Since I'm using Mac OS X, this works just like it does on a Linux box. In my terminal I type the following command:  

```
crontab -e
```
  
This opens vi for me, so I type the following, which will exectute my transfer.sh script every morning at 7:30am.  
  

```
  
30 7 * * * $HOME/transfer.sh  

```
  
  
That's It! One side note, however... the bash scripts that I've written must be executable by the user under which cron runs. Usually, the following command will make a file executable for its owner:  

```
chmod u+x filename
```
  
Resources:  
[debian-administration.org](http://www.debian-administration.org/articles/152)  
[Wikipedia](http://en.wikipedia.org/wiki/Cron)  
[linuxproblem.org](http://www.linuxproblem.org/art_9.html)![](https://blogger.googleusercontent.com/tracker/4123748873183487963-5549773385995764114?l=bradmontgomery.blogspot.com)