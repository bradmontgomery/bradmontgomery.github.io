---
date: '2009-06-26T09:47:00+00:00'
title: '"Adding" Q objects in Django'
draft: false
tags:
- Python
- django
- web
slug: adding-q-objects-in-django
description: ''
markup: md
url: /blog/adding-q-objects-in-django/
aliases:
- /blog/2009/06/26/adding-q-objects-in-django/

---

I've got a Django app with the following Model:  
  

```
  
class Story(models.Model):  
    title = models.CharField(max_length=255)  
    content = models.TextField()  

```
  
  
The Problem:   
I wanted to build a simple search feature that OR'ed all the search terms. Essentially, I wanted SQL resembling the following:  

```
SELECT \* from myapp_stories where   
    title LIKE '%term1%' OR content LIKE '%term1%' OR   
    title LIKE '%term2%' OR content LIKE '%term2%';   

```
  
  
The Solution:   
You can *add* django's Q objects together! This is a feature not currently discussed in the docs, but I dug through the source code and I discovered that a Q object is really just a node in a Tree! More specifically, Q is a subclass of django.utils.tree.Node (check it out, it's cool!) A Node has a attribute called a *connector*. Q objects have two possible connectors: *AND* and *OR*. But how do we connect Q objects? Well, a Node has a handy *add(node, conn\_type)* method whose parameters include another Node and a connection type.  
  
As previously mentioned, the possible connection types for Q objects are *AND* and *OR*, so Q objects can be added together by doing something like this:  
  

```
# ANDing Q objects  
q_object = Q()  
q_object.add(Q(), Q.AND)  
  
# ORing Q objects  
q_object = Q()  
q_object.add(Q(), Q.OR)  

```
  
  
So, the solution to my Search view is as follows:  
  

```
  
from django.db.models import Q  
from models import Story  
  
def search(request):  
    '''   
 Generic Search: GET should contain the following:   
 terms - the search keywords separated by spaces  
 '''  
    terms = request.GET.get('terms', None)  
    term_list = terms.split(' ')  
  
    stories = Story.objects.all()  
  
    q = Q(content__icontains=term_list[0]) | Q(title__icontains=term_list[0])  
    for term in term_list[1:]:  
        q.add((Q(content__icontains=term) | Q(title__icontains=term)), q.connector)  
  
    stories = stories.filter(q)  
  
    return render_to_response('myapp/search.html', locals(), \  
            context_instance=RequestContext(request))  

```
  
  
Needless to say, Q objects are quite powerful!![](https://blogger.googleusercontent.com/tracker/4123748873183487963-102694916469535041?l=bradmontgomery.blogspot.com)