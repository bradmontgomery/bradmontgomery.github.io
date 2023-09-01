---
date: '2013-04-07T21:19:19.991633+00:00'
title: Django Manager Testing Woes
draft: false
tags:
- django
- managers
- mock
- models
- python
- testing
slug: django-manager-testing-woes
description: <p>I've recently run...
markup: html
url: /blog/django-manager-testing-woes/
aliases:
- /blog/2013/04/07/django-manager-testing-woes/

---

<p>I've recently run into some strange behavior while testing some
custom Django managers. While, I can't list all of the exact code (it's not
open source), I'll try to list some simple examples that illustrate the problem
so (hopefully), this post will be helpful for others.</p>

<p>To get started, assume I have the following Model and Manager:</p>

<pre class="python"><code>class DefaultThingManager(models.Manager):
    def things():
        # A custom method that retrieves some set of DefaultThing
        # objects. This doesn't override any Manager methods.

class DefaultThing(Model):
    # Some fields.

    objects = DefaultThingManager()
</code></pre>

<p>I've also got some other Manager and Model. Note that this model inherits from
<code>DefaultThingManager</code> (there's some other behavior we want from that class).</p>

<pre class="python"><code>class OtherThingManager(DefaultThingManager):
    def things():
        # Overridden to work with the OtherThing class.

class OtherThing(Model):
    # Some fields.

    objects = OtherThingManager()
</code></pre>

<p>So, that's really the gist of the models and managers. The managers don't
really do anything unusual, but I wanted to write unit tests for them, so
I created a test case that looks something like this:</p>

<pre class="python"><code># defined in tests/defaultthingmanager.py

class TestDefaultThingManager(TestCase):

    def setUp(self):
        # This is my attempt to Fake a Model.
        class M(Model):
            objects = DefaultThingManager()
        self.M = M
        self.assertIsInstance(self.M.objects, DefaultThingManager)

    def test_things(self):
        # Heavily uses Mock to test stuff... eg, to test that the method
        # filtered something correctly, I do stuff like this:
        _f = self.M.objects.filter
        self.M.objects.filter = Mock()

        self.M.objects.things()
        self.M.objects.filter.assert_has_calls([
            # check for stuff here...
        ])
        self.M.objects.filter = _f
</code></pre>

<p>Now, to test the <code>OtherThingManager</code>, I created a similar test case</p>

<pre class="python"><code># defined in tests/otherthingmanager.py

class TestOtherThingManager(TestCase):

    def setUp(self):
        class M(Model):
            objects = OtherThingManager()
        self.M = M
        self.assertIsInstance(self.M.objects, OtherThingManager)

    def test_things(self):
        # Similar to above
</code></pre>

<p>This is where things get a little confusing. While writing these test cases,
I'd run tests restricting them to the test case or the individual test, like
so:</p>

<pre class="python"><code>python manage.py test myapp.TestOtherThingManager</code></pre>

<p>or:</p>

<pre class="python"><code>python manage.py test myapp.TestOtherThingManager.test_things</code></pre>

<p>Doing this, all worked as expected. However, when I ran the full test suite
for an app, my <code>TestOtherThingManager</code> case would start failing. For some
reason, the fake class's manager was an instance of <code>DefaultThingManager</code>
instead of <code>TestOtherThingManager</code>!</p>

<pre class="python"><code>======================================================================
ERROR: test_things (myapp.tests.otherthingmanager.TestOtherThingManager)
----------------------------------------------------------------------
Traceback (most recent call last):
  File &quot;/Users/brad/django/myproject/myapp/tests/managers/otherthingmanager.py&quot;, line 25, in setUp
    self.assertIsInstance(self.M.objects, OtherThingManager)
AssertionError: &lt;myapp.models.DefaultThingManager object at 0x10ae80ed0&gt; is not an instance of &lt;class 'myapp.models.OtherThingManager'&gt;</code></pre>

<p>Now this <em>really</em> made me scratch my head (as well as mutter a few choice words
under my breath). I still don't know why this happened, but here's how I
fixed it.</p>

<p>Remember that fake Model class in <code>setUp</code>? It's now named something different
in each TestCase.</p>

<pre class="python"><code># tests/otherthingmanager.py

class TestOtherThingManager(TestCase):

    def setUp(self):
        class O(Model):  # O for &quot;Other&quot; instead of &quot;M&quot; for Model
            objects = OtherThingManager()
        self.O = O
        self.assertIsInstance(self.O.objects, OtherThingManager)
</code></pre>

<p>Now that the fake Model class has a unique name, all tests pass when run
individually or during a full test suite.</p>

<p>Unfortunately, I don't know whether or not I should blame Mock (it does magic
things at the module, level, right?) or if there's something going on behind
the scenes with Django's test suite that I don't understand. I'm happy my
tests run (100% coverage!), but I've still got a fairly significant uneasy
feeling about all of this.</p>

<p>I'm certain that my method of faking a Model class in <code>setUp</code> is probably
the real culprit, here, and I'd love to have someone <em>enlighten</em> me!</p>

<p>Thanks for reading this far!</p>

<p><strong>UPDATE:</strong>  There's absolutely <em>no reason</em> why you can't just instantiate an ModelManager by itself. For example:</p>

<pre class="python"><code># tests/otherthingmanager.py

class TestOtherThingManager(TestCase):

    def setUp(self):
        self.objects = OtherThingManager()  # This doesn't have to be attached to a Model
        self.assertIsInstance(self.objects, OtherThingManager)
</code></pre>

<p>Lesson learned?  Unless you absolutely need a model, don't make things harder than they need to be!</p>