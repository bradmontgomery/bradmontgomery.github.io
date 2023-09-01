---
date: '2013-10-12T04:29:57.421012+00:00'
title: Getting the Most out of ack
draft: false
tags:
- ack
- grep
- tools
slug: getting-most-out-ack
description: <p><code>ack</code> ...
markup: html
url: /blog/getting-most-out-ack/
aliases:
- /blog/2013/10/12/getting-most-out-ack/

---

<p><code>ack</code> is an amazing tool. If you're not familiar with it,
it's a lot like grep (the official site is at <a href="http://beyondgrep.com/">beyondgrep.com</a>).
It's a command-line tool that helps you find things in files, particularly source code.
However, like a lot of command-line tools, it's all-too-easy to learn just the
basics and forget that many of these tools can do so much more!</p>

<p>Without further ado, here are a few of the ways I frequently use <code>ack</code> while working with Django.</p>

<h2>Ignoring folders</h2>
<p>It's so frustrating to search for a snippet of python code, only to have your
screen fill up with irrelevant results (I'm looking at you migrations and css files!)</p>

<p>When this happens, just ignore the stuff you don't need:</p>

<pre class="bash"><code>ack --ignore-dir=myapp/migrations</code></pre>

<h2>Ingoring files</h2>
<p>While we're at it, you can also ignore specific files, or any file that matches
a regex. Perhaps you're looking for reference to a Django model, but you don't need
to know that it's in models.py, so just ignore that file!</p>

<pre class="bash"><code>ack --ignore-file=match:models.py SomeModel</code></pre>

<p>Better, but you might also want to ignore that model.js file (or perhaps it's
called model_views.js). You can do that with a simple regex! And while we're at it,
lets go ahead and ignore any migrations:</p>

<pre class="bash"><code>ack --ignore-file=match:/^model/ --ignore-dir=migrations/ SomeModel</code></pre>

<h2>Just Python, please</h2>

<p><code>ack</code> also lets you restrict searches to specific file types:</p>
<pre class="bash"><code>ack --type=python SomeModel</code></pre>

<p>There's also a shortcut for this:</p>
<pre class="bash"><code>ack --python SomeModel</code></pre>

<p>Or ruby if you prefer:</p>
<pre class="bash"><code>ack --ruby 'def foo'</code></pre>

<p>Similarly, you can tell ack to ignore any files that it doesn't understand with
the <code>-k</code> or <code>--known-types</code> flag.</p>

<pre class="bash"><code>ack -k SomeCode</code></pre>

<p>To get a list of all the filetypes that <code>ack</code> knows about, just run:</p>
<pre class="bash"><code>ack --help-types</code></pre>


<h2>Be insensitive!</h2>
<p>For some reason, I sometimes forget that default searches are case sensitive.
If, like me, you're pronE tO TYpos, you can perform case insensitive searches with:</p>
<pre class="bash"><code>ack -i whatever</code></pre>


<h2>Digging deeper</h2>
<p>As you might have noticed, <code>ack</code> comes with some default behavior.
You can inspect these defaults with:</p>
<pre class="bash"><code>ack --dump</code></pre>

<p>Now, if you want to start customizing this behavior, create an <code>.ackrc</code> file,
and tweak it to your heart's content. A good way to get started is to let ack generate
this file for you! (<strong>careful!</strong> this command will overwrite your
<code>.ackrc</code> file if you already have one.)</p>

<pre class="bash"><code>ack --create-ackrc &gt; ~/.ackrc</code></pre>

<h2>Have some fun</h2>
<p>The <code>ack</code> developers are not without a sense of humor. Certainly
you should take the time to investigate all of the following:</p>

<pre class="bash"><code>ack --bar
ack --cathy
ack --thpppt</code></pre>

<h2>Wrapping Up</h2>
<p>There's <em>so much more</em> to <code>ack</code> than what I've listed here.
Do yourself a favor and periodically skim the output of <code>ack --help</code>,
then take some time to look through the manpage (<code>man ack</code>).</p>

<p>Happing searching!</p>