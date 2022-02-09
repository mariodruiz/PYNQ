***************
Getting Started
***************

You need a supported Xilinx platform to get started. How you get PYNQ depends
on your platform. For some Zynq and Zynq Ultrascale+ platforms you can download 
an SD card image to boot the board. For other platforms, including Alveo and Kria 
SOM boards, you can install PYNQ onto your host Operating System. 

If you have one of the following boards, you can follow the quick start guide.
Go to the `PYNQ support forum <https://discuss.pynq.io/>`_ for help.

Zynq, Zynq Ultrascale+ and Zynq RFSoC
=====================================

.. toctree::
    :maxdepth: 1
       
    getting_started/pynq_z1_setup.rst
    getting_started/pynq_z2_setup.rst
    getting_started/zcu104_setup.rst
    Kria KV260 <https://github.com/Xilinx/Kria-PYNQ>
    PYNQ-ZU <https://xilinx.github.io/PYNQ-ZU/getting_started.html>
    Ultra96 <https://ultra96-pynq.readthedocs.io/en/latest/getting_started.html>
    RFSoC 2x2 <https://www.rfsoc-pynq.io/getting_started.html>

Alveo and XRT supported platforms
=================================

.. toctree::
    :maxdepth: 1
    
    getting_started/alveo_getting_started.rst
    getting_started/pynq_alveo

Connecting to your board
========================

.. toctree::
    :maxdepth: 1

    getting_started/configure_wifi_on_your_pynq_image                    
    getting_started/ethernet_configuration
    getting_started/find_ip_address
    getting_started/connecting_to_jupyter_notebook

Jupyter Introduction
=======================

PYNQ makes use of `Jupyter <https://jupyter.org>`_. If you are new to Jupyter, 
you can follow the introductory tutorials:

.. toctree::
    :maxdepth: 1
       
    getting_started/python_environment
    getting_started/jupyter_notebooks
    getting_started/jupyter_notebooks_advanced_features
    
Example overlays and notebooks
==============================
    
You can find a selection of PYNQ projects and notebooks on the 
`PYNQ community webpage <http://www.pynq.io/community.html>`_. These are 
projects from other PYNQ users that you can install and use on your own 
PYNQ platform (assuming the design supports your platform). 

You can also install additional overlays and notebooks using the PYNQ *command
line interface*:

.. toctree::
    :maxdepth: 1
       
    pynq_cli


Using PYNQ with other boards
============================

You can find other PYNQ enabled boards on the `PYNQ.io boards <http://www.pynq.io/board.html>`_ page. 

If you have another Xilinx-based platform you would like to use with PYNQ, see the following guide:


.. toctree::
    :maxdepth: 1
       
    getting_started/other_boards.rst
    

