---
date: '2009-04-24T18:36:00+00:00'
title: Restricting Access by Group in Django
draft: false
tags:
- Python
- django
- web
slug: restricting-access-by-group-in-django
description: <p>Django's <a href=...
markup: html
url: /blog/restricting-access-by-group-in-django/
aliases:
- /blog/2009/04/24/restricting-access-by-group-in-django/

---

<p>Django's <a href="http://docs.djangoproject.com/en/1.0/topics/auth/">authentication</a>
system provides built-in support for Groups.  When developing an app, you may
want to prevent users in a particular group from accessing part of your app.</p>

<p>For example, if you were building a tool to be used by <em>Faculty</em>
and <em>Students</em>, it's quite possible that there would be parts of the
app you wouldn't want <em>Students</em> to access (like the part that allows a
User to change grades!). Luckily, there's a decorator called
<em><a href="http://docs.djangoproject.com/en/1.0/topics/auth/#limiting-access-to-logged-in-users-that-pass-a-test">user_passes_test</a></em>
that allows you to easily perform this sort of thing. Let's see an example:</p>

<div class="highlight" ><pre><span style="color: #007020; font-weight: bold">from</span> <span style="color: #0e84b5; font-weight: bold">django.contrib.auth.decorators</span> <span style="color: #007020; font-weight: bold">import</span> login_required, user_passes_test<br /><br /><span style="color: #555555; font-weight: bold">@login_required</span><br /><span style="color: #555555; font-weight: bold">@user_passes_test</span>(<span style="color: #007020; font-weight: bold">lambda</span> u: u<span style="color: #666666">.</span>groups<span style="color: #666666">.</span>filter(name<span style="color: #666666">=</span><span style="color: #4070a0">&#39;Student&#39;</span>)<span style="color: #666666">.</span>count() <span style="color: #666666">==</span> <span style="color: #40a070">0</span>, login_url<span style="color: #666666">=</span><span style="color: #4070a0">&#39;/myapp/denied/&#39;</span>)<br /><span style="color: #007020; font-weight: bold">def</span> <span style="color: #06287e">some_view</span>(request):<br /><br />    <span style="color: #60a0b0; font-style: italic"># Do whatever this view should do</span><br /></pre></div>

<p>The view above (which lacks any content) actually uses two decorators.
The first <em>login_required</em> simply requires that a user be logged in.
The second, <em>user_passes_test</em>, requires a function as the first argument.
This function must accept a User object and return True or False.
If True, the User can view the page.  If False, the user cannot view the page.</p>

<p>We define this function using a python
<a href="http://docs.python.org/reference/expressions.html#lambdas">Lambda Expression</a>.
It simply uses the ORM to check if a User is in the <em>Student</em> group.
In this example, <b>u</b> would be an instance of django.contrib.auth.models.User.</p>

<div class="highlight" ><pre><span style="color: #007020; font-weight: bold">lambda</span> u: u<span style="color: #666666">.</span>groups<span style="color: #666666">.</span>filter(name<span style="color: #666666">=</span><span style="color: #4070a0">&#39;Student&#39;</span>)<span style="color: #666666">.</span>count() <span style="color: #666666">==</span> <span style="color: #40a070">0</span><br /></pre></div>

<p>Additionally, you can specify the keyword argument <em>login_url</em> to the
<em>user_passes_test</em> decorator.  Normally, if the user failed the test this
would redirect them to a login page.  However, in our case, they're already
logged in (because of the <em>login_required</em> decorator), so this just acts
as a redirect page.  In this example, it would redirect to a url that we've
specified which might contain an Access Denied message (<em>with giant red
blinking letters</em>!)</p>

<p>Just kidding.</p>

<p>UPDATE: There is one slight caveat to this solution so far... it breaks if
your user is not already logged in. In fact, this will result in</p>

<p><b>AttributeError</b>:<code>'NoneType' object has no attribute '_meta'</code></p>

<p>So, to account for that, we need to put the logic that tests for
Student-group membership into its own function.  The result would look
something like the following:</p>

<div class="highlight" ><pre><span style="color: #007020; font-weight: bold">def</span> <span style="color: #06287e">not_in_student_group</span>(user):<br />    <span style="color: #007020; font-weight: bold">if</span> user:<br />        <span style="color: #007020; font-weight: bold">return</span> user<span style="color: #666666">.</span>groups<span style="color: #666666">.</span>filter(name<span style="color: #666666">=</span><span style="color: #4070a0">&#39;Student&#39;</span>)<span style="color: #666666">.</span>count() <span style="color: #666666">==</span> <span style="color: #40a070">0</span><br />    <span style="color: #007020; font-weight: bold">return</span> <span style="color: #007020">False</span></pre></div>

<p>This makes sure the user object exists before trying the test, and if not,
we assume the test fails (by returning False). Now, our decorator will look
something like this:</p>

<div class="highlight" ><pre><span style="color: #555555; font-weight: bold">@login_required</span><br /><span style="color: #555555; font-weight: bold">@user_passes_test</span>(not_in_student_group, login_url<span style="color: #666666">=</span><span style="color: #4070a0">&#39;/advising/denied/&#39;</span>)<br /><span style="color: #007020; font-weight: bold">def</span> <span style="color: #06287e">some_view</span>(request):<br />    <span style="color: #60a0b0; font-style: italic"># ...</span><br /></pre></div><div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/4123748873183487963-1124320250064783173?l=bradmontgomery.blogspot.com' alt='' /></div>