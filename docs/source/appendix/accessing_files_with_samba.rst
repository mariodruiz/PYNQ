.. _accessing-files-with-samba:

*****************************
Accessing files with Samba
*****************************

.. NOTE:: 
   `Samba <https://www.samba.org/>`_, a file sharing service, is running on the
   board with you are using a PYNQ image. Samba may need to be installed 
   separately if you installed PYNQ on top of another image (E.g. Kria SOM).
   Samba allows you to access the Pynq home area as a network drive, to
   transfer files to and from the board.
   Samba is available for PYNQ but this functionality is superseded by Jupyter
   Lab which has drag-and-drop support in the browser for copying files to the
   board.  
   

Accessing Files on The Board with Samba
=======================================

.. NOTE:: 
    In the examples below change the hostname or IP address to match your
    board settings.

To access the PYNQ home area in Windows Explorer type one of the following in
the navigation bar.

.. code-block:: console
    
   \\192.168.2.99\xilinx        # If connected to a Computer with a Static IP

When prompted, the username is **xilinx** and the password is **xilinx**. The
following screen should appear:

.. image:: ../images/samba_share.JPG
    :align: center

To access the home area in Ubuntu, open a file broswer, click Go -> Enter
Location and type one of the following in the box:

.. code-block:: console
    
  smb://192.168.2.99/xilinx        # If connected to a Computer with a Static IP

When prompted, the username is **xilinx** and the password is **xilinx** 