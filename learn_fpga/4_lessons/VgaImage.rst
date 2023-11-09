.. _vga_image:

############
VGA tutorial
############

In this tutorial, I will explain how to display a picture on a monitor using Red Pitaya. 
I used Xilinx Vivado 2021.1 for hardware programming with Xilinx SDK 2021.1 for software applications. 
The picture is just a simple matrix with "1" and "0" that represent black and white pixels. 
The picture can be scaled and moved and it can display different patterns.

Required hardware:

* Red pitaya
* Hardware extension for VGA connector

.. figure:: img/VgaImage1.png
    :alt: Logo
    :align: center



Step-by-step tutorial
=====================

Open Vivado and choose to create a new project, type in the project name and project location. It is recommended to choose a location that has no spaces in the file path because Vivado can have some problems with it.
Click *next* till you come to the page where you have to define what hardware you are using.
Select *"Boards"* and choose Red Pitaya.

Vivado doesn't have Red Pitaya installed by default so you have to copy board definitions from  `github <https://github.com/RedPitaya/RedPitaya/tree/master/fpga/brd>`_ to *C:/Xilinx/Vivado/.../data/boards/board_files/*.

We will use Block design to design our project because it is more manageable, but we will still have to write some VHDL code because not all the IPs we will be using are already implemented in Vivado. 
We will start by writing code in VHDL and creating our custom-made IPs.

First, we need to define the resolution and frequency of the monitor. 
Below is a table with values chosen for resolution 800 x 600, with a frequency of 50 MHz.


+----------------------+---------------------------+---------------------------+
| VGA 800 x 600        | Number of periods         | Number of rows            |
+======================+===========================+===========================+
| period               | H = 1040                  | V = 666                   |
+----------------------+---------------------------+---------------------------+
| visible section      | Hp = 800                  | Vp = 600                  |
+----------------------+---------------------------+---------------------------+
| pulse start          | Hf = 856                  | Vf = 637                  |
+----------------------+---------------------------+---------------------------+
| pulse duration       | Hs = 120                  | Vs = 6                    |
+----------------------+---------------------------+---------------------------+

For displaying the picture we need a process that runs line by line on the screen. 
Below is the process that shifts the cursor on the screen, with a frequency of 50 MHz. (*vga_vhdl.vhd*)


.. code-block:: vhdl

    P1: process (clk50)
    begin
        if rising_edge(clk50) then 
            clk_div <= not(clk_div);
            if hst_sig < (H-1) then
                hst_sig <= hst_sig +1;

            else
                hst_sig <= (others => '0');
                if vst_sig < V-1 then
                    vst_sig <= vst_sig +1;
                else 
                    vst_sig <= (others => '0');
                end if;
            end if;
        end if;
    end process;

A second process is to read the data from the array (*picture.vhd*).

.. code-block:: vhdl

    P2: process (hst_sig, vst_sig, cx_sig, cy_sig)
    begin
        if (hst_sig < Hp) and (vst_sig < Vp) then -- and en = '1' then
            if(cx_sig < Hslika) and (cy_sig < Vslika) then
                if slika(to_integer(cy_sig))( to_integer(cx_sig)) = '1' then
                    rgb <= "111";
                else
                    rgb <= "000"; 
                end if;
            else
                rgb <= "001";
            end if;
        else
            rgb <= "000";
        end if;
    end process;

Image for display

