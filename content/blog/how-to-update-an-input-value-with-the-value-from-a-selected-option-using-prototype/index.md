---
date: '2008-08-12T10:32:00+00:00'
title: How to update an input value with the value from a selected option using Prototype
draft: false
tags:
- Javascript
- Programming
- web
slug: how-to-update-an-input-value-with-the-value-from-a-selected-option-using-prototype
description: ''
markup: md
url: /blog/how-to-update-an-input-value-with-the-value-from-a-selected-option-using-prototype/
aliases:
- /blog/2008/08/12/how-to-update-an-input-value-with-the-value-from-a-selected-option-using-prototype/

---

Today, I needed to set the value of an HTML input element based on the value of a option in a select element. This is fairly easy to do with [Prototype's writeAttribute](http://www.prototypejs.org/api/element/writeAttribute). Here's an example:  
  
A simple javascript function to do the work:  

```
function populate_input(){  
    var field = $('tf\_select').getValue();   
    $('tf').writeAttribute('value', field);  
}  

```
  
  
A simple HTML snippet to see it in action:  

```
<div>  
<p><select id="tf\_select" name="tf\_select" onchange="populate\_input();">  
<option value="">- choose one -</option>  
<option value="v1">value 1</option>  
<option value="v2">value 2</option>  
</select><br/><input type="test" id="tf" name="tf" value=""/></p>  
</div>  

```
  
  
And yes... I know the title of this post is almost longer than the post itself!