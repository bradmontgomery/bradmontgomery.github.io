---
date: '2009-01-05T19:29:00+00:00'
title: Add a Context Processor for your Django app using Sites
draft: false
tags:
- Programming
- Python
- django
slug: add-a-context-processor-for-your-django-app-using-sites
description: ''
markup: md
url: /blog/add-a-context-processor-for-your-django-app-using-sites/
aliases:
- /blog/2009/01/05/add-a-context-processor-for-your-django-app-using-sites/

---

I've recently refactored a significant number of my Django Apps so that they include the "[sites](http://docs.djangoproject.com/en/dev/ref/contrib/sites/#ref-contrib-sites)" framework. Essentially, this allows me to use the same code (and database) for multiple sites.

For Example, if I was was building a CMS (and I am!), I might have a model that defines a "page":


```
from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

class Page(models.Model):
    title = models.CharField('title', max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User)
    sites = models.ManyToManyField(Site,
                  help_text="This page will be displayed on the selected Sites")
```


Note that the Page class has a [ManyToManyField](http://docs.djangoproject.com/en/dev/ref/models/fields/#manytomanyfield) relation ship to a Django Site, which allows a page to be associated with one or more Sites. The neat thing about this, is that when I publish content on a Page, it can be published to one or more sites!

While working with this, I discovered I often wanted to write template code that *knew* which which Site it was associated. For example, I might have a base template containing a block inside html head elements so templates that inherit it can include external javascript or CSS files. For example, *base.html* might include the following:

```
<html>
<head>
<title>
    {% block title %}{% endblock %}
</title>
    {% block head %} {% endblock %}
</head>
```


Then, in any template that inherits from base.html, I could do something like the following:

```

{% extends "base.html" %}
{% block head %}
    {% ifequal current_site.domain "www.whatever.com" %}
        <link rel="stylesheet" type="text/css" href="/media/whatever.css" />
    {% endifequal %}
{% endblock %}

```


There trick here, though, is "How is my template going to know what site is being requested?"

I *could* put something like the following in **every** view I write...

```
current_site = Site.objects.get_current()
```
BUT, that's a lot of extra stuff to type. Especially if you have a lot of views.

The clever thing to do, would be to write code so that a Site object containing the currently requested site is automatically added to the current [Context](http://docs.djangoproject.com/en/dev/ref/templates/api/#basics). We can do that by writing our own **Context Processor**!

And that's just what I did! The following code is fairly simple. It just retrieves the current Site from given request object (using Site.objects.get_current()), then returns a dictionary mapping the current site to the variable name **current_site**.

```
from django.conf import settings
from django.contrib.sites.models import Site

def current_site(request):
'''
A context processor to add the "current site" to the current Context
'''
    try:
        current_site = Site.objects.get_current()
        return {
            'current_site': current_site,
        }
    except Site.DoesNotExist:
        # always return a dict, no matter what!
        return {'current_site':''} # an empty string
```


For this to work, we've got to add the function above to the list of TEMPLATE_CONTEXT_PROCESSORS in our project settings file. My project directory is called "mysite", so I created a folder called "context_processors", and in it, I created a file called "current_site.py". That file contains the function *current_site* defined above.

To get my new context processor working, I've got to edit mysite/settings.py, which now looks something like the following:

```
TEMPLATE_CONTEXT_PROCESSORS = (
    "mysite.context_processors.current_site.current_site",
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
)

```


Voila! Now, while writing template code, I can always access the *current_site* variable!![](https://blogger.googleusercontent.com/tracker/4123748873183487963-4532705687996021665?l=bradmontgomery.blogspot.com)
