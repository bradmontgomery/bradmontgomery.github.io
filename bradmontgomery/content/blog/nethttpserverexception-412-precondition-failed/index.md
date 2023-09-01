---
date: '2012-02-05T20:15:19+00:00'
title: 'Net::HTTPServerException: 412 "Precondition Failed"'
draft: false
tags:
- chef
slug: nethttpserverexception-412-precondition-failed
description: <p>So, I've been wor...
markup: html
url: /blog/nethttpserverexception-412-precondition-failed/
aliases:
- /blog/2012/02/05/nethttpserverexception-412-precondition-failed/

---

<p>So, I've been working with <a href="http://www.opscode.com/chef/" _mce_href="http://www.opscode.com/chef/">Chef</a> quite a bit, lately. Every once in a while, I'll bootstrap a new node and it fails with this:</p>
<pre><code>Net::HTTPServerException: 412 "Precondition Failed"</code></pre>
<p>Every single time this has happened to me, I've had stop and scratch my head. <em>Why can't I remember what causes this!?</em> Well, in my case it's usually a misspelled cookbook or recipe name. For example, I might have a <code>role</code> that looks something like this:</p><pre><code class="ruby">name "sample-server"
description "sample apache server"
run_list "role[apache::default]"
</code></pre><p>Can you spot the problem? The opscode cookbook for apache is named <strong>apache2</strong>!</p><pre><code class="ruby">name "sample-server"
description "sample apache server"
run_list "role[apache2::default]"
</code></pre>
<p>So, one complaint that I have about chef is that <code>Net::HTTPServerException: 412 "Precondition Failed"</code> should probably say something like <code>Net::HTTPServerException: 412 "Couldn't find cookbook 'apache'"</code>. Oh well... <em>C'est la vie</em></p>