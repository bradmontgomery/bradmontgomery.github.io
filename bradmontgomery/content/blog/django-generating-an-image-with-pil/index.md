---
date: '2008-07-16T10:37:00+00:00'
title: 'Django: Generating an Image with PIL'
draft: false
tags: []
slug: django-generating-an-image-with-pil
description: ''
markup: md
url: /blog/django-generating-an-image-with-pil/
aliases:
- /blog/2008/07/16/django-generating-an-image-with-pil/

---

I've been reading through the [Django Book](http://www.djangobook.com/), and in [chapter 11](http://www.djangobook.com/en/1.0/chapter11/) they talk about generating non-HTML content (such as PDF files, Images, RSS/Atom Feeds). They mention using [PIL](http://www.pythonware.com/products/pil/) to generate images, but they don't give an example. So, I thought I'd post a simple example View that generates an image.  
  

```
def pil\_image(request):  
    ''' A View that Returns a PNG Image generated using PIL'''  
  
    import Image, ImageDraw   
  
    size = (100,50)             # size of the image to create  
    im = Image.new('RGB', size) # create the image  
    draw = ImageDraw.Draw(im)   # create a drawing object that is  
                                # used to draw on the new image  
    red = (255,0,0)    # color of our text  
    text_pos = (10,10) # top-left position of our text  
    text = "Hello World!" # text to draw  
    # Now, we'll do the drawing:   
    draw.text(text_pos, text, fill=red)  
      
    del draw # I'm done drawing so I don't need this anymore  
      
    # We need an HttpResponse object with the correct mimetype  
    response = HttpResponse(mimetype="image/png")  
    # now, we tell the image to save as a PNG to the   
    # provided file-like object  
    im.save(response, 'PNG')  
  
    return response # and we're done!  

```
  
  
This example just draws simple text, but the drawing code could be replaced by something more elaborate such as code that opens and scales existing images.  
  
A note of concern: The Image object (im) **MUST** be saved as a PNG for this to work. Luckily, the Image.save method expects a file-like object as its first parameter, so we can use django's HttpResponse object here. Also, the example above doesn't make use of any particular Font for the drawing, so if you do want to draw text, you'll want to take a look at PIL's [ImageDraw Documentation](http://www.pythonware.com/library/pil/handbook/imagedraw.htm).  
  
(on a side note: the html for the code above was generated using [dpaste](http://dpaste.com), which rocks!)![](https://blogger.googleusercontent.com/tracker/4123748873183487963-9092702185978828760?l=bradmontgomery.blogspot.com)