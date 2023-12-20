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
description: ''
markup: md
url: /blog/django-models-mixins-for-cleaner-code/
aliases:
- /blog/2012/09/26/django-models-mixins-for-cleaner-code/

---


I've been using Mixins lately to DRY-ly 
make certain behavior available to several different Django models. If you're not familiar
with mixins, there's a [great discussion over on StackOverflow](http://goo.gl/rN3Ye).




Here's a simple example to illustrate what I've been doing. In building 
[Work for Pie](http://workforpie.com), we've got a
`UserProfile` model that looks something like this:




```
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    tagline = models.CharField(max_length=140)
    biography = models.TextField()
    avatar_url = models.URLField(max_length=256)

    # several other things, too...
```


But, we also have a number of other models that are associated with `User`
objects, such as a `Score`:




```
class Score(models.Model):
    user = models.ForeignKey(User) 
    score = models.IntegerField()

    # some other stuff
```


Now, there are a number of scenarios where you might want to display a User's
`Score`, and that's not too difficult to do using the ORM. In fact,
we've got a [Manager method](http://goo.gl/Jn1Bo), `latest`,
that lets us get the most recent `Score` associated with a User.




```
score = Score.objects.filter(user__username='bkmontgomery').latest()
```


However... that soon starts to feel redundant if you want to include a user's 
score elsewhere—in an other app or a somewhat unrelated model, for example.
Image that we also have comments:




```
class Comment(models.Model):
    user = models.ForeignKey(User, help_text="The comment's author") 
    content = models.TextField()
```


What if you always wanted to show a users score next to their comments? You
might do something like this in a template (*assume `comment`
is a Comment instance*):




```
<span class="score">{{ comment.user.score_set.latest }}<span>
```


Likewise, if you wanted to link back to the user's profile, you might do
something like this:




```
<a href="{{ comment.user.userprofile.get_absolute_url }}">view profile<a>
```

This works, but it's fairly verbose.


Save some effort...
-------------------


Here's where a Mixin can save you some work. First, let's assume that we 
want to be able to access a user's score on any model that also has a ForeignKey
to `User`. You could build a `ScoreMixin` class like the
following:



```
class ScoreMixin(object):
    """Mixin to another class to provide access to a User's ``Score``."""
    @property
    def score(self):
        """Get the latest score for the User who saved this Job."""
        if not hasattr(self, "_score"):
            self._score = self.user.score_set.latest()
        return self._score
```

*Keep in mind: this code assumes any model that inherits from this class
will have a `user` attribute.*


We can now augment our `Comment` class as follows, which will give
all `Comment` instances a `score` attribute:




```
class Comment(ScoreMixin, models.Model):
    user = models.ForeignKey(User, help_text="The comment's author") 
    content = models.TextField()
```

Now, our template can be a bit more concise:



```
<span class="score">{{ comment.score }}<span>
```

I've found that simple cases like this, let me easily reuse some behavior for models
that already have a common attribute or field.

