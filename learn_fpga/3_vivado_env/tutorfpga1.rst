.. _install_Vivado:

##############################
Installation of Vivado 2020.1
##############################

This installation tutorial is intended for anyone who wants to use the FPGA of the Red Pitaya board. You need one of the following on your computer or virtual machine: Ubuntu OS, Linux Mint OS, or Windows with WSL (Windows Subsystem for Linux). After that, follow the instructions to install Vivado 2020.1.

.. note::

    **Why not use an up-to-date Vivado Version?**

    The reason is quite simple actually, Red Pitaya software was written for Vivado version 2020.1.

**********************
Install Vivado 2020.1
**********************

#. Head to |AMD's downloads webpage|.
#. Go to **Vivado Archive** and select the **2020.1** option.

   .. figure:: img/Vivado Archive.png
       :width: 1000
       :align: center

   .. figure:: img/Vivado-2020_1.png
       :width: 1000
       :align: center

#. In the 2020.1 dropdown menu, scroll down until you see the "Vivado Design Suite - HLx Editions - 2020.1  Full Product Installation" (just after the first download link).

   .. figure:: img/Vivado-update1.png
       :width: 1000
       :align: center
   
   .. figure:: img/Vivado-full-download.png
       :width: 1000
       :align: center

#. There are three download links. Use the **Vivado HLx 2020.1: All OS installer Single-File Download (TAR/GZIP - 35.51 GB)** as Windows and Linux self extracting Web Installers do not work since Xilinx was acquired by AMD.

   .. figure:: img/Vivado-tar-file.png
       :width: 1000
       :align: center

#. After clicking on the link, you will be asked to sign in. Use your AMD username and password. If you don't have an AMD account, you will have to create one. It's free. 

   .. figure:: img/AMD_sign_in.png
       :width: 500
       :align: center

#. You will be redirected to the download centre, where you input your information and click on the "DOWNLOAD" button at the bottom of the page to start the download. Please note that this is a 35 GB file so depending on your internet connection it might take a while.

   .. figure:: img/AMD_download_centre.png
      :width: 1000
      :align: center

#. Extract the .tar.gz file using your preffered method.

.. |AMD's downloads webpage| raw:: html

    <a href="https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vivado-design-tools.html" target="_blank">AMD's downloads webpage</a>


---------
Windows
---------

To extract the *.tar.gz* file you will need a program like *7zip* or *WinRAR*.

Install Vivado as you would any other program, but remember/write down the path to the installation folder; you will need it later. Do not forget to install the libraries at the end of this webpage (through the WSL).
Refer to Linux installation process from `Installation Wizard <install_wizard>`_ onwards.

---------
Linux
---------

Now you have to run the downloaded file for installation. Open a terminal, go to the downloaded file directory (**cd Downloads/**).

First, extract the downloaded *.tar.gz* file. Use the following command:

.. code-block:: shell

   tar -xvzf example1.tar.gz

or extract it to a specific directory:

.. code-block:: shell

   tar -xvzf <file-name>.tar.gz -C </path/to/directory>


.. TODO update instructions from here

The first command is to make the file executable, and the second is to run the file.

.. code-block:: bash
    
    chmod +x ./Xilinx_Unified_2020.1_0602_1208_Lin64.bin
    sudo ./Xilinx_Unified_2020.1_0602_1208_Lin64.bin

Vivado 2020.1 is not supported on Ubuntu version 20.04 or above (but it works just fine)—when installing it you will encounter the following warning:

.. figure:: img/Warning1.png
    :width: 1000
    :align: center


The installer window will also glitch and disappear after you click **OK** – forcing you to press **Ctrl+C** in the terminal to force quit the installation process.

.. figure:: img/Warning2.png
    :width: 1000
    :align: center


To avoid this warning, we will "fake" our OS version for the duration of the installation process. Locate the **os-release** file in the **/etc** directory. Open the file as the super user with a text editor (nano, for example):

.. code-block:: bash

    sudo nano os-release

Make a note of the **VERSION** line (for Ubuntu 20.04, it should be **VERSION="20.04.6 LTS (Focal Fossa)"**). Then, in the **VERSION** line, change it to **VERSION="18.04.4 LTS (Bionic Beaver)"** and save the file (**DO NOT** forget to change it back once the installation is complete). The edited file should look like this:

Quick reference version lines for different Ubuntu versions:

- Ubuntu 18.04 - VERSION="18.04.4 LTS (Bionic Beaver)"
- Ubuntu 20.04 - VERSION="20.04.6 LTS (Focal Fossa)"
- Ubuntu 22.04 - VERSION="20.04.4 LTS (Jammy Jellyfish)"

.. figure:: img/Warning3.png
    :width: 1000
    :align: center

.. note::

   If Ubuntu installs packages while you are faking the OS version and this causes an issue with the system, try to execute the following command:

   .. code-block:: shell

      sudo apt-get install --reinstall base-files

Re-run the installation file:

.. code-block:: bash
    
    sudo ./Xilinx_Unified_2020.1_0602_1208_Lin64.bin

Now the installation process should go through.


.. figure:: img/Screen2.png
    :width: 1000
    :align: center


.. _install_wizard:

It will open this installation wizard. Click Next.

.. figure:: img/Screee3.png
    :width: 1000
    :align: center


Insert your Xilinx ID and password. Check **Download and install Now**. Click Next.

.. figure:: img/Screen4.png
    :width: 1000
    :align: center


Check all the boxes. Click Next.

.. figure:: img/Screen5.png
    :width: 1000
    :align: center


Check **Vivado HL WebPACK**. Click Next.

.. figure:: img/Screen6.png
    :width: 1000
    :align: center


Check all the boxes in the next image. Uncheck *Ultrascale* and *Ultrascale+* as you don't need them. Click Next.

.. figure:: img/Screen7.png
    :width: 1000
    :align: center


The default installation directory is **/opt/Xilinx**, so install there. Click Next.

Check the information and click Install. Now wait for the download and installation.

It will open the licence manager, and you will have to get the free WebPACK licence file. Click **Connect Now** or **Save Link As**. This will take you to the Xilinx licence manager website, where you must follow the instructions to generate the **ISE WebPACK license**. The licence file will be sent to your registered e-mail address. After that, click on **Load License** and click **Copy License** to copy your **.lic** file to register Vivado.

.. figure:: img/Screen8.png
    :width: 1000
    :align: center


Install additional libraries after installing Vivado by running the following command in Terminal.

.. code-block:: bash

    sudo apt-get install libxft2 libxft2:i386

.. note:: 

   If you are running a 32-bit system, libxft2:i386 library will not install (*Unable to locate package libxft2:i386*). Solution? Install *libxft2*, which we already did :D.

.. warning::

   When the installation finishes do **NOT** forget to change your **VERSION** in the **os-release** file back to what is was before – failure to do so might cause problems with other programs.

   If Ubuntu happens to install some updates while you are faking the OS version and this causes an issue with the system, try to execute the following command:

   .. code-block:: shell

      sudo apt-get install --reinstall base-files
