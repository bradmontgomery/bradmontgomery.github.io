---
date: '2008-08-12T10:32:00+00:00'
title: How to update an input value with the value from a selected option using Prototype
draft: false
tags:
- Javascript
- Programming
- web
slug: how-to-update-an-input-value-with-the-value-from-a-selected-option-using-prototype
description: Today, I needed to s...
markup: html
url: /blog/how-to-update-an-input-value-with-the-value-from-a-selected-option-using-prototype/
aliases:
- /blog/2008/08/12/how-to-update-an-input-value-with-the-value-from-a-selected-option-using-prototype/

---

Today, I needed to set the value of an HTML input element based on the value of a option in a select element.  This is fairly easy to do with <a href="http://www.prototypejs.org/api/element/writeAttribute">Prototype's writeAttribute</a>. Here's an example:<br /><br />A simple javascript function to do the work:<br /><div class="highlight" ><pre><span style="color: #007020; font-weight: bold">function</span> populate_input(){<br />    <span style="color: #007020; font-weight: bold">var</span> field <span style="color: #666666">=</span> $(<span style="color: #4070a0">&#39;tf_select&#39;</span>).getValue(); <br />    $(<span style="color: #4070a0">&#39;tf&#39;</span>).writeAttribute(<span style="color: #4070a0">&#39;value&#39;</span><span style="color: #666666">,</span> field);<br />}<br /></pre></div><br /><br />A simple HTML snippet to see it in action:<br /><div class="highlight" ><pre><span style="color: #062873; font-weight: bold">&lt;div&gt;</span><br /><span style="color: #062873; font-weight: bold">&lt;p&gt;&lt;select</span> <span style="color: #4070a0">id=&quot;tf_select&quot;</span> <span style="color: #4070a0">name=&quot;tf_select&quot;</span> <span style="color: #4070a0">onchange=&quot;populate_input();&quot;</span><span style="color: #062873; font-weight: bold">&gt;</span><br /><span style="color: #062873; font-weight: bold">&lt;option</span> <span style="color: #4070a0">value=&quot;&quot;</span><span style="color: #062873; font-weight: bold">&gt;</span>- choose one -<span style="color: #062873; font-weight: bold">&lt;/option&gt;</span><br /><span style="color: #062873; font-weight: bold">&lt;option</span> <span style="color: #4070a0">value=&quot;v1&quot;</span><span style="color: #062873; font-weight: bold">&gt;</span>value 1<span style="color: #062873; font-weight: bold">&lt;/option&gt;</span><br /><span style="color: #062873; font-weight: bold">&lt;option</span> <span style="color: #4070a0">value=&quot;v2&quot;</span><span style="color: #062873; font-weight: bold">&gt;</span>value 2<span style="color: #062873; font-weight: bold">&lt;/option&gt;</span><br /><span style="color: #062873; font-weight: bold">&lt;/select&gt;&lt;br/&gt;&lt;input</span> <span style="color: #4070a0">type=&quot;test&quot;</span> <span style="color: #4070a0">id=&quot;tf&quot;</span> <span style="color: #4070a0">name=&quot;tf&quot;</span> <span style="color: #4070a0">value=&quot;&quot;</span><span style="color: #062873; font-weight: bold">/&gt;&lt;/p&gt;</span><br /><span style="color: #062873; font-weight: bold">&lt;/div&gt;</span><br /></pre></div><br /><br />And yes... I know the title of this post is almost longer than the post itself!<div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/4123748873183487963-1905114992701722468?l=bradmontgomery.blogspot.com' alt='' /></div>