---
date: '2010-06-09T09:12:00+00:00'
title: Vim Syntax highlighting for Apache Config Files
draft: false
tags:
- apache
- django
- vim
slug: vim-syntax-highlighting-for-apache-config-files
description: I use Django with Ap...
markup: html
url: /blog/vim-syntax-highlighting-for-apache-config-files/
aliases:
- /blog/2010/06/09/vim-syntax-highlighting-for-apache-config-files/

---

I use Django with Apache and mod_wsgi.  Each project that I work on has different apache config files, so I like to keep those in the same mercurial repo that contains my django project's code.<br /><br />For some time now, it's been bugging me that vim doesn't do syntax highlighting for those apache configs (nor the wsgi files). I finally decided to do something about it, and I'm glad I did, because it's a fairly simple fix:<br /><br />My project directory layout often look like this:<br /><pre><br />~/django_projects/projectname/<br />    __init__.py<br />    apache_configs/<br />        projectname<br />        projectname.wsgi<br />    manage.py<br />    settings.py<br />    myapp/<br /></pre><br />Vim does syntax highlighting for apache files based on their path. To get vim to recognize the files in the <em>apache_configs</em> directory, you need to edit (or create) <em>~/.vim/filetype.vim</em> and add the following:<br /><pre><br />au BufNewFile,BufRead ~/django_projects/de_concierge/apache_configs/*wsgi setf python<br />au BufNewFile,BufRead ~/django_projects/de_concierge/apache_configs/* setf apache <br /></pre><br />You'd have to add variants of this for each separate project, but this works well for me. <br /><br />There's several other ways you can modify this, and the solution that I used comes from <a href="http://groups.google.com/group/vim_mac/browse_thread/thread/26c3a097e6e69c5f">this thread on the vim_mac mailing list</a>.  (There's also a lot of good info in <em>:help new-filetype </em>).<div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/4123748873183487963-5589084931666424010?l=bradmontgomery.blogspot.com' alt='' /></div>