---
date: '2015-04-25T22:50:25.238289+00:00'
title: Nice ArrayField widgets with choices and chosen.js
draft: false
tags:
- arrayfield
- django
- postgresql
- python
slug: nice-arrayfield-widgets-choices-and-chosenjs
description: ''
markup: md
url: /blog/nice-arrayfield-widgets-choices-and-chosenjs/
aliases:
- /blog/2015/04/25/nice-arrayfield-widgets-choices-and-chosenjs/

---

One of the really cool new features in Django 1.8 is the [support for Postgres-specific fields](https://docs.djangoproject.com/en/1.8/releases/1.8/#new-postgresql-specific-functionality). I'm very excited to be able to use
things like PostgreSQL arrays or hstore without 3rd-party add-ons.


Unfortnately, the default form inputs for `ArrayField`s are less
than stellar. So, in this post I want to explore a few things:


* a Model who's `ArrayField` only accepts items from a
set of predefined choices
* a ModelForm that makes use of [chosen.js](http://harvesthq.github.io/chosen/) (which I still really like!)


Let's start with a simple model: the quintessential `Post`. This
time, however, it also accepts a set of labels (or tags). Let's start with the
set of acceptable labels (this example is short):



```
LABEL_CHOICES = (
    ('django', 'Django'),
    ('python', 'Python'),
)
```

And now our model. Note that the `ArrayField`'s first argument is
a `CharField` (that's the [base\_field](https://docs.djangoproject.com/en/1.8/ref/contrib/postgres/fields/#arrayfield)), and that is where
we define the choices that are allowed as input.



```
class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    labels = ArrayField(
        models.CharField(max_length=32, blank=True, choices=LABEL_CHOICES),
        default=list,
        blank=True,
    )
```

Note that labels are optional, and that the default is an empty list (or no
labels). Now, we'd typically define a `ModelForm` as follows:



```
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'labels']
```

While this *will* work, there are a couple of fairly significant
problems with it:


1. By default, the `labels` field gets rendered as a simple text input, e.g. `<input id="id_labels" name="labels" type="text">`.
2. You don't get any sort of selection for the choices, and...
3. You must enter choices as a comma-separated string (with NO spaces!); if you get one wrong, the form validators will throw an Exception.


So, while it technically works, it's really not very friendly at all. Let's make it better.


First, django's `ModelForm` gives us a nice hook for specifying a widget for any fields via a `widgets` attribute within the form's inner Meta class. We'll use this technique to customize our form's output, but first let's build a custom Widget.



```
class ArrayFieldSelectMultiple(forms.SelectMultiple):
    """This is a Form Widget for use with a Postgres ArrayField. It implements
    a multi-select interface that can be given a set of `choices`.

    You can provide a `delimiter` keyword argument to specify the delimeter used.

    """

    def __init__(self, *args, **kwargs):
        # Accept a `delimiter` argument, and grab it (defaulting to a comma)
        self.delimiter = kwargs.pop("delimiter", ",")
        super(ArrayFieldSelectMultiple, self).__init__(*args, **kwargs)

    def render_options(self, choices, value):
        # value *should* be a list, but it might be a delimited string.
        if isinstance(value, str):  # python 2 users may need to use basestring instead of str
            value = value.split(self.delimiter)
        return super(ArrayFieldSelectMultiple, self).render_options(choices, value)

    def value_from_datadict(self, data, files, name):
        if isinstance(data, MultiValueDict):
            # Normally, we'd want a list here, which is what we get from the
            # SelectMultiple superclass, but the SimpleArrayField expects to
            # get a delimited string, so we're doing a little extra work.
            return self.delimiter.join(data.getlist(name))
        return data.get(name, None)
```

This widget implements a `<select type="multiple">` widget
for our labels, and it's options will consist of the items from our `LABEL_CHOICES`. Pay attention to the comments in the widget, because there are a
few gotchas in there.


Now, to incorporate this widget into our `PostForm`. Note that we
also specify a css class of "chosen" using the `attrs` keyword argument. In addition, we specify an inner `Media` class, so our form knows
how to load the javascript and css assets for chosen.js (and jquery).


This assumes you've got jquery and chosen installed as part of your project's
static files. I typically have them organized in a similar fashion:



```
static/
    js/
        jquery.min.js
    chosen/
        chosen.min.css
        chosen.jquery.min.js
        ...
```


```
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'labels']
        widgets = {
            "labels": ArrayFieldSelectMultiple(
                choices=LABEL_CHOICES, attrs={'class': 'chosen'}),
        }

    class Media:
        css = {
            "all": ("chosen/chosen.min.css", )
        }
        js = ("js/jquery.min.js", "chosen/chosen.jquery.min.js")
```

And that's it! When this form is rendered, the `labels` widget
will look something like: 



```
<select multiple="multiple" class="chosen" id="id_labels" name="labels">
<option value="django">Django</option>
<option value="python">Python</option>
</select>
```

Just don't forget to render the form's media in your template with, `{{ form.media }}`.

If you've got jquery & chosen.js installed correctly, you should get a
multi-select widget with pre-defined options that's very usable, with results
stored in a PostgreSQL array field.



