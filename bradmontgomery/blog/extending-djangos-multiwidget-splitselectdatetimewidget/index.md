---
date: '2008-11-19T12:49:00+00:00'
title: "Extending Django's MultiWidget: SplitSelectDateTimeWidget"
draft: false
tags:
- Python
- django
slug: extending-djangos-multiwidget-splitselectdatetimewidget
description: ''
markup: md
url: /blog/extending-djangos-multiwidget-splitselectdatetimewidget/
aliases:
- /blog/2008/11/19/extending-djangos-multiwidget-splitselectdatetimewidget/

---

This entry is an update to [SelectTimeWidget: A custom Django Widget](/blog/selecttimewidget-a-custom-django-widget/).   
  
The Problem: I want to use a Single widget object for a DateTimeField, but I want it to consist of select elements with appropriate options for month, day, year, hour, minute, and second. Additionally, I want to be able to specify a 12-hour format, so I would then need options for "a.m." and "p.m."  
  
Fortunately, Django's SelectDateWidget (from django.forms.extras.widgets) takes care of the Date portion of this, and I've previously written a similar SelectTimeWidget. Now, I just need to find some way to appropriately combine the two widgets.  
  
After a little digging in Django's source code, I found something called a MultiWidget (in django.forms.widgets). From it's docstring:


> A widget that is composed of multiple widgets.

Wow! This sounds like JUST what I need! Luckily, just beneath it is the definition of a SplitDateTimeWidget(MultiWidget), which combines two TextInput widgets for DateTimeFields. So taking that as an example, I've written the  [SplitSelectDateTimeWidget](http://www.djangosnippets.org/snippets/1206/).  
  
To Use the SplitSelectDateTimeWidget you might do something similar to this:


```
# Default usage of SplitSelectDateTimeWidget  
class TimeForm(Form):  
    dt = DateTimeField(widget=SplitSelectDateTimeWidget())  

```
  
  
A slightly more complex example hooks into the flexibility of the underlying widgets (SelectDateWidget and SelecTimeWidget):  



```
class TimeForm(Form)  
    dt = DateTimeField(widget=SplitSelectDateTimeWidget(hour_step=2, \  
    minute_step=15, second_step=30, twelve_hr=True, years=[2008,2009,2010]))  

```
  
The above example displays hours in increments of 2, minutes in increments of 15, and seconds in increments of 30. Likewise, only the years 2008, 2009,and 2010 are displayed in the years' options.  
  
The output of a form using the SplitSelectDateTimeWidget looks something similar to this:  
  
![SplitSelectDateTimeWidget](http://files.bradmontgomery.net/images/datetimeselect.png "SplitSelectDateTimeWidget")

![](https://blogger.googleusercontent.com/tracker/4123748873183487963-8329154980397267028?l=bradmontgomery.blogspot.com)