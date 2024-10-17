---
date: '2017-02-01T22:46:52.151549+00:00'
title: Sending SMS messages with Amazon SNS and Python
draft: false
tags:
- aws
- python
- sms
- sns
- texting
slug: sending-sms-messages-amazon-sns-and-python
description: ''
markup: md
url: /blog/sending-sms-messages-amazon-sns-and-python/
aliases:
- /blog/2017/02/01/sending-sms-messages-amazon-sns-and-python/

---

There are many services out there that will let you programmatically send
SMS messages. One of the more popular is [Twilio](https://www.twilio.com),
and they have a great API and a python client that's easy to use. There's
an interesting [quora thread](https://www.quora.com/How-do-I-send-text-messages-from-a-python-script-to-a-mobile-number-if-possible-with-a-free-gateway)
with several other suggestions as well.

Another option is to use Amazon's [Simple Notification Service](https://aws.amazon.com/sns/) (SNS), which also supports sending SMS messages. I recently
incorporated this into a project, and thought I'd share.

## Step 1: API key + boto3

If you're already using AWS, you've probably jumped through these hoops. I'm
not going to walk you through them, but just realize you need to figure out how
to sign up for an AWS account and get some api keys.

The second part of this is [boto3](https://aws.amazon.com/sdk-for-python/),
amazon's python sdk.

 pip install boto3

Boto's [quickstart guide](https://boto3.readthedocs.io/en/latest/guide/quickstart.html) should help, and it also includes some info on getting boto configured.

## Step 2: Send your message


At the bare minimum, you can just send a message directly to a single phone
number. Here's the code:

 import boto3

 # Create an SNS client
 client = boto3.client(
 "sns",
 aws\_access\_key\_id="YOUR ACCES KEY",
 aws\_secret\_access\_key="YOUR SECRET KEY",
 region\_name="us-east-1"
 )

 # Send your sms message.
 client.publish(
 PhoneNumber="+12223334444",
 Message="Hello World!"
 )

Note the formate of the phone number. It's got to be in something called
[E.164 format](https://en.wikipedia.org/wiki/E.164). For US phone numbers,
this includes the `+1` country code, then the area code + the rest of the phone
number without any additional formatting.

If you just need to send a message every once in a while (e.g. to notifiy yourself
when something happens), then congrats! You're done.

## Step 3: Do actual Pub-Sub

If you need to send messages to multiple recipients, it's worthwhile to read
though Amazon's docs on [sending to multiple phone numbers](http://docs.aws.amazon.com/sns/latest/dg/sms\_publish-to-topic.html).

The SNS service implements the [Publish-Subscribe](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe\_pattern) pattern, and you can use it to send messages to a \_topic\_. Here are the steps to make this work:

1. Create a named topic. This is just a commuication channel to which you can
 \_subscribe\_ phone numbers.
2. Subscibe your recipients to the topic.
3. Publish a message on the topic.

The python code looks something like this:


 import boto3

 # Create an SNS client
 client = boto3.client(
 "sns",
 aws\_access\_key\_id="YOUR ACCES KEY",
 aws\_secret\_access\_key="YOUR SECRET KEY",
 region\_name=us-east-1
 )

 # Create the topic if it doesn't exist (this is idempotent)
 topic = client.create\_topic(Name="notifications")
 topic\_arn = topic['TopicArn'] # get its Amazon Resource Name

 # Add SMS Subscribers
 for number in some\_list\_of\_contacts:
 client.subscribe(
 TopicArn=topic\_arn,
 Protocol='sms',
 Endpoint=number # <-- number who'll receive an SMS message.
 )

 # Publish a message.
 client.publish(Message="Good news everyone!", TopicArn=topic\_arn)

All your susbscibers should recieve an SMS message once you've
published it on the topic. In addition, you should be able to monitor SNS
usage on the [AWS console](https://console.aws.amazon.com/), which will tell
you how many messages are sent (as well as how many sms mesages fail). If you
plan to use SNS for any commercial usage, you'll also want to read up on
[SNS Pricing](https://aws.amazon.com/sns/pricing/).

That's it! Hope this article has helped. Let me know in the comments below :)