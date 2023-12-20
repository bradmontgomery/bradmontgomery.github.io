---
date: '2011-01-05T15:58:04+00:00'
title: 'Fix: Leopard libedit detected.'
draft: false
tags: []
slug: fix-leopard-libedit-detected
description: ''
markup: md
url: /blog/fix-leopard-libedit-detected/
aliases:
- /blog/2011/01/05/fix-leopard-libedit-detected/

---

If you use [iPython](http://ipython.scipy.org/) on OS X, you've probably seen this: `Leopard libedit detected.`, and then noticed some very quirky behavior related to spacing, and command history. In short, that behavior is related to default version of the `readline` library bundled in OS X (It's not GNU readline). 


If you use pip and virtualenv, just instalilng readline doesn't help. So, how do you fix this? Well, the *quick and dirty* way to fix this is with:


```
easy_install -a readline
```

For the whole story, see this discussion:
<https://groups.google.com/forum/#!topic/python-virtualenv/BEQAurh9EZw/discussion>


Many thanks to [@idangazit](http://twitter.com/idangazit/) for [this tweet](http://twitter.com/idangazit/status/22268724274798593) which helped me find this "*solution*".

