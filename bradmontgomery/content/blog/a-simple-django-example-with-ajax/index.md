---
date: '2008-11-24T15:11:00+00:00'
title: A simple Django example with Ajax
draft: false
tags:
- Javascript
- ajax
- django
slug: a-simple-django-example-with-ajax
description: ''
markup: md
url: /blog/a-simple-django-example-with-ajax/
aliases:
- /blog/2008/11/24/a-simple-django-example-with-ajax/

---

I often employ Ajax in HTML forms in order to update the list of options in select elements. For example, suppose a form consists of two select elements, and the options in the second depends on the values selected in the first. A simple example of this might be an Automobile Rental website that lets you choose the type of vehicle as well as the color. Not all vehicles come in the same color, though, so you might have a form that looks similar to the following:  
  

```
<select name="auto" id="auto" onchange="get\_vehicle\_colors();">  
<option value="">-- select a vehicle type --</option>  
<option value="car">Car</option>  
<option value="truck">Truck</option>  
<option value="motorcycle">Motorcycle</option>  
</select>  
  
<select name="color" id="color">  
<option value="">-- choose a vehicle first--</option>  
</select>  

```
  
In this example, you would choose the type of automobile you wanted, then employ Ajax to set the appropriate color values for the *color* element.  
  
A Django app that provides this sort of functionality, might have a Model resembling the following (omitting various methods and Meta classes):  

```
class Color(models.Model):  
    color = models.CharField(max_length=256)  
  
class Auto(models.Model):  
    type = models.CharField('auto type', max_length=256)  
    colors = models.ManyToManyField(Color)   

```
  
Likewise, a form (similar to the one above) could be built with:  

```
from django import forms  
from models import Color, Auto  
  
class AutoForm(forms.Form):  
    TYPE_CHOICES = [('', '-- choose a type --'), ] + [(t.type, t.type) for t in Auto.objects.all()]  
    COLOR_CHOICES = [(c.color, c.color) for c in Color.objects.all()]  
    COLOR_CHOICES.insert(0, ('', '-- choose a vehicle type first --'))  
      
    type = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.Select(attrs={'onchange':'get\_vehicle\_color();'}))  
    color = forms.ChoiceField(choices=COLOR_CHOICES)  

```
  
Notice the use of the *widget* paramter on the Form's *type* field. Django Forms only render the most basic HTML, so in order to set an *onchange* attribute for a select element, we have to specify that attribute in *attrs*, which is a dictionary of element attribute name/value pairs. More information about customizing Form widgets can be found in Django's [widget reference](http://docs.djangoproject.com/en/dev/ref/forms/widgets/#ref-forms-widgets).  
  
Another thing to note is the COLOR\_CHOICES attribute. A ChoiceField will validate that any user-submitted content is conteint in its provided *choices*. So, the COLOR\_CHOICES must contain all valid colors for an Auto. However, we make sure the first choice is a default value that will later get updated by our AJAX request.  
  
For the most part, this form would be used as in any other Django app, but since we're adding in a little Ajax, I include my javascript libraries (in this example, [Prototype](http://prototypejs.org/)) in the same template as the form. So, my template code looks something like this:  

```
{% extends "base.html" %}  
{% block head %}  
<script type="text/javascript" src="/site\_media/prototype.js"></script>  
<script type="text/javascript" src="/site\_media/my\_ajax\_function.js"></script>  
{% endblock %}  
  
{% block content %}  
    {% if form\_was\_valid %}  
        {# ... show whatever... #}  
    {% else %}  
        <form action="/auto/reserve/" method="POST">  
        <ul>  
        {{ form.as\_ul}}  
        <li><label for="submit">&nbsp;</label>  
        <input type="submit" id="submit" name="submit" value="Submit"/></li>  
        </ul>  
        </form>  
    {% endif %}  
{% endblock %}  

```
  
There are two items of note, here. The first is that this template builds on top of a *base.html* template which contains my sites layout and definitions for blocks. The second, is that one of those blocks--head--is inside my page's head element so that I can reference arbitrary javascript files (or CSS if I needed to) in only the templates that need them. It may be a minor note, but including your javascript libraries ONLY when you need them might save you some load-time and bandwidth.  
  
Now, what does the stuff in the *my\_ajax\_function.js* look like? When a Django form gets rendered, every form element automatically gets an *id* attribute whose value is the name of the field, prefixed by "id\_". So, our type and color Select widgets would have attributes id="id\_type" and id="id\_color", respectively.  
  
So what is it that our Javascript needs to do?1. When an auto type is selected (determined by the *onchange* event, grab the value of that type (*$('id\_type').getValue()*)
2. Construct the XMLHttpRequest with the appropriate POST data (the type of Auto chosen--accomplished using the $H shortcut to create a [Hash](http://prototypejs.org/api/hash))
3. Send that back to the webserver (at the appropriate URL, which we've set as */auto/ajax\_color\_request/*)
4. Listen for a response from the server,
5. And if that response contains any text (hopefully a list of available colors), update the select element with that text

  
  

```
function get_vehicle_color(){  
    new Ajax.Request('/auto/ajax\_color\_request/', {   
    method: 'post',  
    parameters: $H({'type':$('id\_type').getValue()}),  
    onSuccess: function(transport) {  
        var e = $('id\_color')  
        if(transport.responseText)  
            e.update(transport.responseText)  
    }  
    }); // end new Ajax.Request  
}  

```
  
So now we've got a model and a form (outfitted with some nifty Ajax code, no less), how would we set up a view and a URLconf? Well, the URLconf works the same as in any other app, so we just have to set an entry that maps to the view that handles the Ajax request. If the name of this app is *auto*, and it lives in a project called *mysite*, our URLconf might look like the following:  

```
urlpatterns = patterns('mysite.auto.views',  
    (r'^ajax\_color\_request/$', 'ajax\_color\_request'),  
    # ... everything else...  
)  

```
  
And it would map our URL (www.example.com/auto/ajax\_color\_request/) to a view named *ajax\_color\_request*.  
  
Now for the view. Since our Ajax request is sending its data via post, we can pull it from request.POST (which is a dictionary-like object), and then retrieve all the colors associated with a particular type of Auto.  
  

```
def ajax\_color\_request(request):  
    # Expect an auto 'type' to be passed in via Ajax and POST  
    if request.is_ajax() and request.method == 'POST  
        auto_type = Auto.objects.filter(type=request.POST.get('type', ''))  
        colors = auto_type.colors.all() # get all the colors for this type of auto.  
    return render_to_response('auto/ajax\_color\_request.html', locals())  

```
  
Now, all we have to do is send that data back to the client as a snippet of HTML which will get written to the appropriate select element. I've chosen to do this in a very simple template:  

```
{% for c in colors %}  
    <option value="{{ c.color }}">{{ c.color|title }}</option>  
{% endfor %}  

```
  
  
And there you have it. A simple bit of Ajax in a Django app.![](https://blogger.googleusercontent.com/tracker/4123748873183487963-641240897788708420?l=bradmontgomery.blogspot.com)