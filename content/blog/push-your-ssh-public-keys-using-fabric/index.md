---
date: '2009-04-30T15:45:00+00:00'
title: Push Your SSH Public keys using Fabric
draft: false
tags:
- Python
- fabric
slug: push-your-ssh-public-keys-using-fabric
description: ''
markup: md
url: /blog/push-your-ssh-public-keys-using-fabric/
aliases:
- /blog/2009/04/30/push-your-ssh-public-keys-using-fabric/

---

This came across my twitter radar today from *[@bitprophet](http://twitter.com/bitprophet/)* (aka: Jeff Forcier), who just happens to be the new maintainer for [Fabric](http://www.nongnu.org/fab/):  
  

```
def push\_key():  
    keyfile = '/tmp/%s.pub' % env.user  
    run('mkdir -p ~/.ssh && chmod 700 ~/.ssh')  
    put('~/.ssh/id\_rsa.pub', keyfile)  
    run('cat %s >> ~/.ssh/authorized\_keys' % keyfile)  
    run('rm %s' % keyfile)  

```
  
  
Everything you need to push your public key to an external server using Fabric.![](https://blogger.googleusercontent.com/tracker/4123748873183487963-1296451718188870554?l=bradmontgomery.blogspot.com)