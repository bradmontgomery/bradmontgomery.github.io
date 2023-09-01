---
date: '2015-03-17T04:54:01.779392+00:00'
title: 'Django hack: Help text on a model instance'
draft: false
tags:
- curry
- django
- functional
slug: django-hack-help-text-modal-instance
description: <p>If you've been be...
markup: html
url: /blog/django-hack-help-text-modal-instance/
aliases:
- /blog/2015/03/17/django-hack-help-text-modal-instance/

---

<p>If you've been been working with <a href="https://www.djangoproject.com/">Django</a> for
a while, you're probably familiar with the <code>help_text</code> attribute for model
fields. It gives us a hook for adding descriptive text that gets automatically
included on forms or in the admin.</p>

<p><strong>But what if you want to access that same information on an instance of
model object?</strong></p>

<p>Let's look at an example! Assume we have a simple model:</p>


<pre><code class="python">class BlogPost(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True,
        help_text="A unique title for this thing"
    )
    content = models.TextField(
        help_text="A content for this thing"
    )</code></pre>

<p>Here we have a simple blog post. If we were building an app, we might use a
ModelForm subclass that allows users to create an instance of a BlogPost. It
would look something like this:</p>


<pre><code class="python">class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost</code></pre>

<p>And in our view we might create an unbound instance of this form with
<code>form = BlogPostForm()</code>, then in our template we might have markup that
loooks something like this:</pre>

<pre><code class="html">&lt;form&gt;
  {{ form.as_p }}
&lt;/form&gt;</code></pre>

<p>That generates a decent-looking form, with our model's help-text included. The
markup would be similar to the following:</p>

<pre><code>&lt;<span class="pl-ent">p</span>&gt;
  &lt;<span class="pl-ent">label</span> <span class="pl-e">for</span>=<span class="pl-s1"><span class="pl-pds">"</span>id_title<span class="pl-pds">"</span></span>&gt;Title:&lt;/<span class="pl-ent">label</span>&gt;
  &lt;<span class="pl-ent">input</span> <span class="pl-e">id</span>=<span class="pl-s1"><span class="pl-pds">"</span>id_title<span class="pl-pds">"</span></span> <span class="pl-e">maxlength</span>=<span class="pl-s1"><span class="pl-pds">"</span>50<span class="pl-pds">"</span></span> <span class="pl-e">name</span>=<span class="pl-s1"><span class="pl-pds">"</span>title<span class="pl-pds">"</span></span> <span class="pl-e">type</span>=<span class="pl-s1"><span class="pl-pds">"</span>text<span class="pl-pds">"</span></span> /&gt;
  &lt;<span class="pl-ent">span</span> <span class="pl-e">class</span>=<span class="pl-s1"><span class="pl-pds">"</span>helptext<span class="pl-pds">"</span></span>&gt;A unique title for this thing&lt;/<span class="pl-ent">span</span>&gt;
&lt;/<span class="pl-ent">p</span>&gt;
&lt;<span class="pl-ent">p</span>&gt;
  &lt;<span class="pl-ent">label</span> <span class="pl-e">for</span>=<span class="pl-s1"><span class="pl-pds">"</span>id_description<span class="pl-pds">"</span></span>&gt;Description:&lt;/<span class="pl-ent">label</span>&gt;
  &lt;<span class="pl-ent">textarea</span> <span class="pl-e">cols</span>=<span class="pl-s1"><span class="pl-pds">"</span>40<span class="pl-pds">"</span></span> <span class="pl-e">id</span>=<span class="pl-s1"><span class="pl-pds">"</span>id_description<span class="pl-pds">"</span></span> <span class="pl-e">name</span>=<span class="pl-s1"><span class="pl-pds">"</span>description<span class="pl-pds">"</span></span> <span class="pl-e">rows</span>=<span class="pl-s1"><span class="pl-pds">"</span>10<span class="pl-pds">"</span></span>&gt;&lt;/<span class="pl-ent">textarea</span>&gt;
  &lt;<span class="pl-ent">span</span> <span class="pl-e">class</span>=<span class="pl-s1"><span class="pl-pds">"</span>helptext<span class="pl-pds">"</span></span>&gt;A description for this thing&lt;/<span class="pl-ent">span</span>&gt;
&lt;/<span class="pl-ent">p</span>&gt;</code></pre>


<p>Notice the <code>&lt;span class="helptext"&gt;</code> elements!</p>

<p>Unfortunately, it's not as straightforwad if we want to access that same bit of
information on a model instance. However, Django already does something a little
magical that for model fields that include a set of choices. From the
<a href="https://docs.djangoproject.com/en/1.7/ref/models/fields/#choices">
choices documentation </a>:</p>

<blockquote>
    For each model field that has choices set, Django will add a method to
    retrieve the human-readable name for the field’s current value. See
    get_FOO_display() in the database API documentation.
</blockquote>


<p>So, I decided to look up <a href="https://github.com/django/django/blob/ea3168dc6ced391d848c511a14cfcecfeac9d401/django/db/models/fields/__init__.py#L660">how they did this</a>
and I discovered the django implementation of curry, in <code>django.utils.functional.curry</code>.</p>

<p>For the purposes of this post, curry will let us dynamically create a method
on a class, defining it's parameters at run-time.</p>

<p>Let's look at how this works. First, lets see how to access a field's <code>help_text</code>:


<pre><code class="python">class BlogPost(models.Model):
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
                return field.help_text</code></pre>

<p>Now, all we need to do is figure out how to dynamically create a method,
<code>get_title_help_text</code> that calls <code>_get_help_text('title')</code>. Below is an
updated version of our model; Take a look at it's <code>__init__</code> method.</p>

<pre><code class="python">from django.db import models
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
            setattr(self, method_name, curried_method)</code></pre>

<p>Now, in our template we can display a BlogPost's field values, as well as call
a method to access each field's defined help text.</p>

<pre><code>&lt;<span class="pl-ent">p</span>&gt;
  {{ post.title }}&lt;<span class="pl-ent">br</span>/&gt;
  &lt;<span class="pl-ent">span</span>&gt;{{ post.get_title_help_text }}&lt;/<span class="pl-ent">span</span>&gt;
 &lt;/<span class="pl-ent">p</span>&gt;
&lt;<span class="pl-ent">p</span>&gt;
  {{ post.content }}&lt;<span class="pl-ent">br</span>/&gt;
  &lt;<span class="pl-ent">span</span>&gt;{{ post.get_content_help_text }}&lt;/<span class="pl-ent">span</span>&gt;
&lt;/<span class="pl-ent">p</span>&gt;</code></pre>

<p>Pretty cool.</p>