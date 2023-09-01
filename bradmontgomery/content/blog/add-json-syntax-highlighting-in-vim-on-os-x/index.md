---
date: '2010-01-15T15:03:00+00:00'
title: Add JSON syntax highlighting in Vim on OS X
draft: false
tags: []
slug: add-json-syntax-highlighting-in-vim-on-os-x
description: This is how I got Vi...
markup: html
url: /blog/add-json-syntax-highlighting-in-vim-on-os-x/
aliases:
- /blog/2010/01/15/add-json-syntax-highlighting-in-vim-on-os-x/

---

This is how I got Vim to do syntax highlighting for JSON files (Max OS X - Snow Leopard)<br /><ol><li>Download the syntax file from <a href="http://www.vim.org/scripts/script.php?script_id=1945">http://www.vim.org/scripts/script.php?script_id=1945</a>. (I got <b>json.vim</b> version 0.4)</li><li>If it doesn't already exist, create a <b>.vim/ftplugin</b> in your home directory.</li><li>Put <b>json.vim</b> into <b>.vim/ftplugin</b></li><li>Add the following lines in your <b>.vimrc</b> file (mine is located at ~/.vimrc)<pre>au BufRead,BufNewFile *.json set filetype=json<br />au! Syntax json source /Users/brad/.vim/ftplugin/json.vim</pre>Note that you'll have to change the path to your json.vim file so that it works on your computer.</li><li>Now, got edit a .json file!</li><br /></ol><div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/4123748873183487963-7146046294850823266?l=bradmontgomery.blogspot.com' alt='' /></div>