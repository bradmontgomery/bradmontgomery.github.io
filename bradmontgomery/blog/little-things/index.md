---
date: '2013-12-29T18:50:15.583798+00:00'
title: The little things
draft: false
tags:
- generators
- lambda
- map
- python
slug: little-things
description: ''
markup: md
url: /blog/little-things/
aliases:
- /blog/2013/12/29/little-things/

---

I ran across an interesting line of code today, and thought I'd share some
insights. First, though we need a little context. Imagine reading several lines
of data from a csv file (using
[python's built-in
`csv` module](http://docs.python.org/2/library/csv.html)). You'll typically have some code that looks
something like this:



```
import csv
with open('data.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # Do some stuff with each row,
        # where the row is a list of strings.
```

So, that's what we've got, and within the `for` loop, I found
this code:



```
row = map(lambda x: x.strip(), row)
```

What does it do? It simply strips whitespace from the beginng and ending of
each item in our list of strings. But *how* it accomplishes this is worth
picking apart.


First, this code uses `map` to apply a function to each item in
the list. Then, we construct an anonymous `lambda` function which
accepts a parameter, calls the input's `strip` method and returns
the result.


Essentially, we call a function for each item in the list. Keep in mind,
we're also doing this inside a `for` loop. That's a function call
for each cell in your CSV file.


We can also achieve the same outcome with a list comprehension:



```
row = [x.strip() for x in row]
```

OR with a generator! (note the parenthesis instead of square brackets)



```
row = (x.strip() for x in row)
```

Measure it
----------


Out of curiosity, I decided to time this with just a few rows of data
(10, in particular). I used `timeit` to run this code on my
laptop (a late-2011 macbook air) with some simple data. Here's what I found:



```
>>> import timeit
>>> timeit.timeit(
...    stmt="map(lambda x: x.strip(), row)",
...    setup="row = [' {0} '.format(i) for i in range(10)]"
... )
2.491640090942383

```

With 1,000,000 rows of data (the default number of test iterations, and
an admittedly unlikely scenario for a one-off CSV import) this code runs in
about two and a half seconds.


Now lets see how the list comprehension and generator versions for the
same code stack up!



```
>>> timeit.timeit(
...    stmt="[x.strip() for x in row]",
...    setup="row = [' {0} '.format(i) for i in range(10)]"
... )
1.6442670822143555

```

Quite a bit better! *Nearly* a second faster. Let's see about
the generator:



```
>>> timeit.timeit(
...    stmt="(x.strip() for x in row)",
...    setup="row = [' {0} '.format(i) for i in range(10)]"
... )
0.48253297805786133

```

Yep. About two whole seconds faster than our original code.


So what's the take-away, here? Well,
[generator expressions](http://www.python.org/dev/peps/pep-0289/)
are pretty amazing. **Use them**.


Finally, small things add up. Little decisions, like whether to use
`map` + `lambda` or a generator expression can have
fairly significant impact on the performance of your software.

