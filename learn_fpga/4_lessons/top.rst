FPGA lessons
############

=============
Project setup
=============

* Windows 10 or Ubuntu 18.04 or higher
* Vivado 2020.1
* Rep Pitaya FPGA ecosystem

    - Xilinx SDK is available from |Xilinx downloads page|
    - |Red Pitaya FPGA Ecosystem|

.. |Xilinx downloads page| raw:: html

    <a href="https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vivado-design-tools/archive.html" target="_blank">Xilinx downloads page</a>

.. |Red Pitaya Ecosystem| raw:: html

    <a href="https://github.com/RedPitaya/RedPitaya-FPGA" target="_blank">Red Pitaya Ecosystem</a>


At this point, it is assumed that your Red Pitaya has successfully connected to the local network using |SSH| (Linux or Windows with WSL) or |Putty| (Windows). If not, follow Red Pitaya’s official |quick start| instructions.

.. |Putty| raw:: html

    <a href="https://redpitaya.readthedocs.io/en/latest/developerGuide/software/console/ssh/ssh.html#windows-10" target="_blank">Putty</a>

.. |SSH| raw:: html

    <a href="https://redpitaya.readthedocs.io/en/latest/developerGuide/software/console/ssh/ssh.html#establish-remote-ssh-connection" target="_blank">SSH</a>

.. |quick start| raw:: html

    <a href="https://redpitaya.readthedocs.io/en/latest/quickStart/first.html#connect-to-red-pitaya" target="_blank">quick start instructions</a>


For the FPGA development platform, we will use Xilinx’s Vivado Design Suite with SDK. At the time of writing, the latest version was Vivado 2020.1. However, other versions would also work. The Vivado Suite can be installed for free with a WebPACK licence, which can be downloaded after registration from their webpage.

To install Vivado, please use the |Vivado installation guide|.

.. |Vivado installation guide| raw:: html

    <a href="https://redpitaya-knowledge-base.readthedocs.io/en/latest/learn_fpga/3_vivado_env/tutorfpga1.html#installation-of-vivado" target="_blank">Vivado installation guide</a>

If you are planning on developing or changing the ecosystem, you can instead install the Vitis platform (which includes Vivado and SDK, version 2020.1 or higher).

#. Register, download and install |Vitis|
#. Obtain free WebPACK licence

.. |Vitis| raw:: html

    <a href="https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vitis/archive-vitis.html" target="_blank">Vitis</a>

To work with Vivado and its instruments in Windows, we use the TCL shell and command prompt. Launch **Vivado HLS 2020.1 Command Prompt**. Change to the folder with the cloned Red Pitaya project and launch the project generation:

.. code-block:: shell-session

    cd C:/Users/RedPitaya/fpga
    vivado -source red_pitaya_vivado_project_Z10.tcl -tclargs v0.94

On Linux, it will work through the terminal; however, to gain access to some required commands, run **settings64.sh** (located in the Vivado folder). Then you can execute the Vivado command (which will open the Vivado program; the file needs to be executed at every boot-up).

.. code-block:: shell-session

    /opt/Xilinx/Vivado/2020.1/settings64.sh
    vivado -source red_pitaya_vivado_project_Z10.tcl -tclargs v0.94


When executing this command, the script will be launched, and this script will generate a project for the Red Pitaya Z10 (STEMlab 125-14) in the folder **RedPitaya-FPGA/prj/v0.94/project**.

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
