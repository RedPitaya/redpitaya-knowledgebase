######################
Installation of Vivado
######################

This installation tutorial is intended for anyone who wants to use the FPGA of the Red Pitaya board. You need one of the following on your computer or virtual machine: Ubuntu OS, Linux Mint OS, or WSL (Windows Subsystem for Linux). After that, follow the instructions to install Vivado.

**************
Install Vivado
**************

Download |Vivado| -Linux Self-Extracting Web Installer (Ubuntu or Linux Mint), or Windows Self Extracting Web Installer (WSL). If you don't have an Xilinx account, you will have to create one. It's free. 

.. |Vivado| raw:: html

    <a href="https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vivado-design-tools/archive.html" target="_blank">Vivado Design Suite 2020.1 - HLx Editions</a>


.. figure:: ./../img/Screen1.png
    :width: 50%
    :align: center

    - For Windows: Install Vivado as you would any other program, but remember/write down the path to the installation folder; you will need it later. Do not forget to install the libraries at the end of this webpage (through the WSL).
    - For Linux, just follow the installation process below.


Now you have to run the downloaded file for installation. Open a terminal, go to the downloaded file directory (**cd Downloads/**), and insert the following commands. The first command is to make the file executable, and the second is to run the file.

.. code-block:: bash
    
    chmod +x ./Xilinx_Unified_2020.1_0602_1208_Lin64.bin
    sudo ./Xilinx_Unified_2020.1_0602_1208_Lin64.bin

Vivado 2020.1 is not supported on Ubuntu version 20.04 or above (but it works just fine)—when installing it you will encounter the following warning:

.. figure:: ./../img/Warning1.png
    :width: 50%
    :align: center



The installer window will also glitch and disappear after you click **OK** – forcing you to press **Ctrl+C** in the terminal to force quit the installation process (this will happen with both the unified and Linux web-installer).

.. figure:: ./../img/Warning2.png
    :width: 50%
    :align: center



To avoid this warning, we will "fake" our OS version for the duration of the installation process (this needs to be done for both the unified and Linux web-installer). Locate the **os-release** file in the **/etc** directory. Open the file as the super user with a text editor (nano, for example):

.. code-block:: bash

    sudo nano os-release

Make a note of the **VERSION** line (for Ubuntu 20.04, it should be **VERSION="20.04.3 LTS (Focal Fossa)"**). Then, in the **VERSION** line, change it to **VERSION="18.04.4 LTS (Bionic Beaver)"** and save the file (DO NOT** forget to change it back once the installation is complete). The edited file should look like this:

.. figure:: ./../img/Warning3.png
    :width: 50%
    :align: center


Re-run the installation file:

.. code-block:: bash
    
    sudo ./Xilinx_Unified_2020.1_0602_1208_Lin64.bin

Now the installation process should go through.


.. figure:: ./../img/Screen2.png
    :width: 50%
    :align: center


It will open this installation wizard. Click Next.

.. figure:: ./../img/Screee3.png
    :width: 50%
    :align: center


Insert your Xilinx ID and password. Check **Download and install Now**. Click Next.

.. figure:: ./../img/Screen4.png
    :width: 50%
    :align: center


Check all the boxes. Click Next.

.. figure:: ./../img/Screen5.png
    :width: 50%
    :align: center


Check **Vivado HL WebPACK**. Click Next.

.. figure:: ./../img/Screen6.png
    :width: 50%
    :align: center


Check all the boxes in the next image. Uncheck *Ultrascale* and *Ultrascale+* as you don't need them. Click Next.

.. figure:: ./../img/Screen7.png
    :width: 50%
    :align: center


The default installation directory is **/opt/Xilinx**, so install there. Click Next.

Check the information and click Install. Now wait for the download and installation.

It will open the licence manager, and you will have to get the free WebPACK licence file. Click **Connect Now** or **Save Link As**. This will take you to the Xilinx licence manager website, where you must follow the instructions to generate the **ISE WebPACK license**. The licence file will be sent to your registered e-mail address. After that, click on **Load License** and click **Copy License** to copy your **.lic** file to register Vivado.

.. figure:: ./../img/Screen8.png
    :width: 50%
    :align: center


Install additional libraries after installing Vivado by running the following command in Terminal. 

.. code-block:: bash

    sudo apt-get install libxft2 libxft2:i386

When the installation finishes do **NOT** forget to change your **VERSION** in the **os-release** file back to what is was before – failure to do so might cause problems with other programs.
