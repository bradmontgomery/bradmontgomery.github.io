---
date: '2014-03-21T20:16:55.011764+00:00'
title: Your VM has become "inaccessible."
draft: false
tags:
- vagrant
- virtualbox
slug: your-vm-has-become-inaccessible
description: ''
url: /blog/your-vm-has-become-inaccessible/
aliases:
- /blog/2014/03/21/your-vm-has-become-inaccessible/

---

Today I ran out of disk space on my Macbook Air. I mean, *completely* out of
space. I use vagrant and
Virtualbox for work, and I knew that had
several large, but older snapshots of virtual machines that I could remove to
free up space.

And that's how today fell apart.

I also use the vagrant-vbox-snapshot
plugin, and that's the tool I typically use to take snapshots when I need them.

So, looking into my project folder, I run the following:

    $ vagrant snapshot list

    Name: 2013-11-05 (UUID: ... )
    Name: 2014-01-26 (UUID: ... )
    Name: 2014-02-07 (UUID: ... )
    Name: 2014-02-22 (UUID: ... )

I tend to name my snapshots after the date on which I take them. Each of these
is around 8Gb in size, so I decide to delete the oldest one.

    $ vagrant snapshot delete 2013-11-05

Unfortunately, whenever you remove a snapshot, VirtualBox decides to write some
data to disk. Think about that for a second.

*You can't remove a snapshot if your disk is full!*

This command attempted to remove a snapshot, then after a minute failed with
a scary message (which I forgot to copy, and have since lost). And because the
VM is hosed, vagrant will offer the following complaint:


> Your VM has become "inaccessible." Unfortunately, this is a critical error
> with VirtualBox that Vagrant can not cleanly recover from. Please open
> VirtualBox and clear out your inaccessible virtual machines or find a way
> to fix them.

And if you run vagrant status, you'll see something like this

    Current machine states:

    my\_vm inaccessible (virtualbox)

So, I did what Vagrant told me, and opened up VirtualBox. Well, the GUI tools
listed *my\_vm*, but also had a label next to it that said, *inaccessible*, and
as far as I could, there were no enabled options that would let me do anything.

Needless to say, I was ready to freak out a little.

All is not lost, however. You see, there's a directoy where VirtualBox stores
it's machine images and it's config data. For me, that's in ~/VirtualBox VMs/.

Inside that directory, vagrant should create a directory for each of it's
vms. So, I had some data at ~/VirtualBox VMs/someproject\_myvm\_1234567890.
The contents fo this folder look something like:

     .
     ├── Logs/
     ├── Snapshots/
     ├── box-disk1.vmdk
     ├── myproject\_myvm\_1234567890.vbox
     └── myproject\_myvm\_1234567890.vbox-pre

That file with the .vbox-pre is an automatically generated backup of the
VirtualBox config file, prior to it saving a VM. So, here's what I did:

Replace the .vbox config with the .vbox-pre config:


    cat myproject\_myvm\_1234567890.vbox-pre > myproject\_myvm\_1234567890.vbox

After that, my both VirtualBox and vagrant appeared to work with my VMs.

Crisis averted, and with only a couple hours lost.
