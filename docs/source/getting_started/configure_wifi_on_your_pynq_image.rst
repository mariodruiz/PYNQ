.. _configure-wifi-on-your-pynq-image:

*********************************
Configure WiFi on your PYNQ image 
*********************************

These instructions are for configuring WiFi when you are using a PYNQ SD card
image. The PYNQ image has a Python script (boot.py) that runs when the system
starts. You can add your WiFi details to the startup script so that your 
board connects to your local WiFi. 
Your board needs to support WiFi or you need to use a supported 
:ref:`usb-wifi-device`.

* Insert your MicroSD card loaded with a PYNQ image to a card reader on your 
  computer

The MicroSD card should appear as a USB storage device called **PYNQ**. 

* Open this device and open the `boot.py` file in a text editor. 

This is a Python file that runs when the board starts up. 

* Find the following lines near the top of the file and delete the # symbol to 
  uncomment them. 

.. code-block:: Python

   #from pynq.lib import Wifi

   #port = Wifi()
   #port.connect('your_ssid', 'your_password', auto=True)

* Replace `your_ssid` with the SSID of the local WiFi network you want the board
  to connect to, and replace `your_password` with the WiFi password.  

* Go back and continue with the board setup steps. 

When you turn on your board with this MicroSD card, it should automatically 
connect to the WiFi network you specified.

You can find the IP by first connecting a terminal to the board, then running
the following command in Linux command line:

   .. code-block:: console

      ip a show wlan0

Continue to :ref:`connecting-to-jupyter-notebook`.