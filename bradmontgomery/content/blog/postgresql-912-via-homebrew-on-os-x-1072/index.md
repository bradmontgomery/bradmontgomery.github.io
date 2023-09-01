---
date: '2011-12-22T06:20:39+00:00'
title: PostgreSQL 9.1.2 via homebrew on OS X 10.7.2
draft: false
tags:
- django
- homebrew
- osx
- postgresql
- python
slug: postgresql-912-via-homebrew-on-os-x-1072
description: <p>I just picked up ...
markup: html
url: /blog/postgresql-912-via-homebrew-on-os-x-1072/
aliases:
- /blog/2011/12/22/postgresql-912-via-homebrew-on-os-x-1072/

---

<p>I just picked up a snazzy new Macbook Air, and I'm working on setting up my development 
   environment(s). For the most part this has been fairly easy.  I pull in my repos from 
   <a href="https://github.com/bradmontgomery" _mce_href="https://github.com/bradmontgomery">github</a> and <a href="https://bitbucket.org/bkmontgomery" _mce_href="https://bitbucket.org/bkmontgomery">bitbucket</a>, 
   and I use <a href="http://pypi.python.org/pypi/virtualenv" _mce_href="http://pypi.python.org/pypi/virtualenv">virtualenv</a> and <a href="http://www.pip-installer.org/" _mce_href="http://www.pip-installer.org/">pip</a>
   to organize all my python packages (mostly installing from 
   <a href="http://www.pip-installer.org/en/latest/requirements.html" _mce_href="http://www.pip-installer.org/en/latest/requirements.html">requirements files</a>). Most of the other 
   command-line tools get intalled with <a href="http://mxcl.github.com/homebrew/" _mce_href="http://mxcl.github.com/homebrew/">homebrew</a>, and this time around I 
   decided to install PostgreSQL with homebrew.</p>
<p>I didn't keep track of all the steps I followed, but I'm pretty sure I just kept all the defaults 
   while installing. I set up a new database cluster with <code>initdb</code> and then I created a 
   local user (no password) and set up a database for one of my Django apps.  But then I got this 
   error when running syncdb:</p>
<pre><code>OperationalError: could not connect to server: Permission denied
    Is the server running locally and accepting
    connections on Unix domain socket "/var/pgsql_socket/.s.PGSQL.5432"?
</code></pre>

<p>That's odd. I did some digging and didn't really find much info that seem relevant 
   (though there is this ticket: <a href="https://trac.macports.org/ticket/30125" _mce_href="https://trac.macports.org/ticket/30125">https://trac.macports.org/ticket/30125</a>).
   However, when I explicitly specified a <code>HOST</code> value in my django settings, things just started working.</p>
<pre class="python"><code>DATABASES = { 
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'somedb',  
        'USER': 'someuser', 
        'PASSWORD': '', 
        'HOST': 'localhost',
        'PORT': '', 
    }   
}
</code></pre>

<p>I'm not quite sure what's going on here, or if this is a bug in PostgreSQL. Other than that little 
   snag, everything seems to be working swell.</p>
<p>Apparently reinstalling <code>psycopg2</code> also fixes this problem:</p><pre><code>pip install -U psycopg2</code></pre>
<p>Thanks to <a href="https://twitter.com/lukeman" _mce_href="https://twitter.com/lukeman">@lukeman</a> for the tip, and to <a href="https://twitter.com/dstufft" _mce_href="https://twitter.com/dstufft">@dstufft</a> who helped him!<br><br>:)</p>