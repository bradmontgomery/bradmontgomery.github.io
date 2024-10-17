---
date: '2011-12-13T16:00:48+00:00'
title: Chosen.js in the Django admin
draft: false
tags:
- chosenjs
- django
- javascript
- jquery
- python
- web
slug: chosenjs-in-the-django-admin
description: ''
markup: md
url: /blog/chosenjs-in-the-django-admin/
aliases:
- /blog/2011/12/13/chosenjs-in-the-django-admin/

---

**Update Nov 23, 2013**: I've written a little app ([django-chosenadmin](https://github.com/bradmontgomery/django-chosenadmin)) that'll automatically add this to every app.


Quite some time ago, I ran across the [chosen.js](http://harvesthq.github.com/chosen/) 
plugin for jQuery and Prototype (I'm using the jQuery flavor). My first thought upon seeing 
this was, "*This would rock in Django's admin app.*" Yet for some reason, I didn't make that 
happen.

Until recently.


I maintain a project where about 10 people use the admin app extensively. They manage several apps that 
have foreign keys to django's `User` model. This works well enough, but there are a few thousand
user accounts. That makes the default `<select>` elements fairly unwieldy, and the 
`<select multiple>` widgets are just horrendous!


Fortunately, the `chosen.js` plugin is fairly straighforward to install for the 
admin. You'll first need to grab a copy of `chosen.js` and (if you want to use them) the default CSS and sprite files. 
I just grabbed the most current version from [github](https://github.com/harvesthq/chosen).


* `chosen.js`: 
 <https://github.com/harvesthq/chosen/blob/master/chosen/chosen.jquery.min.js>
* `chosen.css`: 
 <https://github.com/harvesthq/chosen/blob/master/chosen/chosen.css>
* `chosen-sprite.png`: 
 <https://github.com/harvesthq/chosen/blob/master/chosen/chosen-sprite.png>


My static files are organized as follows. Note that I put chosen's CSS & sprite 
files in a subdirectory named `chosen`:



```
project_directory/
    static/
        css/
            chosen/
                chosen.css
                chosen-sprite.png
        js/
            chosen.js
    

```

Now, you can override the admin app's 
 [change\_form.html](https://github.com/django/django/blob/master/django/contrib/admin/templates/admin/change_form.html) 
 template (be sure to get a copy for *your* version of django. You can do this by putting your 
 own copy of the template in your project's templates directory (see your `TEMPLATE_DIRS` setting). 
 For me, that looks like this:



```
project_directory/
    templates/
        admin/
            change_form.html

```

In that template, there's an `extrahead` block. At the bottom of that block, you need to include a 
link to the plugin and the css file. Since this is a jQuery plugin, you'll also need to include a link to jQuery.
(*Even though django's admin comes bundled with jQuery, it's namespaced, so to use a 3rd-party plugin, you need
your own copy of the library. See 
[this note](https://docs.djangoproject.com/en/dev/ref/contrib/admin/#modeladmin-media-definitions)*)



```
<script 
    src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js" 
    type="text/javascript"></script>
<script 
    src="{{ STATIC_URL }}js/chosen.jquery.min.js" 
    type="text/javascript"></script>
<link rel="stylesheet" href="{{ STATIC_URL }}css/chosen/chosen.css"/>

```

Now, you can apply the chosen plugin to all `<select>` elements!



```
<script type="text/javascript">
$(document).ready(function() {
    $('select').chosen();
});
</script>

```

However, this has one unfortunate side effect. Django's admin app contains a custom multi-select widget, 
 that normally looks like this:  

![django admin custom multi-select](http://files.bradmontgomery.net/images/django-admin-multi-select.png)


The chosen plugin dutifully mangles the custom widget, which is probably not what you want:  

![django admin custom multi-select](http://files.bradmontgomery.net/images/django-admin-broken-multi-select.png)


The admin app's custom widget includes javascript that gets loaded after the page loads. Luckily, it includes a `filtered` 
class on the elements to which it is applied. So, we need the `chosen` plugin to load *after* the admin app's javascript
has run.


The only what I got that to work was to use `setTimeout`. This is definitely a hack, and I'd love to see a more elegant
solution... but it works. So, the previous code to initialize the chosen plugin would be replaced with the following:



```
<script type="text/javascript">
setTimeout(function() {
    $('select').not('.filtered').chosen();
}, 1000);
</script>

```

Now the plugin gets loaded about 1 second after the page is finished loading, so you get *both* the admin app's 
custom multi-select widget and the `chosen.js` plugin. There's a visible delay before the plugin gets loaded, 
but you could tweak the second argument to minimize this somewhat. For my needs, the benefits of the more usable interface 
for `<select>` elements outweigh the cost of loading the plugin.

