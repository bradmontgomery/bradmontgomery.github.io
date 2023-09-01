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
description: <p>I've been using V...
markup: html
url: /blog/easy-custom-vagrant-packages/
aliases:
- /blog/2012/04/16/easy-custom-vagrant-packages/

---

<p>I've been using Vagrant quite a bit lately, and one of the nice things you can do with it is to define your own package. This makes it easy to share your VMs with others. It's also nice to have the same stuff installed on every VM that you create! So, here's how you create a package.</p>
<p>To do this, you'll need to Install VirtualBox and Vagrant. (At the time of writing, I'm using <a class="reference external" href="https://www.virtualbox.org/wiki/Download_Old_Builds" _mce_href="https://www.virtualbox.org/wiki/Download_Old_Builds">VirtualBox 4.0.16</a> and <a class="reference external" href="http://vagrantup.com/" _mce_href="http://vagrantup.com/">Vagrant 1.0.2</a>)</p>
<p>Once you have those installed, we can get started. I'm using Ubuntu Lucid (10.04, 64-bit), but you could pick your own linux flavor. Look over the list at <a class="reference external" href="http://vagrantbox.es/" _mce_href="http://vagrantbox.es/">http://vagrantbox.es/</a>. First, set up a default box:</p>
<pre>$ vagrant box add lucid64 http://files.vagrantup.com/lucid64.box
</pre>
<p>That may take a while to download the image. Once it complets, you can see a list of your boxes:</p>
<pre>$ vagrant box list
</pre>
<p>You should see one named <tt class="docutils literal">lucid64</tt> (unless you picked a differenc flavor). Now, intialize a Vagrant configuration:</p>
<pre>$ vagrant init
</pre>
<p>Check out the created <tt class="docutils literal">Vagrant</tt> file. I've stripped mine down to the following:</p>
<pre><code class="ruby"># -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::Config.run do |config|
  config.vm.box = "lucid64"
  config.vm.network :hostonly, "192.168.111.111"
end
</code></pre>
<p>Make sure the IP address for your VM doesn't conflict with any other networks on which your host machine may be connected.</p>
<p>Create a virtual machine based on the default lucid64 box:</p>
<pre>$ vagrant up
</pre>
<p>It'll take a just a little bit of time for the VM to boot, and you'll probably see something like this:</p>
<pre>$ vagrant up
[default] VM already created. Booting if it's not already running...
[default] Clearing any previously set forwarded ports...
[default] Forwarding ports...
[default] -- 22 =&gt; 2222 (adapter 1)
[default] Creating shared folders metadata...
[default] Clearing any previously set network interfaces...
[default] Preparing network interfaces based on configuration...
[default] Booting VM...
[default] Waiting for VM to boot. This can take a few minutes.
[default] VM booted and ready for use!
[default] Configuring and enabling network interfaces...
[default] Mounting shared folders...
[default] -- v-root: /vagrant
</pre>
<p>So, now we want to log into the VM and update it. Run each of the following commands:</p>
<pre>$ vagrant ssh
$ sudo apt-get update
$ sudo apt-get upgrade -y
$ exit
</pre>
<p>Now, run the following commands to reload vagrant (rebooting the VM) and install the Virtual Box Guest Additions:</p>
<pre>$ vagrant reload
$ vagrant ssh
$ sudo apt-get install build-essential module-assistant linux-headers-$(uname -r) dkms -y
$ wget -c http://download.virtualbox.org/virtualbox/4.0.16/VBoxGuestAdditions_4.0.16.iso
$ sudo mount VBoxGuestAdditions_4.0.16.iso -o loop /mnt
$ sudo sh /mnt/VBoxLinuxAdditions.run --nox11
$ exit
</pre>
<p>Reload the VM just to make sure all the new kernal modules are used:</p>
<pre>$ vagrant reload
</pre>
<p>At this point, you could install any other softward that you want available on all of your virtual machines. For example, I installed curl, git, htop, nmap, and I installed and configured Chef so all of my VMs can easily connect to our Chef server and register themselves. So, install your favorite tools:</p>
<pre>$ sudo aptitude install curl git-core htop nmap -y
</pre>
<p>Now, create a package that you can use as a base box or distribute to others:</p>
<pre>$ vagrant package
</pre>
<p>You should now have a <tt class="docutils literal">package.box</tt> file, which you can use as a base box for future VMs. To use this as your <tt class="docutils literal">base</tt> box, run:</p>
<pre>$ vagrant box add base package.box
</pre>
<p>Now, when you run <tt class="docutils literal">vagrant up</tt>, your VM will be created from the box you just created!</p>