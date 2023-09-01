---
date: '2012-09-26T20:28:07+00:00'
title: Django Models & Mixins for cleaner code
draft: false
tags:
- django
- mixins
- programming
- python
slug: django-models-mixins-for-cleaner-code
description: "<p>\nI've been using ..."
markup: html
url: /blog/django-models-mixins-for-cleaner-code/
aliases:
- /blog/2012/09/26/django-models-mixins-for-cleaner-code/

---

<p>
I've been using Mixins lately to <abbr title="Don't Repeat Yourself">DRY</abbr>-ly 
make certain behavior available to several different Django models. If you're not familiar
with mixins, there's a <a href="http://goo.gl/rN3Ye" _mce_href="http://goo.gl/rN3Ye">great discussion over on StackOverflow</a>.
</p>

<p>
Here's a simple example to illustrate what I've been doing. In building 
<a href="http://workforpie.com" _mce_href="http://workforpie.com" target="_blank">Work for Pie</a>, we've got a
<code>UserProfile</code> model that looks something like this:
</p>

<pre class="python"><code>class UserProfile(models.Model):
    user = models.OneToOneField(User)
    tagline = models.CharField(max_length=140)
    biography = models.TextField()
    avatar_url = models.URLField(max_length=256)

    # several other things, too...</code></pre>

<p>
But, we also have a number of other models that are associated with <code>User</code>
objects, such as a <code>Score</code>:
</p>

<pre class="python"><code>class Score(models.Model):
    user = models.ForeignKey(User) 
    score = models.IntegerField()

    # some other stuff</code></pre>

<p>
Now, there are a number of scenarios where you might want to display a User's
<code>Score</code>, and that's not too difficult to do using the ORM. In fact,
we've got a <a href="http://goo.gl/Jn1Bo" _mce_href="http://goo.gl/Jn1Bo">Manager method</a>, <code>latest</code>,
that lets us get the most recent <code>Score</code> associated with a User.
</p>

<pre class="python"><code>score = Score.objects.filter(user__username='bkmontgomery').latest()</code></pre>

<p>
However... that soon starts to feel redundant if you want to include a user's 
score elsewhere—in an other app or a somewhat unrelated model, for example.
Image that we also have comments:
</p>

<pre class="python"><code>class Comment(models.Model):
    user = models.ForeignKey(User, help_text="The comment's author") 
    content = models.TextField()</code></pre>

<p>
What if you always wanted to show a users score next to their comments? You
might do something like this in a template (<em>assume <code>comment</code>
is a Comment instance</em>):
</p>

<pre class="html"><code>&lt;span class="score"&gt;{{ comment.user.score_set.latest }}&lt;span&gt;</code></pre>

<p>
Likewise, if you wanted to link back to the user's profile, you might do
something like this:
</p>

<pre class="html"><code>&lt;a href="{{ comment.user.userprofile.get_absolute_url }}"&gt;view profile&lt;a&gt;</code></pre>

<p>This works, but it's fairly verbose.</p>

<h2>Save some effort...</h2>
<p>Here's where a Mixin can save you some work. First, let's assume that we 
want to be able to access a user's score on any model that also has a ForeignKey
to <code>User</code>. You could build a <code>ScoreMixin</code> class like the
following:</p>

<pre class="python"><code>class ScoreMixin(object):
    """Mixin to another class to provide access to a User's ``Score``."""
    @property
    def score(self):
        """Get the latest score for the User who saved this Job."""
        if not hasattr(self, "_score"):
            self._score = self.user.score_set.latest()
        return self._score</code></pre>

<p><em>Keep in mind: this code assumes any model that inherits from this class
will have a <code>user</code> attribute.</em></p>

<p>We can now augment our <code>Comment</code> class as follows, which will give
all <code>Comment</code> instances a <code>score</code> attribute:

</p><pre class="python"><code>class Comment(ScoreMixin, models.Model):
    user = models.ForeignKey(User, help_text="The comment's author") 
    content = models.TextField()</code></pre>

<p>Now, our template can be a bit more concise:</p>
<pre class="html"><code>&lt;span class="score"&gt;{{ comment.score }}&lt;span&gt;</code></pre>

<p>I've found that simple cases like this, let me easily reuse some behavior for models
that already have a common attribute or field.</p>