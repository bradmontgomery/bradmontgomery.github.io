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
description: ''
markup: md
url: /blog/django-admin-filters-arrayfields/
aliases:
- /blog/2015/09/30/django-admin-filters-arrayfields/

---

I've written before about
[the cool
ArrayField support in Django](/blog/nice-arrayfield-widgets-choices-and-chosenjs/), and this is another such post. In this one,
we'll take a look and see how to turn your model's ArrayField values into
filters in the admin.


To start out, let's assume we have a model that contains a simple title
(a `CharField`) and some keywords (an `ArrayField`).
It might look something like this:



```
from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=128)
    keywords = ArrayField(
        models.CharField(max_length=32, blank=True),
        default=list,
        blank=True,
    )
```

This model, `Item`, allows an optional list if keywords (chars)
giving you a default of an empty list. Now, you *could* connect it to
django's admin app with the following bit of code. This would list all of the
item titles in the list view, and you'd also get a filter on the right-hand
side, presumably containing the values of your `keywords` field.



```
from django.contrib import admin

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_filter = ('keywords', )

admin.site.register(models.Item, ItemAdmin)
```


However, if you write this, you'll soon notice something strange. The admin
treats each `Item`'s list of a keywords as a single option for the
list filter! That means you get filter options like `['foo', 'bar']` and `['foo', 'bar', 'bingo']`. Yuck!




![these are not the list filters you're looking for...](//i.imgur.com/LePgVfd.png)
This is probably not what you had in mind.

What we really need to do, is to assemble a unique set of *all possible
values* for the entire collection of `Item`s, then build a custom
admin filter. The custom admin filter is possible by creating a subclass of
`SimpleListFilter`, and you can read all about that in the
[ModelAdmin.list\_filter](https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter) docs.


But first, let's get a unique set of all possible keywords:



```
# query and sort all keywords belonging to Items
keywords = Item.objects.values_list("keywords", flat=True)

# Flatten the nested list of results, and eliminate any empty lists
keywords = [kw for sublist in keywords for kw in sublist if kw]

# Get rid of duplicates and sort them (in alphabetical order)
keywords = sorted(set(keywords))
```

Now, we need to build our custom filter. We'll call it an
`ArrayFieldListFilter`. The django admin docs have an example of this,
and it's worth reading their [example code](https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter) as well (search for the `SimpleListFilter` on that page).



```
# I'll often add this to admin.py...
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
        return queryset
```

Now, we need to add this class as an option to our model admin subclass. To
do that, we'll change `list_filter = ('keywords', )` to
`list_filter = (ArrayFieldListFilter, )`. Your `ItemAdmin`
class should now be:




```
from django.contrib import admin

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_filter = (ArrayFieldListFilter, )

admin.site.register(models.Item, ItemAdmin)
```


And there you have it. A list of all of your `Item`'s keywords,
available to your for filtering your objects in the admin. Keep in mind that
this list is built dynamically (like most admin filters). If you use this code
and don't see any filter options, don't fret! You need to add some keywords to
your existing items, first. Edit an `Item` then come back to the list
view, and then you should see your keywords.



![Working filters!](//i.imgur.com/1NGOchj.png)
There! Doesn't that make more sense?

Hope this helps!


