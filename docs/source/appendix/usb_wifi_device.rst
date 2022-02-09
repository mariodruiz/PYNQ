.. _usb-wifi-device:

USB WiFi Device
===============

If you want to connect your board to a WiFi network, but your board doesn't 
have built-in WiFi support, you may be able to use a USB WiFi dongle. 
The standard PYNQ image is based on Ubuntu and includes drivers for a number of 
popular USB WiFi chipsets.


There are many different brands but most USB WiFi dongles use one of a small 
number of WiFi chipsets. 
If the driver for a chipset is installed then the device should work with your 
board. 
 

The following devices have been tested and work with PYNQ:

   
 .. list-table:: Tested USB WiFi devices
   :widths: 25 25 25 25
   :header-rows: 1

   * - Brand
     - Part number
     - Driver/Chipset
     - Link
   * - Edimax Wi-Fi 4 802.11n Adapter
     - EW-7811Un V2
     - Ralink 5370
     - https://www.edimax.com/edimax/merchandise/merchandise_detail/data/edimax/global/wireless_adapters_n150/ew-7811un_v2/
   * - CanaKit Raspberry Pi WiFi 
     - Wireless Adapter/Dongle (802.11 n/g/b 150 Mbps)
     - Ralink 5370
     - https://www.canakit.com/raspberry-pi-wifi.html
   * - TP-Link 
     - TL-WN323N
     - rtl8xxxu
     - https://www.tp-link.com/us/support/download/tl-wn823n/
   * - TP-Link 
     - TL-WN723N
     - rtl8192cu
     - https://www.tp-link.com/us/support/download/tl-wn723n/

If you have another USB WiFi device that doesn't work with PYNQ you can 
post a question on the `PYNQ support forum <https://discuss.pynq.io/>`_
requesting help to install the driver. 

Plug in your device and run the following command to check if it is 
detected:

.. code-block:: console

   lsusb -t

Include this information in your post on the support forum. 

If you have successfully used another USB WiFi device that isn't listed 
on this page, you can open a pull request to add it or open an issue on 
the `PYNQ GitHub <https://github.com/Xilinx/pynq>`_ asking for it to be added. 
 