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
description: ''
markup: md
url: /blog/vim-jumping-around/
aliases:
- /blog/2012/11/12/vim-jumping-around/

---

So what happens when you open a file in vim, and you're presented with lots of content? Say, 5000 lines of something.


Well, I typically start searching for things: `/keyword`. That works great *when you know what you're
looking for*. But it breaks down quickly when you don't. So, today's vim post is about *moving faster* through pages of text.


Jumping to a line number
------------------------


I have line numbers turned on by default (`:set nu`, if you don't). There are a couple of ways you can jump to specific line numbers.


1. `:42` will jump to line 42.
2. `6G` will jump to line 6. (G is the "Go To" command).


But jumping to line numbers still assumes you sort of know where you're going. (Well, kinda... I've got a bad habbit of just jumping to arbitrarily large line numbers; `:9999999`).


Screen Scrolling
----------------


Vim also lets you scoll through content either a full- or half-screen at a time. This is probably the more correct way to quickly skim through a file when you're unfamiliar with its content.


* `^F`: move *Forward* a full screen (that's CTRL-F)
* `^B`: move *Backward* a full screen (that's CTRL-B)
* `^D`: move *forward* half-a screen (that's CTRL-D). D for *down*
* `^U`: move *backward* half-a screen (that's CTRL-U). U for *up*


You can also scroll the whole screen so that the current position of the cursor moves to top of the screen. That is, if your cursor is on line 53, line 53 moves to the top of the screen. Do that with `z+Enter` (hit *z*, then hit *Enter* or *Return*).


Happy Vimming!

