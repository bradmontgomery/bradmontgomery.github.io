---
date: '2012-10-30T21:30:49+00:00'
title: Customizing Django's password_change view
draft: false
tags:
- django
- programming
- python
- web
slug: customizing-djangos-password_change-view
description: ''
markup: md
url: /blog/customizing-djangos-password_change-view/
aliases:
- /blog/2012/10/30/customizing-djangos-password_change-view/

---

If you have a site where users have the traditional
*username*/*password* combination, you've got to provide some
way to let users **change** their password. Luckily, this is
fairly easy to do with Django. The `auth` app comes with a 
[password\_change](http://goo.gl/sMDqI) view that does what you'd
probably expect.


It's also fairly easy to set up. You add a line similar to the following
to your root URLConf:



```
url(r'^accounts/', include('django.contrib.auth.urls')),
```

You also have to set up some additional templates (e.g. `registration/password_change_form.html`),
but once you've done that, users can change their password using a form that 
looks something like this:



Old password:   

New password:   

New password confirmation: 

Easy! Until...


What if I can't remember my old password?
-----------------------------------------


Or worse, yet, what if your users don't have a usable password? If you're
using something like the excellent [django-social-auth](http://django-social-auth.readthedocs.org/), which lets users log in using OAuth or OpenID (i.e. via
Facebook, Twitter, Google, or some other source) you may run into this case.


So, how can I omit the *Old Password* requirement in the change
password form? We're in luck. The `password_change` view accepts a
`password_change_form` parameter that allows you to specify what form
is used. The `auth` app also contains a form that doesn't require
entering the Old password (it's used in the admin app!). It's called, 
`AdminPasswordChangeForm`. So, all we have to do is update our
root URLConf yet again:



```
from django.contrib.auth.forms import AdminPasswordChangeForm

ulrpatterns = patterns('', 
    
    # ...
    
    url(r'^accounts/password_change/$',  # hijack password_change's url
        'django.contrib.auth.views.password_change',
        {'password_change_form': AdminPasswordChangeForm},
        name="password_change"),
    url(r'^accounts/', include('django.contrib.auth.urls')),
```

Remember that the [url function](http://goo.gl/A2pLz) allows you
to specify keword parameters for views, and that's exactly what we've done with
this: `{'password_change_form': AdminPasswordChangeForm}`. That
customizes the form that gets used in the `password_change` view.


Now, when our users try to change their password, the form looks something
like this:



New password:   

New password confirmation: 

Disclaimer: This *does* remove one additional step that a potential
attacker would need to overcome in order to steal an account. So, make sure you
understand why you'd implement this before you do so.


Cheers!

