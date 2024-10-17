---
date: '2009-04-24T18:36:00+00:00'
title: Restricting Access by Group in Django
draft: false
tags:
- Python
- django
- web
slug: restricting-access-by-group-in-django
description: ''
markup: md
url: /blog/restricting-access-by-group-in-django/
aliases:
- /blog/2009/04/24/restricting-access-by-group-in-django/

---

Django's [authentication](http://docs.djangoproject.com/en/1.0/topics/auth/)
system provides built-in support for Groups. When developing an app, you may
want to prevent users in a particular group from accessing part of your app.


For example, if you were building a tool to be used by *Faculty*
and *Students*, it's quite possible that there would be parts of the
app you wouldn't want *Students* to access (like the part that allows a
User to change grades!). Luckily, there's a decorator called
*[user\_passes\_test](http://docs.djangoproject.com/en/1.0/topics/auth/#limiting-access-to-logged-in-users-that-pass-a-test)*
that allows you to easily perform this sort of thing. Let's see an example:



```
from django.contrib.auth.decorators import login_required, user_passes_test  
  
@login\_required  
@user\_passes\_test(lambda u: u.groups.filter(name='Student').count() == 0, login_url='/myapp/denied/')  
def some\_view(request):  
  
    # Do whatever this view should do  

```

The view above (which lacks any content) actually uses two decorators.
The first *login\_required* simply requires that a user be logged in.
The second, *user\_passes\_test*, requires a function as the first argument.
This function must accept a User object and return True or False.
If True, the User can view the page. If False, the user cannot view the page.


We define this function using a python
[Lambda Expression](http://docs.python.org/reference/expressions.html#lambdas).
It simply uses the ORM to check if a User is in the *Student* group.
In this example, **u** would be an instance of django.contrib.auth.models.User.



```
lambda u: u.groups.filter(name='Student').count() == 0  

```

Additionally, you can specify the keyword argument *login\_url* to the
*user\_passes\_test* decorator. Normally, if the user failed the test this
would redirect them to a login page. However, in our case, they're already
logged in (because of the *login\_required* decorator), so this just acts
as a redirect page. In this example, it would redirect to a url that we've
specified which might contain an Access Denied message (*with giant red
blinking letters*!)


Just kidding.


UPDATE: There is one slight caveat to this solution so far... it breaks if
your user is not already logged in. In fact, this will result in


**AttributeError**:`'NoneType' object has no attribute '_meta'`


So, to account for that, we need to put the logic that tests for
Student-group membership into its own function. The result would look
something like the following:



```
def not\_in\_student\_group(user):  
    if user:  
        return user.groups.filter(name='Student').count() == 0  
    return False
```

This makes sure the user object exists before trying the test, and if not,
we assume the test fails (by returning False). Now, our decorator will look
something like this:



```
@login\_required  
@user\_passes\_test(not_in_student_group, login_url='/advising/denied/')  
def some\_view(request):  
    # ...  

```
