---
date: '2007-01-05T21:13:00+00:00'
title: Migrating PHP scripts to MySQL from PostgreSQL
draft: false
tags:
- Programming
- mysql
- php
- postgresql
slug: migrating-php-scripts-to-mysql-from-postgresql
description: <p>I've recently had...
markup: html
url: /blog/migrating-php-scripts-to-mysql-from-postgresql/
aliases:
- /blog/2007/01/05/migrating-php-scripts-to-mysql-from-postgresql/

---

<p>I've recently had to work on a project where I needed toconvert some very basic <a href="http://php.net" _mce_href="http://php.net">PHP</a> code thataccessed a <a href="http://www.postgresql.org/" _mce_href="http://www.postgresql.org/">postgresql</a>database so that it would work with <a href="http://mysql.com/" _mce_href="http://mysql.com/">mysql</a>. For the most part, this has beenfairly simple thanks to <a href="http://freshmeat.net/projects/rpl/" _mce_href="http://freshmeat.net/projects/rpl/">rpl</a>. Many of PHP'sdatabase functions have very similar names, so I simply use rpl toconvert the existing code. Here's a simple bashscript that I put together to convert some of my postgresqlfunctions to mysql:</p>
<pre class="bash"><code>
#!/bin/bash
if [ ! -n "$1" ]
then
   echo "Usage: `basename $0` "
  exit 1;
fi

X=$1

echo "---- Relacing pg_ with mysql_ in $X"

rpl -R -x'.php' 'pg_pconnect' 'mysql_pconnect' $X
rpl -R -x'.php' 'pg_connect' 'mysql_connect' $X
rpl -R -x'.php' 'pg_query' 'mysql_query' $X
rpl -R -x'.php' 'pg_fetch_row' 'mysq_fetch_row' $X
rpl -R -x'.php' 'pg_fetch_assoc' 'mysq_fetch_assoc' $X
rpl -R -x'.php' 'pg_close' 'mysq_close' $X
rpl -R -x'.php' 'pg_num_rows' 'mysq_num_rows' $X
rpl -R -x'.php' 'pg_numrows' 'mysq_num_rows' $X
rpl -R -x'.php' 'pg_last_error' 'mysql_error' $X
</code></pre>
<p>Just in case your curious about converting from postgresql or
mysql to sqlite, I've compiled the following table 
of analogous functions from <a href="http://php.net" _mce_href="http://php.net">php.net</a>:</p><table class="mceItemTable">
<thead>
<tr><th>PostgreSQL</th><th>MySQL</th><th>SQLite</th></tr>
</thead>
<tbody>
<tr>
<td>pg_connect</td>
<td>mysql_connect</td>
<td>sqlite_open // open or create database</td>
</tr>
<tr>
<td>pg_query</td>
<td>mysql_query</td>
<td>sqlite_query</td>
</tr>
<tr>
<td>pg_fetch_row</td>
<td>mysql_fetch_row</td>
<td rowspan="2">sqlite_fetch_array (ordinal and associative)</td>
</tr>
<tr>
<td>pg_fetch_assoc</td>
<td>mysql_fetch_assoc</td>
</tr>
<tr>
<td>pg_close</td>
<td>mysql_close</td>
<td>sqlite_close</td>
</tr>
<tr>
<td>pg_num_rows or pg_numrows</td>
<td>mysql_num_rows</td>
<td>sqlite_num_rows</td>
</tr>
</tbody>
</table><p><br mce_bogus="1"></p>