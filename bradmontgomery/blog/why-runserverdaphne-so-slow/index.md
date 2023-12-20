---
date: '2017-01-03T16:59:52.007696+00:00'
title: Why is runserver/daphne so slow?
draft: false
tags:
- channels
- daphne
- django
- node
- node_modules
- react
slug: why-runserverdaphne-so-slow
description: ''
markup: md
url: /blog/why-runserverdaphne-so-slow/
aliases:
- /blog/2017/01/03/why-runserverdaphne-so-slow/

---

\*\*(tl;dr) I installed django-channels and now my runserver command is very very slow. django-debug-toolbar was sort of the culprit (not really, because it was my own fault)\*\*

## The problem

I've just started a new project using [django-channels](https://channels.readthedocs.io/en/stable/). Websockets + channels is incredibly powerful, but I noticed something strange: While running django in debug mode, the development server was incredibly slow (on the average of 60s-90s per response).

After a bit of digging, it seemed that django-debug-toolbar was to blame, so I started turning off different panels to see what was the problem. Long story short: the `StaticFilesPanel` was taking a long time to generate it's data? 

## Here's why

1. I'm building a chat app using react, and it's in a django app named `chat`.
2. I've organized my react app so that it's \_inside\_ my django app's static directory, e.g. `my\_project/chat/static/my\_react\_chat`
3. As part of my front end development, I end up with a `node\_modules` directory with lots and lots of stuff.
4. In development, I'm using the [default staticfiles finders](https://docs.djangoproject.com/en/1.10/ref/settings/#std:setting-STATICFILES\_FINDERS) which will happily search through all of your django app's directories looking for static files. This takes some time when you a billion gigs worth of node modules.
5. Daphne's default timeout is 60s, and those static files finders take longer than that.

So, for the moment, I'll either disable the `StaticFilesPanel` while I'm working on my react app, or I'll just try to remember to blow away my `node\_modules` directory when I don't need it.

I've probably not got my react development organized quite right when integrating with a django app, but I'm doing what makes sense to me. Perhaps I should see what everyone else is doing. `¯\\_(ツ)\_/¯`