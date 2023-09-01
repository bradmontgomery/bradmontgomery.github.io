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
description: <p><strong>Update No...
markup: html
url: /blog/chosenjs-in-the-django-admin/
aliases:
- /blog/2011/12/13/chosenjs-in-the-django-admin/

---

<p><strong>Update Nov 23, 2013</strong>: I've written a little app (<a href="https://github.com/bradmontgomery/django-chosenadmin" target="_blank">django-chosenadmin</a>) that'll automatically add this to every app.</p>

<p>Quite some time ago, I ran across the <a href="http://harvesthq.github.com/chosen/" _mce_href="http://harvesthq.github.com/chosen/">chosen.js</a> 
plugin for jQuery and Prototype (I'm using the jQuery flavor). My first thought upon seeing 
this was, "<em>This would rock in Django's admin app.</em>" Yet for some reason, I didn't make that 
happen.</p><p>Until recently.</p>

<p>I maintain a project where about 10 people use the admin app extensively.  They manage several apps that 
have foreign keys to django's <code>User</code> model. This works well enough, but there are a few thousand
user accounts. That makes the default <code>&lt;select&gt;</code> elements fairly unwieldy, and the 
<code>&lt;select multiple&gt;</code> widgets are just horrendous!</p>

<p>Fortunately, the <code>chosen.js</code> plugin is fairly straighforward to install for the 
admin. You'll first need to grab a copy of <code>chosen.js</code> and (if you want to use them) the default CSS and sprite files. 
I just grabbed the most current version from <a href="https://github.com/harvesthq/chosen" _mce_href="https://github.com/harvesthq/chosen">github</a>.</p>
<ul>
<li><code>chosen.js</code>: 
    <a href="https://github.com/harvesthq/chosen/blob/master/chosen/chosen.jquery.min.js" _mce_href="https://github.com/harvesthq/chosen/blob/master/chosen/chosen.jquery.min.js">
    https://github.com/harvesthq/chosen/blob/master/chosen/chosen.jquery.min.js</a></li>
<li><code>chosen.css</code>: 
    <a href="https://github.com/harvesthq/chosen/blob/master/chosen/chosen.css" _mce_href="https://github.com/harvesthq/chosen/blob/master/chosen/chosen.css">
    https://github.com/harvesthq/chosen/blob/master/chosen/chosen.css</a></li>
<li><code>chosen-sprite.png</code>: 
    <a href="https://github.com/harvesthq/chosen/blob/master/chosen/chosen-sprite.png" _mce_href="https://github.com/harvesthq/chosen/blob/master/chosen/chosen-sprite.png">
    https://github.com/harvesthq/chosen/blob/master/chosen/chosen-sprite.png</a></li>
</ul>

<p>My static files are organized as follows. Note that I put chosen's CSS &amp; sprite 
files in a subdirectory named <code>chosen</code>:</p>
<pre>project_directory/
    static/
        css/
            chosen/
                chosen.css
                chosen-sprite.png
        js/
            chosen.js
    
</pre>

<p>Now, you can override the admin app's 
    <a href="https://github.com/django/django/blob/master/django/contrib/admin/templates/admin/change_form.html" _mce_href="https://github.com/django/django/blob/master/django/contrib/admin/templates/admin/change_form.html">change_form.html</a> 
    template (be sure to get a copy for <em>your</em> version of django. You can do this by putting your 
    own copy of the template in your project's templates directory (see your <code>TEMPLATE_DIRS</code> setting).  
    For me, that looks like this:</p>
    
<pre>project_directory/
    templates/
        admin/
            change_form.html
</pre>

<p>In that template, there's an <code>extrahead</code> block. At the bottom of that block, you need to include a 
link to the plugin and the css file. Since this is a jQuery plugin, you'll also need to include a link to jQuery.
(<em>Even though django's admin comes bundled with jQuery, it's namespaced, so to use a 3rd-party plugin, you need
your own copy of the library. See 
<a href="https://docs.djangoproject.com/en/dev/ref/contrib/admin/#modeladmin-media-definitions" _mce_href="https://docs.djangoproject.com/en/dev/ref/contrib/admin/#modeladmin-media-definitions">this note</a></em>)</p>

<pre class="html"><code>&lt;script 
    src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js" 
    type="text/javascript"&gt;&lt;/script&gt;
&lt;script 
    src="{{ STATIC_URL }}js/chosen.jquery.min.js" 
    type="text/javascript"&gt;&lt;/script&gt;
&lt;link rel="stylesheet" href="{{ STATIC_URL }}css/chosen/chosen.css"/&gt;
</code></pre>
<p>Now, you can apply the chosen plugin to all <code>&lt;select&gt;</code> elements!</p>
<pre class="javascript"><code>&lt;script type="text/javascript"&gt;
$(document).ready(function() {
    $('select').chosen();
});
&lt;/script&gt;
</code></pre>

<p>However, this has one unfortunate side effect. Django's admin app contains a custom multi-select widget, 
    that normally looks like this:<br>
    <img src="http://files.bradmontgomery.net/images/django-admin-multi-select.png" _mce_src="http://files.bradmontgomery.net/images/django-admin-multi-select.png" alt="django admin custom multi-select"></p>
<p>The chosen plugin dutifully mangles the custom widget, which is probably not what you want:<br>
    <img src="http://files.bradmontgomery.net/images/django-admin-broken-multi-select.png" _mce_src="http://files.bradmontgomery.net/images/django-admin-broken-multi-select.png" alt="django admin custom multi-select"></p>
<p>The admin app's custom widget includes javascript that gets loaded after the page loads. Luckily, it includes a <code>filtered</code> 
class on the elements to which it is applied. So, we need the <code>chosen</code> plugin to load <em>after</em> the admin app's javascript
has run.</p>
<p>The only what I got that to work was to use <code>setTimeout</code>. This is definitely a hack, and I'd love to see a more elegant
solution... but it works. So, the previous code to initialize the chosen plugin would be replaced with the following:</p>
<pre class="javascript"><code>&lt;script type="text/javascript"&gt;
setTimeout(function() {
    $('select').not('.filtered').chosen();
}, 1000);
&lt;/script&gt;
</code></pre>
<p>Now the plugin gets loaded about 1 second after the page is finished loading, so you get <em>both</em> the admin app's 
custom multi-select widget and the <code>chosen.js</code> plugin. There's a visible delay before the plugin gets loaded, 
but you could tweak the second argument to minimize this somewhat. For my needs, the benefits of the more usable interface 
for <code>&lt;select&gt;</code> elements outweigh the cost of loading the plugin.</p>