.. code-block:: vhdl

    type logo is array(0 to 19) of std_logic_vector(0 to 79);
    signal slika: logo := (
    "00000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "00000000100000000000000000000000000000000000000000000000000000000000000000000000",
    "00000001100000000000000000000000000000000000000000000000000000000000000000000000",
    "00000001000000000000000000000000000000000000000000000000000000000000000000000000",
    "00000001001000000000000000000000000000000000000000000000000000000000000000000000",
    "00000001001000000000000000000000000000100000000000000000000000000000000000000000",
    "00000001111000000000000000000000000000100000000001001111111111111111111111111111",
    "00001001111000000000000000000000000000100000000000001000000000000000000000000000",
    "00010011111001000001011001111100011111100011110001011111011111100100000101111110",
    "00011111111111000001100010000010100000100100001001001000000000010100000100000001",
    "00000000000000000001000010000010100000100100001001001000000000010100000100000001",
    "00000000000000000001000010000010100000100100001001001000001111110100000100111111",
    "01111110000000000001000011111000100000100100001001001000010000010100000101000001",
    "00111110011001100001000010000000100000100100001001001000010000010100000101000001",
    "00111100011001100001000010000000100000100100001001001000010000010100000101000001",
    "00011110000000000001000010000000100000100100001001001000010000010100000101000001",
    "00011111111111000001000001111100011111100111110001000111001111110011111100111111",
    "00011111111110000000000000000000000000000100000000000000000000000000000100000000",
    "00000000000000000000000000000000000000000100000000000000000000000000000100000000",
    "00000000000000000000000000000000000000000000000000000000000000000000000000000000");

Which looks like this: 

.. figure:: img/VgaImage3.png
    :alt: Logo
    :align: center
    :width: 50%

For the monitor to work correctly, it is necessary to send synchronization pulses at the exact time, for the exact duration (*vga_vhdl.vhd*).

.. code-block:: vhdl

    --signals to synchronize the screen
    hsync <= '1' when hst_sig >= Hf and hst_sig < Hf + Hs else '0';
    vsync <= '1' when vst_sig >= Vf and vst_sig < Vf + Vs else '0';
    rgb_out <= rgb_in;
    end Behavioral;


These two code files are packed in a separate IP and have the following simple block diagram.

.. figure:: img/VgaImage4.png
    :alt: Logo
    :align: center

Before synthesizing the project, do not forget to create a wrapper over the block design (if it is not already created). Otherwise, the top module will not be found

.. figure:: img/VgaImage5.png
    :alt: Logo
    :align: center



