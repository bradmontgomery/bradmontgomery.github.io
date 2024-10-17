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
description: ''
markup: md
url: /blog/safari-is-cooler-than-you-think/
aliases:
- /blog/2008/09/04/safari-is-cooler-than-you-think/

---

When you really start digging into Mac OS X, it's fairly mind-boggling how much *extra stuff* it has that your average user never sees. I recently encountered a problem on my MacBook Pro, where the [Optical Audio was overriding my internal speakers](http://discussions.apple.com/thread.jspa?messageID=7760823�), which prevented me from hearing any audio (without using headphones). Unfortunately, there's no easy-to-access preference pane to enable or disable various audio devices. This led me on a search for command-line utilities to manage system preferences.  
  
(hang on, I'll get to Safari in a second...)  
  
Eventually I ran into Amit Singh's list of [OS X Hacking tools](http://www.kernelthread.com/mac/osx/tools.html), where I stumbled upon the **[defaults](http://developer.apple.com/documentation/Darwin/Reference/ManPages/man1/defaults.1.html)** command. **defaults** is the magic "change any setting for Mac OS X on the command line" tool that you (by you, I mean me) never knew about!  
  
So, what does this have to do with Safari? Well, after looking for more information on how to use **defaults**, I stumbled upon Mac OS X Tips' [Top 15 Terminal Commands for Hidden Mac OS X Settings](http://www.macosxtips.co.uk/index_files/terminal-commands-for-hidden-mac-os-x-settings.html), one of which really caught my attention:  
  

```
defaults write com.apple.safari IncludeDebugMenu 1
```
  
  
This enables a "Debug" Menu ("Develop" menu on Safari 3). The Developer menu allows you to:  
* Change Safari's user-agent, so you can masquerade as IE, Firefox, Opera, earlier versions of Safari, or even the iPhone version of Safari
* View a Web Inspector - allows you to view scripts, css files, and other information associated with a Web page...
* View a network timeline - showing the time it took to download each component linked in a web-page...
* Disable stuff - like javascript, css, java, caches...

  
  
It's not quite the [Web Developer plugin](https://addons.mozilla.org/en-US/firefox/addon/60) for Firefox, but it does give you additional control over Safari.  
  
And the Network timeline looks pretty darn cool!  
  
ps: i never did find a way to disable the optical audio...guess i got side-tracked.  
  
**[Update: 10/05/2008]** I just realized there's an easier way to enable this in the Advanced Preferences Tab... just enable the "Show Develop menu in menu bar" option! (as in the screenshot below)  
  
![Show Develop menu in menu bar](http://bradmontgomery.net/images/Safari_Advanced.png)  
  
I guess it pays to pay attention to your app's options!