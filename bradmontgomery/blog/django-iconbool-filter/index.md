---
date: '2015-08-26T16:58:38.410252+00:00'
title: A django iconbool filter
draft: false
tags:
- django
- filter
- python
slug: django-iconbool-filter
description: ''
markup: md
url: /blog/django-iconbool-filter/
aliases:
- /blog/2015/08/26/django-iconbool-filter/

---

Django's template laguage includes a lot of really useful
[built-in tags and filters](https://docs.djangoproject.com/en/1.8/ref/templates/builtins/), but sometimes you just need to
[build your own](https://docs.djangoproject.com/en/1.8/howto/custom-template-tags/). There are many reasons why you might want to do this, but
I'm lazy, and I like to build filters and tags that let me take shortcuts
in the template.


Here's one example of a simple filter that let's me be lazy: an *iconbool* filter.


Motivation
----------


I really like [Font-Awesome](https://fortawesome.github.io/Font-Awesome/icons/), and any time I need to represent a boolean value, I like to use an icon. Here's one such example:



```
User has Widget?
{% if user.has_widget %}
  <i class="fa fa-check"></i> Yes
{% else %}
  <i class="fa fa-ban"></i> No
{% endif %}
```

Now, that's not a lot of code, but if you're doing a lot of this type of
markup, it can get tedious really quick (imagine building a grid of this kind of
content)!


Wouldn't it be so much nicer to write this, instead? (Yes, it would!)



```
User has Widget? {{ user.has_widget|iconbool }}
```

Build your custom filter
------------------------


We can accomplish the above with a simple, custom django filter. Let's call it
`iconbool`. It's going to be a simple function that returns a very
simple string of markup based on some input.



```
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter("iconbool", is_safe=True)
def iconbool(value):
    """Given a boolean value, this filter outputs a font-awesome icon + the
    word "Yes" or "No"

    Example Usage:

        {{ user.has_widget|iconbool }}

    """
    if bool(value):
        result = '<i class="fa fa-check"></i> Yes'
    else:
        result = '<i class="fa fa-ban"></i> No'
    return mark_safe(result)
```

That's it! Put this in your app's `templatetags` directory
(for example: `myapp/templatetags/myapp_filters.py`), and remember to
load the template library in your templates (e.g. `{% load myapp_filters %}`).


And remember, being lazy is good! Don't forget that django template filters
can save you lots of work.

