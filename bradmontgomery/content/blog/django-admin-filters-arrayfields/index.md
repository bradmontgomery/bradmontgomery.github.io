---
date: '2015-09-30T22:42:44.207595+00:00'
title: Django Admin Filters from ArrayFields
draft: false
tags:
- admin
- array
- arrayfield
- django
- filter
- postgresql
slug: django-admin-filters-arrayfields
description: <p>I've written befo...
markup: html
url: /blog/django-admin-filters-arrayfields/
aliases:
- /blog/2015/09/30/django-admin-filters-arrayfields/

---

<p>I've written before about
<a href="/blog/nice-arrayfield-widgets-choices-and-chosenjs/">the cool
ArrayField support in Django</a>, and this is another such post. In this one,
we'll take a look and see how to turn your model's ArrayField values into
filters in the admin.</p>

<p>To start out, let's assume we have a model that contains a simple title
(a <code>CharField</code>) and some keywords (an <code>ArrayField</code>).
It might look something like this:</p>

<pre><code class="python">from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=128)
    keywords = ArrayField(
        models.CharField(max_length=32, blank=True),
        default=list,
        blank=True,
    )</code></pre>

<p>This model, <code>Item</code>, allows an optional list if keywords (chars)
giving you a default of an empty list. Now, you <em>could</em> connect it to
django's admin app with the following bit of code. This would list all of the
item titles in the list view, and you'd also get a filter on the right-hand
side, presumably containing the values of your <code>keywords</code> field.</p>


<pre><code class="python">from django.contrib import admin

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_filter = ('keywords', )

admin.site.register(models.Item, ItemAdmin)</code></pre>

<p>
However, if you write this, you'll soon notice something strange. The admin
treats each <code>Item</code>'s list of a keywords as a single option for the
list filter! That means you get filter options like <code>['foo', 'bar']</code> and <code>['foo', 'bar', 'bingo']</code>. Yuck!
</p>

<figure>
  <img src="//i.imgur.com/LePgVfd.png"
       alt="these are not the list filters you're looking for..."/>
  <figcaption>This is probably not what you had in mind.</figcaption>
</figure>

<p>What we really need to do, is to assemble a unique set of <em>all possible
values</em> for the entire collection of <code>Item</code>s, then build a custom
admin filter. The custom admin filter is possible by creating a subclass of
<code>SimpleListFilter</code>, and you can read all about that in the
<a href="https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter">ModelAdmin.list_filter</a> docs.</p>

<p>But first, let's get a unique set of all possible keywords:</p>


<pre style="clear: right;"><code class="python"># query and sort all keywords belonging to Items
keywords = Item.objects.values_list("keywords", flat=True)

# Flatten the nested list of results, and eliminate any empty lists
keywords = [kw for sublist in keywords for kw in sublist if kw]

# Get rid of duplicates and sort them (in alphabetical order)
keywords = sorted(set(keywords))</code></pre>

<p>Now, we need to build our custom filter. We'll call it an
<code>ArrayFieldListFilter</code>. The django admin docs have an example of this,
and it's worth reading their <a href="https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter">example code</a> as well (search for the <code>SimpleListFilter</code> on that page).</p>

<pre><code class="python"># I'll often add this to admin.py...
class ArrayFieldListFilter(admin.SimpleListFilter):
    """This is a list filter based on the values
    from a model's `keywords` ArrayField. """

    title = 'Keywords'
    parameter_name = 'keywords'

    def lookups(self, request, model_admin):
        # Very similar to our code above, but this method must return a
        # list of tuples: (lookup_value, human-readable value). These
        # appear in the admin's right sidebar

        keywords = Item.objects.values_list("keywords", flat=True)
        keywords = [(kw, kw) for sublist in keywords for kw in sublist if kw]
        keywords = sorted(set(keywords))
        return keywords

    def queryset(self, request, queryset):
        # when a user clicks on a filter, this method gets called. The
        # provided queryset with be a queryset of Items, so we need to
        # filter that based on the clicked keyword.

        lookup_value = self.value()  # The clicked keyword. It can be None!
        if lookup_value:
            # the __contains lookup expects a list, so...
            queryset = queryset.filter(keywords__contains=[lookup_value])
        return queryset</code></pre>


<p>Now, we need to add this class as an option to our model admin subclass. To
do that, we'll change <code>list_filter = ('keywords', )</code> to
<code>list_filter = (ArrayFieldListFilter, )</code>. Your <code>ItemAdmin</code>
class should now be:
</p>

<pre><code class="python">from django.contrib import admin

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_filter = (ArrayFieldListFilter, )

admin.site.register(models.Item, ItemAdmin)</code></pre>

<p>
And there you have it. A list of all of your <code>Item</code>'s keywords,
available to your for filtering your objects in the admin. Keep in mind that
this list is built dynamically (like most admin filters). If you use this code
and don't see any filter options, don't fret! You need to add some keywords to
your existing items, first. Edit an <code>Item</code> then come back to the list
view, and then you should see your keywords.</p>

<figure>
  <img src="//i.imgur.com/1NGOchj.png" alt="Working filters!"/>
  <figcaption>There! Doesn't that make more sense?</figcaption>
</figure>

<p>Hope this helps!</p>
