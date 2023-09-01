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
description: <p>One of the really...
markup: html
url: /blog/nice-arrayfield-widgets-choices-and-chosenjs/
aliases:
- /blog/2015/04/25/nice-arrayfield-widgets-choices-and-chosenjs/

---

<p>One of the really cool new features in Django 1.8 is the <a href="https://docs.djangoproject.com/en/1.8/releases/1.8/#new-postgresql-specific-functionality">support for Postgres-specific fields</a>. I'm very excited to be able to use
things like PostgreSQL arrays or hstore without 3rd-party add-ons.</p>

<p>Unfortnately, the default form inputs for <code>ArrayField</code>s are less
than stellar. So, in this post I want to explore a few things:</p>

<ul>
<li>a Model who's <code>ArrayField</code> only accepts items from a
set of predefined choices</li>
<li>a ModelForm that makes use of <a href="http://harvesthq.github.io/chosen/">chosen.js</a> (which I still really like!)</li>
</ul>

<p>Let's start with a simple model: the quintessential <code>Post</code>. This
time, however, it also accepts a set of labels (or tags). Let's start with the
set of acceptable labels (this example is short):</p>

<pre><code class="python">LABEL_CHOICES = (
    ('django', 'Django'),
    ('python', 'Python'),
)</code></pre>

<p>And now our model. Note that the <code>ArrayField</code>'s first argument is
a <code>CharField</code> (that's the <a href="https://docs.djangoproject.com/en/1.8/ref/contrib/postgres/fields/#arrayfield">base_field</a>), and that is where
we define the choices that are allowed as input.</p>

<pre><code class="python">class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    labels = ArrayField(
        models.CharField(max_length=32, blank=True, choices=LABEL_CHOICES),
        default=list,
        blank=True,
    )</code></pre>

<p>Note that labels are optional, and that the default is an empty list (or no
labels). Now, we'd typically define a <code>ModelForm</code> as follows:</p>

<pre><code class="python">class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'labels']</code></pre>

<p>While this <em>will</em> work, there are a couple of fairly significant
problems with it:</p>

<ol>
<li>By default, the <code>labels</code> field gets rendered as a simple text input, e.g. <code>&lt;input id="id_labels" name="labels" type="text"&gt;</code>.</li>
<li>You don't get any sort of selection for the choices, and...</li>
<li>You must enter choices as a comma-separated string (with NO spaces!); if you get one wrong, the form validators will throw an Exception.</li>
</ol>

<p>So, while it technically works, it's really not very friendly at all. Let's make it better.</p>

<p>First, django's <code>ModelForm</code> gives us a nice hook for specifying a widget for any fields via a <code>widgets</code> attribute within the form's inner Meta class. We'll use this technique to customize our form's output, but first let's build a custom Widget.</p>

<pre><code class="python">class ArrayFieldSelectMultiple(forms.SelectMultiple):
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
        return data.get(name, None)</code></pre>


<p>This widget implements a <code>&lt;select type="multiple"&gt;</code> widget
for our labels, and it's options will consist of the items from our <code>LABEL_CHOICES</code>. Pay attention to the comments in the widget, because there are a
few gotchas in there.</p>


<p>Now, to incorporate this widget into our <code>PostForm</code>. Note that we
also specify a css class of "chosen" using the <code>attrs</code> keyword argument. In addition, we specify an inner <code>Media</code> class, so our form knows
how to load the javascript and css assets for chosen.js (and jquery).</p>

<p>This assumes you've got jquery and chosen installed as part of your project's
static files. I typically have them organized in a similar fashion:</p>

<pre>static/
    js/
        jquery.min.js
    chosen/
        chosen.min.css
        chosen.jquery.min.js
        ...</pre>

<pre><code class="python">class PostForm(forms.ModelForm):
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
        js = ("js/jquery.min.js", "chosen/chosen.jquery.min.js")</code></pre>

<p>And that's it! When this form is rendered, the <code>labels</code> widget
will look something like: </p>

<pre><code class="html">&lt;select multiple="multiple" class="chosen" id="id_labels" name="labels"&gt;
&lt;option value="django"&gt;Django&lt;/option&gt;
&lt;option value="python"&gt;Python&lt;/option&gt;
&lt;/select&gt;</code></pre>

<p>Just don't forget to render the form's media in your template with, <code>{{ form.media }}</code>.

<p>If you've got jquery &amp; chosen.js installed correctly, you should get a
multi-select widget with pre-defined options that's very usable, with results
stored in a PostgreSQL array field.</p>