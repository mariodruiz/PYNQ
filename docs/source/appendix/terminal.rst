.. _opening-a-serial-terminal:

*****************************
Opening a USB Serial Terminal
*****************************

.. NOTE::
    Jupyter has a built-in terminal that you can access through your browser inside
    the Jupyter environment. We recommend you use this terminal. If you can't access
    The Jupyter terminal, you can open a terminal using a USB cable to your board. 

If you need to access a terminal, you can connect the micro-USB
cable from your computer to the board and open a terminal. You can use the
terminal to check the network connection of the board. You will need to have
terminal emulator software installed on your computer. `PuTTY
<http://www.putty.org/>`_ is one application that can be used, and is available
for free on Windows. To open a terminal, you will need to know the COM port for
the board.

Windows
=======

On Windows, you can find this in the Windows *Device Manager* in the control panel. 
   
  1. Open the Device Manager, expand the *Ports* menu
  2. Find the COM port for the *USB Serial Port*.  e.g. COM5
  3. Open PuTTY

Once PuTTY is open, enter the following settings:
    
  4. Select serial
  5. Enter the COM port number
  6. Enter the serial terminal settings (below)
  7. Click *Open*

Full terminal Settings:
    
  * 115200 baud
  * 8 data bits
  * 1 stop bit
  * No Parity
  * No Flow Control

Linux/Mac
=========


Open a Terminal window on MacOS or an XTerm (or your favorite terminal program) on Linux.

Issue the following command to view current serial devices.

   .. code-block:: console

      ls /dev/cu.usb*

Connect a Micro USB cable to the board and your computer.

Issue the following command again to identify the device.

   .. code-block:: console

      ls /dev/cu.usb*

Identify the change of items in the list, and issue the following command:

   .. code-block:: console

      screen /dev/<device> 115200 -L

For example, if the difference was *cu.usbmodem0004*, the command would be:

   .. code-block:: console

      screen /dev/cu.usbmodem0004 115200 -L

Using the terminal
==================
  
Hit *Enter* in the terminal window to make sure you can see the command prompt:

.. code-block:: console
    
    xilinx@pynq:/home/xilinx#

You can then run the same commands listed above to change the hostname, or configure a proxy. 

You can also check the hostname of the board by running the *hostname* command:

.. code-block:: console
    
    hostname

You can also check the IP address of the board using the *ip* command:

.. code-block:: console
    
    ip a
