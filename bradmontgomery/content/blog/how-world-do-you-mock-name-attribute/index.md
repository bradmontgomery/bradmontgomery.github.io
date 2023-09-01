---
date: '2013-03-15T03:43:17.745865+00:00'
title: How in the world do you Mock a name attribute?
draft: false
tags:
- mock
- python
- testing
slug: how-world-do-you-mock-name-attribute
description: ''
markup: md
url: /blog/how-world-do-you-mock-name-attribute/
aliases:
- /blog/2013/03/15/how-world-do-you-mock-name-attribute/

---

**Or...**  My adventures with Mock. Part 1.


I've been working a lot with
[Mock](http://www.voidspace.org.uk/python/mock/)
lately (and by *lately*, I meand for the last three months). Though it
takes a while to wrap your head around it, it's an amazing and powerful testing
tool.


To get started, let's look at some of the neat things you can do with Mock.
Take this class, for example:



```
class Thing(object):
    shape = 'square'
    color = 'blue'

    def calculate(self):
        # ... do some stuff ...

```

If you were writing a test, and you wanted a Mocked `Thing`, but
still wanted to ensure that your mock object had `shape` and
`color` attributes, you'd do the following:

```
>>> from mock import Mock
>>> thing = Mock(shape='square', color='blue')
>>> thing.shape
'square'
>>> thing.color
'blue'
```

Cool! You get attributes whose values you can test against, and you still
have a mock object on which you can call methods:



```
>>> from mock import Mock
>>> thing.calculate()  # pretend this calculates something
<Mock name='mock.calculate()' id='4338034768'>
```

I think Mock really shines when you're working with code that hits external
APIs (I do this a *lot* with
[Work for Pie](https://workforpie.com)). Imagine for a minute that
the `Thing.calculate()` sent some data up to an external API, then
used the results to calculate and return a value. With a Mocked object, your
tests can run without hitting the api. This is a Good Thing! In order to write
that test, you'd do somethign like this



```
from mock import calls

def test_calculate():
    thing = Mock(shape='square', color='blue')
    thing.calculate()
    thing.assert_has_calls([call.calculate()])
```

So what was that thing about `name` attributes?
-----------------------------------------------


Now here's where things get tricky. For one reason or another, many of my
API-wrapper classes have a `name` attribute. The Mock class also
has a keyword argument `name`, that lets you give the Mock a name
(the [docs](http://www.voidspace.org.uk/python/mock/mock.html#mock.Mock) say this is useful for debugging).


So, how in the world am I supposed to write a Mock for something like this,
and still be able to specify the value of an attribute?



```
class SomeAPIWrapper(object):
    name = 'brad'
    token = 'secret'
```

Well, this **does not work**:



```
>>> api = Mock(name='brad', token='secret')
>>> api.token  # Ok, this looks fine.
'secret'
>>> api.name  # not what I want
<Mock name='important-thing-here.name' id='4337316944'>
```

Luckily, there's this neat class called a
[PropertyMock](http://www.voidspace.org.uk/python/mock/mock.html#mock.PropertyMock). It took me a bit to figure out how to use it, but it's
essentially used as a property or an attribute on another class (including
another mock). I honestly don't know if this is *supposed to work this
way* or if this is a nasty hack (feel free to [let me
know](/contact/) one way or another), but this is how I attached a `name`
attribute to a Mock object:



```
>>> from mock import Mock, PropertyMock
>>> # Create a Mock for my ``SomeAPIWrapper`` class above
>>> api = Mock(token='secret')
>>> # Create a PropertyMock representing the ``name`` attribute
>>> p = PropertyMock(return_value='brad')
>>> # Replace Mock's name with our new property
>>> type(api).name = p
>>>
>>> # Now see what happens
>>> api.token
'secret'
>>> api.name
'brad'
```

Now, your Mock objects can have a name attribute with an expected return
value.



