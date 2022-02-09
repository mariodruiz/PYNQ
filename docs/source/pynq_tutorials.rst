.. _pynq-tutorials:

**************
PYNQ Tutorials
**************

This page is a collection of material from the PYNQ team, partners, and PYNQ users 
covering a range of topics related to design and development with PYNQ. 
You can write your own tutorials and post them 
to the `PYNQ support forum <https://discuss.pynq.io/c/tutorials-workshops/15>`_. 
You can submit a pull request to the `PYNQ GitHub repository <https://github.com/Xilinx/pynq>`_
linking your tutorial from this page. 

.. |youtube_icon| image:: ./images/youtube_social_circle_white.png
.. |jupyter_icon| image:: ./images/jupyter.png 
.. |vivado_icon| image:: ./images/vivado.png 
.. |python_icon| image:: ./images/python.png 
.. |blog_icon| image:: ./images/blog.png 
.. |vitis_icon| image:: ./images/vitis_hls.png 

PYNQ Workshop
=============

The `PYNQ workshop material <https://github.com/Xilinx/PYNQ_Workshop>`_ is an introduction
training workshop developed but the PYNQ team. It includes PDF presentations and hands-on 
exercises and is recommended for beginners. 
The material is based on the PYNQ-Z2 board but can be used on other PYNQ boards. 

* Session 1: `Introduction to using Jupiter with PYNQ <https://github.com/Xilinx/PYNQ_Workshop/tree/master/Session_1>`_ |jupyter_icon| 
* Session 2: `Introduction to using peripherals with the PYNQ base Overlay <https://github.com/Xilinx/PYNQ_Workshop/tree/master/Session_2>`_ |jupyter_icon| 
* Session 3: `Introduction to PYNQ IOPs and the logictools overlay <https://github.com/Xilinx/PYNQ_Workshop/tree/master/Session_3>`_ |jupyter_icon| 
* Session 4: `Introduction to designing overlays <https://github.com/Xilinx/PYNQ_Workshop/tree/master/Session_4>`_ |jupyter_icon| 

Using PYNQ
==========

* `Introduction to Jupyter Lab running on PYNQ <https://youtu.be/r6N0G0ekV8w>`_ |jupyter_icon| |youtube_icon|
* `Exploring the PYNQ environment with Jupyter Lab <https://youtu.be/Y4l8H1jZ5Y0>`_ |jupyter_icon| |youtube_icon|
* `Example of basic visualisation with Jupyter <https://youtu.be/MlU-tstNYp0>`_ |jupyter_icon| |youtube_icon|
* `What’s in My Bitstream - A Pythonic Approach to Discovering FPGA Contents <https://discuss.pynq.io/t/whats-in-my-bitstream-a-pythonic-approach-to-discovering-fpga-contents/653>`_ |blog_icon| |python_icon|
* `Example of using AXI GPIO <https://youtu.be/TpCax4yjxUM>`_ |jupyter_icon| |youtube_icon|
* `Example of using MMIO <https://youtu.be/zbumITJQ2Z8>`_ |jupyter_icon| |youtube_icon|
* `Using Register Map <https://youtu.be/vK1cEEdKAds>`_ |jupyter_icon| |youtube_icon|
* `Example of a allocating memory (the memory can be used from the programmable logic) <https://youtu.be/Z6BkKAleLxc>`_ |jupyter_icon| |youtube_icon|
* `FPGA data movement with NumPy <https://discuss.pynq.io/t/fpga-data-movement-using-numpy/734>`_ |blog_icon| |python_icon|
* `Example of using the AXI DMA <https://youtu.be/K4OkNH17hiA>`_ |jupyter_icon| |youtube_icon|


IP Examples
^^^^^^^^^^^

* `Using a new hardware design with PYNQ (AXI GPIO) <https://discuss.pynq.io/t/tutorial-using-a-new-hardware-design-with-pynq-axi-gpio/146>`_ |blog_icon| |jupyter_icon| |vivado_icon|
* `Using PS GPIO to control peripherals with the Kria KV260 <https://youtu.be/48CbhK2PAcE>`_ |youtube_icon| |python_icon| 
* `PWM On PYNQ: How To Control A Stepper Motor (Makarena Labs) <https://discuss.pynq.io/t/tutorial-use-axi-timer-as-an-ip-no-microblaze/3312>`_ |blog_icon| |python_icon| 
* `Using MicroBlazes (Makarena Labs) <https://www.makarenalabs.com/microblaze-on-pynq-soft-processor-on-fpga>`_ |blog_icon| |python_icon| 


Hardware design
===============

Vivado
^^^^^^

