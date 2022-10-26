Title: Home IP Camera setup with a Mac (or just an iPhone)
Date: 2012-03-10 10:09
Author: Doug
Category: Tech
Tags: DHCP, iPad, IPCamera, iPhone, Mac, Port Mapping, Router
Slug: home-ip-camera-setup-with-a-mac-or-just-an-iphone
Status: published

I just purchased a new wireless IP camera from Amazon and it works great. I didn't use any of the software that came with the camera and I did it all with my Macbook or I could have done it all with my iPhone or iPad.

# IP Cameras

I've been looking at cameras for a long time. Mainly, so I can see who is at the front door. It would be nice if I could be notified every time someone came to the door or even just dropped a package off. I looked at wired cameras but they all involve me getting into the attic, not something I like to do anymore. Based on the very helpful reviews on Amazon I took the plunge and bought a [Wireless IP Camera Pan/Tilt](http://www.amazon.com/gp/product/B003LNZ1L6/ref=oh_o01_s00_i00_details "Wireless IP Camera Pan/Tilt"){target="_blank"}. It was very inexpensive at \$58.03 and free shipping with Amazon Prime.

So what did I get? Well... a little confused at first. Come to find out there are numerous cameras all sold under different names, like: HooToo, Apexis, FosCam, EasyN, Wansview, and LofTek. From what I can tell these are all basically made by the same company and work the same way. The camera I ordered was Wansview, the camera that I received was HooToo. The pictures look identical.

