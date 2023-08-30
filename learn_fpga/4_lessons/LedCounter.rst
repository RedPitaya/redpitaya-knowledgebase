.. _led_counter::


##############
LED Counter
##############

.. note::

    The instructions here are an example for STEMlab 125-14. For other boards the process is the same, but diferent flags must be used. Please see the :ref:`Vivado Project Setup <create_fpga_project>` for more information.


========================
Prepare the environment
========================

Download and extract the |RP FPGA| to a folder/directory on your computer.

.. |RP FPGA| raw:: html

   <a href="https://github.com/RedPitaya/RedPitaya-FPGA" target="_blank">Red Pitaya FPGA Git repository</a>


.. tabs::

   .. tab:: Linux

         Open Vivado and in Vivado Tcl Console navigate to the base folder **RedPitaya-FPGA** and make a clean Red Pitaya Vivado project.

        .. code-block:: bash

            . /opt/Xilinx/Vivado/2020.1/settings64.sh
            cd Downloads/
            cd RedPitaya-FPGA/
            make project PRJ=v0.94 MODEL=Z10

        .. figure:: ./../img/Screen9.png
            :width: 50%
            :align: cente


   .. tab:: Windows

        On Windows search for **Vivado HLS 2020.1 Command Prompt** and launch it.

       Using the command line navigate to the extracted folder and make a Vivado project:

       .. code-block:: bash

            cd Downloads/
            cd RedPitaya-FPGA/
            make project PRJ=v0.94 MODEL=Z10

        .. figure:: ./../img/Vivado_HLS_console_windows.png
            :width: 50%
            :align: cente



This will automatically generate a complete project in the **RedPitaya-FPGA/prj/v0.94** directory.


===========
Description
===========

In this project, we will learn how to create a simple LED binary counter using some basic VHDL code. We will also learn how we can replace one of the rarely used components in the Red Pitaya FPGA, the MIMO PID, and replace it with our own FPGA component.
Our FPGA component will contain the code for a binary LED counter, but later on you can use the same structure and completly reprogram the functionality.











After you confirm that both synthesis and implementation will be executed beforehand, the longer process starts. After successful completion of synthesis, implementation, and bitstream generation, the bit file can be found at **Examples/Led_blink/tmp/Led_blink/Led_blink.runs/impl_1/system_wrapper.bit**.

Copy the newly generated bit file to the RedPitaya’s **/root/tmp** folder using WinSCP or type the following commands in the Linux console.

.. code-block:: shell-session

    cd Examples/v0.94/tmp/Led_blink/Led_blink.runs/impl_1/
    scp system_wrapper.bit root@your_rp_ip:Led_blink.bit

Finally, we are ready to program the FPGA with our own bitstream file located in the **/root/** folder on Red Pitaya. 
To program the FPGA simply execute the following line in the Linux console on your Red Pitaya (use Putty):

.. code-block:: shell-session

    cat /root/Led_blink.bit > /dev/xdevcfg

Now, you should see an LED blink. Don’t worry, you did not destroy your Red Pitaya. If you want to roll back to the official Red Pitaya FPGA program, run the following command:

.. tabs::

    .. group-tab:: OS version 1.04 or older

        .. code-block:: shell-session

            redpitaya> cat /opt/redpitaya/fpga/fpga_0.94.bit > /dev/xdevcfg

    .. group-tab:: OS version 2.00

        .. code-block:: shell-session

            redpitaya> overlay.sh v0.94

or simply restart your Red Pitaya.

