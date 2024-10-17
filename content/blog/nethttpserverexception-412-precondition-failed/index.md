---
date: '2012-02-05T20:15:19+00:00'
title: 'Net::HTTPServerException: 412 "Precondition Failed"'
draft: false
tags:
- chef
slug: nethttpserverexception-412-precondition-failed
description: ''
markup: md
url: /blog/nethttpserverexception-412-precondition-failed/
aliases:
- /blog/2012/02/05/nethttpserverexception-412-precondition-failed/

---

So, I've been working with [Chef](http://www.opscode.com/chef/) quite a bit, lately. Every once in a while, I'll bootstrap a new node and it fails with this:



```
Net::HTTPServerException: 412 "Precondition Failed"
```

Every single time this has happened to me, I've had stop and scratch my head. *Why can't I remember what causes this!?* Well, in my case it's usually a misspelled cookbook or recipe name. For example, I might have a `role` that looks something like this:


```
name "sample-server"
description "sample apache server"
run_list "role[apache::default]"

```
Can you spot the problem? The opscode cookbook for apache is named **apache2**!


```
name "sample-server"
description "sample apache server"
run_list "role[apache2::default]"

```

So, one complaint that I have about chef is that `Net::HTTPServerException: 412 "Precondition Failed"` should probably say something like `Net::HTTPServerException: 412 "Couldn't find cookbook 'apache'"`. Oh well... *C'est la vie*

