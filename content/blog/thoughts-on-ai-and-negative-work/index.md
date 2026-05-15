---
date: '2026-05-16 00:00:00+00:00'
title: Thoughts on AI and Negative Work
draft: true
tags:
- ai
- programming
slug: thoughts-on-ai-and-negative-work
description: "Thoughts on software development with AI, and the concept of Negative Work."
markup: md
url: /blog/thoughts-on-ai-and-negative-work/
aliases:
- /blog/2026/05/16/thoughts-on-ai-and-negative-work/

---

There's a lot happening in the software industry right now, and honestly it's hard to know what to make of it. Companies are laying off engineers. Middle management is getting hollowed out. People who've never written a line of production code in their careers are being handed development responsibilities — because, hey, AI can do the hard parts, right?

It's exciting. It's confusing. And it's making me think about some old ideas that feel suddenly very relevant again.

## The 10x Developer and the Developer Who Does Negative Work

You've probably heard of the "10x developer" — the mythical programmer who produces ten times the output of their peers. The concept traces back to research by Tom DeMarco and Tim Lister, who ran [Coding War Games](https://medium.com/ingeniouslysimple/the-origins-of-the-10x-developer-2e0177ecef60) starting in 1977. They found enormous productivity differences between organizations, but here's the thing: they attributed that variance to *work environment*, not to individual talent. Quiet offices beat open-plan chaos (you know... where EVERYBODY in the industry is forced to work).

But buried in that same body of research is a concept that doesn't get nearly as much airtime: the **Net Negative Producing Programmer** (NNPP). G. Gordon Schulmeyer coined the term to describe a developer whose output — through excessive bugs, unnecessary complexity, or just plain bad code — is so costly to clean up that the team would actually be *more* productive without them. Removing them increases throughput. That's a harsh framing, but it points at something real: not all code contribution is positive contribution.

