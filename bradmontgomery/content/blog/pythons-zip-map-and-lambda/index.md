---
date: '2013-04-01T16:29:14.615885+00:00'
title: Python's zip, map, and lambda
draft: false
tags:
- lambda
- map
- python
- zip
slug: pythons-zip-map-and-lambda
description: ''
markup: md
url: /blog/pythons-zip-map-and-lambda/
aliases:
- /blog/2013/04/01/pythons-zip-map-and-lambda/

---

Many novice programmers (and even experienced programmers who are new to
python) often get confused when they first see `zip`, `map`, and
`lambda`. This post will provide a simple scenario that (hopefully) clarifies
how these tools can be used.


To start, assume that you've got two collections of values and you need to keep
the largest (or smallest) from each. These could be metrics from two different
systems, stock quotes from two different services, or just about anything. For
this example we'll just keep it generic.


So, assume you've got `a` and `b`: two lists of integers. The goal is to
merge these into one list, keeping whichever value is the largest at each
index.



```
>>> a = [1, 2, 3, 4, 5]
>>> b = [2, 2, 9, 0, 9]

```

This really isn't difficult to do procedurally. You *could* write a simple
function that compares each item from `a` and `b`, then stores the largest
in a new list. It might look something like this:



```
def pick_the_largest(a, b):
    result = []  # A list of the largest values

    # Assume both lists are the same length
    list_length = len(a)
    for i in range(list_length):
        result.append(max(a[i], b[i]))
    return result

```

While that's fairly straightforward and easy to read, there is a more concise,
more pythonic way to solve this problem.


zip
===


Lets first look at `zip`. This function takes two equal-length collections,
and merges them together in pairs. If we use this on our list of values, we
get the following:



```
>>> zip(a, b)
[
    (1, 2),
    (2, 2),
    (3, 9),
    (4, 0),
    (5, 9)
]

```

You now have one list, but it contains pairs of items from `a` and `b`.
For more information, check out
[zip in the python documentation](http://bit.ly/python-zip).


lambda
======


`lambda` is just a shorthand to create an anonymous function. It's often used
to create a *one-off* function (usually for scenarios when you need to pass
a function as a parameter into another function). It can take a parameter, and
it returns the value of an expression. For more information, see the Python
[documentation on lambdas](http://bit.ly/python-lambdas).



```
lambda <input>: <expression>

```

Now, assuming that you have a tuple (or a pair of values), you can create a
function that picks the larger of the pair:



```
lambda pair: max(pair)

```

map
===


`map` takes a function, and applies it to each item in an iterable (such as
a list). You can get a more complete definition of
[map from the python documentation](http://bit.ly/python-map), but it
essentially looks something like this:



```
map(some_function, some_iterable)

```

This is where our `lambda` expression comes in handy, and since `zip`
returns an iterable, we can write a solution for our original problem as a
concise one-liner (which I'll break over 3 lines to make it readable). Try
reading this code from the bottom-up.



```
>>> map(  # apply the lambda to each item in the zipped list
        lambda pair: max(pair),  # pick the larger of the pair
        zip(a, b)  # create a list of tuples
    )
[2, 2, 9, 4, 9]

```

So, putting it all together



```
>>> a = [1, 2, 3, 4, 5]
>>> b = [2, 2, 9, 0, 9]
>>> map(lambda pair: max(pair), zip(a, b))
[2, 2, 9, 4, 9]

```

Python's `map`, `lambda`, and `zip` are powerful and effective tools! I
hope this post has been informative. Thanks for reading :)

