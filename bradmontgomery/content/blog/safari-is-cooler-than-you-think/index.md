---
date: '2008-09-04T15:12:00+00:00'
title: Safari is Cooler than you Think!
draft: false
tags:
- Apps
- OS
- Safari
- X
- web
slug: safari-is-cooler-than-you-think
description: When you really star...
markup: html
url: /blog/safari-is-cooler-than-you-think/
aliases:
- /blog/2008/09/04/safari-is-cooler-than-you-think/

---

When you really start digging into Mac OS X, it's fairly mind-boggling how much <em>extra stuff</em> it has that your average user never sees.  I recently encountered a problem on my MacBook Pro, where the <a href="http://discussions.apple.com/thread.jspa?messageID=7760823&#7760823">Optical Audio was overriding my internal speakers</a>, which prevented me from hearing any audio (without using headphones).  Unfortunately, there's no easy-to-access preference pane to enable or disable various audio devices.  This led me on a search for command-line utilities to manage system preferences.<br /><br />(hang on, I'll get to Safari in a second...)<br /><br />Eventually I ran into Amit Singh's list of <a href="http://www.kernelthread.com/mac/osx/tools.html">OS X Hacking tools</a>, where I stumbled upon the <b><a href="http://developer.apple.com/documentation/Darwin/Reference/ManPages/man1/defaults.1.html">defaults</a></b> command.  <b>defaults</b> is the magic "change any setting for Mac OS X on the command line" tool that you (by you, I mean me) never knew about!<br /><br />So, what does this have to do with Safari?  Well, after looking for more information on how to use <b>defaults</b>, I stumbled upon Mac OS X Tips' <a href="http://www.macosxtips.co.uk/index_files/terminal-commands-for-hidden-mac-os-x-settings.html">Top 15 Terminal Commands for Hidden Mac OS X Settings</a>, one of which really caught my attention:<br /><br /><pre>defaults write com.apple.safari IncludeDebugMenu 1</pre><br /><br />This enables a "Debug" Menu ("Develop" menu on Safari 3).  The Developer menu allows you to:<br /><ul><li>Change Safari's user-agent, so you can masquerade as IE, Firefox, Opera, earlier versions of Safari, or even the iPhone version of Safari</li><li>View a Web Inspector - allows you to view scripts, css files, and other information associated with a Web page...</li><li>View a network timeline - showing the time it took to download each component linked in a web-page...</li><li>Disable stuff - like javascript, css, java, caches...</li></ul><br /><br />It's not quite the <a href="https://addons.mozilla.org/en-US/firefox/addon/60">Web Developer plugin</a> for Firefox, but it does give you additional control over Safari.<br /><br />And the Network timeline looks pretty darn cool!<br /><br />ps: i never did find a way to disable the optical audio...guess i got side-tracked.<br /><br /><b>[Update: 10/05/2008]</b> I just realized there's an easier way to enable this in the Advanced Preferences Tab... just enable the "Show Develop menu in menu bar" option! (as in the screenshot below)<br /><br /><img src="http://bradmontgomery.net/images/Safari_Advanced.png" alt="Show Develop menu in menu bar"/><br /><br />I guess it pays to pay attention to your app's options!<div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/4123748873183487963-7935637856182059427?l=bradmontgomery.blogspot.com' alt='' /></div>