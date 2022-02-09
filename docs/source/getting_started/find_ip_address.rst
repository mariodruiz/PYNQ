.. _find-the-ip-address:

*****************************
Find IP address of your board
*****************************

.. note:: 
   This section assumes you have connected your board to a network with a 
   DHCP server - e.g. your home network where your router is the DHCP server. 
   Your board will be assigned a dynamic IP address which means it can change
   over time or if you reset your router or your board. In practice most routers
   Will assign the same IP address to the same device, the IP address may change
   and you will need to follow these steps again to find the new IP address for 
   your board.  


You can find the IP address in several ways. 

Ping
====

The default hostname of a board is `pynq`. Your network may support hostname 
resolution. This means that if you try to connect to the hostname of your board,
the hostname will used to lookup the IP address to the board. 

From a command prompt or terminal on your host PC run:

.. code-block:: console

   ping pynq 

This may automatically resolve the hostname to the IP address, and you can return 
to previous section to connect to your board. 

Serial terminal
===============

This is a good way to get the IP address of your board and general troubleshooting.
Follow the instructions if you need help :ref:`opening-a-serial-terminal`.

* Connect a USB cable and open a serial terminal to the board
* Run the following to report information about the board's network adapters

.. code-block:: console

   ip a

This will return info similar to the output below:

.. code-block:: console
   :emphasize-lines: 11,21

   1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
      link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
      inet 127.0.0.1/8 scope host lo
         valid_lft forever preferred_lft forever
      inet6 ::1/128 scope host
         valid_lft forever preferred_lft forever
   2: dummy0: <BROADCAST,NOARP> mtu 1500 qdisc noop state DOWN group default qlen 1000
      link/ether 1a:ee:e0:5e:27:89 brd ff:ff:ff:ff:ff:ff
   3: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
      link/ether 00:05:6b:01:c6:66 brd ff:ff:ff:ff:ff:ff
      inet 192.168.68.136/24 brd 192.168.68.255 scope global dynamic eth0
         valid_lft 7146sec preferred_lft 7146sec
      inet 192.168.2.99/24 brd 192.168.2.255 scope global eth0:1
         valid_lft forever preferred_lft forever
      inet6 fe80::205:6bff:fe01:c666/64 scope link
         valid_lft forever preferred_lft forever
   4: sit0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN group default qlen 1000
      link/sit 0.0.0.0 brd 0.0.0.0
   5: wlan0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast state DOWN group default qlen 1000
      link/ether d4:7b:b0:08:36:d2 brd ff:ff:ff:ff:ff:ff
      inet 192.168.68.145/24 brd 192.168.68.255 scope global dynamic wlan0
         valid_lft 7025sec preferred_lft 7025sec
 
Check your router
=================

You can usually find details of all devices on your network, including the IP address
that has been assigned to each device. 
Check the manual for your router or look for log-in details on a sticker on your router.
 
Scan your network
=================

Apps are available for smart phones and PCs that allow them to scan WiFi networks 
and identify devices connected to the network. This can be a convenient way to find 
the IP address of your board. 

Search your App Store for "network scanner" or similar to find a suitable App. 
`Fing <https://www.fing.com/>`_ which is available for Windows, Apple and 
Android is one example. 