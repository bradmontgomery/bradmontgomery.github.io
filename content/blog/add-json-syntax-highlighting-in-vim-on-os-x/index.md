---
date: '2010-01-15T15:03:00+00:00'
title: Add JSON syntax highlighting in Vim on OS X
draft: false
tags: []
slug: add-json-syntax-highlighting-in-vim-on-os-x
description: ''
markup: md
url: /blog/add-json-syntax-highlighting-in-vim-on-os-x/
aliases:
- /blog/2010/01/15/add-json-syntax-highlighting-in-vim-on-os-x/

---

This is how I got Vim to do syntax highlighting for JSON files (Max OS X - Snow Leopard)  
1. Download the syntax file from <http://www.vim.org/scripts/script.php?script_id=1945>. (I got **json.vim** version 0.4)
2. If it doesn't already exist, create a **.vim/ftplugin** in your home directory.
3. Put **json.vim** into **.vim/ftplugin**
4. Add the following lines in your **.vimrc** file (mine is located at ~/.vimrc)
```
au BufRead,BufNewFile *.json set filetype=json  
au! Syntax json source /Users/brad/.vim/ftplugin/json.vim
```
Note that you'll have to change the path to your json.vim file so that it works on your computer.
5. Now, got edit a .json file!
  

