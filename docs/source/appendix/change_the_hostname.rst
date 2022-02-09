.. _change-the-hostname:

*******************
Change the hostname
*******************

If your PYNQ board will connect to a network where more PYNQ boards may be 
connected, you should change your hostname before your connect to the network 
or immediately after connecting. This is a common requirement in a work or
university environment. You can change the hostname from a terminal. You can use
the USB cable to connect a terminal. A terminal is also available in the Jupyter
environment and can be used from an internet browser.

To access the Jupyter terminal, in the Jupyter portal home area, select **New >>
Terminal**.

.. image:: ../images/dashboard_files_tab_new.JPG
    :height: 300px
    :align: center
       
This will open a terminal inside the browser as root.

Use the preloaded pynq_hostname.sh script to change your board's hostname.

.. code-block:: console
    
    pynq_hostname.sh <NEW HOSTNAME>

The board must be restarted for the changes to be applied.

.. code-block:: console
    
    shutdown -r now

Note that as you are logged in as root, sudo is not required. If you connect a
terminal from the USB connection, you will be logged in as the *xilinx* user and
sudo must be added to these commands.

When the board reboots, reconnect using the new hostname. 

If you can't connect to your board, see the step below to open a terminal using
the micro USB cable.
