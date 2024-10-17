---
date: '2020-05-17T23:28:36.891528+00:00'
title: Git workflow
draft: false
tags:
- git
- process
- workflow
slug: git-workflow
description: ''
markup: md
url: /blog/git-workflow/
aliases:
- /blog/2020/05/17/git-workflow/

---

It's 2020. People and teams are still using and adopting git. As new teams
are created, at some point, someone asks, "what's a good git workflow for us?"

Here's a workflow that has served me well over the past few years working in small
teams.

## Assumptions

1. You're using [git](https://git-scm.com/).
1. You have an authoritative git repo somewhere (e.g. github, bitbucket, gitlab, etc),
 and that repo is named `origin` (this is the default name of remotes in git).
1. `master` is golden; i.e. that's where the production code is deployed from,
 or the branch from which the release build happens.
1. You and everyone on your team can clone the repo.

## Starting some work


You're about to start some new work, i.e. a new feature, a bug fix, etc.


1. `git checkout master`: Make sure you're on the master branch.
1. `git pull origin master`: Make sure you have the latest version of the code
 on your system.
1. `git checkout -b WHATEVER`: Create a new branch for your work. I'm not a
 stickler for branch names, but it \*should\* be a unique name, otherwise you'll
 accidentally end up putting your commits in someone else's work.
1. Do the work.
1. `git push origin WHATEVER`: Push your work up to the repo.
1. At this point, use your shared repo's systems to create a Pull/Merge request
 or whatever it's called that lets others on your team compare your code
 with that in master. This allows you to get feedback early.

Continue this process every day until your feature is complete or your bug is
fixed. Typically, however, these branches are more-or-less ephemeral. They only
live for the duration of the feature or bugfix.

\*\*Pro-tip\*\*: If you get new commits when you pull from master, then [rebase](https://git-scm.com/book/en/v2/Git-Branching-Rebasing)
your commits onto master \*\*IF AND ONLY IF\*\* nobody has pulled your commits down
from your branch. THIS is important.

Rebasing is dangerous, but it makes all of your work look like it happend AFTER
the last commit in master: `git checkout WHATEVER`, then `git rebase master`.

Repeat.


## Merging work

At some point, you finish the bugfix or feature addition, and then you need to
get it adding into the project. You want to \*merge your commits into master\*.

1. Get your stuff code-reviewed. Have someone else on your team look over your
 stuff and get approval / or a `:thumbsup:`. There's a lot on the internet
 about code review, but I'm a big fan of doing it so someone else on the team
 knows what happens, and just to sanity check what's going on. Kudos if you
 did this several times during development.
1. Set up something in your online repo to run your tests for you. (you've got
 tests right?) Don't merge until the tests pass.
1. Once approved, use your online repo's tools to Merge the code. (if you've
 been rebasing every step of the way, this should almost always merge cleanly).
1. Delete the feature / bugfix branch. (Now is a good time to go learn about l
 [`git prune`](https://git-scm.com/docs/git-prune)).


## Gettin fancy with feature branches.

At some point, you may want to have some work that's not part of master, but
that you can build or deploy for people to use. This is a "feature branch",
and the workflow is exactly the same as above... except you merge into the
feature branch instead of master.

Ideally... you'll eventually merge this feature into master. Here are some
examples:

1. We use a `staging` branch for things we want to let people try out before
 it goes out to all customers.
1. You may use a `version2` branch for a big re-work of something, and you're
 not quite ready to merge that into the same branch as your production code.

Etc, etc.

Long-lived feature branches are fine, and the above workflow can work with them
quite well. Just communicate with your team about the feature branch.


## Conclusion

This is essentially a simple git workflow. Google "git workflow" for a hundred
variations on this, but this process has worked well for me.