.. tabs::

    .. tab:: OS version 1.04 or older

        Please note that you need to change the forward slashes to backward slashes on Windows.

        1. Open Terminal or CMD and go to the .bit file location.

        .. code-block:: bash
    
            cd <Path/to/RedPitaya/repository>/prj/Examples/VGA_image/tmp/VGA_image/VGA_image.runs/impl_1

        2. Send the .bit file to the Red Pitaya with the ``scp`` command or use WinSCP or a similar tool to perform the operation.

        .. code-block:: bash

            scp system_wrapper.bit root@rp-xxxxxx.local:/root/VGA_image.bit

        3. Now establish an SSH communication with your Red Pitaya and check if you have the copy *VGA_image.bit* in the root directory.

        .. code-block:: bash

            redpitaya> ls

        4. Load the *VGA_image.bit* to **xdevcfg** with

        .. code-block:: bash

            redpitaya> cat VGA_image.bit > /dev/xdevcfg

    .. tab:: OS version 2.00

        The 2.00 OS uses a new mechanism of loading the FPGA. The process will depend on whether you are using Linux or Windows as the ``echo`` command functinality differs bewteen the two.

        Please note that you need to change the forward slashes to backward slashes on Windows.

        1. On Windows, open **Vivado** and use the **TCL console**. Alternatively, use **Vivado HSL Command Prompt** (use Windows search to find it). Navigate to the *.bit* file location.

           On Linux, open the **Terminal** and go to the *.bit* file location.

           .. code-block:: bash

               cd <Path/to/RedPitaya/repository>/prj/Examples/VGA_image/tmp/VGA_image/VGA_image.runs/impl_1

        2. Create *.bif* file and use it to generate a binary bitstream file (*system_wrapper.bit.bin*)

           **Windows (Vivado TCL console or Vivado HSL Command Prompt):**

           .. code-block:: bash

               echo all:{ system_wrapper.bit } >  system_wrapper.bif
               bootgen -image system_wrapper.bif -arch zynq -process_bitstream bin -o system_wrapper.bit.bin -w

           **Linux and Windows (WSL + Normal CMD):**

           .. code-block:: bash

               echo -n "all:{ system_wrapper.bit }" >  system_wrapper.bif
               bootgen -image system_wrapper.bif -arch zynq -process_bitstream bin -o system_wrapper.bit.bin -w

        3. Using a standard command prompt, send the *.bit.bin* file to the Red Pitaya with the ``scp`` command or use WinSCP or a similar tool to perform the operation.

           .. code-block:: bash
   
               scp system_wrapper.bit.bin root@rp-xxxxxx.local:/root/VGA_image.bit.bin

        4. Now establish an SSH communication with your Red Pitaya and check if you have the copy *VGA_image.bit.bin* in the root directory (you can use Putty or WSL).

           .. code-block:: bash

               redpitaya> ls

        5. Finally, we are ready to program the FPGA with our own bitstream file located in the **/root/** folder on Red Pitaya. 
           To program the FPGA simply execute the following line in the Red Pitaya Linux terminal that will load the *VGA_image.bit.bin* image into the FPGA:

           .. code-block:: bash

               redpitaya> fpgautil -b VGA_image.bit.bin


If everything is working correctly, you should see a Red Pitaya logo image displayed on your monitor after the cable is connected.


Automatic generation of the example from the repository
==========================================================

- First, download the |RP FPGA| to your computer and navigate to the **RedPitaya-FPGA/prj/Examples** folder.
- Open the **make_project.tcl** file, uncomment the line *"set project_name Vga_image"*, and comment all other "set project" lines.
- Open *Vivado 2020.1* and in Vivado Tcl Console navigate to the base folder: **RedPitaya-FPGA/prj/Examples**. 

.. |RP FPGA| raw:: html

   <a href="https://github.com/RedPitaya/RedPitaya-FPGA" target="_blank">Red Pitaya FPGA Git repository</a>


.. figure:: img/VgaImage2.png
    :alt: Logo
    :align: center

- Then run the script by typing into the following command into the TCL console. If the TCL console is not open got to *Tools → Run Tcl Script*:

  .. code-block:: shell-session

      source make_project.tcl

.. figure:: img/LedBlink2.png
    :alt: Logo
    :align: center

- **make_project.tcl** automatically generates a complete project in the **RedPitaya-FPGA/prj/Examples/Vga_image/** directory.

Take a moment to examine the block design.

If the Block Design is not open, click on **Flow => Open Block Design** from the top menu or select **Open Block Design** on the left-hand side of the window (under *IP INTEGRATOR*). When you are ready, click **Generate Bitstream** at the bottom-left part of the window to generate a bitstream file.

After you confirm that both Synthesis and Implementation will be executed beforehand, the longer process starts. After successful completion of synthesis, implementation, and bitstream generation, the bit file can be found at **Examples/Vga_image/tmp/Vga_image/Vga_image.runs/impl_1/system_wrapper.bit**.

Finally, we are ready to program the FPGA with our own bitstream file.


Conclusion
===========

Congratulations!!! You have successfully created the VGA image project!

If you want to roll back to the official Red Pitaya FPGA program, run the following command:

.. tabs::

    .. group-tab:: OS version 1.04 or older

        .. code-block:: shell-session

            redpitaya> cat /opt/redpitaya/fpga/fpga_0.94.bit > /dev/xdevcfg

    .. group-tab:: OS version 2.00

        .. code-block:: shell-session

            redpitaya> overlay.sh v0.94

or simply restart your Red Pitaya.


Author & Source
===============

Original author: Jaka Koren

Original lesson: `link <https://lniv.fe.uni-lj.si/xilinx/tutorial-jkoren.htm>`_
