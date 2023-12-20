---
date: '2012-03-10T21:43:49+00:00'
title: Running with Zombies.
draft: false
tags:
- fun
- iphone
- running
- zombies
slug: running-with-zombies
description: ''
markup: md
url: /blog/running-with-zombies/
aliases:
- /blog/2012/03/10/running-with-zombies/

---

I picked up the [Zombies, Run!](https://www.zombiesrungame.com/) app today, and I'm pretty excited about it. If you haven't heard about it, check out their video:



I've only had one run with the game, but the story felt very well-done, and I really like how they've added an extra element of fun to my run. Of course, I'm a fan of all things "[Zombie Apocalypse](http://en.wikipedia.org/wiki/Zombie_apocalypse#Zombie_apocalypse)".


If you do [pick up a copy](http://itunes.apple.com/us/app/zombies-run!/id503519713), spend some time setting up a decent play list. The story unfolds in small bits of dialog, but then launches into your own music. You'll hear a bit more of the story between each song.


I'm pretty happy about my playlist, even though I only got through the first 17 songs today. Here it is:




Zombies, Run! Playlist (22 Songs, 1.3 hours)| Song |  Artist  |  Time (seconds) |
| --- | --- | --- |
|  Micro Cuts  |  Muse  |  218  |
|  Them Bones  |  Alice in Chains  |  149  |
|  Name of the Game  |  The Crystal Method  |  255  |
|  Rebirth  |  Boy Hits Car  |  242  |
|  Still Running  |  Chevelle  |  223  |
|  Unreal Tournament - Go Down  |  Epic Games  |  178  |
|  Bloody Cape  |  Deftones  |  217  |
|  Excessive Reaction  |  Nonpoint  |  171  |
|  Cotopaxi  |  The Mars Volta  |  218  |
|  Unreal - Isotoxin  |  Epic Games  |  246  |
|  Darkening Days  |  Switched  |  219  |
|  Licking Cream  |  Sevendust  |  197  |
|  Insatiable  |  Helmet  |  154  |
|  Closer To The Edge  |  30 Seconds To Mars  |  273  |
|  Temptation  |  VAST  |  189  |
|  Jesus Or A Gun  |  Fuel  |  238  |
|  Endure  |  Nonpoint  |  178  |
|  We've Had Enough  |  Alkaline Trio  |  168  |
|  Crawl  |  Staind  |  269  |
|  Jambi  |  Tool  |  448  |
|  Until The End [Explicit]  |  Breaking Benjamin  |  252  |
|  Maybe  |  Faktion  |  296  |


Complaints
----------


* **Missions don't auto-progress**. After you finish a mission, the app enters "radio mode". This means it plays music interspersed with dialog. I like this mode, but I wish I had a way to tell the game to just move to the next mission once I finished on. I mean, I did an 8 mile run, and I only completed two missions! `:-(`
* **The audio mix is buggy**. I don't know if anyone else has had this problem, but during the second mission, the audio started acting funny. I could hear the dialog just fine, but once a song started playing, the audio was really suppressed until I picked up some supplies. At that point, my music played at a normal volume. This was really annoying because I either had to fumble with the volume on my phone or go halfway through a song without being able to hear.


Takeaway
--------


I like the game. It's a neat idea, and I'm pretty curious to see how it unfolds. I'd already been running, but this will definitely make me look forward to that next run just a bit more. If you don't run, it could still be a fun game. Got for a 15 minute walk and give it a try `:)`


PS:
---


You can export a playlist in iTunes. Just right-click on the playlist, then choose *Export* and save it in a plain text file. You get lots of information about each song, but I pulled out the bits I wanted with this awk command:



```
awk -F\t '{print $1, " --- " $2, " --- ", $8 }' Zombies.txt
```

Also, here's a map of my run.

