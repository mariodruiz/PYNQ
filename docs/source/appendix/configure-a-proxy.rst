.. _configure-a-proxy:

*****************
Configure a proxy
*****************

If your board is connected to a network that uses a proxy, you need to set the
proxy variables on the board. 

Open a terminal and enter the following
where you should replace "my_http_proxy:8080" and "my_https_proxy:8080" with
your proxy settings. If necessary, check with your IT department or system 
administrator for these details. 

.. code-block:: console
    
    set http_proxy=my_http_proxy:8080
    set https_proxy=my_https_proxy:8080