---
date: '2010-05-28T15:39:00+00:00'
title: Convert Tables to Unordered Lists
draft: false
tags:
- BeautifulSoup
- Programming
- Python
- web
slug: convert-tables-to-unordered-lists
description: ''
markup: md
url: /blog/convert-tables-to-unordered-lists/
aliases:
- /blog/2010/05/28/convert-tables-to-unordered-lists/

---

If you've ever had the pleasure of working with old HTML content, you've surely seen some <table>'s where they don't belong. Lately, that's the sort of thing I've been dealing with on a regular basis, and for some reason, I often see a list of information in a table.  
  
Wouldn't it be nice if there were an easy way to turn these tables into unordered lists? Thanks to [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/), this is really not that difficult.  
  
Here's the code:  

```
from BeautifulSoup import BeautifulSoup, Tag   
  
def table2ul(content, flatten_rows=False):  
    """   
 Convert a <table> into a <ul>.  
 Each cell, <td>, gets converted into a list item <li> unless  
 the flatten\_rows paramter is given. In this case, all content from   
 a table row, <tr>, gets converted into a list item.  
 """  
    soup = BeautifulSoup(content, convertEntities=BeautifulSoup.HTML_ENTITIES, smartQuotesTo="html")  
  
    for table in soup.findAll('table'):  
        ul = Tag(soup, 'ul')  
  
        if flatten_rows:  
            for row in table.findAll('tr'):  
                li = Tag(soup, 'li')  
                for cell in row.findAll('td'):  
                    li.contents.extend(cell.contents)  
                ul.append(li)  
        else:  
            for cell in table.findAll('td'):  
                li = Tag(soup, 'li')  
                li.contents = cell.contents  
                ul.append(li)  
        table.replaceWith(ul)  
  
    return soup.prettify()
```
  
  
Now, suppose we had the following HTML snippet:
```
<h1>Some heading</h1>  
<p>Some paragraph with stuff in it</p>  
<table>  
<tr><td> row 1, <strong>col1</strong></td><td>row 1, col2</td></tr>  
<tr><td> row 2, col1</td><td><em><a href="http://google.com">row 2</a></em>, col2</td></tr>  
</table>  
  
<h2>A second heading</h2>  
<p>more peee</p>
```
  
  
Passing this in to **table2ul** would convert each cell into a list item, <li>. 
```
>>> table2ul(content)
```
  

```
<h1>  
 Some heading  
</h1>  
<p>  
 Some paragraph with stuff in it  
</p>  
<ul>  
 <li>  
  row 1,  
  <strong>  
   col1  
  </strong>  
 </li>  
 <li>  
  row 1, col2  
 </li>  
 <li>  
  row 2, col1  
 </li>  
 <li>  
  <em>  
   <a href="http://google.com">  
    row 2  
   </a>  
  </em>  
  , col2  
 </li>  
</ul>  
<h2>  
 A second heading  
</h2>  
<p>  
 more peee  
</p>
```
  
  
But what if we don't want each <td> converted into an <li%gt>? What if we want all the content from entire row in an <li>? In that case, just set the optional **flatten\_rows** parameter:  

```
>>> table2ul(content, flatten_rows=True)
```
  

```
<h1>  
 Some heading  
</h1>  
<p>  
 Some paragraph with stuff in it  
</p>  
<ul>  
 <li>  
  row 1,  
  <strong>  
   col1  
  </strong>  row 1, col2  
 </li>  
 <li>  
  row 2, col1  
  <em>  
   <a href="http://google.com">  
    row 2  
   </a>  
  </em>  
  , col2  
 </li>  
</ul>  
<h2>  
 A second heading  
</h2>  
<p>  
 more peee  
</p>
```
  
  
This has been somewhat useful for me. Hope it's useful for you!