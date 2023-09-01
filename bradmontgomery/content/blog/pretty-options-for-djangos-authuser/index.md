---
date: '2010-04-22T09:07:00+00:00'
title: Pretty options for Django's auth.User
draft: false
tags:
- Python
- django
- web
slug: pretty-options-for-djangos-authuser
description: ''
markup: md
url: /blog/pretty-options-for-djangos-authuser/
aliases:
- /blog/2010/04/22/pretty-options-for-djangos-authuser/

---

Several of my Django Apps have Foreign Key relationships to django.contrib.auth.model.User. In Django's admin app, these show up a select elements displaying the username attribute. For some people, that may be OK, but for most of the people with which I work, it's not. We want to see *prettier* options, i.e. each User's full name as the options in that select element.  
  
So, here's how it works. We override the ModelChoiceField (for ForeignKeys) and the ModelMultipleChoiceField (for ManyToMany Fields):  

```
from django.forms import ModelChoiceField, ModelMultipleChoiceField  
  
class UserModelChoiceField(ModelChoiceField):  
    '''   
 A ModelChoiceField to represent User   
 select boxes in the Auto Admin   
 '''  
    def label\_from\_instance(self, obj):  
        return "%s (%s)"%(obj.get_full_name(), obj.username)  
  
class UserModelMultipleChoiceField(ModelMultipleChoiceField):  
    '''   
 Similar to UserModelChoiceField, provide a nicer-looking   
 list of user names for ManyToMany Relations...  
 '''  
    def label\_from\_instance(self, obj):  
        return "%s (%s)"%(obj.get_full_name(), obj.username)  

```
  
  
Then, to customize the admin, you need to create a custome ModelForm for your Model. So, if I had a Model that looked like this:   

```
class MyModel(models.Model):  
    user = models.ForeignKey(User)  

```
  
  
You'd need to create the following ModelForm:  

```
class MyModelAdminForm(forms.ModelForm):  
    user = UserModelChoiceField(User.objects.all().order_by('first\_name', 'last\_name', 'username'))  
  
    class Meta:  
        model = MyModel  

```
  
  
  
Now, when you create a ModelAdmin class for the MyModel, you specify the above form:  

```
from models import MyModel  
from forms import MyModelAdminForm  
  
class MyModelAdmin(admin.ModelAdmin):  
    form = MyModelAdminForm  
admin.site.register(MyModel, MyModelAdmin)  

```
  
  
At this point, the choices for User objects in the admin should contain the user's full name and their username in parenthesis.![](https://blogger.googleusercontent.com/tracker/4123748873183487963-2524432454961244471?l=bradmontgomery.blogspot.com)