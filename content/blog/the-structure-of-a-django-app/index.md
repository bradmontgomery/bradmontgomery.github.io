---
date: '2008-07-15T10:57:00+00:00'
title: The Structure of a Django App
draft: false
tags:
- Programming
- Python
- django
- web
slug: the-structure-of-a-django-app
description: ''
markup: md
url: /blog/the-structure-of-a-django-app/
aliases:
- /blog/2008/07/15/the-structure-of-a-django-app/

---

[Previously](http://bradmontgomery.blogspot.com/2008/06/lions-tigers-and-web-development.html), I'd lamented the difficultly present in choosing an web development framework. I'd worked through several [symfony](http://www.symfony-project.org/) tutorials, and though I could see the benefits down the road, it just didn't feel right to me (yes... "feel" is a technical drawback).  
  
So, I checked out a copy of [Django](http://www.djangoproject.com/), and I haven't looked back. If you're the least bit proficient with python, and you need to build a database-driven web site, USE DJANGO! They have superb [documentation](http://www.djangoproject.com/documentation/), a free book (the [The Django Book](http://djangobook.com/)), and there's a built-in development server included so you don't **have** to get Apache and mod-python (or some other webserver) running somewhere before you can start writing code.   
  
The fist thing that really made me like Django was the structure of it. First of all, a site is organized as a project. Multiple projects may be set up for different websites. Inside a project, you build an App. (Note that a project may have one or more Apps).  
  
The App is where you do most of your work, it really consists of four parts:1. Models
2. Views
3. The URLconf
4. Template(s)

   
  
**Models** (models.py) define your data. Instead of building tables in your database, you build python classes in your model. Django will give you the SQL to create your database tables. Now, what's really cool, is Django's Automatically generated Admin interface. All you really need is the model, and the Admin interface provides a password-protected, web-based, interface to your data.   
  
**Views** (views.py) are essentially functions that extract the correct data based on some (or no) input. Some may think this is an over-simplification, but in Django, the View is the "view of your data". The functions in your View will pass data back to the Templates where they are displayed.  
  
The **URLconf** (urls.py) is magic. Well, it sort of seems that way, but it just uses regular expressions to match urls and pass data to the View. So, "out of the box", Django supports pretty URLs so there's no need to do any url rewriting to get them.  
  
Last (but not least) are the **Templates**. Django sports it's own template language, and apparently it also supports a host of pre-existing template engines. I personally have never used existing template engines, so this is all a bit new to me. However, the Django template language appears both concise and powerful.  
  
Now, there's a bit more to it that what I've described here, but if you're wondering about Django (like I was), go ahead and check out [their overview](http://www.djangoproject.com/documentation/overview/), skim [the installaltion guide](http://www.djangoproject.com/documentation/install/), and then start working [the tutorial](http://www.djangoproject.com/documentation/tutorial01/). I did, and I haven't looked back.