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
    
.. |Red Pitaya FPGA Ecosystem| raw:: html

    <a href="https://github.com/RedPitaya/RedPitaya-FPGA" target="_blank">Red Pitaya Ecosystem</a>


At this point, it is assumed that your Red Pitaya has successfully connected to the local network using |SSH| (Linux or Windows with WSL) or |Putty| (Windows). If not, follow Red Pitaya’s official |quick start| instructions.

.. |Putty| raw:: html

    <a href="https://redpitaya.readthedocs.io/en/latest/developerGuide/software/console/ssh/ssh.html#windows-10" target="_blank">Putty</a>

.. |SSH| raw:: html

    <a href="https://redpitaya.readthedocs.io/en/latest/developerGuide/software/console/ssh/ssh.html#establish-remote-ssh-connection" target="_blank">SSH</a>

.. |quick start| raw:: html

    <a href="https://redpitaya.readthedocs.io/en/latest/quickStart/first.html#connect-to-red-pitaya" target="_blank">quick start instructions</a>


For the FPGA development platform, we will use Xilinx’s Vivado Design Suite with SDK. Vivado 2020.1 was used to develop the Red Pitaya software, hence this is the version we will use. Other Vivado versions might also work, but they would require some dirty software fixes, so we do not recommend using them. The Vivado Suite can be installed for free with a WebPACK licence, which can be downloaded after registration from their webpage.

To install Vivado 2020.1, please use the :ref:`Vivado installation guide <install_Vivado>`.

If you are planning on developing or changing the ecosystem, you can instead install the Vitis platform (which includes Vivado and SDK, version 2020.1 or higher).

#. Register, download and install |Vitis|
#. Obtain free WebPACK licence

.. |Vitis| raw:: html

    <a href="https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vitis/archive-vitis.html" target="_blank">Vitis</a>


To work with Vivado 2020.1 and its instruments in Windows, we use the TCL shell and command prompt. Launch **Vivado HLS 2020.1 Command Prompt**. Change to the folder with the cloned Red Pitaya project and launch the project generation:

.. code-block:: shell-session

    cd RedPitaya-FPGA
    make project PRJ=v0.94 MODEL=Z10

.. note::

    If you plan on using Vitis, please note that you will not have access to **Vivado HLS 2020.1 Command Prompt** which is used in the tutorial to launch the projects on Windows.
    Instead you will have to use the following command to create a clean project:

    .. code-block:: shell-session

        vivado -source red_pitaya_vivado_project_Z10.tcl -tclargs v0.94


On Linux, you only need the terminal. However, to gain access to some required commands, run **settings64.sh** (located in the Vivado 2020.1 folder). Then you can execute the Vivado command (which will open the Vivado program; the file needs to be executed at every boot-up).

.. code-block:: shell-session

    /opt/Xilinx/Vivado/2020.1/settings64.sh
    cd RedPitaya-FPGA
    make project PRJ=v0.94 MODEL=Z10

When executing this command, Vivado 2020.1 will be opened, and the script will generate an empty project for the Red Pitaya STEMlab 125-14 in the folder **RedPitaya-FPGA/prj/v0.94/project**.


=======
Lessons
=======

.. toctree::
   :maxdepth: 1

   LedCounter.rst
   LedBlink.rst
   KnightRider.rst
   StopWatch.rst
   FreqCounter.rst
   SimpleCalculator.rst
   SimpleAvarage.rst
   VgaImage.rst
   PingPong.rst
   Laboratory for Integrated Circuit Design <https://lniv.fe.uni-lj.si/redpitaya/>
