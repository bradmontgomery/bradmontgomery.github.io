---
date: '2013-03-07T19:39:54.168594+00:00'
title: Calculate a Week Range for a Date
draft: false
tags:
- date
- isocalendar
- python
- range
slug: calculate-week-range-date
description: ''
markup: md
url: /blog/calculate-week-range-date/
aliases:
- /blog/2013/03/07/calculate-week-range-date/

---

Math with dates and date ranges is often *fun & enlightening*! As
a testament to the fun of calculating dates (particularly ranges of dates), I
present the following:


Given a date, how would you find the range of dates that describe the week
during which your original date lies? In other words, assume today is *March
7, 2013* (and it is... for now anyway). Can you answer these two questions:

1. What was last Sunday's date?
2. What will be the date on Saturday?


*NOTE: I'm assuming weeks start on Sunday and end on Saturday. I'm in the
US and that's how people in my area typically define a "week".*


Here's some Python code that calculates this. (also available at
<https://gist.github.com/bradmontgomery/5110985>)



```
from datetime import timedelta

def week_range(date):
    """Find the first/last day of the week for the given day.
    Assuming weeks start on Sunday and end on Saturday.

    Returns a tuple of ``(start_date, end_date)``.

    """
    # isocalendar calculates the year, week of the year, and day of the week.
    # dow is Mon = 1, Sat = 6, Sun = 7
    year, week, dow = date.isocalendar()

    # Find the first day of the week.
    if dow == 7:
        # Since we want to start with Sunday, let's test for that condition.
        start_date = date
    else:
        # Otherwise, subtract `dow` number days to get the first day
        start_date = date - timedelta(dow)

    # Now, add 6 for the last day of the week (i.e., count up to Saturday)
    end_date = start_date + timedelta(6)

    return (start_date, end_date)
```

Now, playing with this in a python shell...



```
>>> from datetime import datetime
>>> d = datetime(2013, 3, 7)
>>> week_range(d)
(datetime.datetime(2013, 3, 3, 0, 0),
 datetime.datetime(2013, 3, 9, 0, 0))
```

This is also useful if you've got a Django site, and you want to find
the Users that joined during a certain week:



```
>>> from django.contrib.auth.models import User
>>> d = datetime(2013, 3, 7)
>>> week = week_range(d)
>>> User.objects.filter(date_joined__range=week)
[<User ...>, ...]
```

Cool, huh. Check out the docs for [`timedelta`](http://docs.python.org/2/library/datetime.html#timedelta-objects) and
[`isocalendar`](http://docs.python.org/2/library/datetime.html#datetime.date.isocalendar) for more information.




