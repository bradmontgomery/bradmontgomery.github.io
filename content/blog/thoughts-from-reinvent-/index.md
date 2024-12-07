---
date: '2024-12-07 21:06:59.241301+00:00'
title: Thoughts from re:Invent 2024
draft: false
tags:
- aws
- developer
- technology
- industry
slug: thoughts-from-reinvent-
description: 'Generative AI, Bedrock, and easy (easier) data lakes.'
markup: md
url: /blog/thoughts-from-reinvent-2024/
aliases:
- /blog/2024/06/07/thoughts-from-reinvent-2024/

---

I've just gotten home from a week at AWS re:Invent. There were so many new product announcements,
but the overarching theme of the conference was (surprising to no-body) Generative AI.

It was pretty eye-opening to hear stories from across a number of industries about how other
companyies have already started integrating Generative AI into their processes and workflows &mdash;
_although_ the most common story told was:

* Amazon Q for for developers.
* Amazon Q to do big project upgrades (e.g. Java code)
* Amazon Q to help write test cases.

None of these are surprising, really.

And while I feel like I could absolutely see this coming, I've also realized that _my own_ journey into
the world of Genative AI is lagging. But I have _some idead_! (watch this space)

Personally, the exciting take-aways for me are:

* Amazon Q &amp; Bedrock are really powerful tools. I want to build something with Bedrock and see how
  this all works in practice.
* S3 Table buckets and S3 Metadata buckets are going to save a lot of people a lot of work &mdash; Table Buckets
  provide native support for Apache Iceberg and handle all the maintenance behind the scences and Metadata buckets
  give you a reliable place to store metadata so S3 is now (if it wasn't already) the best way to build out a Data
  Lake, Lakhouse, wharehouse whatever you want to call it.
* I'd somehow missed the memo that AWS was building [their own silicon](https://aws.amazon.com/silicon-innovation/)
  cloud computing workloads. The [AWS Trainium](https://aws.amazon.com/ai/machine-learning/trainium/) announcments
  just make me realized that's easier than ever to build & train ML models at scale.


This was my first time at re:Invent, so I have a ton of thoughts to process, but these are the (technology) highlights.
