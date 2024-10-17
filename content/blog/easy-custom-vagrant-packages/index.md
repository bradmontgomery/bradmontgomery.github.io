---
date: '2012-04-16T18:44:44+00:00'
title: Easy Custom Vagrant Packages
draft: false
tags:
- chef
- linux
- vagrant
- virtualbox
slug: easy-custom-vagrant-packages
description: ''
markup: md
url: /blog/easy-custom-vagrant-packages/
aliases:
- /blog/2012/04/16/easy-custom-vagrant-packages/

---

I've been using Vagrant quite a bit lately, and one of the nice things you can do with it is to define your own package. This makes it easy to share your VMs with others. It's also nice to have the same stuff installed on every VM that you create! So, here's how you create a package.


To do this, you'll need to Install VirtualBox and Vagrant. (At the time of writing, I'm using [VirtualBox 4.0.16](https://www.virtualbox.org/wiki/Download_Old_Builds) and [Vagrant 1.0.2](http://vagrantup.com/))


Once you have those installed, we can get started. I'm using Ubuntu Lucid (10.04, 64-bit), but you could pick your own linux flavor. Look over the list at <http://vagrantbox.es/>. First, set up a default box:



```
$ vagrant box add lucid64 http://files.vagrantup.com/lucid64.box

```

That may take a while to download the image. Once it complets, you can see a list of your boxes:



```
$ vagrant box list

```

You should see one named lucid64 (unless you picked a differenc flavor). Now, intialize a Vagrant configuration:



```
$ vagrant init

```

Check out the created Vagrant file. I've stripped mine down to the following:



```
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::Config.run do |config|
  config.vm.box = "lucid64"
  config.vm.network :hostonly, "192.168.111.111"
end

```

Make sure the IP address for your VM doesn't conflict with any other networks on which your host machine may be connected.


Create a virtual machine based on the default lucid64 box:



```
$ vagrant up

```

It'll take a just a little bit of time for the VM to boot, and you'll probably see something like this:



```
$ vagrant up
[default] VM already created. Booting if it's not already running...
[default] Clearing any previously set forwarded ports...
[default] Forwarding ports...
[default] -- 22 => 2222 (adapter 1)
[default] Creating shared folders metadata...
[default] Clearing any previously set network interfaces...
[default] Preparing network interfaces based on configuration...
[default] Booting VM...
[default] Waiting for VM to boot. This can take a few minutes.
[default] VM booted and ready for use!
[default] Configuring and enabling network interfaces...
[default] Mounting shared folders...
[default] -- v-root: /vagrant

```

So, now we want to log into the VM and update it. Run each of the following commands:



```
$ vagrant ssh
$ sudo apt-get update
$ sudo apt-get upgrade -y
$ exit

```

Now, run the following commands to reload vagrant (rebooting the VM) and install the Virtual Box Guest Additions:



```
$ vagrant reload
$ vagrant ssh
$ sudo apt-get install build-essential module-assistant linux-headers-$(uname -r) dkms -y
$ wget -c http://download.virtualbox.org/virtualbox/4.0.16/VBoxGuestAdditions_4.0.16.iso
$ sudo mount VBoxGuestAdditions_4.0.16.iso -o loop /mnt
$ sudo sh /mnt/VBoxLinuxAdditions.run --nox11
$ exit

```

Reload the VM just to make sure all the new kernal modules are used:



```
$ vagrant reload

```

At this point, you could install any other softward that you want available on all of your virtual machines. For example, I installed curl, git, htop, nmap, and I installed and configured Chef so all of my VMs can easily connect to our Chef server and register themselves. So, install your favorite tools:



```
$ sudo aptitude install curl git-core htop nmap -y

```

Now, create a package that you can use as a base box or distribute to others:



```
$ vagrant package

```

You should now have a package.box file, which you can use as a base box for future VMs. To use this as your base box, run:



```
$ vagrant box add base package.box

```

Now, when you run vagrant up, your VM will be created from the box you just created!

