---
date: '2016-02-09T00:31:00.530693+00:00'
title: Young Coders at PyTennessee 2016
draft: false
tags: []
slug: young-coders-pytennessee-2016
description: ''
markup: md
url: /blog/young-coders-pytennessee-2016/
aliases:
- /blog/2016/02/09/young-coders-pytennessee-2016/

---

On February 6, 2016 I had the pleasure of teaching the Young Coders class at
[PyTennesse](https://www.pytennessee.org). It was an incredibly fun and rewarding
experience, and I'm looking forward to doing this again at some point in the future.



## The class

We had ten young coders ranging in ages from 12 to 17, and spent
most of Saturday morning quickly plowing through examples of using python
as a calculator, exploring data types like integers, floats, strings, and
lists. We kicked things off around 8:30am and spent most of the day exploring, 
python in IDLE.

Nearly every one in the class has \_seen\_ python at some point--either from
an online learning service like Codecademy or from a class at school. This
was fairly surprising to me, and it was also encouraging. Every single attendee
in this class was excited and eager to learn more. So we quickly plowed through
the early informative content, and jumped into functions before lunch.

By lunchtime, we'd \_just\_ dug into the `turtle` module, and we spent several
minutes after lunch tweaking our drawings. Surprisingly, these students didn't
seem too interested in the venerable turtle, so we continued on.

At this point, we started what I think was the highlight of the class. A simple,
text-based guessing game, a la: \_What number am I thinking of\_. After helping
the students through a very simple first version, they quickly thought of
ways to improve it. As soon as we ran the code, I was hearing questions like:

- How can we make sure the \_secret number\_ is random?
- How can we keep guessing?
- Can we count how many attempts it takes to guess the right number?
- Can we make the game start over once you guess the right number?
- Cam we make the game restart only 3 times.

These iterations lasted for about an hour, and I think it's amazing how
rewarding it can be to create even the simplest of software, when you're
invested in the ideas behind it.

Once we wrapped up this game, we jumped into Al Sweigart's set of games from
[Invent with python](http://inventwithpython.com/pygame/). We looked at games that simply move an image around a screen,
and others that have more complicated gameplay (Wormy, then Squirrel Eat
Squirrel--a Katamari Damacy clone). For the most part, we changed simple
settings in these games (FPS, colors, health meters, movement speed, etc),
but after a an hour and a half, I could see the momentum fading, so we wrapped
up the "official work" at about 2:45pm.


## The gear

This year we did \_something different\_; rather than raspberry pi's for all of
the young coders, we decided to try out Chromebooks running Linux. Thanks to
the [magic of crouton](https://github.com/dnschneid/crouton), all of the students received an Asus 300M Chromebook
with instructions on how to boot into Ubuntu, and that's where we did our work.

If you're curious how these were configured, you can check out my guide in
the [young coders tutorial repo](https://github.com/bradmontgomery/young-coders-tutorial/blob/pytn2016/2016/chromebooks.md). As with anything, there are some pros & cons of using Chromebooks over the raspberry pi:

### Pros

- With a laptop, there's no need to mess with monitors, keyboards, and mice
- This group of kids seemed perfectly OK with the idea of multiple OSes; they
 figured out ChromeOS pretty quickly, and seems to easily grasp how to boot
 ubuntu.
- ChromeOS is pretty easy to use, and it's a nice OS by itself.
- Having your own laptop is an exciting thing!
- Chromebooks (~ $200) are more expensive than raspberry pis (~ $30), but as a conference organizer, 
 you may have to pay to rent monitors and provide keyboards & mice. In the long run, for PyTN, the price worked out to be about the same.

### Cons

In no particular order...

- You \_have\_ to enable developer mode to use crouton. This yields a scary
 error message every time you boot the machine. It also makes it really easy
 for the machine to wipe & re-initial the hard drive, meaning it's likely
 you'll lose some stuff (This actually happened to one student, but luckily
 I was able to re-create their linux image on Sunday during the conference)
- Students have to jump through a few hoops to get linux booted; it's possible
 they may forget how to do this by the time they get home.
- Minecraft may be off the table. Minecraft on the raspberry pi is a special
 thing. It's great for kids, and it's free... but only on raspberry pi. If
 you're running linux, you have to use the commercial version of Minecraft,
 and while \_a lot\_ of kids already have an account, it's likely not everyone
 will. So, for PyTN 2016, we skipped minecraft.


## Lessons Learned

While I think the session went really well at this years conference, I do think there's some 
room for improvement. Here are a few things I would do different next time:

- \*\*Hide Minecraft\*\*. I said we skipped minecraft. And we did. However, I installed
 the minecraft binary on the laptops, and it didn't take long for the kids to
 discover this. We had a hard time getting back on track after lunch because
 Minecraft had already stolen their attention.
- \*\*Turn off Wifi\*\*. It's handy if you can prevent the machines from connecting
 to the internet. You can do all of the young coders curriculum without an
 internet connection, and limiting internet means the students won't jump on
 the internet and find something else to distract them. I made this mistake, and
 it took me a while to pull their attention away from minecraft and some
 web-based games.
- \*\*Control the junk food\*\*. Unlimited cookies, chips, and coca-cola seems like an
 awesome idea. And if you're 12-years-old, you'll take full advantage of that.
 It's probably not a good a idea to let the kids have free range at a junk food
 buffet. A little is fun, but after an hour or so you'll lose some attention to
 the pile of sugar.
- \*\*Volunteers are awesome\*\*. Luckily the PyTN class was pretty small (ten
 students), and we managed to make the class happen without too many pitfalls
 without any additional volunteers. \_However\_, if you think about teaching one
 of these take time to find some volunteers. I volunteered for Young Coders in
 PyOhio 2015, and there were about three volunteers for approximately 25 students, and
 that seemed to work fairly well.

I personally found teaching this class to be incredibly rewarding, and I'm
thankful to [Katie Cunningham](http://therealkatie.net) and
[Barbara Shaurette](http://www.mechanicalgirl.com) for their work creating the
curriculum and for many many iterations of this this class in the past. Their
work has made it easy to pick up the tools and run a class. If you're at all
interested in doing this, you can certainly pick up the tools and do it too!