The BJT transistor connected as a diode
#######################################

Objective
__________

The purpose of this activity is to investigate the forward and reverse
current vs. voltage characteristics of a bipolar junction transistor
(BJT) connected as a diode.


Notes
______

.. _hardware: http://redpitaya.readthedocs.io/en/latest/doc/developerGuide/125-10/top.html
.. _Oscilloscope: http://redpitaya.readthedocs.io/en/latest/doc/appsFeatures/apps-featured/oscSigGen/osc.html
.. _Signal: http://redpitaya.readthedocs.io/en/latest/doc/appsFeatures/apps-featured/oscSigGen/osc.html
.. _generator: http://redpitaya.readthedocs.io/en/latest/doc/appsFeatures/apps-featured/oscSigGen/osc.html
.. _here: http://redpitaya.readthedocs.io/en/latest/doc/developerGuide/125-14/extent.html#extension-connector-e2
.. _simple: http://red-pitaya-active-learning.readthedocs.io/en/latest/Activity20_DiodeRectifiers.html
.. _rectifier: http://red-pitaya-active-learning.readthedocs.io/en/latest/Activity20_DiodeRectifiers.html
.. _OP484: http://www.analog.com/media/en/technical-documentation/data-sheets/OP184_284_484.pdf
.. _inverting: http://red-pitaya-active-learning.readthedocs.io/en/latest/Activity13_BasicOPAmpConfigurations.html#inverting-amplifier
.. _Jupyter: http://jupyter.org/index.html
.. _Notebook: http://jupyter.org/index.html


In this tutorials we use the terminology taken from the user manual
when referring to the connections to the Red Pitaya STEMlab board
hardware_.

Oscilloscope_ & Signal_ generator_ application is used for generating
and observing signals on the circuit.

Extension connector pins used for **+5V**, **-3.3V** and **+3.3V**
voltage supply are show in the documentation here_.


.. note:: 
   Red Pitaya STEMlab outputs can generate voltage signals with
   maximal output range of +/- 1V (2Vpp). For this experiment the
   higher signal amplitudes are required. Because of that we will use
   an OP484_ in the inverting_ opamp configuration to enable OUT1/OUT2
   signal amplification achieving voltage swing between +4.7V  to
   -3.2V. An OP484 will be supplied from STEMlab +5V and -3.3V voltage
   rails. Gain of the inverting amplifier will be set to ~5, where
   :math:`R_i  = 2.2k \Omega` and :math:`R_f  = 10k \Omega`
	 
   Try to answer why we have used an OP484 instead for example OP27 or
   OP97. (hint "rail-to-rail").
   

The Diode Connected NPN transistor
___________________________________

Materials
----------

- Red Pitaya STEMlab 
- 1x OP484_ quad rail-rail op-amp
- 1x 1kΩ Resistor
- 1x 10kΩ Resistor
- 1x 2.2kΩ Resistor
- 1x small signal NPN transistor (2N3904)
- 1x small signal PNP transistor (2N3906)
- 1x Solder-less Breadboard
- 1x 9V battery

An NPN transistor connected as is shown on figure 1 will behave as an
regular diode. We can show that by measuring the NPN response using
Oscilloscope & Signal generator application.


.. figure:: img/Activity_22_Fig_01.png
   :name: 22_fig_01
   :align: center

   NPN as a diode connection diagram 

   
.. note::
   Note that amplification circuit shown on figure 1 (left) is not the
   main subject of this experiment. This circuit is added only to
   amplify OUT1 signal.
   
   From here you can consider point :math:`-5xV_{OUT1}` as your main
   excitation signal.
   


Procedure
----------

1. Build the circuit from figure 1 on the breadboard. Set R1=2.2kΩ,
   R2=10kΩ and R3=1kΩ
   

   .. figure:: img/Activity_22_Fig_02.png
      :name: 22_fig_02
      :align: center

      NPN as a diode connection on the breadboard 

   
   .. warning::
      Before connecting the circuit to the STEMlab -3.3V and +3.3V  pins
      double check your circuit. The  -3.3V and +3.3V  voltage supply
      pins do not have short circuit handling and they can be damaged in
      case of short circuit.
   

2. Start the Oscilloscope & Signal generator application
   
3. In the OUT1 settings menu set Amplitude value to 0.8V, DC offset to
   -0.12 V, Frequency to 1kHz to apply the input voltage.
   
   From the waveform menu select TRIANGLE, deselect SHOW and select
   enable.
   