\[caption id="attachment_174" align="alignleft" width="300"\][![](http://robotcraft.org/wp-content/uploads/2012/02/41OzFZqMirL._SL500_AA300_.jpg "HooToo Internet Camera"){.size-full .wp-image-174 width="300" height="300"}](http://robotcraft.org/wp-content/uploads/2012/02/41OzFZqMirL._SL500_AA300_.jpg) HooToo Internet Camera\[/caption\]

This is a pretty neat piece of equipment. No it is not Apple quality, and no it is not especially easy to set up and configure. However, they have gone out of their way to make it doable and they do NOT require a Windows-based PC.

Of course it comes with a camera. Not a great one, but fine for the price. It also comes with Pan/Tilt built-in. It works very well. The infrared LEDs work and come on automatically when it starts getting dark. They will light up your 25' hallway just fine in pitch black conditions. A built-in mic is nice so you can hear what is going on, a CAT-5 cable for a physical connection to your network, a Wifi connection and a power adapter. Yes, you have to plug it into power wherever you are going to put it.

It has a built-in web server that provides all the features of the camera to your Mac or iPad. You really just connect to it with Safari and you are good to go. Very nice.

The IP in IP Camera means that it communicates over TCP/IP not through USB or FireWire. This camera does not connect directly to your Mac, it connects to your network and then is available to any other device on your network, wither Mac, PC, iPhone, iPad, etc.

# Network Environment

I have a pretty standard all Apple network environment. I have a 13" MacBook Air running Lion, an Airport Extreme base station with wired and wireless devices connected to it, and an iPhone and iPad connected wirelessly. All standard equipment.

The IP camera works in this environment just fine, it is just another device on the network. It can connect through a CAT-5 cable physically or wirelessly through Wifi. Either way works exactly the same as far as the user is concerned.

The hardest part is understanding what it means to connect to the local network, and not just to the Mac.

# Routers

A router helps route IP traffic around your home, but more importantly through your cable/dsl modem to your Internet Service Provider (ISP) and on to the internet.

The Airport Extreme is very easy to set up and manage. It pretty much defaults to just what you want out of the box. I won't go into all the details because it is probably already working for you if you are reading this page.

## DHCP

This is the technology that is built into your router that lets you have one IP address from your ISP but have lots of different devices in your home that have their own unique local IP address. This is a bit confusing, but it works. Anytime you add a new device to your local network (either wired or wireless) it is automatically assigned a unique local IP address by the router, usually in the range of 192.168.0.1 to 192.168.0.255. These are known to the industry as non-routing IP addresses. This means they do not get routed outside of your, um, router. They are only visible to other devices on your local network. This is a good thing, it helps protect them from outside intruders. What they can't see they can't attack very easily.

The point of all this is that you have one external IP address assigned to you by your Internet Service Provider (ISP). Your Airport Extreme router then uses DHCP to assign unique local IP address to all the devices connected in your house. When you connect your camera it is assigned a unique IP address.

By the way your external IP address is probably (unless you pay extra) assigned to your house by using DHCP and it may change at anytime. Read later about DDNS to get around this so you can access your camera from your iPhone/iPad or other device when you are not at home.

# Setup Software

The first thing I wanted to do was to get the camera connected to my home wireless network. There are a couple of ways to do this. However, I found it very easy to just turn it on... hmmm... really I connected it to the CAT-5 wired network first, found its IP address using one of the following apps then accessed its built-in web server using Safari on my Mac, by entering the IP address in the Url field (Ex. 192.168.0.182).  I worked through the setup webpage and found the wireless network, added the security password (known as Share key on their built-in server) for my wireless network then connected it to the wireless network by unplugging the CAT-5 network cable. Whew, not really hard but there are a lot of steps.

[IP Scanner (Free)](http://itunes.apple.com/us/app/ip-scanner/id404167149?mt=12 "IP Scanner (Free)"){target="_blank"} in the Mac App store, and [IP Scanner Home](http://itunes.apple.com/us/app/ip-scanner-home/id422293948?mt=12 "IP Scanner Home"){target="_blank"} in the Mac App store. One of these apps, is very useful for finding your camera the first time it is connected to your wired or wireless network. They show the assigned IP address and hardware address (sometimes called the MAC address) of every device on your network. I tried the free version at first but it was limited to only showing the first 5 devices it found. The new camera did not show up, so I purchased the app and it displayed all the devices on my network. Very helpful indeed!

[IP Network Scanner Lite](http://itunes.apple.com/us/app/ip-network-scanner-lite/id335517828?mt=8 "IP Network Scanner Lite"){target="_blank"} in the iOS App store. If you are going for the no Mac option and prefer to use your iPhone or iPad then this app is by the same company. I tried the free version and it worked very well. However, it is limited to only showing the first 5  devices on your network. If you have more than that then you will have to purchase the full version. At \$9.99 it is more than the Mac version.

This type of software may be more convenient now that Apple has removed the device list from version 6.x of their Aiport Utility software. Well, it does show the connected wireless devices, but only the first 6. You might get lucky, or have less than this connected. I was surprised how many devices are on wireless these days.

So there you are. You have now connected a new wireless IP Pan/Tilt camera to your wireless network and never installed any of the software that came with it. You either did it on your Mac or your iPhone/iPad. So far you have only used one extra app to find the IP address and then used the standard Safari browser to access the cameras built-in web server.

But there is more. You don't want to have to lookup the IP address of the camera every time you want to use it. Your wireless Airport Extreme (router) may assign it a new IP address at any time. You really want to set it to a known location so that you can find it from anywhere.

# DHCP Reservations

There are two basic ways to make sure a device always has the same IP address. You can do everything manually or you can use the Airport Utility to make a DHCP reservation.

The new Airport software makes this really easy. Just edit your base station, click on the Network tab and then click the plus sign under the DHCP Reservations section.

Give it a good description like "IP Camera" or "IP Camera Front Door", select Reserve address by "MAC Address" (this is the hardware address assigned to all devices). Type in the MAC address of your camera or use copy/paste from on the apps above.  Then type in the permanent IPv4 address that you want. Make sure no other device on your network is assigned this same address. When you click Save you will now always know the local address of your IP camera. Well, ok click Update to make the changes to your router.

Mine is 192.168.0.82 and I can type this into any browser and access the built-in webpage on the camera. It will never change. Very cool!

## Port Mapping

See what I did there. I said "local address". That means any device connected to your local network can see your camera at the reserved IP address. But, what if you leave your local network and want access? Your router can help you here too. It is called Port Mapping, it allows an external device to navigate through your router to the specific device you want.

What is a port? If you think of the IP address your house is assigned by your ISP as your street address, then the port is like which door to use. Everything has standard ports, web sites, email, Skype, Minecraft, they all have different ports be default. As long as you don't interfere with another port on your network then you can use anything you want. Well it has to be above port number 1024, but that is a long story.

I chose port 25000 for my front door camera. It is unused on my network and it is a nice easy number to remember. The new Apple Airport Utility makes this very easy to set up. Start the utility again on your Mac or iPhone/iPad. Select your Airport base station and then select Network. Check the check-box to Enable NAT Port Mapping Protocol. Next click the plus sign to add a new Port Mapping.

Give it a good description like "IP Camera", or "Front Door Camera". Enter 25000 for the Public TCP port, enter your reserved IP address for your camera Ex. 192.168.0.182, then enter 80 as the Private TCP Ports. This is the default port for the webpage on your IP camera. Click Save. Click update to make changes to the router.

\* My Airport Utility seems to have a bug, it would not let me click save until I entered a Public UDP port as well. I put in 25000 and it worked.

There you have it. You can now type in your ISP assigned external IP address and append  :25000 and you will see the webpage from your camera.

So you are asking how you find your external IP address assigned by your ISP? Airport Utility to the rescue. Just click the world map icon at the top labeled Internet and a pop-up bubble shows the router address. Something like: 71.81.163.5. You would type in 71.81.163.5:25000 into your browser to access your camera.

Remember you just made a hole in your network security to allow anyone from the outside to see your camera. This means they now have at least a little access to your home network. Be careful what port mappings you create, every new one provides more access, and more chance for security problems.

Wow, you have now reserved a specific IP address for your camera and mapped a port through your router so that you can access it from anywhere in the world by just typing that address and port into a browser window. Powerful!

So, what happens when you get a new IP address assigned by your ISP? That's right you have to start Airport utility all the time to see your external IP router address. Not very convenient if you are not at home and want to connect to your network. See the next section on setting up a DDNS to give you a permanent address that you can always find, anywhere in the world, at anytime.

## DDNS

Remember above when I said your ISP probably issues your house a dynamic IP address and that it could change at any time. Yep, that's right. Any time. It probably changes every few months.

I will have to continue this in the next article in this series. Stay tuned, more to come.

# Viewing Software

[IP Cam Viewer Pro](http://itunes.apple.com/us/app/ip-cam-viewer-pro/id402656416?mt=8 "IP Cam Viewer Pro"){target="_blank"} in the iOS App store.

[EvoCam](http://www.evological.com/evocam.html "EvoCam for the Mac"){target="_blank"} for the Mac.

Safari Browser

 
