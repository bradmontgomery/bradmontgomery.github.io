---
date: '2026-05-08 15:38:11.872360+00:00'
title: My AI Journey (for now)
draft: false
tags:
- ai
- programming
- personal
slug: my-ai-journey-for-now
description: "I'm on the AI bandwagon. Here's how I got there."
markup: md
url: /blog/my-ai-journey-for-now/
aliases:
- /blog/2026/05/08/my-ai-journey-for-now/

---


It was re:Invent 2024 where it really hit me. AI &mdash; particularly LLMs &mdash; were coming, and in a big way (btw,
yes, I'm using the em-dash. Don't hate on it, it has a purpose. Long live the em-dash). Anyway, I'm on the AI bandwagon,
and this is how I got here.

## let's back up a bit

Ok, I was skeptical for a long time. I signed up for ChatGPT in 2022, and at the time I really struggled to think
about how to use these tools for _work_ (writing code in particular). I did some experiments, and had models
write snippets of Python, and was impressed — but try as I might, I couldn't see how to roll that into a workflow.

You see, I was already proficient. I didn't see LLMs as an accelerant for my dev work. Quite the opposite actually. I
didn't like some of the decisions it made (fwiw, I still don't but that's another matter).

I thought [ChatGPT was a toy](https://bradmontgomery.net/blog/chatgpt-choosing-javascript-framework/), and that's how
I treated it. Much like [I would treat the output of a Markov chain](https://github.com/bradmontgomery/shaney).


## But the image models were surprising

I will admit however, that the [image models](https://bradmontgomery.net/blog/we-are-all-inventors/) were something
fascinating. I played with them. I kept coming back to them. I knew something magical was happening.

We've been hearing & seeing deepfakes on the internet for some time, and I think collectively all of us in tech knew
this was coming. So, looking back it's hilarious to me that I understood that AI models could generate audio, video, and
images that would fool us, but I was dense to realize that it would be able to generate _really good_ text, and even
code.

## So I experimented

In early 2025 I got access to Amazon Q for developers (quickly renamed to Kiro). That's really where I started to see
what's possible. Now, my _primary professional role_ is no longer that of a heads-down, hands-on-keyboard all day
developer. So most of what I created was proof of concept code, rough ideas for how to implement something, examples
on how to fix security findings, etc.

One of the breakthrough moments for me was a prompt like the following (using kiro, and probably Claude Sonnet):

> Use the aws cli tool to connect to my aws account using the environment variables set in my terminal. Map out what's
> configured in this account, and create a Markdown file describing the account. Use Mermaidjs to create a diagram
> of AWS services that are configured.

And it worked. It worked really really well.  This just instantly solved a problem that I was facing on a day-to-day
basis.

We started investigating how to build AI-powered applications. I learned about LangChain and all their related tools. I
learned about Amazon Bedrock. I learned about Guardrails, Agents, and context limitations.

## Then I dove in head-first.

What happened next (over the course of a year and a half) was a whirlwind of learning, experimenting, using, failing,
learning, and repeating. This is going to be really abbreviated, but hopefully you get the idea.

1. I paid for github copilot, and set up the copilot-cli tool.
1. I dove into projects that I've published (and some that I haven't), and brought almost everything up to date. Updated
   project directories, everything using pyproject.toml and uv. Modern packages. More tests. If you look at my github
   profile you'll see a flurry of activity in late 2025.
1. I stopped looking at code outside of `git diff`. Everything's just an AI agent on the CLI.
1. I ditched copilot-cli and started using Claude Code — but still with models served by GitHub.
1. I started exploring local models via Ollama & Hugging Face.
1. I finally closed my Flickr account and downloaded all my images. I have a very crude Flickr clone running on my PC. I did not write a line of code for this.
1. I built a little Strava clone (more data visualization, zero socials -- it's still a private repo, but maybe not forever)
1. I continued.
1. I worked with and advised a team of CodeCrew graduates during a project with [Uncomplicated Inc](https://uncomplicatedinc.com/). Everything was AI-driven. We made mistakes, we learned. We continued.
1. I signed up for Claude Code, and started doing all of this again.
1. In my day-job, I got access to Claude Code. I'm mapping out bigger projects. I'm building skills for code review, project analysis, security reviews.
1. I'm talking to people. Lots of people. I'm asking questions. I'm reading. I'm watching YouTube.
1. I help teach a pilot class for Tech901 that lead to Azure AI-900 and AI-102; Microsofts AI Fundamentals and AI Engineering certifications.
1. I learned how to use Azure Foundry.
1. Repeat repeat repeat.

## What I've learned

The tools are really good. The models are really good. This *really is* an evolution of _how_ we build software.

But these are all still tools. They have limitations. There's a skillset that accompanies these tools -- yes, prompt
engineering is still a thing. Writing Skills is still a thing. Knowing when and why you might use an MCP server is
a thing. Managing context, and knowing why that's important is a thing.

But also, everything else we know about building software is still relevant.

I've seen people really struggle to build software by prompting AI, because they didn't know how to build software
already — just watch LinkedIn to see people telling stories about this. There's a VAST well of knowledge beyond code,
syntax, and programming languages that goes into building software. ALL of that is more important than ever.


## What I fear

I lived through the first dot-com crash. Shortly after, there was a prevalent sense that software engineering in the US
was dead — that outsourcing software development would be the way of the future. This had a decades-long impact of driving
people away from Computer Science. We saw what happened — the premise was wrong, there was a rush to hire, and there just
weren't enough people to fill the needs. I'm a little afraid that we'll repeat this mistake.

Some people think AI is going to remove the need to study computer science, software engineering, or programming. I don't think it's true.

I think this is a false premise. Yes, _writing the code_ itself might be de-prioritized, but there's still EVERYTHING ELSE
that's involved. And that's a lot.

None of us know what the future holds. I'm excited about the new tools we have, I'm excited about the ability to create
software more quickly. But all the problems that caused software delivery to be difficult are still there.

We still need smart people to work on this stuff.

---

*This article was proofread and edited by Claude (Anthropic).*
