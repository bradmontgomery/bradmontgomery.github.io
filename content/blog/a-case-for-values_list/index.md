---
date: '2010-07-19T16:25:00+00:00'
title: A case for values_list
draft: false
tags:
- django
- python
- web
slug: a-case-for-values_list
description: ''
markup: md
url: /blog/a-case-for-values_list/
aliases:
- /blog/2010/07/19/a-case-for-values_list/

---

Here's the Scenario: I have a model (lets call it Contact) with two Foreign Keys, one of which is related to User in Django's contrib.auth app. I need to build a form that lets me select an existing object, and a new user.   



```
class ContactType(Model):  
    name = CharField(max_length=128)  
  
class Contact(Model):  
    user = ForeignKey(User)  
    contact_type = ForeignKey(ContactType)  
    # possibly more fields...
```
I need to select from existing models, so my first thought might be to build a form that uses two `[ModelChoiceField](http://docs.djangoproject.com/en/1.2/ref/forms/fields/#django.forms.ModelChoiceField)`'s. I also want to modify the way that my form displays each choice, so I *could* extend ModelChoiceField by overriding the `label_from_instance` method:  



```
class UserModelChoiceField(ModelChoiceField):  
    def label\_from\_instance(self, obj):  
        return "%s (%s)"%(obj.get_full_name(), obj.username)  
  
class ContactModelChoiceField(ModelChoiceField):  
    def label\_from\_instance(self, obj):  
        return '%s (%s)' % (obj.type, obj.user.get_full_name())  
  
class CopyContactForm(forms.Form):  
    contact = ContactModelChoiceField(Contact.objects.all())  
    new_user = UserModelChoiceField(User.objects.all().order_by('first\_name', 'last\_name', 'username')) 
```
This actually provides a solution to my original problem, but it's not very efficient. Notice that both the `UserModelChoiceField` and the `ContactModelChoiceField` call methods on each object with the latter accessing a foreign key. In an app with 600 Users and 600 Contacts, this form would generate around 1200 queries!  
  
There's actually a very efficient way to generate the same sort of form using `[values\_list](http://docs.djangoproject.com/en/dev/topics/db/optimization/#use-queryset-values-and-values-list)`, especially, when you realize that the form really just needs to contain something like the following:  



```
<select>  
<option value="1">John Doe</option>  
<option value="2">Jane Doe</option>  
  
</select>
```
So a more efficient solution to my problem looks something like the code below, which yields two queries.  



```
class CopyContactForm(forms.Form):  
    contact = forms.ChoiceField(choices=[(c[0], '%s (%s %s)'%(c[1],c[2],c[3])) \  
        for c in Contact.objects.values_list('id', 'type\_\_name', 'user\_\_first\_name', 'user\_\_last\_name')])  
    new_user = forms.ChoiceField(choices=[(u[0], '%s %s (%s)'%(u[1],u[2],u[3])) \  
        for u in User.objects.values_list('id', 'first\_name', 'last\_name', 'username')])  

```
