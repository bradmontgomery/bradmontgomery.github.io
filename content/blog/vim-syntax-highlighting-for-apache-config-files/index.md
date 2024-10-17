---
date: '2010-06-09T09:12:00+00:00'
title: Vim Syntax highlighting for Apache Config Files
draft: false
tags:
- apache
- django
- vim
slug: vim-syntax-highlighting-for-apache-config-files
description: ''
markup: md
url: /blog/vim-syntax-highlighting-for-apache-config-files/
aliases:
- /blog/2010/06/09/vim-syntax-highlighting-for-apache-config-files/

---

I use Django with Apache and mod\_wsgi. Each project that I work on has different apache config files, so I like to keep those in the same mercurial repo that contains my django project's code.  
  
For some time now, it's been bugging me that vim doesn't do syntax highlighting for those apache configs (nor the wsgi files). I finally decided to do something about it, and I'm glad I did, because it's a fairly simple fix:  
  
My project directory layout often look like this:  

```
  
~/django_projects/projectname/  
    __init__.py  
    apache_configs/  
        projectname  
        projectname.wsgi  
    manage.py  
    settings.py  
    myapp/  

```
  
Vim does syntax highlighting for apache files based on their path. To get vim to recognize the files in the *apache\_configs* directory, you need to edit (or create) *~/.vim/filetype.vim* and add the following:  

```
  
au BufNewFile,BufRead ~/django_projects/de_concierge/apache_configs/*wsgi setf python  
au BufNewFile,BufRead ~/django_projects/de_concierge/apache_configs/* setf apache   

```
  
You'd have to add variants of this for each separate project, but this works well for me.   
  
There's several other ways you can modify this, and the solution that I used comes from [this thread on the vim\_mac mailing list](http://groups.google.com/group/vim_mac/browse_thread/thread/26c3a097e6e69c5f). (There's also a lot of good info in *:help new-filetype* ).