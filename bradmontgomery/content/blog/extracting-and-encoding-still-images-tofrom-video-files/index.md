---
date: '2008-08-11T09:05:00+00:00'
title: Extracting and Encoding Still images to/from Video files
draft: false
tags:
- Apps
- Video
slug: extracting-and-encoding-still-images-tofrom-video-files
description: ''
markup: md
url: /blog/extracting-and-encoding-still-images-tofrom-video-files/
aliases:
- /blog/2008/08/11/extracting-and-encoding-still-images-tofrom-video-files/

---

[ffmpeg](http://ffmpeg.mplayerhq.hu) is a cool tool.  
  
While it's got many many features and uses, I mostly use it to extract frames (or still images) from a video and create a video out of frames. While [instructions on how to do this](http://ffmpeg.mplayerhq.hu/faq.html#SEC14) are posted on their list of FAQs, it's probably worth posting again.  
  
To extract all frames from a video file named "video.mpg": 
```
ffmpeg -i video.mpg frame%d.jpg
```
This will produce a series of JPEG image files named file1.jpg, file2.jpg... file10.jpg, file11.jpg... etc.  
  
I often like to have a zero prepended to the number associated with a frame. For exaple, if I knew there were 500 frames in the entire video, I would like to have the first frame named "file001.jpg" instead of "file1.jpg". This can be achieved by specifying the number of digits to use in the output file name (such as 3 in the example below):
```
ffmpeg -i video.mpg frame%3d.jpg
```
Now, to create a video named "movie.mpg" from a series of images named something like "frameX.jpg" (where X is the frame number), you could do something like this:
```
ffmpeg -f image2 -i frame%d.jpg movie.mpg
```
The caveat here is that the input frames MUST be numbered as if they were extracted from the video. So, if you had zero-padded filenames (as in the case where we used "frame%3d.jpg" to extract images), you'd have to account for that when encoding those images back into a movie.  
  
For example: 
```
ffmpeg -f image2 -i frame%3d.jpg movie.mpg
```
  
  
A Note on image formats: In the example above where we created a video file from a set of still images, the "-f image2" option to ffmpeg specifies a video format. Available formats can be displayed using the command 
```
ffmpeg -formats
```
 Note that this is not the same as a [container format](http://en.wikipedia.org/wiki/Container_format_(digital)) (such as .mpg, .avi, .mov... etc). If this sounds a little confusing, you may want to read up on [digital video encoding](http://en.wikipedia.org/wiki/Digital_video#Encoding).![](https://blogger.googleusercontent.com/tracker/4123748873183487963-8162317062922827536?l=bradmontgomery.blogspot.com)