.. _ethernet-configuration:

**********************
Ethernet Configuration
**********************

Connect to a Network
====================

If you connect to a network (e.g. your home router, or other network), 
your board will automatically be assigned an IP address. 
If you are using a school or work network should make sure you have permission 
to connect your board the network.

* Connect your board to a port on a router/switch with an Ethernet cable

Your board will be assigned a dynamic IP address. You need to find the 
address (manually or automatically) to connect to your board.

Your network may support hostname resolution. This allows you to use the 
hostname of the board and your network will resolve this to the IP of the board.  

* In your web browser, try browse to the hostname of the board `http://pynq`. 

If this doesn't work, you need to follow the instructions to
:ref:`find-the-ip-address` of the board. Once you find the IP address, you can 
Proceed to the next step :ref:`connecting-to-jupyter-notebook`
  
* Optional: you should :ref:`change-the-hostname` of the board if you think there 
  may be more than one PYNQ board on your network
* Optional: see *Configure Proxy Settings* below if you need to configure a proxy. 


Direct Ethernet connection to your computer
===========================================

The last option is to connect your board directly to your computer. You need to 
have a spare Ethernet port on your computer, and permissions to configure your 
network interface to assign a static IP address to your computer. See the steps
below. 
 
You can use an Ethernet cable to connect your board to your computer. 
If your computer doesn't have an Ethernet port, you can also use a 
USB-to-Ethernet adapter.
With a direct connection, you will be able to use PYNQ, but unless you can 
bridge the Ethernet connection to the board to an Internet connection on your 
computer, your board will not have Internet access. 
You will be unable to update or load new packages without Internet access or
copying files to your board in some other way. 

Connect directly to a computer (Static IP):

  1. :ref:`assign-a-static-ip-address`
  2. Connect the board to your computer's Ethernet port
  3. The board IP address is: 192.168.2.99 (the default static IP address 
     for the board)

Continue to :ref:`connecting-to-jupyter-notebook`.