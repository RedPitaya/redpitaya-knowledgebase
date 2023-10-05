
.. _create_fpga_project:

####################
Programming the FPGA
####################

After the installation of Vivado, we will have to clone the FPGA repository and edit an existing project for our "Hello World" (Blink) project.

****************************
Clone FPGA GitHub repository
****************************

Go to the |RP FPGA| site and download the ZIP folder of this project.
 
.. figure:: ./../img/FPGArepository.jpg
     :height: 200px
     :align: center

.. |RP FPGA| raw:: html

     <a href="https://github.com/RedPitaya/RedPitaya-FPGA" target="_blank">Red Pitaya FPGA Github</a>


If you are using Windows, download the project repository and extract it to a folder of your choice. Remember the path to the location of the extracted repository (when you will be searching for your disk location in the WSL, go to the root directory and move into the mnt directory). 

Alternatively, if you are using Linux or WSL, you can first install git, then move to a desired location and make a clone of the Red Pitaya Git repository:

.. code-block:: bash

    sudo apt-get install git
    git clone https://github.com/RedPitaya/RedPitaya-FPGA.git



********************
Make an FPGA project
********************

Go to the downloaded Red Pitaya FPGA Repository ZIP location and extract it to a folder/directory on your computer.


.. tabs::

     .. tab:: Linux

          Open Vivado and using the TCL console navigate to the extracted folder and make a Vivado project.

          .. code-block:: bash

               . /opt/Xilinx/Vivado/2020.1/settings64.sh
               cd Downloads/
               cd RedPitaya-FPGA/
               make project PRJ=v0.94 MODEL=Z10

          .. figure:: ./../img/Screen9.png
               :width: 50%
               :align: center


     .. tab:: Windows

          On Windows search for **Vivado HLS 2020.1 Command Prompt** and launch it.

          Using the command line navigate to the extracted folder and make a Vivado project:

          .. code-block:: bash

               cd Downloads/
               cd RedPitaya-FPGA/
               make project PRJ=v0.94 MODEL=Z10

          .. figure:: ./../img/Vivado_HLS_console_windows.png
               :width: 50%
               :align: center



.. note::

    The instructions above are an example for how to create an empty *v0.94* project for STEMlab 125-14. For other boards, please use the flags in the table below. For more information on alternative Project flag options options, please refer to |dev_guide_software|.

    Table of required build flags for the recommended *v0.94* FPGA project per board:
    
    +------------------------------+---------------------+---------------------+
    | Model                        | Build Project flag  | Build Model flag    |
    +==============================+=====================+=====================+
    | | STEMlab 125-10             | PRJ=v0.94           | MODEL=Z10           |
    | | STEMlab 125-14             |                     |                     |
    +------------------------------+---------------------+---------------------+
    | STEMlab 125-14-Z7020         | PRJ=v0.94           | MODEL=Z20_14        |
    +------------------------------+---------------------+---------------------+
    | SDRlab 122-16                | PRJ=v0.94           | MODEL=Z20           |
    +------------------------------+---------------------+---------------------+
    | SIGNALlab 250-12             | PRJ=v0.94_250       | MODEL=Z20_250       |
    +------------------------------+---------------------+---------------------+
    | STEMlab 125-14 4Ch Z7020     | PRJ=v0.94           | MODEL=Z20_125_4CH   |
    +------------------------------+---------------------+---------------------+


.. |dev_guide_software| raw:: html

    <a href="https://redpitaya.readthedocs.io/en/latest/developerGuide/software/build/fpga/fpga.html#build-fpga-image" target="_blank">Developers Guide Software</a>



For this project, you will only have to edit the **red_pitaya_top.sv** file. Edit the port **led_o** assignment at the beginning of the file. Change the port to **output logic**.

.. figure:: ./../img/outputled1.png
    :width: 50%
    :align: center

Now, in this section of the file, comment out the **led_o** port.

.. figure:: ./../img/commentled.png
    :width: 50%
    :align: center

Finally, insert this code at the end of the module, before **endmodule: red_pitaya_top**. It will make the LED blink.