The Stack Overflow blog has a pretty good piece (from 2020) on [measuring developer productivity](https://stackoverflow.blog/2020/12/07/measuring-developer-productivity/) that extends this idea with the concept of **negative work**. Developers who are exhausted, distracted, or just grinding through the motions don't just slow down — they produce code that *increases* the total amount of work remaining. It has to be found, understood, and fixed before anything can move forward. The effort to undo it costs more than if nothing had been written at all.

The piece also surfaces a warning that's worth keeping in mind any time someone proposes a new productivity metric:

> When a measure becomes a target, it ceases to be a good measure.
> — Goodhart's Law

Lines of code, commits per week, tickets closed — pick your favorite. The moment you optimize for it, you stop measuring what you actually cared about. Which is going to be a recurring theme as companies try to figure out how to evaluate developer productivity in an AI-assisted world.

## So What Does This Have to Do with AI?

Here's my concern: I think we're about to see a wave of Net Negative Producing Programmers, and a lot of them are going to be wielding AI tools.

LinkedIn has been buzzing with takes about how the future of software development belongs to good engineers who will clean up the messes left behind by "vibe-coded" solutions — the kind of software that looks functional on a demo screen but is quietly a maintenance nightmare underneath. I think those takes are largely right. I also think the more interesting question is: *why* does that keep happening, and will AI make it better or worse?


Surely this has nothing to do with token usage as a metric. Ahem — [**Tokenmaxxing**](https://leaddev.com/ai/tokenmaxxing-and-the-search-for-ai-metrics-that-matter) is a thing now. (Yes, Jensen Huang has reportedly said he'd be "deeply alarmed" if a $500K engineer wasn't burning at least $250K in tokens. Goodhart would like a word.)

The AI optimist case is that LLMs level the playing field. Anyone can now produce working code. The AI pessimist case is that NNPPs used to be limited by their own ability to write bad code — AI removes that constraint. Now anyone can produce *a lot* of bad code, very quickly, with a high degree of confidence that it sort of works until it definitely doesn't.

I've already seen this happen. Both with small groups of people working on greenfield projects, and in larger groups trying to build software and tools _for the enterprise_. I hope we're learning from it.

## But Wait — Does Any of This Matter Anymore?

Here's the counterargument, and I think it's worth taking seriously: **maybe negative work isn't really a problem if code is cheap enough to throw away.**

Chad Fowler has been writing a series called [The Phoenix Architecture](https://aicoding.leaflet.pub/) that makes exactly this case. The foundational argument is that code generation has been commoditized — writing code stopped being the hard part (_I'd argue that writing code was never the hard part, but that's another post_). What that means in practice is that software should be designed to be *disposable*. Components should pass what Fowler calls the Deletion Test: if you can't safely remove a piece of your system, your architecture isn't suited to the AI era. The goal isn't long-lived code. It's safe-to-delete code.

One of the most clarifying reframes in the series is this: *"Code Was Never the Asset."* Customers don't pay for your implementation. They pay for outcomes. The real codebase, in this view, is your evaluations — the specifications and behaviors that define what the system is supposed to do. Those outlive any particular implementation. A working, well-specified system that you regenerate every year is better than a legacy monolith that nobody dares touch.

If Chad Fowler is right — and I think he's largely right — then the concept of negative work has to evolve. Bad code doesn't matter as much if it's safe to delete and regenerate. The NNPP who writes a thousand lines of spaghetti Python is less dangerous if that code can be cleanly replaced next quarter.

*But.* (There's always a but.)

The premise only holds if the rest of your system is actually designed for disposability. Most software in production today is not. And even in systems built for it, the *specifications* — the clarity about what the system should actually do — don't get cheaper just because code generation does. If anything, they get more important. Garbage in, garbage out, but now at scale and velocity.

So the NNPP concept doesn't disappear in the Phoenix Architecture world. It mutates. The net negative producer isn't the one who writes bad code anymore. It's the one who generates bad *outcomes* — who ships systems that don't serve customers, who moves fast because the tools let them and never slows down to ask whether the thing they built was the right thing to build.

## What Martin Fowler Is Thinking About

Martin Fowler recently published [some fragments](https://martinfowler.com/fragments/2026-02-13.html) that I think are worth chewing on here.

On junior developers: the expectation is that they should thrive with LLMs — they're open-minded about the tools and grew up using them. An LLM can serve as an always-available mentor. That's genuinely exciting. But Fowler's caveat is important: juniors still need healthy skepticism of AI guidance. An LLM will confidently teach you the wrong thing if you don't already know enough to push back. That's a tough spot to be in when you're just starting out.

On senior developers: interestingly, many initially resisted LLMs but changed their tune fast after actually using them. A third of them, in Martin Fowler's telling, were "instantly converted." (me included... sort-of, if instantly means 6 months of active usage). Senior devs seem to be gravitating toward using AI to get back to hands-on work — less context-switching into architecture reviews and more time actually building.

On **cognitive debt**: this is where it gets interesting. Fowler references Margaret-Anne Storey's concept, which parallels technical debt but focuses on *shared understanding* rather than code quality. The "cruft" in cognitive debt isn't messy functions — it's lost knowledge about what the system does and why. When you bring AI into a codebase as a generator of code that nobody fully understands, you're not just accumulating technical debt. You're accumulating cognitive debt at an alarming rate. Future maintainers — human or AI — will inherit a system that works until it doesn't, and nobody will know why.

I'm already feeling this too. In my day job and in some of my personal projects, and I know I am not alone.

## The Part Nobody Warned Us About

But the thing that's been rattling around in my head most is this quote from Camille Fournier, which Fowler highlights:

> "The part of 'everyone becomes a manager' in AI that I didn't really think about until now was the mental fatigue of context switching and keeping many tasks going at once, which of course is one of the hardest parts of being a manager and now you all get to enjoy it too"

Yes. *That.*

When you're working with AI tools at any real scale, you're no longer just writing code. You're supervising multiple threads of work, reviewing output, deciding what to keep and what to throw away, maintaining context across several parallel tasks. That is management work. It's cognitively exhausting in exactly the way that management is exhausting, and most developers didn't sign up for it — and haven't been trained for it.

The people who will thrive in this environment aren't just good coders. They're good at managing cognitive load, maintaining context, and knowing when to slow down and actually *understand* what's been generated rather than just shipping it.

## Where Does This Leave Us?

I don't think AI tools are going anywhere, nor do I want them to. I use them. They're useful. But I do think the industry is a bit too optimistic about the net outcome of putting powerful code-generation tools in the hands of everyone, regardless of their understanding of what good software looks like.

The Phoenix Architecture framing is genuinely useful — orienting around outcomes rather than implementations is the right direction. Code being cheap and disposable is a feature, not a bug. But "code is cheap" doesn't mean *understanding is cheap*. It doesn't mean *clarity about what you're building is cheap*. It doesn't mean the cognitive debt of a system that nobody fully comprehends just evaporates because you can regenerate the implementation.

The NNPP concept has always been uncomfortable because it implies some contributions are worse than nothing. In an AI-assisted world, that doesn't go away — it just shifts. The question stops being "did you write good code?" and becomes "did you produce good outcomes?" And the cognitive debt that accumulates when nobody can answer that question is going to be an interesting mess to untangle.

I don't know how this plays out. But I know the people who'll do well are the ones who still own the critical thinking.

Code was never the asset. It was just the embodiment of that thinking — and sometimes we got it wrong, which is why we had to rewrite and refine and (yes, *yes*) now get a little help from AI to collaborate more quickly.

*…wink, nudge. The footer's right there.*

---

*This post was written in collaboration with [Claude Sonnet 4.6](https://www.anthropic.com/claude) and [Claude Opus 4.7](https://www.anthropic.com/claude), AI models by Anthropic.*
