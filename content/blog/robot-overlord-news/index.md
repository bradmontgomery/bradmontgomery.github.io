---
date: '2026-06-15 01:44:04.277411+00:00'
title: Robot Overlord News
draft: false
tags:
- ai
- programming
- web
- tools
slug: robot-overlord-news
description: 'I built an AI news aggregator that uses AI to aggregate some news.'
markup: md
url: /blog/robot-overlord-news/
aliases:
- /blog/2026/06/15/robot-overlord-news/

---

Say hello to <a href="https://robot-overlord.news/" id="robot-overlord-news">robot-overlord.news</a>.


This is a new project I launched this weekend... and by _project_ I mean really simple experiment. The basic premise is easy:

1. Can an AI agent search for news/articles/content for me.
2. Can it save, summarize, and categorize those articles.
3. Can I have a place to skim and/or read them quickly.


The answer -- of course -- is Yes.


## The Agent

None of this is open source or available (yet), but the agent is intentionally simple. It's
[Python + LangGraph](https://reference.langchain.com/python/langgraph) that implements a ReAct-style loop. I'm
only using simple langgraph primitives for this one: StateGraph + MessagesState + ToolNode + hand-written conditional routing.

    Graph:
    START → agent → [should_continue] → tools → agent (loop)
                        ↓ (no tool_calls)
                       END


The basic idea is this:

1. The agent fires up and starts searching the web using the `langchain_community.tools.DuckDuckGoSearchResults` tools.
2. It has a list of topics it should search
3. It then summarizes &amp; categorizes any results &amp; stores those in a Sqlite database.
3. It ends if it can't find any results.

All of that runs in a python loop that just sleeps and repeats every hour or so.

For the moment, this is running locally on my PC using Ollama &amp; Qwen2.5:7b.


## The website

The website -- I'm still surprised I was able to snag *robot-overlord.news* -- is a simple Golang app that I vibe-coded in less than 10 minutes using Claude Code (Sonnet 4.6 with an Opus 4.8 advisor). I didn't save the original prompt, but it was pretty much a one-shot.

I think I made two minor tweaks to the UI.

The next several prompts were to get a working `cloudformation.yaml` + `nginx.conf` and a service file to run the binary.  By the way, being able to bundle all your templates + css + code logic into a go binary is freaking amazing. It's so simple, all this runs on a t3.micro EC2 instance.

I'm sure there will be updates in the future, but for now, this is it. Just a simple aggregation of AI-related news.

## The takeaway

All together this entire project took me less than 4 hours.

* The LangGraph agent was a random idea that I vibe-coded (and actually read all the python) in about 1.5 hours. I spent more time looking at the results it spit out than I spent looking at the code.
* The website literally took 5 minutes.
* It took a little longer to get it deployed, but building it & deploying it to AWS took less than an hour.
* I spent more time brainstorming on a domain name.
* I literally spent the most amount of time just thinking up the idea.

And isn't that last bullet the point? Isn't this what we've been searching for all along in computing? We now have a way to dream up ideas and accelerate the execution.

It may be a dumb idea at the end of the day, but who cares. I got to experiment &amp; had a little fun along the way.
