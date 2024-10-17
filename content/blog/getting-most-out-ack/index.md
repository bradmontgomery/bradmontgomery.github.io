---
date: '2013-10-12T04:29:57.421012+00:00'
title: Getting the Most out of ack
draft: false
tags:
- ack
- grep
- tools
slug: getting-most-out-ack
description: ''
markup: md
url: /blog/getting-most-out-ack/
aliases:
- /blog/2013/10/12/getting-most-out-ack/

---

`ack` is an amazing tool. If you're not familiar with it,
it's a lot like grep (the official site is at [beyondgrep.com](http://beyondgrep.com/)).
It's a command-line tool that helps you find things in files, particularly source code.
However, like a lot of command-line tools, it's all-too-easy to learn just the
basics and forget that many of these tools can do so much more!


Without further ado, here are a few of the ways I frequently use `ack` while working with Django.


Ignoring folders
----------------


It's so frustrating to search for a snippet of python code, only to have your
screen fill up with irrelevant results (I'm looking at you migrations and css files!)


When this happens, just ignore the stuff you don't need:



```
ack --ignore-dir=myapp/migrations
```

Ingoring files
--------------


While we're at it, you can also ignore specific files, or any file that matches
a regex. Perhaps you're looking for reference to a Django model, but you don't need
to know that it's in models.py, so just ignore that file!



```
ack --ignore-file=match:models.py SomeModel
```

Better, but you might also want to ignore that model.js file (or perhaps it's
called model\_views.js). You can do that with a simple regex! And while we're at it,
lets go ahead and ignore any migrations:



```
ack --ignore-file=match:/^model/ --ignore-dir=migrations/ SomeModel
```

Just Python, please
-------------------


`ack` also lets you restrict searches to specific file types:



```
ack --type=python SomeModel
```

There's also a shortcut for this:



```
ack --python SomeModel
```

Or ruby if you prefer:



```
ack --ruby 'def foo'
```

Similarly, you can tell ack to ignore any files that it doesn't understand with
the `-k` or `--known-types` flag.



```
ack -k SomeCode
```

To get a list of all the filetypes that `ack` knows about, just run:



```
ack --help-types
```

Be insensitive!
---------------


For some reason, I sometimes forget that default searches are case sensitive.
If, like me, you're pronE tO TYpos, you can perform case insensitive searches with:



```
ack -i whatever
```

Digging deeper
--------------


As you might have noticed, `ack` comes with some default behavior.
You can inspect these defaults with:



```
ack --dump
```

Now, if you want to start customizing this behavior, create an `.ackrc` file,
and tweak it to your heart's content. A good way to get started is to let ack generate
this file for you! (**careful!** this command will overwrite your
`.ackrc` file if you already have one.)



```
ack --create-ackrc > ~/.ackrc
```

Have some fun
-------------


The `ack` developers are not without a sense of humor. Certainly
you should take the time to investigate all of the following:



```
ack --bar
ack --cathy
ack --thpppt
```

Wrapping Up
-----------


There's *so much more* to `ack` than what I've listed here.
Do yourself a favor and periodically skim the output of `ack --help`,
then take some time to look through the manpage (`man ack`).


Happing searching!

