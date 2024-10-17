---
date: '2015-10-10T19:27:40.047401+00:00'
title: Date lookups in Django
draft: false
tags:
- database
- django
- lookups
- orm
- postgres
- python
slug: date-lookups-django
description: ''
markup: md
url: /blog/date-lookups-django/
aliases:
- /blog/2015/10/10/date-lookups-django/

---

A while ago I [tweeted](https://twitter.com/bkmontgomery/status/615665645594632192)
out something that I've wanted to see in Django for a very long time, yet have
never really taken the time to investigate or implement it:



> I wish [#django](https://twitter.com/hashtag/django?src=hash) had this: 
> 
> M.objects.filter(datetimefield\_\_date=<http://t.co/MVFXsN4Ivk>(2015, 6, 29))
> 
> Has that ever been attempted?
> 
> — Brad Montgomery (@bkmontgomery) [June 29, 2015](https://twitter.com/bkmontgomery/status/615665645594632192)



Django's ORM has a [very rich set of field lookups](https://docs.djangoproject.com/en/1.8/topics/db/queries/#field-lookups), but at present, it doesn't support an exact
date lookup. At least not with the syntax I would expect. Luckily, that tweet
got some very handy responses, so let's do a bit of exploring.


Assume we have the following model. For the now, the only field we care about
is the `created` field.



```
from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
```

Again, what I *wish* we could do is an exact date lookup using a
`__date` lookup. If you try that:



```
from datetime import date
Item.objects.filter(created__date=date(2015, 10, 1))
```

Well, you get an exception.



```
FieldError: Unsupported lookup 'date' for AutoCreatedField or join on the field not permitted.
```

Fear not, there are a handful of ways to acheive the same results. One way
is to use the date-based lookups that django already provides. Such as
`__day`, `__month`, and `__year`. 



```
dt = date(2015, 10, 1)
Item.objects.filter(
    created__day=dt.day, 
    created__month=dt.month, 
    created__year=dt.year
)
```

That's a technique I've used quite a lot in the past. It's fairly verbose,
yet it's pretty readable. Another technique is to use the `__range`
lookup. You can use a datetime object's
[replace method](https://docs.python.org/3.4/library/datetime.html#datetime.date.replace)
to set minimum and maximum values for the time-related attributes (and the
[docs for datetime objects](https://docs.python.org/3.4/library/datetime.html#datetime-objects)
list these values).



```
# Create a datetime object spanning a full day
dt = datetime.now()
start = dt.replace(hour=0, minute=0, second=0, microsecond=0)
end = dt.replace(hour=23, minute=59, second=59, microsecond=999999)

# Query for objects that fall within that day.
Item.objects.filter(created__range=(start, end))
```

One neat suggestion came from [Jason Myers](https://twitter.com/jasonamyers)
notes that you can use the `__contains` lookup with dates:



```
Item.objects.filter(created__contains=date(2015, 10, 1))
```

Another from [Josh Ourisman](https://twitter.com/joshourisman) takes
advantage of the fact that dates are really just strings (at least in postgres):



```
Item.objects.filter(created__startswith='2015-10-01')
```

[Joshua Ginsberg](https://twitter.com/j00bar) suggested using a
custom database function prior to filtering. So, in the spirit of learning new
things available in Django 1.8, I did just that. With a
[Func() expression](https://docs.djangoproject.com/en/1.8/ref/models/expressions/#func-expressions).


In PostgreSQL, you could run the following query to view the date store
on an Item:



```
select created from items limit 1;
>  2015-10-01 12:37:23.620442+00
```

It turns out, PostgreSQL has a handy
[`date` function](http://www.postgresql.org/docs/9.4/static/functions-datetime.html)) that gives us just the date part of a datetime string.



```
select date(created) from items limit 1;
>  2015-10-01
```

`Func()` expressions (using in conjunction with `F()`
expressions and the `aggregate` method will let us call postgres's
date function from python!



```
from django.db.models import Func, F

# Note, this is PostgreSQL-specific.
# Build a queryset annotated with the date portion of the `created` datetime.
queryset = Item.objects.annotate(
  created_date=Func(F('created'), function='DATE')
)

# Now, we can query agains that annotation:
items = queryset.filter(created_date=date(2015, 10, 1))  # What we want!


```

Pretty Cool!


So there you have a number of ways to do date-based lookups in Django. These
will probably get you where you want to go most of the time.


**But wait! There's more!** It turns out, you can build your
own lookups. The [Lookup API reference](https://docs.djangoproject.com/en/1.8/ref/models/lookups/)
was introduced in Django 1.7, yet I've not dabbled with it. Stay Tuned, because
in my next post, I'll see just how hard it is to implement that `__date`
lookup (if nothing else gets in my way over the next few days).


