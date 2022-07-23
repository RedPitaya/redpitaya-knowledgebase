####################
Programming the FPGA
####################

After the installation of Vivado, we will have to clone the FPGA repository and edit an existing project for our Hello World project.

****************************
Clone FPGA GitHub repository
****************************

Go to the |RP FPGA| site and download the ZIP folder of this project.
 
.. figure:: ./../img/clonerepo1.png
    :height: 200px
    :align: center

.. |RP FPGA| raw:: html

   <a href="https://github.com/RedPitaya/RedPitaya-FPGA" target="_blank">Red Pitaya FPGA Github</a>


Alternatively, if you are using Linux, you can first install git, then move to a desired location and make a clone of the Red Pitaya Git repository:

.. code-block:: bash
  
  sudo apt-get install git
  git clone https://github.com/RedPitaya/RedPitaya-FPGA.git



*******************
Make an FPGA project
*******************

Go to the downloaded ZIP location and extract it. You will enter the FPGA folder and make a Vivado project. Open a terminal and input the following commands.

.. code-block:: bash

    cd Downloads/
    cd RedPitaya/
    cd fpga/
    . /opt/Xilinx/Vivado/2020.1/settings64.sh
    make project PRJ=v0.94 MODEL=Z10

.. note::

    In order to open a project for models SDRlab 122-16 or SIGNALlab 250-12, you need to specify MODEL=Z20 or MODEL=Z20_250 as a parameter.


.. figure:: ./../img/Screen9.png
    :width: 50%
    :align: center

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

Now you have to start synthesis, implementation, and writing a bitstream. Press the button to start the synthesis.

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

You have to send this file to your Red Pitaya board. Open a terminal and connect to your Red Pitaya using an SSH connection. Also, enable the read/write operation on the Red Pitaya.

.. code-block:: bash
    
    ssh root@your Red Pitaya IP
    redpitaya> rw

Open another Terminal and go to the .bit file location.

.. code-block:: bash
    
    cd Downloads/RedPitaya-FPGA/prj/v0.94/project/repitaya.runs/impl_1
    
Send the file .bit to the Red Pitaya with ``scp`` command.

.. code-block:: bash
    
    scp red_pitaya_top.bit root@your Red Pitaya IP:/tmp

Go back to the Red Pitaya Terminal and check if you have the copy **red_pitaya_top.bit**

.. code-block:: bash

    redpitaya> cd /tmp
    redpitaya> ls

Load the **red_pitaya_top.bit** to **xdevcfg** with

.. code-block:: bash

    redpitaya> cat /tmp/red_pitaya_top.bit >/dev/xdevcfg

Congratulations, the LED should now be blinking, and the project should be running on the FPGA.
