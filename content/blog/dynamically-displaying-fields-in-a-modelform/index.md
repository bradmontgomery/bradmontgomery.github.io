---
date: '2009-04-21T13:31:00+00:00'
title: Dynamically Displaying Fields in a ModelForm
draft: false
tags:
- Programming
- django
- web
slug: dynamically-displaying-fields-in-a-modelform
description: ''
markup: md
url: /blog/dynamically-displaying-fields-in-a-modelform/
aliases:
- /blog/2009/04/21/dynamically-displaying-fields-in-a-modelform/

---

**The Problem**: I want to dynamically include some fields in a ModelForm based on some external criteria. Sometimes I want the fields displayed, sometimes I don't.   
  
I'm going to try to explain this scenario through a (albeit contrived) example. I have a Model that looks like the following:  
  

```
class Suff(models.Model):  
    foo = models.CharField(max_length=255)  
    bar = models.BooleanField(default=False, blank=True)  
  
    def is\_foo\_bar(self):  
        ''' is this model's foo attribute set to 'bar' '''  
        return self.foo == 'bar'  

```
  
  
Normally, if I needed a Form for this Model, I would subclass a ModelForm like the following:  

```
class StuffForm(models.ModelForm):  
    class Meta:  
        model = Stuff  
        fields = ('foo', 'bar')  

```
  
  
However, if I do NOT want the 'bar' field to be displayed by default I would need to remove it from the ModelForms list of fields (or use something like *exclude = ('bar', )* ). But, if this form is created with an instance of Stuff whose *foo* attribute contains the string *bar*, I would like for the Form's 'bar' field to be displayed.  
  
I originally tried to accomplish this task by overridding StuffForm's \_\_init\_\_ method, and adding a new BooleanField when the desired circumstances arose... However, I stumpled across Ross Poulton's [Dynamic ModelForms in Django](http://www.rossp.org/blog/2008/dec/15/modelforms/), and then I realized it would be much easier to **prevent a ModelForm's Field from being displayed** than it would be to dynamically create one.  
  
In order to accomplish this, the StuffForms's \_\_init\_\_ method would look something like the following:  

```
def \_\_init\_\_(self, \*args, \*\*kwargs):  
    super(StuffForm, self).__init__(\*args, \*\*kwargs)  
      
    # If this form is created without an instance, OR  
    # If the instance's foo field is != 'bar'  
    if not kwargs.has_key('instance') or (kwargs.has_key('instance') and \  
        not kwargs['instance'].is_foo_bar()):  
        # Remove this field from the form.  
        del self.fields['bar']  

```
Done. I get all the benefits of a ModelForm, and the *bar* field is not displayed unless it should be.