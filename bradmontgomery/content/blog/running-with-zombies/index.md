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
description: <p>I picked up the <...
markup: html
url: /blog/running-with-zombies/
aliases:
- /blog/2012/03/10/running-with-zombies/

---

<p>I picked up the <a href="https://www.zombiesrungame.com/" _mce_href="https://www.zombiesrungame.com/">Zombies, Run!</a> app today, and I'm pretty excited about it. If you haven't heard about it, check out their video:</p>
<p><iframe width="560" height="315" src="http://www.youtube.com/embed/GyFqZtKvya0" _mce_src="http://www.youtube.com/embed/GyFqZtKvya0" frameborder="0" allowfullscreen=""></iframe></p>
<p>I've only had one run with the game, but the story felt very well-done, and I really like how they've added an extra element of fun to my run. Of course, I'm a fan of all things "<a href="http://en.wikipedia.org/wiki/Zombie_apocalypse#Zombie_apocalypse" _mce_href="http://en.wikipedia.org/wiki/Zombie_apocalypse#Zombie_apocalypse">Zombie Apocalypse</a>".</p>
<p>If you do <a href="http://itunes.apple.com/us/app/zombies-run!/id503519713" _mce_href="http://itunes.apple.com/us/app/zombies-run!/id503519713">pick up a copy</a>, spend some time setting up a decent play list. The story unfolds in small bits of dialog, but then launches into your own music. You'll hear a bit more of the story between each song.</p>
<p>I'm pretty happy about my playlist, even though I only got through the first 17 songs today. Here it is:</p>

<table class="mceItemTable">
<caption>Zombies, Run! Playlist (22 Songs, 1.3 hours)</caption>
<thead>
<tr><th>Song</th><th> Artist </th><th> Time (seconds)</th></tr>
</thead>
<tbody>
<tr><td> Micro Cuts </td><td> Muse </td><td> 218 </td></tr>
<tr><td> Them Bones </td><td> Alice in Chains </td><td> 149 </td></tr>
<tr><td> Name of the Game </td><td> The Crystal Method </td><td> 255 </td></tr>
<tr><td> Rebirth </td><td> Boy Hits Car </td><td> 242 </td></tr>
<tr><td> Still Running </td><td> Chevelle </td><td> 223 </td></tr>
<tr><td> Unreal Tournament - Go Down </td><td> Epic Games </td><td> 178 </td></tr>
<tr><td> Bloody Cape </td><td> Deftones </td><td> 217 </td></tr>
<tr><td> Excessive Reaction </td><td> Nonpoint </td><td> 171 </td></tr>
<tr><td> Cotopaxi </td><td> The Mars Volta </td><td> 218 </td></tr>
<tr><td> Unreal - Isotoxin </td><td> Epic Games </td><td> 246 </td></tr>
<tr><td> Darkening Days </td><td> Switched </td><td> 219 </td></tr>
<tr><td> Licking Cream </td><td> Sevendust </td><td> 197 </td></tr>
<tr><td> Insatiable </td><td> Helmet </td><td> 154 </td></tr>
<tr><td> Closer To The Edge </td><td> 30 Seconds To Mars </td><td> 273 </td></tr>
<tr><td> Temptation </td><td> VAST </td><td> 189 </td></tr>
<tr><td> Jesus Or A Gun </td><td> Fuel </td><td> 238 </td></tr>
<tr><td> Endure </td><td> Nonpoint </td><td> 178 </td></tr>
<tr><td> We've Had Enough </td><td> Alkaline Trio </td><td> 168 </td></tr>
<tr><td> Crawl </td><td> Staind </td><td> 269 </td></tr>
<tr><td> Jambi </td><td> Tool </td><td> 448 </td></tr>
<tr><td> Until The End [Explicit] </td><td> Breaking Benjamin </td><td> 252 </td></tr>
<tr><td> Maybe </td><td> Faktion </td><td> 296 </td></tr>
</tbody>
</table>

<h2>Complaints</h2>
<ul>
<li><strong>Missions don't auto-progress</strong>.  After you finish a mission, the app enters "radio mode". This means it plays music interspersed with dialog.  I like this mode, but I wish I had a way to tell the game to just move to the next mission once I finished on. I mean, I did an 8 mile run, and I only completed two missions! <code>:-(</code></li>
<li><strong>The audio mix is buggy</strong>.  I don't know if anyone else has had this problem, but during the second mission, the audio started acting funny. I could hear the dialog just fine, but once a song started playing, the audio was really suppressed until I picked up some supplies. At that point, my music played at a normal volume. This was really annoying because I either had to fumble with the volume on my phone or go halfway through a song without being able to hear.</li>
</ul>
<h2>Takeaway</h2>
<p>I like the game. It's a neat idea, and I'm pretty curious to see how it unfolds.  I'd already been running, but this will definitely make me look forward to that next run just a bit more. If you don't run, it could still be a fun game. Got for a 15 minute walk and give it a try <code>:)</code></p>
<h2>PS:</h2>
<p>You can export a playlist in iTunes. Just right-click on the playlist, then choose <em>Export</em> and save it in a plain text file. You get lots of information about each song, but I pulled out the bits I wanted with this awk command:</p>
<pre><code class="awk">awk -F\t '{print $1, " --- " $2, " --- ", $8 }' Zombies.txt</code></pre>
<p>Also, here's a <a href="" http:="" runkeeper.com="" user="" bkmontgomery="" activity="" 74636447"="" _mce_href="/admin/blog/blogpost/130/&quot;http:/runkeeper.com/user/bkmontgomery/activity/74636447">map of my run</a>.</p>