* `Rebuilding the PYNQ base overlay (v2.6, PYNQ- <https://discuss.pynq.io/t/tutorial-rebuilding-the-pynq-base-overlay-pynq-v2-6/1993/11>`_ |blog_icon| |vivado_icon|
* `Creating a new Vivado hardware design for PYNQ <https://discuss.pynq.io/t/tutorial-creating-a-hardware-design-for-pynq/145>`_ |blog_icon| |vivado_icon|
* `Creating a design with SPI, I2C, UART On PYNQ: A PL Approach (Makarena Labs) <https://www.makarenalabs.com/spi-i2c-uart-on-pynq-a-pl-approach/>`_ |blog_icon| |vivado_icon|
* `Creating a new Verilog module Overlay <https://discuss.pynq.io/t/tutorial-creating-a-new-verilog-module-overlay/1530>`_ |blog_icon| |vivado_icon|
* `Creating a Verilog Overlay with bidirectional pins <https://discuss.pynq.io/t/tutorial-creating-a-verilog-overlay-with-bidirectional-pins/1610>`_ |blog_icon| |vivado_icon|
* `How to accelerate a Python function (FIR filter) with PYNQ (FPGA Developer) <https://youtu.be/LoLCtSzj9BU>`_ |youtube_icon| |vivado_icon| 


Two part tutorial on using PS GPIO with PYNQ, covering the Vivado design in part 1, then using the design from PYNQ in part 2. 

* `Building a hardware design to use PS GPIO (Part 1) <https://youtu.be/a5NnLozPEI0>`_ |blog_icon| |vivado_icon|
* `Using PS GPIO with PYNQ (Part 2) <https://youtu.be/rAHR3fmYFro>`_ |blog_icon| |jupyter_icon|

Two part tutorial on using a DMA with PYNQ, covering the Vivado design in part one, then using the design from PYNQ in part two. 

* `Creating a Vivado hardware design with a DMA (Part 1) <https://discuss.pynq.io/t/tutorial-pynq-dma-part-1-hardware-design/3133/8>`_ |blog_icon| |vivado_icon|
* `Using a DMA from PYNQ (Part 2) <https://discuss.pynq.io/t/tutorial-pynq-dma-part-2-using-the-dma-from-pynq/3134>`_ |blog_icon| |jupyter_icon|


HLS design
^^^^^^^^^^

Three part tutorial on using a HLS stream IP with DMA. Part 1 covers the HLS design, part 2 covers the Vivado design and part 3 shows how to use the design from PYNQ. 

* `Using a HLS stream IP with DMA tutorial (Part 1: HLS design) <https://discuss.pynq.io/t/tutorial-using-a-hls-stream-ip-with-dma-part-1-hls-design/3344>`_ |blog_icon| |vitis_icon| 
* `Using a HLS stream IP with DMA tutorial (Part 2: Vivado design) <https://discuss.pynq.io/t/tutorial-using-a-hls-stream-ip-with-dma-part-2-vivado-design/3345>`_ |blog_icon| |vivado_icon|
* `Using a HLS stream IP with DMA tutorial (Part 3: using the HLS IP from PYNQ) <hhttps://discuss.pynq.io/t/tutorial-using-a-hls-stream-ip-with-dma-part-3-using-the-hls-ip-from-pynq/3346>`_ |blog_icon| |jupyter_icon| 

RTL design
^^^^^^^^^^

* `Developing Verilog AXI Stream Overlays and interfacing to ZYNQ <https://discuss.pynq.io/t/developing-verilog-axi-stream-overlays-and-interfacing-to-zynq/1643>`_ |blog_icon| |vivado_icon|

Hardware Debug
^^^^^^^^^^^^^^

* `Using an ILA with PYNQ to debug IP <https://discuss.pynq.io/t/using-ila-to-debug-ip/2855>`_ |blog_icon| |vivado_icon|

Building a PYNQ image
=====================

* `Quick Porting of PYNQ using Pre-built Images <https://discuss.pynq.io/t/quick-porting-of-pynq-using-pre-built-images/1075/15>`_ |blog_icon|
* `Building PYNQ for a custom board (v2.6) <https://discuss.pynq.io/t/pynq-2-6-custom-board-image-build-method-that-works/2894>`_ |blog_icon|
* `Deploying PYNQ with Jupyter and PetaLinux <https://discuss.pynq.io/t/deploying-pynq-and-jupyter-with-petalinux/677>`_ |blog_icon|

Software tutorials
==================

* `Using Docker with PYNQ <https://discuss.pynq.io/t/docker-xilinx-platforms-pynq/1962>`_ |blog_icon|
* `Dynamically Creating Usable Python Objects <https://discuss.pynq.io/t/dynamically-creating-usable-python-objects-the-overlay-class/762>`_ |blog_icon| |jupyter_icon|
* `Creating a PyPi package for your design <https://discuss.pynq.io/t/using-pypi-to-deliver-fpga-overlays/1031>`_ |blog_icon| |python_icon| 
* `Interactive C++ on the Kria-SoM in Jupyter Lab <https://discuss.pynq.io/t/interactive-c-on-the-kria-som-in-jupyter-lab/3667>`_ |blog_icon| |jupyter_icon|

