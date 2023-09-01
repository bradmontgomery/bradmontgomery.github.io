---
date: '2009-11-24T12:07:00+00:00'
title: Sticky Groups
draft: false
tags:
- Linux
- web
slug: sticky-groups
description: I often deploy web p...
markup: html
url: /blog/sticky-groups/
aliases:
- /blog/2009/11/24/sticky-groups/

---

I often deploy web projects in a directory that's not <em>owned</em> by the user under which my webserver runs.  Therefor, I often have to change permissions so the webserver can read from or write to certain files. So, for this example, let's assume I'm logged in to my linux box as <em>brad</em>, and I'm using apache which runs under the user <em>www-data</em>. <br />To give apache access to my public_html directory, I'd change ownership for the directory and all of its contents:<pre>chown -R brad:www-data public_html</pre><br />I may also need to allow apache to write to a certain directory:<pre>chmod g+w public_html/somedir</pre><br />Now, if I modify any files in <em>public_html</em>, I don't want to have to change the group permissions (that is, apache's permissions), so lets make the group ownership <strong>sticky</strong>:<br /><pre>chmod g+s public_html</pre><br />Now, any new files that I add beneath the <em>public_html</em> directory will be part of the <em>www-data</em> group.<div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/4123748873183487963-7915480253587113591?l=bradmontgomery.blogspot.com' alt='' /></div>