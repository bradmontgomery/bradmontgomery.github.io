---
date: '2015-03-17T04:54:01.779392+00:00'
title: 'Django hack: Help text on a model instance'
draft: false
tags:
- curry
- django
- functional
slug: django-hack-help-text-modal-instance
description: ''
markup: md
url: /blog/django-hack-help-text-modal-instance/
aliases:
- /blog/2015/03/17/django-hack-help-text-modal-instance/

---

If you've been been working with [Django](https://www.djangoproject.com/) for
a while, you're probably familiar with the `help_text` attribute for model
fields. It gives us a hook for adding descriptive text that gets automatically
included on forms or in the admin.


**But what if you want to access that same information on an instance of
model object?**


Let's look at an example! Assume we have a simple model:



```
class BlogPost(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True,
        help_text="A unique title for this thing"
    )
    content = models.TextField(
        help_text="A content for this thing"
    )
```

Here we have a simple blog post. If we were building an app, we might use a
ModelForm subclass that allows users to create an instance of a BlogPost. It
would look something like this:



```
class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
```

And in our view we might create an unbound instance of this form with
`form = BlogPostForm()`, then in our template we might have markup that
loooks something like this:

```
<form>
  {{ form.as_p }}
</form>
```

That generates a decent-looking form, with our model's help-text included. The
markup would be similar to the following:



```
<p>
  <label for="id\_title">Title:</label>
  <input id="id\_title" maxlength="50" name="title" type="text" />
  <span class="helptext">A unique title for this thing</span>
</p>
<p>
  <label for="id\_description">Description:</label>
  <textarea cols="40" id="id\_description" name="description" rows="10"></textarea>
  <span class="helptext">A description for this thing</span>
</p>
```

Notice the `<span class="helptext">` elements!


Unfortunately, it's not as straightforwad if we want to access that same bit of
information on a model instance. However, Django already does something a little
magical that for model fields that include a set of choices. From the
[choices documentation](https://docs.djangoproject.com/en/1.7/ref/models/fields/#choices) :



> 
>  For each model field that has choices set, Django will add a method to
>  retrieve the human-readable name for the field’s current value. See
>  get\_FOO\_display() in the database API documentation.
> 


So, I decided to look up [how they did this](https://github.com/django/django/blob/ea3168dc6ced391d848c511a14cfcecfeac9d401/django/db/models/fields/__init__.py#L660)
and I discovered the django implementation of curry, in `django.utils.functional.curry`.


For the purposes of this post, curry will let us dynamically create a method
on a class, defining it's parameters at run-time.


Let's look at how this works. First, lets see how to access a field's `help_text`:



```
class BlogPost(models.Model):
    title = models.CharField(...)
    content = models.TextField(...)

    def _get_help_text(self, field_name):
        """Given a field name, return it's help text."""

        # Let's iterate over all the fields on this model.
        for field in self._meta.fields:
            # The name of your field is stored as
            # a name attribute on the field object
            if field.name == field_name:
                # and there's the help_text!
                return field.help_text
```

Now, all we need to do is figure out how to dynamically create a method,
`get_title_help_text` that calls `_get_help_text('title')`. Below is an
updated version of our model; Take a look at it's `__init__` method.



```
from django.db import models
from django.utils.functional import curry


class BlogPost(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True,
        help_text="A unique title for this thing"
    )
    content = models.TextField(
        help_text="A content for this thing"
    )

    def _get_help_text(self, field_name):
        """Given a field name, return it's help text."""
        for field in self._meta.fields:
            if field.name == field_name:
                return field.help_text

    def __init__(self, *args, **kwargs):
        # Call the superclass first; it'll create all of the field objects.
        super(BlogPost, self).__init__(*args, **kwargs)

        # Again, iterate over all of our field objects.
        for field in self._meta.fields:
            # Create a string, get_FIELDNAME_help text
            method_name = "get_{0}_help_text".format(field.name)

            # We can use curry to create the method with a pre-defined argument
            curried_method = curry(self._get_help_text, field_name=field.name)

            # And we add this method to the instance of the class.
            setattr(self, method_name, curried_method)
```

Now, in our template we can display a BlogPost's field values, as well as call
a method to access each field's defined help text.



```
<p>
  {{ post.title }}<br/>
  <span>{{ post.get_title_help_text }}</span>
 </p>
<p>
  {{ post.content }}<br/>
  <span>{{ post.get_content_help_text }}</span>
</p>
```

Pretty cool.





