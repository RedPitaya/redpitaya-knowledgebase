.. _vga_draw:

#########
VGA draw
#########

This is a continuation of the project → :ref:`vga image <vga_image>`


====================
Building the Project
====================

Move to folder RedPitaya/fpga/prj/Examples. 
Uncomment the line "set project_name Vga_draw" and comment all files in the make_project.tcl file. 
Open Vivado and in Vivado Tcl Console navigate to the base folder: *RedPitaya/fpga/prj/Examples*. 

.. figure:: img/VgaImage2.png
    :alt: Logo
    :align: center

Then run the script source make_project.tcl. Tools → Run Tcl Script.


=====================
Step by step tutorial
=====================

After the previous project started working, I wanted to be able to change the picture pattern, picture size and location on the screen. 
I added a few more ports which will be later controlled through AXI_GPIO, with Vitis application.

.. code-block:: vhdl

    entity picture is
        Port (
            clk50: in STD_LOGIC;
            data_position: in unsigned(16 downto 0);
            Offset: in unsigned(15 downto 0);
            size: in unsigned(15 downto 0);
            data_in: in STD_LOGIC;
            hst: out unsigned(10 downto 0);
            vst: out unsigned(9 downto 0);
            rgb: out STD_LOGIC_VECTOR(2 downto 0));
    end picture;


* clk50 - 50 MHz clock
* data_position - position to write the data + Write enable bit
* Offset - picture location on the screen
* size - picture size
* data_in - "1" or "0" that are written in array
* hst, vst - current position on the screen
* rgb - signal to be displayed on the screen


I created another block design and connect. It is as seen in the picture.

.. figure:: img/VgaDraw1.png
    :alt: Logo
    :align: center


Block diagram explained
***********************


If you are doing your block design for the first time, 
I reccomend the Zynq book as a good starting point, because it explains basic step how to build a project in vivado.

Ok, let's explain block diagram:

1. First we start with the Zynq7 processing system, these are the brains.
2. I added three AXI_GPIO blocks
    ◦ The first one is connected to on board leds, and it is there just to check if the program is running
    ◦ The second one has two outputs, first one is controlling where and when we write our data to array, on second, the actual data is comming in.
    ◦ The third one also has two outputs, the first one controls the position on the screen, the second one picture size.
3. pictureIP is used to save picture, and to read from the array
4. VGA IP is used to set signals to synchronize the screen and output the data.
5. There is another IP, Clocking Wizard. Linux sets the clock on the FCLK_CLK0 port to 125 MHz, and because we need 50 MHz, we place a Clocking Wizard to lower the clock frequency to the desired rate.


Picture IP and VGA IP located in *RedPitaya\fpga\prj\Examples\Vga_draw*

Setting 50 MHz clock
***********************

First we need to set the source clock from the ZYNQ7 IP.

.. figure:: img/VgaDraw2.png
    :alt: Logo
    :align: center

After setting the 125 MHz clock we have to devide it to 50 MHz that is used in our case. For this we use the Clocking Wizard.

.. figure:: img/VgaDraw3.png
    :alt: Logo
    :align: center

.. figure:: img/VgaDraw4.png
    :alt: Logo
    :align: center


Exporting hardware
***********************

Go to File → Export → Export Hardware

.. figure:: img/VgaDraw5.png
    :alt: Logo
    :align: center

Use a fixed platform type.

.. figure:: img/VgaDraw6.png
    :alt: Logo
    :align: center

Select Include bitstream

.. figure:: img/VgaDraw7.png
    :alt: Logo
    :align: center

Complete the instructions and note the location of the file. In my case, a file named design_1_wrapper

Creating Vitis platform project
*******************************

Start vitis

.. figure:: img/VgaDraw8.png
    :alt: Logo
    :align: center

Press → Create Platform Project
Set the project name and choose **Create from hardware specification (XSA)**
Then point to the generated xsa file (Do not forget to specify the operating system as Linux):

.. figure:: img/VgaDraw9.png
    :alt: Logo
    :align: center

And press finish


The last step is building:

.. figure:: img/VgaDraw10.png
    :alt: Logo
    :align: center

Now we can use the resulting platform to write a program.


Creating Vitis application project
**********************************

Go to File → New → Application project. Click next and select the platform you just created

.. figure:: img/VgaDraw11.png
    :alt: Logo
    :align: center

Press next and set the project name. Leave the rest of the parameters by default.
The next step is choosing a template. I use an empty application.


Copies to the project main.c from the project *RedPitaya/fpga/prj/Examples/Vga_draw/Vitis_sources*

We need the math.h library, so open the Properties of the project and add m

.. figure:: img/VgaDraw12.png
    :alt: Logo
    :align: center

The project should compile.



Vitis code explained
********************

For every AXI_GPIO we have to define its address and its size as is shown below

.. code-block:: c

    static unsigned long addr;
    static unsigned long addr_2;
    static unsigned long addr_3;

    addr = 0x41200000;  
    addr_2 = 0x41220000;	
    addr_3 = 0x41210000;

This is how we define dual port. Second port is shifted by 0x0008.

.. code-block:: c

    data_position = map_base_2 + (addr_2 & MAP_MASK_2);
    data_in = map_base_2 + ((addr_2 + 0x0008) & MAP_MASK_2);



How to run an application on Red Pitaya
****************************************

For running the program on Red Pitaya I used Winscp, to transfer a *.bit* file from vivado and *.elf* file from SDK on the board.

Then open Putty, and run the application.

Go to folder where you saved files on Red Pitaya and type:

.. code-block:: bash
    
    cat <file_name.bit> >/dev/xdevcfg
    chmod +x <file_name.elf>
    ./ <file_name.elf>