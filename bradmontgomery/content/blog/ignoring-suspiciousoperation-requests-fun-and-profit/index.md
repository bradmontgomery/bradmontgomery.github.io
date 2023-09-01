---
date: '2015-12-16T15:20:03.113439+00:00'
title: Ignoring SuspiciousOperation requests for fun and (profit?)
draft: false
tags: []
slug: ignoring-suspiciousoperation-requests-fun-and-profit
description: <p>If you run a Djan...
markup: html
url: /blog/ignoring-suspiciousoperation-requests-fun-and-profit/
aliases:
- /blog/2015/12/16/ignoring-suspiciousoperation-requests-fun-and-profit/

---

<p>If you run a Django site, you're probably familiar with those periodic emails due to a <a href="https://docs.djangoproject.com/en/dev/ref/exceptions/#suspiciousoperation">SuspiciousOperation</a> exception; it happens when your site receives a request that contains a host header that's now found in the <a href="https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-ALLOWED_HOSTS">ALLOWED_HOSTS</a> setting. Yes, they're annoying, and while it's good to know when this happens, I've found that there will typically be one or two requests that you get frequently (I'm looking at you, request for <code>/azenv.php</code> from <code>check.proxyradar.com</code>).</p>

<p>In these cases, I think it's ok to just block these requests, so we no longer get those annoying emails. We can do this with a fairly simple middleware. It'll need to be listed first in your <code>MIDDLEWARE_CLASSES</code> settings, otherwise some other middleware might trigger the SuspiciousOperation exception.</p>


<p>First, though, let's set a list of urls in our settings. I called these <code>IGNORE_BAD_HOST_HEADERS</code>, and added as follows:</p>

<pre><code class="python">IGNORE_BAD_HOST_HEADERS = [
    'proxyradar.com',  # Stupid check.proxyradar.com/azenv.php
]</code></pre>

<p>I have a <code>utils</code> app where I include miscellaneous bits of code, so in <code>utils/middleware.py</code>, I added the following class:</p>

<pre><code class="python">from django.conf import settings
from django.http import HttpResponse

class IgnoreRequestMiddleware(object):
    """Sometimes we get obviously bad requests. If we can detect those, we'll
    just ignore them outright, returning a little easer egg instead.

    To test this, set DEBUG=False, and use:

         curl --verbose --header 'Host: example.com' 'http://yoursite.com'

    NOTE: In order for this to work, this must be listed first in the
    MIDDLEWARE_CLASSES setting.

    """
    def _ignore_domain(self, request):
        """ignore requests from obviously bad domains. This will circumvent
        those annoying Invalid HTTP_HOST header errors."""
        ignored_domains = getattr(settings, 'IGNORE_BAD_HOST_HEADERS', [])
        return any([
            domain in request.META.get('HTTP_HOST', '')
            for domain in ignored_domains
        ])

    def process_request(self, request):
        if self._ignore_domain(request):
            teapot = """&lt;html&gt;&lt;body&gt;&lt;pre&gt;
                                   (
                        _           ) )
                     _,(_)._        ((
                ___,(_______).        )
              ,'__.   /       \    /\_
             /,' /  |""|       \  /  /
            | | |   |__|       |,'  /
             \`.|                  /
              `. :           :    /
                `.            :.,'
                  `-.________,-'

            &lt;/pre&gt;&lt;/body&gt;&lt;/html&gt;"""
            resp = HttpResponse(teapot)
            resp.status_code = 418
            return resp</code></pre>

<p>Now, in your settings, you'll need to add something similar to:</p>

<pre><code class="python">MIDDLEWARE_CLASSES = [
    'utils.middleware.IgnoreRequestMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    ...
]</code></pre>

<p>And there you go! No more annoying SuspiciousOperation emails due to requests from that one particular host.  Now, this is kind of a hack, albeit a fun one. A <strong>much better</strong> solution to this problem would be to block these requests at your webserver (e.g. in apache or nginx).</p>

<p>In any event, you can deploy and and check it out with curl: <code> curl --verbose --header 'Host: example.com' 'http://yoursite.com'</code>.</p>