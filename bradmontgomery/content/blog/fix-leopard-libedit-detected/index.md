---
date: '2011-01-05T15:58:04+00:00'
title: 'Fix: Leopard libedit detected.'
draft: false
tags: []
slug: fix-leopard-libedit-detected
description: <p>If you use <a hre...
markup: html
url: /blog/fix-leopard-libedit-detected/
aliases:
- /blog/2011/01/05/fix-leopard-libedit-detected/

---

<p>If you use <a href="http://ipython.scipy.org/" _mce_href="http://ipython.scipy.org/">iPython</a> on OS X, you've probably seen this: <code>Leopard libedit detected.</code>, and then noticed some very quirky behavior related to spacing, and command history.  In short, that behavior is related to default version of the <code>readline</code> library bundled in OS X (It's not GNU readline). </p> 

<p>If you use pip and virtualenv, just instalilng readline doesn't help. So, how do you fix this?&nbsp;Well, the <em>quick and dirty</em> way to fix this is with:</p><pre>easy_install -a readline</pre>

<p>For the whole story, see this discussion:
<a href="https://groups.google.com/forum/#!topic/python-virtualenv/BEQAurh9EZw/discussion" _mce_href="https://groups.google.com/forum/#!topic/python-virtualenv/BEQAurh9EZw/discussion">https://groups.google.com/forum/#!topic/python-virtualenv/BEQAurh9EZw/discussion</a></p>

<p>Many thanks to <a href="http://twitter.com/idangazit/" _mce_href="http://twitter.com/idangazit/">@idangazit</a> for <a href="http://twitter.com/idangazit/status/22268724274798593" _mce_href="http://twitter.com/idangazit/status/22268724274798593">this tweet</a> which helped me find this "<em>solution</em>".</p>