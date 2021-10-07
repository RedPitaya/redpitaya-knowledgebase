FPGA lessons
############

=============
Project setup
=============

* Windows 10 or Ubuntu 18.04
* Vivado 2020.1
* RepPitaya ecosystem project

Xilinx SDK is available from Xilinx downloads page:
https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vivado-design-tools/archive.html

Ecosystem:
https://github.com/RedPitaya/RedPitaya.git


At this stage it is assumed that Red Pitaya is successfully connected the local network with an established ssh (or `Putty <https://redpitaya.readthedocs.io/en/latest/developerGuide/software/console/ssh/ssh.html>`_) connection. 
If not, follow Red Pitaya’s official `quick-start <https://redpitaya.readthedocs.io/en/latest/quickStart/quickStart.html>`_ instructions.

For the FPGA development platform we will use Xilinx’s Vivado Design Suite with SDK. At the time of writing the latest version was Vivado 2020.1, however, other versions would also work. 
The Vivado Suite can be installed for free with WebPACK licence, which can be downloaded after registration from their webpage.

To install Vivado follow these steps:

#. Register, download and install latest `Vivado Design Suite with SDK <https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vivado-design-tools/archive.html>`_. 
#. Obtain free WebPACK licence


To work with Vivado and its instruments in Windows we use TCL shell and Command prompt. Launch **Vivado HLS 2020.1 Command Prompt**
Change to the folder with cloned RedPitaya project and launch the project generation:

.. code-block:: shell-session

    cd C:/Users/RedPitaya/fpga
    vivado -source red_pitaya_vivado_project_Z10.tcl -tclargs v0.94

On Linux it will work via the terminal, however, to get access to some necessary commands you should execute settings64.sh (located in the Vivado folder). 
Then you can execute Vivado command. 

.. code-block:: shell-session

    /opt/Xilinx/Vivado/2020.1/settings64.sh
    vivado -source red_pitaya_vivado_project_Z10.tcl -tclargs v0.94


When executing this command, the script will be launched and this script will generate a project for RedPitaya Z10 into the folder RedPitaya/fpga/prj/v0.94/project. 

=======
Lessons
=======

.. toctree::
   :maxdepth: 1

   LedBlink.rst
   KnightRider.rst
   StopWatch.rst
   FreqCounter.rst
   SimpleCalculator.rst
   SimpleAvarage.rst
   VgaImage.rst
   PingPong.rst
   Laboratory for Integrated Circuit Design <https://lniv.fe.uni-lj.si/redpitaya/>