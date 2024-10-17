---
date: '2013-09-12T04:24:13.304178+00:00'
title: An Attribute by any other name...
draft: false
tags:
- __gettattr__
- attributes
- descriptors
- programming
- properties
- python
slug: attribute-any-other-name
description: ''
markup: md
url: /blog/attribute-any-other-name/
aliases:
- /blog/2013/09/12/attribute-any-other-name/

---

Let's explore some python attributes, shall we? (note: this is python 2.7.x)


Attributes
----------


Let's consider a simple class, `N`, with a single attribute,
`numbers` containing values 0 - 9.



```
class N(object):
    numbers = range(10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

We can create an instance of this class, then perform some operations on
the attribute (like accessing or setting its values).



```
>>> n = N()

>>> n.numbers  # get the value of the attribute
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> n.numbers = range(10, 20)  # Change the value of the attribute
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

```

Simple enough, right? This is usually what you expect with attributes on
a python class. Just for the sake of completeness, let's look at another way
to create an attribute on a class:



```
class N(object):
    def __init__(self, *args, **kwargs):
        self.numbers = range(10)
```

This is analagous to our first example. The `__init__` method is
called when we instantiate (or create an object from) the `N`
class. We can still access and change the `numbers` attribute.


In either case, you can list the attributes of the `n` object,
and you should see a list containing `'numbers'`:



```
>>> dir(n)
['__class__', '__delattr__', '__dict__', ..., 'numbers']
```

Properties
----------


In the examples above, the `numbers` attribute is simply a
variable referencing some value. Python also allows you to create a
*property* ([one of python's built-in
functions](http://goo.gl/iP3o6)). It's essentially a method that behaves as if it were an
attribute. Think of it as an attribute who's value is *calculated* every
time it's accessed.


What if we wanted an `even_numbers` attribute?



```
class N(object):
    numbers = range(10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    @property
    def even_numbers(self):
        return [num for num in self.numbers if num % 2 == 0]
```

The `@property` decorator converts our `even_numbers`
method into a property. We can now access it like so:



```
>>> n = N()
>>> n.numbers  # get the value of the attribute
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> n.even_numbers
[0, 2, 4, 6, 8]

```

Pretty cool! But what happens when we try to set the value of
`even_numbers`?



```
>>> n.even_numbers = range(10, 20)
---------------------------------------------------------------------------
Traceback (most recent call last)
----> 1 n.even_numbers = range(10, 20)

AttributeError: can't set attribute

```

We've got to define a property's `setter` if we want to do this.



```
class N(object):
    numbers = range(10)

    @property
    def even_numbers(self):
        return [num for num in self.numbers if num % 2 == 0]

    @even_numbers.setter
    def even_numbers(self, values):
        # Just assign the input values to the ``numbers`` attribute.
        # You *could* do something more interesting here if you wanted.
        self.numbers = values

```

We can now set the value of our `even_numbers` property.



```
>>> n.even_numbers = range(10, 20)

>>> n.even_numbers
[10, 12, 14, 16, 18]

>>> n.numbers
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
```

You can read more about properties at Official Python Doc's section on
[built-in functions](http://docs.python.org/2/library/functions.html#property).


\_\_getattr\_\_
---------------


Python has a number of *magic methods* (aka *dunder methods*), and
`__getattr__` is one that defines the behavior of accessing
*non-existing* attributes.


Yes, you can access attributes that *don't exist*!


If you're interested in more about python's magic methods, see the excellent
[A Guide to
Python's Magic Methods](http://www.rafekettler.com/magicmethods.html#access).


Let's implement an `odd_numbers` attribute using
`__getattr__`. (This is probably a bad idea, but it illustrates the
point).


Add the following method to our `N` class:



```
    def __getattr__(self, name):
        if name == "odd_numbers":
            return [num for num in self.numbers if num % 2 != 0]
```

Let's try it out:



```
>>> n = N()

>>> n.numbers
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> n.even_numbers
[0, 2, 4, 6, 8]

>>> n.odd_numbers
[1, 3, 5, 7, 9]
```

Pretty cool! However, there are a couple of caveats.



```
>>> dir(n)
['__class__', '__delattr__', ..., 'even_numbers', 'numbers']
```

Notice anything missing? That's right. There's no `'odd_numbers'`
attribute available. So much for *self-documenting code*!


What about this?



```
>>> n.whoopsies

>>> type(n.whoopsies)
NoneType

```

Aren't we supposed to get an `AttributeError` if we access
an attribute that doesn't exist!? Yes. We are.


Be careful implementing your own `__getattr__` method. Make sure
it does what you want, but be sure to raise an appropriate exception if you
don't want non-existing attributes to silently return `None`.


Here's an example:



```
    def __getattr__(self, name):
        if name == "odd_numbers":
            return [num for num in self.numbers if num % 2 != 0]

        # Raise an AttributeError, for all other attribute names.
        raise AttributeError("'N' object has no attribute '{0}'".format(name))
```

So, now we'd get:



```
>>> n.whoopsies
---------------------------------------------------------------------------
Traceback (most recent call last)
AttributeError: 'N' object has no attribute 'asdf'
```

Now, you might also be thinking, "how would I assign a value to `odd_numbers`?"
Well, there *is* a `__setattr__` method, but be careful!
**Here be dragons**!


Unless you already know what you're doing and you have a good reason, it's
probably not a good idea to start changing the behavior of `__setattr__`.


If you really need to customize the behavior of assignment, you probably want
to use a *descriptor*.


Descriptors
-----------


A descriptor is a class that defines behavior for getting and setting an
attribute.


Let's keep building on our `N` class. What if we only wanted to
access numbers that were primes? What if we wanted to be able to easily
store prime numbers in the `numbers` attribute?


First of all, lets write a little function to determine if a number is prime.
This is not the most efficient way to do it, but it's simple and concise:



```
def is_prime(number):
    """Determine if a number is prime. Shamelessly adapted from:
    http://stackoverflow.com/a/4117879/182778

    Returns True or False
    """
    return number > 1 and all(number % i for i in xrange(2, number))
```

Now, create a class called `PrimeNumbers`. An instance of this
class will eventually be attached to our `N` class.
We add a `__get__` method that defines the behavior we want when
we access a value, and we define a `__set__` method that defines
the behavior we want when we set a value.



```
class PrimeNumbers(object):
    """This class implements a descriptor (ie. a property or attribute) that
    will only store Prime Numbers. The class on which it is attached must have
    a ``numbers`` attribute."""

    def filter_primes(self, numbers):
        """Use the ``is_prime`` function to pluck only primes from a list of
        numbers."""
        return filter(is_prime, numbers)

    def __get__(self, instance, owner):
        """Get only the prime numbers from the ``numbers`` attribute on the
        ``instance`` object (an N object).

        Note:
            * ``instance`` will be an instance of our N class.
            * ``owner`` will be a reference to the N class (not an instance
              of it)

        """
        return self.filter_primes(instance.numbers)

    def __set__(self, instance, values):
        """Set the value of ``instance.numbers``, but *only* store primes.
        ``values`` is just a list of numbers.
        """
        instance.numbers = self.filter_primes(values)
```

Now, we need to update our `N` class so it contains a
`prime_numbers` attribute:



```
class N(object):
    numbers = range(10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    prime_numbers = PrimeNumbers()

    # ... 
```

Now, lets play around with this.



```
>>> n = N()

>>> n.numbers
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> n.prime_numbers
[2, 3, 5, 7]
```

Great! Our `PrimeNumbers.__get__` method removes all non-prime
numbers from the list. Let's try setting some values:



```
>>> n.prime_numbers = range(0,30)

>>> n.prime_numbers
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

>>> n.numbers
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

Interesting! Our `PrimeNumbers.__set__` also removes all non-prime
numbers before storing the result in `n.numbers`!


Note that our `even_numbers` method still works as expected:



```
>>> n.even_numbers
[2]
```

Descriptors are powerful, and give you the tools to build re-usable properties
for your classes. For even more on Descriptors, see the
[Descriptor HowTo Guide](http://docs.python.org/2/howto/descriptor.html)
and the excellent [Python Descriptors Demystified](http://nbviewer.ipython.org/urls/gist.github.com/ChrisBeaumont/5758381/raw/descriptor_writeup.ipynb).


Wrapping Up
-----------


Well, that's it for now. I hope you've enjoyed this short tour of python
*attributes*. If you want to see all the code at once, you can grab the
full example from <https://gist.github.com/bradmontgomery/6432860>.


Thanks for reading!