4. On the left bottom of the screen be sure that  IN1, IN2 and MATH
   V/div are set to 1V/div (You can set V/div by selecting the desired
   channel and using vertical +/- controls)
   
5. Set t/div value to 200us/div (You can set t/div using horizontal
   +/- controls)
   
6. Under MATH channel settings set :math:`IN1-IN2` and select ENABLE.
   
7. Under IN1 and IN2 menu settings set probe to x10 and vertical
   offset to 0.
   

   .. figure:: img/Activity_22_Fig_03.png
      :name: 22_fig_03
      :align: center

      NPN as a diode measurements

.. _previous: http://red-pitaya-active-learning.readthedocs.io/en/latest/Activity19_Diodes.html#procedure-time-domain-measurements

From figure 3 we can see that NPN BJT transistor in configuration
shown on figure 1 behaves as an diode.

Compare results with the diode measurements form previous_ experiment.


VI curve measurements
-----------------------

Since BJT can behave as an diode (configuration shown on figure 1) we
can measure its VI characteristic as we did when performing diode
measurements.

For this task we will use Jupyter Notebook Web application. How to
start Jupyter Notebook and create new project is shown on figure 4
flow chart.


.. note::
   The Jupyter_ Notebook_ is a web application that allows you to
   create and share documents that contain live code, equations,
   visualizations and explanatory text. They have also ensured support
   for the Jupyter application with Red Pitaya libraries enabling
   control of all features of the STEMlab boards such as: signal
   acquisition, signal generation, digital signal control,
   communication etc. The Jupyter Notebook is started on the same way
   as any other applications. After starting Jupyter application a web
   based notebook is opened.  This combination of the notebook,
   STEMlab and Python features makes the STEMlab an excellent tool for
   prototyping and quick programing. Since Jupyter Notebook enables
   text, equation and picture editing this is a perfect tool for
   tutorials, examples and ect.
   

.. figure:: img/Activity_19_Fig_07.png
   :name: 22_fig_04
   :align: center

   Creating new Jupyter notebook

   
If you have successfully created new Jupyter notebook then copy-paste
code bellow and run it.

Code bellow will generate same signal as from figure 6 but it will
plot them in XY graph.

For measuring :math:`VI` curve an "XY" plot is required where x-axis
will represent diode voltage :math:`IN_2` and y-axis a diode current
:math:`(IN_1 - IN_2) / R_3`.
      
     

**Copy code from below into cell 1**

.. literalinclude:: code/Activity_22_Code_01.py
   :language: python
   :linenos:
	  
       
Create new cell (Insert -> Cell Below) and copy code from below into it.

.. literalinclude:: code/Activity_22_Code_02.py
   :language: python
   :linenos:


Run Cell 1 and Cell 2. Notice cell 2 is a main loop for the
acquisition and re-plotting. If you stop the acquisition just run
only cell 2 for starting measurements again.   


After running the code above you should get diode VI characteristic as
is shown on figure 5.


.. figure:: img/Activity_22_Fig_05.png
   :name: 22_fig_05
   :align: center

   VI characteristic measured using Jupyter Notebook

   
On figure 5 BJT  VI characteristic measured in a diode configuration
is shown. Compare this results with diode VI characteristic.

Again we can see hysteresis appearing. Explain why we want to use
transistors as diodes?


Reverse Breakdown Characteristics
---------------------------------

Here we will investigate the reverse break down voltage
characteristics of the emitter base junction of a bipolar junction
transistor (BJT) connected as a diode.


Set up the breadboard as it is shown on figure 6. **The emitter is
connected to the positive battery terminal.**

The the NPN's is likely to have breakdown voltage higher then 10 V and
it may happen that our maximum voltage range will not be sufficient
i.e we will not be able to reverse polarize Q1 above breakdown
voltage. Because of that we have added additional battery to bring up
emitter potential close to the breakdown voltage so when, at some
point our :math:`V_{OUT}` signal goes NEGATIVE the transistor will be
REVERSED PLOARIZIED but differential voltage :math:`V_{E-BC} = V_E -
V_{BC}` will be larger than BREAKDOWN voltage and transistor will
starts conducting.


For example without battery i.e when emitter is on GND we can reverse
polarize Q1 by amount:


.. math::
   :label: 22_eq_01
	   
   V_{E-BC} = V_E - V_{BC} = 0 - (-3.3V) = 3.3V  \quad \text{of} \quad \text{reverse polarization}

With battery added we can achieve reversed polarization by maximal amount

