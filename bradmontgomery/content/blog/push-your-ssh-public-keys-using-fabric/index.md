---
date: '2009-04-30T15:45:00+00:00'
title: Push Your SSH Public keys using Fabric
draft: false
tags:
- Python
- fabric
slug: push-your-ssh-public-keys-using-fabric
description: This came across my ...
markup: html
url: /blog/push-your-ssh-public-keys-using-fabric/
aliases:
- /blog/2009/04/30/push-your-ssh-public-keys-using-fabric/

---

This came across my twitter radar today from <em><a href="http://twitter.com/bitprophet/">@bitprophet</a></em> (aka: Jeff Forcier), who just happens to be the new maintainer for <a href="http://www.nongnu.org/fab/">Fabric</a>:<br /><br /><div class="highlight" ><pre><span style="color: #007020; font-weight: bold">def</span> <span style="color: #06287e">push_key</span>():<br />    keyfile <span style="color: #666666">=</span> <span style="color: #4070a0">&#39;/tmp/</span><span style="color: #70a0d0; font-style: italic">%s</span><span style="color: #4070a0">.pub&#39;</span> <span style="color: #666666">%</span> env<span style="color: #666666">.</span>user<br />    run(<span style="color: #4070a0">&#39;mkdir -p ~/.ssh &amp;&amp; chmod 700 ~/.ssh&#39;</span>)<br />    put(<span style="color: #4070a0">&#39;~/.ssh/id_rsa.pub&#39;</span>, keyfile)<br />    run(<span style="color: #4070a0">&#39;cat </span><span style="color: #70a0d0; font-style: italic">%s</span><span style="color: #4070a0"> &gt;&gt; ~/.ssh/authorized_keys&#39;</span> <span style="color: #666666">%</span> keyfile)<br />    run(<span style="color: #4070a0">&#39;rm </span><span style="color: #70a0d0; font-style: italic">%s</span><span style="color: #4070a0">&#39;</span> <span style="color: #666666">%</span> keyfile)<br /></pre></div><br /><br />Everything you need to push your public key to an external server using Fabric.<div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/4123748873183487963-1296451718188870554?l=bradmontgomery.blogspot.com' alt='' /></div>