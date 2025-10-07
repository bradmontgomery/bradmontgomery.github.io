---
date: '2025-10-07 17:54:12.925729+00:00'
title: What is this LangChain Syntax?
draft: false
tags:
- python
slug: what-is-this-langchain-syntax
description: 'Exploring how LangChain overloaded the | pipe operator.'
markup: md
url: /blog/what-is-this-langchain-syntax/
aliases:
- /blog/2025/54/07/what-is-this-langchain-syntax/

---

## What's this got to do with LangChain?

Honestly... not much.

I've been experimenting with [LangChain](https://python.langchain.com/docs/introduction/) lately, and 
I really like something they did with their [LCEL - LangChain Expression Language](https://python.langchain.com/docs/concepts/lcel/).

They [overloaded the `|` operator](https://python.langchain.com/docs/concepts/lcel/#the--operator) in python. This
let's them write code that _chains_ runnables together; It looks something like:

```python

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model

model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
chain = prompt | model | StrOutputParser()  # <---- Chain these runnables together!
```

Or for a [more advanced example from their docs](https://python.langchain.com/docs/how_to/sequence/):

```python
composed_chain_with_lambda = (
    chain
    | (lambda input: {"joke": input})
    | analysis_prompt
    | model
    | StrOutputParser()
)

composed_chain_with_lambda.invoke({"topic": "beets"})
```


## What is the `|` operator anyway?

In python, this is the [bitwise OR operator](https://docs.python.org/3/reference/expressions.html#binary-bitwise-operations).

For example, if you just execute this code in the python REPL, you'll get the following.

```python
>>> 0 | 0
0

>>> 1 | 0
1

>>> 1 | 1
1
```

## Operator Overloading

In my opinion, this is just a neat example of polymorphism in Python. You can overload these operators to your heart's desire!

Here's a simple example: Let's make the `|` operator perform concatenation for a string.


```python
class MagicString:
    _data = ""

    def __init__(self, data):
        self._data = data
    
    def __str__(self):
        """Coerce this to a str data type."""
        return str(self._data)

    def __or__(self, other):
        return str(self) + str(other) 
```

This gives us a `MagicString` class that knows how to coerce itself to a plain old string and apply the `|` operator to do concatenation.

See it in action:

```python

>>> a = MagicString("hello")
>>> b = MagicString("world")
>>> a | b
helloworld
```

It even works if the right-hand side operand is a plain old string.

```python
>>> a = MagicString("hello")
>>> b = " world"
>>> a | b
hello world
```

Operator Overloading is cool 😎