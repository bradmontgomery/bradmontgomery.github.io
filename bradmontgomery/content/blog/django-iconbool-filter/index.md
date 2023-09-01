---
date: '2015-08-26T16:58:38.410252+00:00'
title: A django iconbool filter
draft: false
tags:
- django
- filter
- python
slug: django-iconbool-filter
description: <p>Django's template...
markup: html
url: /blog/django-iconbool-filter/
aliases:
- /blog/2015/08/26/django-iconbool-filter/

---

<p>Django's template laguage includes a lot of really useful
<a href="https://docs.djangoproject.com/en/1.8/ref/templates/builtins/">
built-in tags and filters</a>, but sometimes you just need to
<a href="https://docs.djangoproject.com/en/1.8/howto/custom-template-tags/">
build your own</a>. There are many reasons why you might want to do this, but
I'm lazy, and I like to build filters and tags that let me take shortcuts
in the template.</p>

<p>Here's one example of a simple filter that let's me be lazy: an <em>iconbool</em> filter.</p>

<h2>Motivation</h2>

<p>I really like <a href="https://fortawesome.github.io/Font-Awesome/icons/">Font-Awesome</a>, and any time I need to represent a boolean value, I like to use an icon. Here's one such example:</p>


<pre><code class="html">User has Widget?
{% if user.has_widget %}
  &lt;i class="fa fa-check"&gt;&lt;/i&gt; Yes
{% else %}
  &lt;i class="fa fa-ban"&gt;&lt;/i&gt; No
{% endif %}</code></pre>

<p>Now, that's not a lot of code, but if you're doing a lot of this type of
markup, it can get tedious really quick (imagine building a grid of this kind of
content)!</p>


<p>Wouldn't it be so much nicer to write this, instead? (Yes, it would!)</p>
<pre><code class="html">User has Widget? {{ user.has_widget|iconbool }}</code></pre>

<h2>Build your custom filter</h2>

<p>We can accomplish the above with a simple, custom django filter. Let's call it
<code>iconbool</code>. It's going to be a simple function that returns a very
simple string of markup based on some input.</p>


<pre><code class="python">from django import template
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
        result = '&lt;i class="fa fa-check"&gt;&lt;/i&gt; Yes'
    else:
        result = '&lt;i class="fa fa-ban"&gt;&lt;/i&gt; No'
    return mark_safe(result)</code></pre>


<p>That's it! Put this in your app's <code>templatetags</code> directory
(for example: <code>myapp/templatetags/myapp_filters.py</code>), and remember to
load the template library in your templates (e.g. <code>{% load myapp_filters %}</code>).</p>

<p>And remember, being lazy is good! Don't forget that django template filters
can save you lots of work.</p>