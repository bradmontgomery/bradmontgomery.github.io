---
date: '2009-03-24T09:28:00+00:00'
title: mod_python checks your blood pressure
draft: false
tags:
- Fun
- Python
- django
slug: mod_python-checks-your-blood-pressure
description: ''
markup: md
url: /blog/mod_python-checks-your-blood-pressure/
aliases:
- /blog/2009/03/24/mod_python-checks-your-blood-pressure/

---

I'm deploying a [django](http://www.djangoproject.com/) project using [mod\_python](http://www.modpython.org/)... now, usually I will just use my package management tools to install a binary version, but this time I need to build it from source.  
  
As I get ready to go through the whole configure/make/make install process, I peruse the output of configure just to make sure everything is ok...  
  
  
checking for gcc... gcc  
checking for C compiler default output file name... a.out  
checking whether the C compiler works... yes  
checking whether we are cross compiling... no  
checking for suffix of executables...   
checking for suffix of object files... o  
checking whether we are using the GNU C compiler... yes  
checking whether gcc accepts -g... yes  
checking for gcc option to accept ANSI C... none needed  
checking for ar... ar  
checking for a BSD-compatible install... /usr/bin/install -c  
checking whether make sets $(MAKE)... yes  
checking for main in -lm... yes  
checking for an ANSI C-conforming const... yes  
**checking your blood pressure... a bit high, but we can proceed**  
configure: checking whether apxs is available...  
checking for --with-apxs... /usr/sbin/apxs executable, good  
checking Apache version... 2.0.52  
checking for Apache libexec directory... /usr/lib/httpd/modules  
checking for Apache include directory... -I/usr/include/httpd  
checking for --with-python... /usr/local/bin/python2.6  
checking Python version... 2.6  
checking Python install prefix... /usr/local  
checking checking where python libraries are installed... /usr/local/lib/python2.6  
checking for Py\_NewInterpreter in -lpython2.6... yes  
checking what libraries Python was linked with... -lpython2.6 -lpthread -ldl -lutil -lm  
checking linker flags used to link Python...   
checking where Python include files are... -I/usr/local/include/python2.6  
checking for --with-python-src... /home/bkmontgomery/Python-2.6.1/src  
checking for --with-mutex-dir... no  
Using MUTEX\_DIR /tmp  
checking for --with-max-locks... 32  
Using 32 MAX\_LOCKS.  
checking for --with-flex... /usr/bin/flex  
found /usr/bin/flex, we'll use this. Use --with-flex to specify another.  
checking flex version... configure: WARNING: Flex version 2.5.4 found.  
 Version 2.5.31 or greater is required. You can generally ignore this  
 warning unless you need to regenerate psp\_parser.c from psp\_parse.l.  
 If you do need regenerate psp\_parser.c, use --with-flex to specify the  
 location of the correct flex version. See the README for more information.  
configure: creating ./config.status  
config.status: creating Makefile  
config.status: creating src/Makefile  
config.status: creating Doc/Makefile  
config.status: creating src/include/mod\_python.h  
config.status: creating test/Makefile  
config.status: creating test/testconf.py  
config.status: creating dist/setup.py  
config.status: creating dist/Makefile  
  
  
Thank you for caring for my health, mod\_python.