.. code-block:: Verilog

    reg [27:0]counter = 28'd0; 
    reg led = 1'b0;
    always @ (posedge adc_clk) begin
        counter = counter+1;
        if (counter == 28'd256000000) begin // 256e6 periods of clock of 128 MHz
            led = ~led; // led will blink with a period of 2 sec
            counter = 28'd0; // start again
        end 
    end
    assign led_o[0] = led; // assign the register to the led output


.. figure:: ./../img/codigoled.png
    :width: 50%
    :align: center

Now you have to start synthesis, implementation, and writing a bitstream. Press the button to start the synthesis. You can also just click on the "Generate bitstream" and all the steps will execute automatically.

.. figure:: ./../img/sith.png
    :width: 50%
    :align: center

After synthesis is finished, start implementation.

.. figure:: ./../img/implementation.png
    :width: 50%
    :align: center

Implementation finished. Start writing the bitstream.

.. figure:: ./../img/bitstream.png
    :width: 50%
    :align: center

The bitstream file **red_pitaya_top.bit** is located in .../prj/v0.94/project/repitaya.runs/impl_1

You have to send this file to your Red Pitaya board. Open a terminal and connect to your Red Pitaya using an SSH connection. Also, enable the read/write operation on the Red Pitaya. To establish the connection you can either use your Red Pitaya's IP address or the "rp-xxxxxx.local", where "xxxxxx" are the last six characters of the MAC address.

.. code-block:: bash
    
    ssh root@rp-xxxxxx.local
    redpitaya> rw


Reprogramming the FPGA
=========================

How the FPGA is reprogrammed depends on the Red Pitaya OS version.

Please make sure that the *PATH environment variable* is set correctly. See :ref:`Vivado installation guide <install_Vivado>` for more information.

.. note::

   On Windows, the process can also be done through a standard Command Prompt, but any ``echo`` commands must be executed inside the Windows Subsystem for Linux (WSL) Terminal (The output file encoding is a problem with Windows ``echo``). For more information, refer to the following forum topics:
   
       - |batch_file_topic_1|
       - |batch_file_topic_2|

.. |batch_file_topic_1| raw:: html

      <a href="https://superuser.com/questions/601282/%cc%81-is-not-recognized-as-an-internal-or-external-command" target="_blank">́╗┐' is not recognized as an internal or external command</a>

.. |batch_file_topic_2| raw:: html

      <a href="https://devblogs.microsoft.com/oldnewthing/20210726-00/?p=105483" target="_blank">Diagnosing why your batch file prints a garbage character, one character, and nothing more</a>

.. tabs::

    .. tab:: OS version 1.04 or older

        Please note that you need to change the forward slashes to backward slashes on Windows.

        1. Open Terminal or CMD and go to the .bit file location.

        .. code-block:: bash
    
            cd <Path/to/RedPitaya/repository>/prj/v0.94/project/repitaya.runs/impl_1

        2. Send the file .bit (*red_pitaya_top.bit* is the default name) to the Red Pitaya with the ``scp`` command.

        .. code-block:: bash

            scp red_pitaya_top.bit root@rp-xxxxxx.local:/root

        3. Now establish an SSH communication with your Red Pitaya and check if you have the copy *red_pitaya_top.bit* in the root directory.

        .. code-block:: bash

            redpitaya> ls

        4. Load the *red_pitaya_top.bit* to **xdevcfg** with

        .. code-block:: bash

            redpitaya> cat red_pitaya_top.bit > /dev/xdevcfg

    .. tab:: OS version 2.00

        The 2.00 OS uses a new mechanism of loading the FPGA. The process will depend on whether you are using Linux or Windows as the ``echo`` command functinality differs bewteen the two.

        Please note that you need to change the forward slashes to backward slashes on Windows.

        1. On Windows, open **Vivado HSL Command Prompt** and go to the *.bit* file location.

           On Linux, open the **Terminal** and go to the *.bit* file location.

           .. code-block:: bash

               cd <Path/to/RedPitaya/repository>/prj/v0.94/project/repitaya.runs/impl_1

        2. Create *.bif* file (for example, *red_pitaya_top.bif*) and use it to generate a binary bitstream file (*red_pitaya_top.bit.bin*)

           **Windows (Vivado HSL Command Prompt):**

           .. code-block:: bash

               echo all:{ red_pitaya_top.bit } >  red_pitaya_top.bif
               bootgen -image red_pitaya_top.bif -arch zynq -process_bitstream bin -o red_pitaya_top.bit.bin -w

           **Linux and Windows (WSL + Normal CMD):**

           .. code-block:: bash

               echo -n "all:{ red_pitaya_top.bit }" >  red_pitaya_top.bif
               bootgen -image red_pitaya_top.bif -arch zynq -process_bitstream bin -o red_pitaya_top.bit.bin -w

        3. Send the file *.bit.bin* to the Red Pitaya with the ``scp`` command.

           .. code-block:: bash
   
               scp red_pitaya_top.bit.bin root@rp-xxxxxx.local:/root

        4. Now establish an SSH communication with your Red Pitaya and check if you have the copy *red_pitaya_top.bit.bin* in the root directory.

           .. code-block:: bash

               redpitaya> ls

        5. Load the *red_pitaya_top.bit.bin* image into the FPGA:

           .. code-block:: bash

               redpitaya> /opt/redpitaya/bin/fpgautil -b red_pitaya_top.bit.bin

After executing the last command, you should see an LED blink. Congratualtions on writing your first FPGA program!


Reverting to original FPGA image
==================================

If you want to roll back to the official Red Pitaya FPGA program, run the following command:

.. tabs::

    .. group-tab:: OS version 1.04 or older

        .. code-block:: shell-session

            redpitaya> cat /opt/redpitaya/fpga/fpga_0.94.bit > /dev/xdevcfg

    .. group-tab:: OS version 2.00

        .. code-block:: shell-session

            redpitaya> overlay.sh v0.94

or simply restart your Red Pitaya.
