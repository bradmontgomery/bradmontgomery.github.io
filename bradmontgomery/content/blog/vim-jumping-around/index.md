---
date: '2012-11-12T17:51:31+00:00'
title: 'Vim: Jumping around!'
draft: false
tags:
- editor
- unix
- vi
- vim
slug: vim-jumping-around
description: <p>So what happens w...
markup: html
url: /blog/vim-jumping-around/
aliases:
- /blog/2012/11/12/vim-jumping-around/

---

<p>So what happens when you open a file in vim, and you're presented with lots of content? Say, 5000 lines of something.</p>

<p>Well, I typically start searching for things: <code>/keyword</code>. That works great <em>when you know what you're
looking for</em>. But it breaks down quickly when you don't. So, today's vim post is about <em>moving faster</em> through pages of text.</p>

<h2>Jumping to a line number</h2>

<p>I have line numbers turned on by default (<code>:set nu</code>, if you don't). There are a couple of ways you can jump to specific line numbers.</p>
<ol>
<li><code>:42</code> will jump to line 42.</li>
<li><code>6G</code> will jump to line 6. (G is the "Go To" command).</li>
</ol>

<p>But jumping to line numbers still assumes you sort of know where you're going. (Well, kinda... I've got a bad habbit of just jumping to arbitrarily large line numbers; <code>:9999999</code>).</p>

<h2>Screen Scrolling</h2>

<p>Vim also lets you scoll through content either a full- or half-screen at a time. This is probably the more correct way to quickly skim through a file when you're unfamiliar with its content.</p>
<ul>
<li><code>^F</code>: move <em>Forward</em> a full screen (that's CTRL-F)</li>
<li><code>^B</code>: move <em>Backward</em> a full screen (that's CTRL-B)</li>
<li><code>^D</code>: move <em>forward</em> half-a screen (that's CTRL-D). D for <em>down</em></li>
<li><code>^U</code>: move <em>backward</em> half-a screen (that's CTRL-U). U for <em>up</em></li>
</ul>

<p>You can also scroll the whole screen so that the current position of the cursor moves to top of the screen. That is, if your cursor is on line 53, line 53 moves to the top of the screen. Do that with <code>z+Enter</code> (hit <em>z</em>, then hit <em>Enter</em> or <em>Return</em>).</p>

<p>Happy Vimming!</p>