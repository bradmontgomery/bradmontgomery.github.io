---
date: '2015-09-03T20:12:42.347829+00:00'
title: Disabling the Forms in Django Rest Framework's Browsable API
draft: false
tags:
- api
- django
- djangorestframework
- python
- restframework
slug: disabling-forms-django-rest-frameworks-browsable-api
description: ''
markup: md
url: /blog/disabling-forms-django-rest-frameworks-browsable-api/
aliases:
- /blog/2015/09/03/disabling-forms-django-rest-frameworks-browsable-api/

---

If you're building a [RESTful](https://en.wikipedia.org/wiki/Representational_state_transfer) api using django, then you're probably aware
of [Django Rest Framework](http://www.django-rest-framework.org/).
It's a great project that will do a lot of the heavy lifting for you. It's also
got this really really nice featur: [the browsable api](http://www.django-rest-framework.org/topics/browsable-api/).


The browsable api gives you out-of-the box access to view your api, and even
to interact with it using some auto-generated forms. This is great during development, because you can quickly see exaclty how your api works. And the browsable api
is also great for production, because it doubles as public documentation (provided
you put some care and effort into your docstrings, but that's another post).


*However*, a lot of people seem to want to disable the browsable api's
forms for their production site. I think this makes sense, and I'm one of those people! Here's how I made it happen:


DRF uses a class to render the browsable api, aptly named the `BrowsableAPIRenderer`. When it generates its context, it creates a `display_edit_forms` variable, and we need to override that. So, we'll create own own renderer class:



```
from rest_framework.renderers import BrowsableAPIRenderer

class BrowsableAPIRendererWithoutForms(BrowsableAPIRenderer):
    """Renders the browsable api, but excludes the forms."""

    def get_context(self, *args, **kwargs):
        ctx = super().get_context(*args, **kwargs)
        ctx['display_edit_forms'] = False
        return ctx
```

You can put that anywhere in your project. I typically have a `utils`
app in most of my projects, so I put that in `utils/renderers.py`.


DRF uses a built-in setting to define a number of its renderes, so we need
to override the `DEFAULT_RENDERER_CLASSES`. My settings for DRF now
look something like this (including the setting for pagination):



```
REST_FRAMEWORK = {
    'PAGINATE_BY': 100,
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'utils.api.BrowsableAPIRendererWithoutForms',
    ),
}
```

And there you have it. Go browse your django rest\_framework-powered api, and
notice that there are no forms!




---


Update: August 22, 2016
-----------------------


While the above worked for quite some time for me, it's certainly a sub-optimal solution, because the  `BrowsableAPIRendererWithoutForms`  class will still do all of the work to render the forms.


 A slightly better solution to this problem is to short-circuit that process altogether. We can do that by overriding two of the parent class's methods:



```
from rest_framework.renderers import BrowsableAPIRenderer

class BrowsableAPIRendererWithoutForms(BrowsableAPIRenderer):
    """Renders the browsable api, but excludes the forms."""

    def get_context(self, *args, **kwargs):
        ctx = super().get_context(*args, **kwargs)
        ctx['display_edit_forms'] = False
        return ctx
    
    def show_form_for_method(self, view, method, request, obj):
        """We never want to do this! So just return False."""
        return False

    def get_rendered_html_form(self, data, view, method, request):
        """Why render _any_ forms at all. This method should return 
        rendered HTML, so let's simply return an empty string.
        """
        return ""
```

That's it! You shouldn't see any forms on your browseable api, *and* they should be just a small bit faster now, since we no longer do any form rendering work.


When doing this kind of stuff, It's always a good idea to look over the original source code, and you can [do that here (DRF v. 3.4.4)](https://github.com/tomchristie/django-rest-framework/blob/3.4.4/rest_framework/renderers.py#L438). If you've stumbled across this post, first of all thanks for reading! Secondly, if you have any suggestions, please let me know in the comments below.