.. math::
   :label: 22_eq_02
	   
   V_{E-BC} = V_E - V_{BC} = 9 - (-3.3V) = 12.3V  \quad \text{of} \quad \text{reverse polarization}


Where :math:`V_{BC}` is maximal negative swing of our excitation
voltage signal :math:`V_{OUT}`.


.. figure:: img/Activity_22_Fig_06.png
   :name: 22_fig_06
   :align: center
		  
   NPN Emitter Base Reverse breakdown configuration 


Procedure
---------

Build the circuit from the figure 6 on the breadboard and continue
with the measurements.


.. figure:: img/Activity_22_Fig_07.png
   :name: 22_fig_07
   :align: center

   NPN Emitter Base Reverse breakdown configuration on the breadboard
   

For this task we will use Jupyter Notebook Web application. How to
start Jupyter Notebook and create new project is shown on figure 4
flow chart.

Since you already have Jupyter Notebook running from previews example
only small update of the code is needed.


.. note::
   You should stop Jupyter Notebook by selecting **Stop** icon on the menu bar.
   After that update **Cell 2** as is shown bellow:

   
.. literalinclude:: code/Activity_22_Code_03.py
   :language: python
   :linenos:

      
As you can see from code above **we have only added "-9"** in order to
take into account battery potential when plotting is executed.

Select Cell 2 and pres **Play** icon on the menu bar. Notice, cell 2
is a main loop for the acquisition and re-plotting. If you stop the
acquisition just run only cell 2 for starting measurements again.

Be sure to measure the actual battery voltage for the most accurate
measurements.

If you have updated Jupyter Notebook code and run it correctly you
should get results similar as is shown on figure 8.


.. figure:: img/Activity_22_Fig_08.png
   :name: 22_fig_08
   :align: center

   NPN Emitter Base Reverse breakdown voltage measurements
   

From figure 8 we can see that reversed breakdown voltage of NPN BJT
2N3904 transistor is around  10V.


Question
--------

Disconnect the collector of Q1 and leave it open. How does this change
the breakdown voltage?



Lowering the effective forward voltage of the diode
___________________________________________________

Here we will investigate a circuit configuration with smaller forward
voltage characteristics than that of a bipolar junction transistor
(BJT) connected as a diode. The turn on voltage of the “diode” is
should be about ~0.1V compared to ~0.7V for the simple diode
connection in the first example.


.. figure:: img/Activity_22_Fig_09.png
   :name: 22_fig_09
   :align: center

   Configuration to lower effective forward voltage drop of diode 


Procedure
---------

1. Build the circuit from figure 9 on the breadboard. Set
   R3=1kΩ,R4=100kΩ and use for Q1 2N3904 NPN and for Q2 2N3904 PNP
   transistor.
   

   .. figure:: img/Activity_22_Fig_10.png
      :name: 22_fig_10

      Configuration to lower effective forward voltage drop of diode
      on the breadboard
      

   .. warning::
      Before connecting the circuit to the STEMlab -3.3V and +3.3V  pins
      double check your circuit. The  -3.3V and +3.3V  voltage supply
      pins do not have short circuit handling and they can be damaged in
      case of short circuit.
   

2. Start the Oscilloscope & Signal generator application.
   
3. In the OUT1 settings menu set Amplitude value to 0.8V, DC offset to
   -0.12 V, Frequency to 1kHz to apply the input voltage.
   
   From the waveform menu select TRIANGLE, deselect SHOW and select
   enable.
   
4. On the left bottom of the screen be sure that  IN1 V/div is set to
   1V/div and IN2 V/div is set to 500mV/div (You can set V/div by
   selecting the desired channel and using vertical +/- controls).
   
5. Set t/div value to 200us/div (You can set t/div using horizontal
   +/- controls).
   
6. Under IN1 and IN2 menu settings set probe to x10 and vertical
   offset to 0.
   
7. Under MATH menu settings set vertical offset to 0.

   
   .. figure:: img/Activity_22_Fig_11.png
      :name: 22_fig_11
      :align: center

      Lower effective forward voltage drop of diode measurements
      

   .. note::

      As you can see from the figure 11 the forward voltage drop is about
      100mV. You can also notice that Q2 is not necessary to lower
      drop-down voltage of the Q1.
   
      The main role here plays resistor R4 connected to the base of the
      Q1. Try to remove Q2 and observe results.
   

   
Question
--------

Could the collector of the PNP Q2 be connected to some other node
such as a negative supply voltage? And what would be the effect?
   
