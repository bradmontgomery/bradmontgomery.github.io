---
date: '2009-11-24T12:07:00+00:00'
title: Sticky Groups
draft: false
tags:
- Linux
- web
slug: sticky-groups
description: ''
markup: md
url: /blog/sticky-groups/
aliases:
- /blog/2009/11/24/sticky-groups/

---

I often deploy web projects in a directory that's not *owned* by the user under which my webserver runs. Therefor, I often have to change permissions so the webserver can read from or write to certain files. So, for this example, let's assume I'm logged in to my linux box as *brad*, and I'm using apache which runs under the user *www-data*.   
To give apache access to my public\_html directory, I'd change ownership for the directory and all of its contents:
```
chown -R brad:www-data public_html
```
  
I may also need to allow apache to write to a certain directory:
```
chmod g+w public_html/somedir
```
  
Now, if I modify any files in *public\_html*, I don't want to have to change the group permissions (that is, apache's permissions), so lets make the group ownership **sticky**:  

```
chmod g+s public_html
```
  
Now, any new files that I add beneath the *public\_html* directory will be part of the *www-data* group.