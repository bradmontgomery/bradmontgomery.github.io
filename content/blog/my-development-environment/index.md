---
date: '2014-06-25T03:12:55.160380+00:00'
title: My Development Environment
draft: false
tags:
- development
- environment
- software
- tools
slug: my-development-environment
description: ''
url: /blog/my-development-environment/
aliases:
- /blog/2014/06/25/my-development-environment/

---

Every once in a while, I like to step back and take a look at the tools that I
use. I don't change my development environment very often, but I do periodically
pull in a new tool here and there. Sometimes they *fit* into my workflow, and
sometimes they don't.

As far as I know, I've never written my thoughts down when doing this, but
in an attempt to keep in line with my Write more. Share more. goal from the beginning of the year,
this seems like a good time to start.

## The Editor

I use MacVim, and I feel fairly
proficient, though I'm certainly not a power user. I keep a fairly light-weight
set of addons.

1. I still use pathogen. It works for me.
 I don't fool around with git submodules; I just put .vim/bundle in my .gitignore.
2. I use nerdtree and nerdcommenter
3. syntastic keeps me out of trouble.
4. vim-flake8 helps keep my python looking A-OK.
5. Too keep things aesthetically pleasing (perhaps more important that you might
 think!), I use set t\_Co=256 and colorscheme desert256 with
 Anonymous Pro,
 set guifont=Anonymous\ Pro:h16.

## Development

Most of my time is spent writing Python, and building Django apps. So of course,
I'm using Django and a whole host of open-source things, but a little lower down
the stack, here's what a typical day might look like:

* I use vagrant to fire up **two** virtual machines
 (backed by VirtualBox) running Ubuntu. Currently 12.04 for my most purposes,
 but my personal projects are running on both 13.10 and 14.04.
* VM #1 is your typicall *all-in-one* box running PostgreSQL and nginx which
 proxies to django's development server (*side note: It took me far too long
 to do this, but letting nginx serve your static media instead of django's
 development server is really awesome*)
* VM #2 is really just a secondary database box. Do you use multiple databases
 in production? If so, then you do during development, too, right? This box
 also runs an instance of memcached (which I
 sometimes enable during development) and Elasticsearch
 (when I need it).
* All of this runs on my scrappy little 2011 Macbook Air (still running 10.8) with
 4Gb of ram, where I do all my editing and my git stuff.
* I use both Chrome and Firefox for front-end work, along with jQuery, and a
 host of plugins and other small tools like underscore.js and
 moment.js.

## Miscellany

I still read the Django Docs online, and
I google for a lot of things, which lands me at stackoverflow
fairly regularly, though no so much that I noticed the recent downtime (my friends
in irc told me about it first).

Google Hangouts keeps me connected with the rest of the team, and though things like
Slack and HipChat seem to
be all the rage, our team is small enough that Hangouts just work.

Honorable mentions go to Trello and Github
just because both sites are a huge part of my daily development workflow.

## Wrapping Up

That's pretty much it. It's not at all fancy, and in fact, I tend to like
simple tools, but I'm always open to trying things to make me more productive
(You know, the old *work smarter not harder* mantra).

Do you see a gaping hole in what I'm doing? Am I missing something blatently
obvious? Let me know in the comments! :)
