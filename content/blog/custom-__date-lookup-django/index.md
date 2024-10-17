---
date: '2015-10-18T20:40:37.236361+00:00'
title: A custom __date lookup for Django
draft: false
tags:
- database
- django
- lookups
- orm
- postgres
- python
slug: custom-__date-lookup-django
description: ''
markup: md
url: /blog/custom-__date-lookup-django/
aliases:
- /blog/2015/10/18/custom-__date-lookup-django/

---


⚠ Django 1.9 now includes a [built-in \_\_date lookup](https://docs.djangoproject.com/en/1.9/ref/models/querysets/#date). If possible, you should use that instead of the code below, which doesn't support timezones.



In my post [last week on date lookups](/blog/date-lookups-django/),
I ended with a promise to take a look at building a
[custom
django lookup](https://docs.djangoproject.com/en/1.8/howto/custom-lookups/) (namely, a `__date` lookup). Django includes
a basic `Lookup` class, and to build your own lookup expressions,
all you really need to do is:

1. Subclass `django.db.models.Lookup`
2. define a `lookup_name` attribute
3. write the `as_sql` method to define how your database should
handle building the query


As promised, here's a quick example. Assume we have the following model (silly,
but simple) model. For illustration purposes, it has both a `DateField`
and a `DateTimeField`. We'll build our lookup, so that it works with
both fields.



```
from django.db import models

class Meeting(models.Model):
    date = models.DateField()
    scheduled = models.DateTimeField()
```

**Step 1:** Let's build the lookup, which I'm going to
creatively name, `DateLookup`.


```
from django.db.models import Lookup

class DateLookup(Lookup):
    """A custom lookup, that lets you query DateField and DateTimeFields by a date"""

    lookup_name = 'date'  # This enables us to use __date='2015-10-18' in a query

    def as_sql(self, compiler, connection):
        # The left-hand-side (lhs) in the query's WHERE clause. It consists
        # of your app name and field name. e.g. '"myapp"."scheduled"'
        # In this case, the left-hand-side has no params.
        lhs, lhs_params = self.process_lhs(compiler, connection)

        # The right-hand-side (rhs) + its params will define the input used
        # in the query's WHERE clause. At this point, the rhs_params will
        # be a datetime object, e.g.: datetime(2015, 10, 18, 0, 0, tzinfo=)
 rhs, rhs\_params = self.process\_rhs(compiler, connection)

 # Both PostgreSQL and MySQL have a DATE function that lets us query
 # by date. The where clause in the generated SQL will look something
 # like, WHERE DATE(scheduled) = '2015-10-18'
 params = lhs\_params + rhs\_params
 return 'DATE(%s) = %s' % (lhs, rhs), params
```

**Step 2:** Register it with the appropriate model field(s).
In this case, both the `DateField` and `DateTimeField`.


The Django docs include an important note about registering custom lookups:



```
from django.db.models.fields import DateField, DateTimeField

DateField.register_lookup(DateLookup)
DateTimeField.register_lookup(DateLookup)
```


> 
> You will need to ensure that this registration happens before you try to
> create any querysets using it. You could place the implementation in a
> models.py file, or register the lookup in the ready() method of an AppConfig.
> 


Now, open a django shell, and you can run a query like the following, which
queries against a date field. This should give you all the Meetings where
`date = datetime.date(2015, 10, 18)`:



```
Meeting.objects.filter(date__date='2015-10-18')
```

Or, you can do the following, which queries agains a datetime field, which
should give you all the meetings where the `scheduled` column
includes 2015-10-18.



```
Meeting.objects.filter(scheduled__date='2015-10-18')
```

There's more to custom lookups in Django, and I highly recommend reading
through the [custom lookups documentation](https://docs.djangoproject.com/en/1.8/howto/custom-lookups/) because it also includes a really great
example, as well.


*Note: All the code in this post was written using Python 3.4 and Django 1.8.*





