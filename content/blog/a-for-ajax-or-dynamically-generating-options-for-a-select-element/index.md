---
date: '2009-07-14T11:42:00+00:00'
title: A for AJAX - OR - Dynamically generating options for a select element.
draft: false
tags:
- Javascript
- Prototype
- ajax
- web
slug: a-for-ajax-or-dynamically-generating-options-for-a-select-element
description: ''
markup: md
url: /blog/a-for-ajax-or-dynamically-generating-options-for-a-select-element/
aliases:
- /blog/2009/07/14/a-for-ajax-or-dynamically-generating-options-for-a-select-element/

---

I don't do a lot of AJAXy web development, but when I do, I usually make use of [Prototype](http://prototypejs.org/). I've recently created a form containing a *<select>* element whose *<option>*s are dynamically generated via an AJAX request. The problem however, is that a ***selected** option* was already in the form. So before the AJAX request, my HTML looked something like this:  

```
<select name="s" id="s">  
<option value="val1">Value 1</option>  
<option value="val2" selected="selected">Value 2</option>  
<option value="val3">Value 3</option>  
</select>
```
  
  
We can then use [Ajax.Request](http://prototypejs.org/api/ajax/request) method to dynamically add items into this list. (Note here that *http://example.com/dynamic/options/* would be a server-side script giving us our dynamically generated *<option>* tags.)   

```
new Ajax.Request('http://example.com/dynamic/options/', {  
    method: 'post',  
    onSuccess: function(transport) {  
        if (transport.responseText)  
            Element.insert($('s'), transport.responseText);  
    }  
}); 
```
  
Our resulting HTML might look something like the following:  
  

```
<select name="s" id="s">  
<option value="val1">Value 1</option>  
<option value="val2" selected="selected">Value 2</option>  
<option value="val3">Value 3</option>  
<option value="val4">Value 4</option>  
<option value="val5">Value 5</option>  
<option value="val6">Value 6</option>  
</select>
```
  
  
One problem that arises, is that once the above *<option>s* are inserted into the original *<select>* element, the originally selected option is no longer selected. (In my experiments using Firefox 3.5 on OS X, the last item — in this case, *Value 6*— becomes selected).  
  
That's not so bad, though, because a little more code will just set the correct <option> as selected. The following code looks at all the options until it finds one with the attribute: *selected="selected"*, and then ... selects it!  

```
var selected_index = 0;  
while (!$('s').down(selected_index).defaultSelected) {  
    selected_index += 1;  
}                 
$('s').selectedIndex = selected_index;
```
  
  
**However...** one must be careful where one puts this code! You **must** take into account that the Ajax Request is **asynchronous** (that's the *A* in AJAX)!   
  
Here's what NOT to do:  

```
function append_options() {  
    // Request the dynamically generated options  
    new Ajax.Request('http://example.com/dynamic/options/', {  
        method: 'post',  
        onSuccess: function(transport) {  
            if (transport.responseText)  
                Element.insert($('s'), transport.responseText);  
        }     
    });   
    // Make sure the correct on is selected. var selected\_index = 0;  
    while (!$('s').down(selected_index).defaultSelected) {  
        selected_index += 1;  
    }  
    $('s').selectedIndex = selected_index;  
}  
document.observe('dom:loaded', function() {  
    append_options();  
});
```
  
  
The Ajax request is sent, but the portion of the code that selects the option containing selected="selected" may get run **before** there is a response to that Request. Therefore, the selected option gets set, then the dynamically generated options get inserted. This is not what we want!  
  
The proper way to do this is to use the *onComplete* callback in Ajax.Request. This will ensure that the code to select the appropriate option is run **after** the Request is completed.   

```
function append_options() {  
    // Request the dynamically generated options  
    new Ajax.Request('http://example.com/dynamic/options/', {  
        method: 'post',  
        onSuccess: function(transport) {  
            if (transport.responseText)  
                Element.insert($('s'), transport.responseText);  
        },    
        onComplete: function(transport) {  
            // Make sure the correct on is selected.  
            var selected_index = 0;  
            while (!$('s').down(selected_index).defaultSelected) {  
                selected_index += 1;  
            }  
            $('s').selectedIndex = selected_index;  
        }  
    });   
}  
document.observe('dom:loaded', function() {  
    append_options();  
});
```
  
  
This is fairly basic AJAX behavior, but for those of us who don't live, breathe, eat, and sleep AJAX, this is an easy mistake to make.  
  
So the moral of this story? Know your tools! It's always good to *Know what's going on!*™![](https://blogger.googleusercontent.com/tracker/4123748873183487963-5043486322654878551?l=bradmontgomery.blogspot.com)