.. _pynq-z1-setup:

*******************
PYNQ-Z1 Setup Guide
*******************
     
Prerequisites
=============

  * PYNQ-Z1 board
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

1. Connect the board to your local WiFi network
2. Wired connection from your board to your network
3. Direct Ethernet connection from your board to your PC 

For the best experience with PYNQ, you should connect your board to a 
network with internet access (usually options 1 & 2). 
This will allow you to update your board and easily install new packages 
including PYNQ Overlays. 

For WiFi (option 1) you need a supported :ref:`usb-wifi-device` and to follow the
steps to :ref:`configure WiFi on your 
PYNQ image<configure-wifi-on-your-pynq-image>` before you setup your board. 

For option 2 or 3, connect your board to your computer's Ethernet port or to 
your wired network with an Ethernet cable.


Getting Started Video
=====================

You can watch the getting started video guide, or follow the instructions in
:ref:`pynqz1-board-setup`.

.. raw:: html

    <embed>
         <iframe width="560" height="315" src="https://www.youtube.com/embed/SuXkbcK3w9E" frameborder="0" allowfullscreen></iframe>
         </br>
         </br>
    </embed>
   
.. _pynqz1-board-setup:

Board Setup
===========

   .. image:: ../images/pynqz1_setup.jpg
      :align: center

  1. Set the **JP4 / Boot** jumper to the *SD* position by
     placing the jumper over the top two pins of JP4 as shown in the image.
     (This sets the board to boot from the Micro-SD card)
   
  2. To power the PYNQ-Z1 from the micro USB cable, set the **JP5 / Power**
     jumper to the *USB* position. (You can also power the board from an external 12V
     power regulator by setting the jumper to *REG*.)

  3. Insert the Micro SD card loaded with the PYNQ-Z1 image into the **Micro
     SD** card slot underneath the board.

  4. Connect the USB cable to your PC/Laptop, and to the **PROG - UART / J14**
     MicroUSB port on the board

  5. Connect your USB Wifi Dongle or Ethernet cable by following 
     the instructions below

  6. Turn the power switch to the *ON* position and check the boot sequence
     In the instructions below. 

.. _turning-on-the-PYNQ-Z1:

Turning On the PYNQ-Z1
----------------------

When you turn on the board the **Red LD13** LED will come on immediately to
confirm that the board has power.  After about a minute, the **Yellow/Green LD12
/Done** LED will light up to show that the Zynq® device is operational.

You should see the two **Blue LD4 & LD5** LEDs and four
**Yellow/Green LD0-LD3** LEDs flash simultaneously. The **Blue LD4-LD5** LEDs
will then turn on and off while the **Yellow/Green LD0-LD3** LEDs remain on. The
system is now booted and ready for use.

Connect to your board
=====================

If you have not already done so, follow one of the steps below to setup your 
network connection to your board:
 
* :ref:`configure-wifi-on-your-pynq-image`
* :ref:`ethernet-configuration`

When your network connection is setup, continue to :ref:`connecting-to-jupyter-notebook`.
