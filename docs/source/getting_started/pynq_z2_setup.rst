.. _pynq-z2-setup:

*******************
PYNQ-Z2 Setup Guide
*******************
     
Prerequisites
=============

  * PYNQ-Z2 board
  * Computer with compatible browser (`Supported Browsers
    <http://jupyter-notebook.readthedocs.org/en/latest/notebook.html#browser-compatibility>`_)
  * USB WiFi dongle or Ethernet cable 
  * Micro USB cable 
  * Micro-SD card with preloaded image, or blank card (Minimum 8GB recommended)

.. NOTE:: 
    If you do not have a Mirco-SD card with a preloaded image, follow :ref:`writing-the-sd-card` 
    instructions. 

Network connection
==================

You will connect to your board using a network connection. There are three main 
options:

1. WiFi connect to your WiFi network
2. Wired connection to your network
3. Direct Ethernet connection from your board to your PC (no internet)

For the best experience with PYNQ, you should connect your board to a 
network with internet access (options 1 & 2). 
This will allow you to update your board and easily install new packages 
including PYNQ Overlays. 

For WiFi (option 1) you need a supported :ref:`usb-wifi-device`. If you 
want to connect to WiFi follow the steps to 
:ref:`configure-wifi-on-your-pynq-image` before you setup your board. 

For option 2 or 3, connect your board to your computer's Ethernet port or to 
your wired network with an Ethernet cable.


Getting Started Video
=====================

You can watch the getting started video guide, or follow the instructions in
:ref:`pynqz2-board-setup`.

.. raw:: html

    <embed>
         <iframe width="560" height="315" src="https://www.youtube.com/embed/RiFbRf6gaK4" frameborder="0" allowfullscreen></iframe>
         </br>
         </br>
    </embed>

.. _pynqz2-board-setup:

Board Setup
===========

   .. image:: ../images/pynqz2_setup.png
      :align: center

  1. Set the **Boot** jumper to the *SD* position.
     (This sets the board to boot from the Micro-SD card)
   
  2. To power the board from the micro USB cable, set the **Power**
     jumper to the *USB* position. (You can also power the board from an 
     external 12V power regulator by setting the jumper to *REG*.)

  3. Insert the Micro SD card loaded with the PYNQ-Z2 image into the **Micro
     SD** card slot underneath the board

  4. Connect the USB cable to your PC/Laptop, and to the **PROG - UART**
     MicroUSB port on the board

  5. Connect your USB Wifi Dongle, or Ethernet cable by following the 
     instructions below

  6. Turn the power switch to the *ON* position and check the boot sequence
     In the instructions below. 

.. _turning-on-the-PYNQ-Z2:

Turning On the PYNQ-Z2
----------------------

When you turn on the board, the **Red** LED will come on immediately to
confirm that the board has power.  After about a minute, the **Yellow/Green
/Done** LED will light up to show that the Zynq® device is operational.

You should see two **Blue** LEDs and four
**Yellow/Green** LEDs flash simultaneously. The **Blue** LEDs
will then turn on and off while the **Yellow/Green** LEDs remain on. The
system is now booted and ready for use.
  
Connect to your board
=====================

If you have not already done so, follow one of the steps below to setup your 
network connection to your board:
 
* :ref:`configure-wifi-on-your-pynq-image`
* :ref:`ethernet-configuration`

When your network connection is setup, conotinue to :ref:`connecting-to-jupyter-notebook`.
