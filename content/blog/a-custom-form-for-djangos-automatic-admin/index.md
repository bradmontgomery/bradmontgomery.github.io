---
date: '2009-01-14T16:08:00+00:00'
title: A Custom form for Django's Automatic Admin.
draft: false
tags:
- Python
- django
- web
slug: a-custom-form-for-djangos-automatic-admin
description: ''
markup: md
url: /blog/a-custom-form-for-djangos-automatic-admin/
aliases:
- /blog/2009/01/14/a-custom-form-for-djangos-automatic-admin/

---

A huge selling-point for Django (at least for developers) is its [Automatic Admin](http://docs.djangoproject.com/en/dev/ref/contrib/admin/#ref-contrib-admin). However, the ease at which the Admin can be set up, might make one second-guess an attempt to customize what is provided by default. Of course, the default admin site may not be without its drawbacks...  
  
Many of the django Apps that I have built, tap into Django's [User Authentication System](http://docs.djangoproject.com/en/dev/topics/auth/#topics-auth). Simply put, when I build a model, it has a Foreign Key to django's User Class.  
  
Here's an example Model:  

```
from django.contrib.auth.models import User  
from django.db import models  
  
class Book(models.Model):  
    author = models.ForeignKey(User)  
    title = models.CharField()
```
  
  
The problem here is that when I create or edit a Book object using the Automatic Admin, the author field is represented by a select element, whose options contain ALL User objects... listed by **username**! Wouldn't it be nice if we could have that listed as "*firstname lastname*" or even as "*lastname, firstname"*? You can! And here's how:  
  
First of all, Django's admin makes extensive use of [ModelForms](http://docs.djangoproject.com/en/dev/topics/forms/modelforms/#topics-forms-modelforms), and fields with a Foreign Key relationship are represented by a [ModelChoiceField](http://docs.djangoproject.com/en/dev/ref/forms/fields/#modelchoicefield). So, all we need to do is extend the ModelChoiceField so that we have something that can be used on any Form that represents a Model with a Foreign Key to a User object. The *label\_from\_instance* method accepts an object (in this case, a User object), and returns a string that will be used between <option> elements. In the example below, I've chosen to format that as "*firstname lastname* (*username*)".  
  

```
from django.forms import ModelChoiceField  
  
class UserModelChoiceField(ModelChoiceField):  
    def label\_from\_instance(self, obj):  
        # Return a string of the format: "firstname lastname (username)"  
        return "%s (%s)"%(obj.get_full_name(), obj.username)
```
  
  
Now, create a ModelForm for your Model, which specifies the new Field to be used for the author. Note that we need to pass it a queryset of Users. Below, I've named this ModelForm, **BookAdminForm** since I'm only going to use this form for the admin pages.   
  

```
from django.forms import ModelForm  
from django.contrib.auth.models import User  
  
class BookAdminForm(ModelForm):  
    author = UserModelChoiceField(User.objects.all().order_by('first\_name'))  
    class Meta:  
        model = Book
```
  
  
Now we set up the ModelAmin for the Book Model. In it, we can specify the form that is used by Django's automatic admin (Note that this [MUST be a ModelForm](http://docs.djangoproject.com/en/dev/ref/contrib/admin/#form)!). Your admin would look something similar to the following:  
  

```
from django.contrib import admin  
from forms import BookAdminForm  
from models import Book  
  
class BookAdmin(admin.ModelAdmin):  
    form = BookAdminForm  
  
admin.site.register(Book, BookAdmin)
```
  
  
Now, when you use the Automatic admin to add or edit existing Book entries, the drop-down list of Author names will be a bit more user-friendly.