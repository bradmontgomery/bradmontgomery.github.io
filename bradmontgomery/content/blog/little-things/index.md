---
date: '2013-12-29T18:50:15.583798+00:00'
title: The little things
draft: false
tags:
- generators
- lambda
- map
- python
slug: little-things
description: <p>I ran across an i...
markup: html
url: /blog/little-things/
aliases:
- /blog/2013/12/29/little-things/

---

<p>I ran across an interesting line of code today, and thought I'd share some
insights. First, though we need a little context. Imagine reading several lines
of data from a csv file (using
<a href="http://docs.python.org/2/library/csv.html">python's built-in
<code>csv</code> module</a>). You'll typically have some code that looks
something like this:</p>

<pre><code class="python">import csv
with open('data.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # Do some stuff with each row,
        # where the row is a list of strings.</code></pre>

<p>So, that's what we've got, and within the <code>for</code> loop, I found
this code:</p>

<pre><code class="python">row = map(lambda x: x.strip(), row)</code></pre>

<p>What does it do? It simply strips whitespace from the beginng and ending of
each item in our list of strings. But <em>how</em> it accomplishes this is worth
picking apart.</p>

<p>First, this code uses <code>map</code> to apply a function to each item in
the list. Then, we construct an anonymous <code>lambda</code> function which
accepts a parameter, calls the input's <code>strip</code> method and returns
the result.</p>

<p>Essentially, we call a function for each item in the list. Keep in mind,
we're also doing this inside a <code>for</code> loop. That's a function call
for each cell in your CSV file.</p>

<p>We can also achieve the same outcome with a list comprehension:</p>
<pre><code class="python">row = [x.strip() for x in row]</code></pre>

<p>OR with a generator! (note the parenthesis instead of square brackets)</p>
<pre><code class="python">row = (x.strip() for x in row)</code></pre>

<h2>Measure it</h2>
<p>Out of curiosity, I decided to time this with just a few rows of data
(10, in particular). I used <code>timeit</code> to run this code on my
laptop (a late-2011 macbook air) with some simple data. Here's what I found:</p>

<pre><code class="python">&gt;&gt;&gt; import timeit
&gt;&gt;&gt; timeit.timeit(
...    stmt="map(lambda x: x.strip(), row)",
...    setup="row = [' {0} '.format(i) for i in range(10)]"
... )
2.491640090942383
</code></pre>

<p>With 1,000,000 rows of data (the default number of test iterations, and
an admittedly unlikely scenario for a one-off CSV import) this code runs in
about two and a half seconds.</p>

<p>Now lets see how the list comprehension and generator versions for the
same code stack up!</p>

<pre><code class="python">&gt;&gt;&gt; timeit.timeit(
...    stmt="[x.strip() for x in row]",
...    setup="row = [' {0} '.format(i) for i in range(10)]"
... )
1.6442670822143555
</code></pre>

<p>Quite a bit better! <em>Nearly</em> a second faster. Let's see about
the generator:</p>

<pre><code class="python">&gt;&gt;&gt; timeit.timeit(
...    stmt="(x.strip() for x in row)",
...    setup="row = [' {0} '.format(i) for i in range(10)]"
... )
0.48253297805786133
</code></pre>

<p>Yep. About two whole seconds faster than our original code.</p>

<p>So what's the take-away, here?  Well,
<a href="http://www.python.org/dev/peps/pep-0289/">generator expressions</a>
are pretty amazing. <strong>Use them</strong>.</p>

<p>Finally, small things add up. Little decisions, like whether to use
<code>map</code> + <code>lambda</code> or a generator expression can have
fairly significant impact on the performance of your software.</p>