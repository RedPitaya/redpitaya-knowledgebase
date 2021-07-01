BJT Common Emitter Amplifier
============================

Objective
---------

The purpose of this experiment is to investigate the common emitter
configuration using the BJT device.

Notes
-----

.. _hardware: http://redpitaya.readthedocs.io/en/latest/doc/developerGuide/125-10/top.html
.. _Oscilloscope: http://redpitaya.readthedocs.io/en/latest/doc/appsFeatures/apps-featured/oscSigGen/osc.html
.. _Signal: http://redpitaya.readthedocs.io/en/latest/doc/appsFeatures/apps-featured/oscSigGen/osc.html
.. _generator: http://redpitaya.readthedocs.io/en/latest/doc/appsFeatures/apps-featured/oscSigGen/osc.html
.. _here: http://redpitaya.readthedocs.io/en/latest/doc/developerGuide/125-14/extent.html#extension-connector-e2


In this tutorials we use the terminology taken from the user manual
when referring to the connections to the Red Pitaya STEMlab board
hardware_.

Oscilloscope_ & Signal_ generator_ application is used for generating
and observing signals on the circuit.

Extension connector pins used for **+5 V**, **-3.3 V** and **+3.3 V**
voltage supply are show in the documentation here_.  

Background
----------

The configuration, shown in Fig. 1, demonstrates an npn transistor
used as a common-emitter amplifier. Output load resistor :math:`R_L`
is chosen such that for the desired nominal collector current
:math:`I_C`, approximately one third of the +5 V voltage (1.6 V)
appears at :math:`V_{CE}` (at DC operating point condition). Resistor 
:math:`R_B` sets the nominal bias operating point for the
transistor (base current :math:`I_B`) to sink the required collector
current :math:`I_C`. The input signal is AC coupled to the base of
the transistor with capacitor :math:`C_1`  to not disturb **DC bias
conditions**. Voltage divider :math:`\frac{R_1}{R_2}` is chosen to
provide a self-biased DC operating point. Resistor :math:`R_E` is used
to add emitter degeneration (current feedback) in order to stabilize
the DC operating point.

The best approach for selecting the :math:`R_L` and :math:`R_E`
is to enable voltage drops across :math:`Q_1`, :math:`R_L` and
:math:`R_E` equal to the 1/3 of the :math:`V_{CC}` (at DC operating
point condition). Therefore :math:`R_E` = :math:`R_L`. Adding the emitter
degeneration resistor has improved the stability of the DC operating
point at the cost of reduced amplifier gain. A higher gain for AC
signals can be restored to some extent by adding capacitor
:math:`C_E` across the degeneration resistor :math:`R_E`, effectively 
setting the " :math:`R_E` " value close to zero for AC
signals. Capacitor :math:`C_2` is added to block the DC component 
of the output signal. 

.. _2N3904: https://www.sparkfun.com/datasheets/Components/2N3904.pdf
.. _The Signal Path: https://www.youtube.com/watch?v=Y2ELwLrZrEM&t=1213s

.. note:: 
    How to design an common-emitter amplifier is nicely explained in a
    video tutorial on `The Signal Path`_ Youtube channel. 


.. figure:: img/Activity_26_Fig_01.png

Figure 1: Common-emitter amplifier configuration 


Quick calculation of the common emitter amplifier
-------------------------------------------------

Suppose that we want to design an amplifier with the gain
:math:`A = 5` using npn transistor 2N3904_ and a voltage supply of 
:math:`V_{CC} = 5V`.


For the npn transistor 2N3904 we can assume that :math:`\beta = 100` and
:math:`v_{CE_{sat}} = 0.2 V`. First step is to set DC operating point
by deciding voltages across :math:`R_L`, :math:`R_E` and :math:`Q_1`.  

   
.. math::

   V_{R_L}+(V_{CE}+v_{CE_{sat}})+V_{R_E} = V_{CC}  \quad  (1)


If we take into account :math:`v_{CE_{sat}}` and 1/3 ratio of
voltages on :math:`R_L`, :math:`R_E` and :math:`Q_1` we get following:


.. math::
      
   1.6 V + 1.6 V + 0.2 V + 1.6 V = 5 V  \quad (2)


From desired value of gain :math:`A` we can calculate :math:`R_L`
using Eqs. (3) -- (7) 

.. math::
      
   A  = \beta \frac{R_{out}}{R_{in}}.  \quad (3)

where :math:`R_{out}` is the resistor connected in series with the
collector and :math:`R_{in}` is the resistor connected in series
with the base. 

.. math::

   R_{out} = R_L  \quad \text{and,} \quad R_{in} = R_{B} \quad (4)

It follows:

.. math::
      
   A  = \beta \frac{R_L}{R_B}   \quad (5)

In this step we need to **set current ratings of our amplifier**
i.e we need to choose :math:`I_C` to calculate :math:`R_L`. 

Let's set :math:`I_C = 5 mA`, then
 
.. math:: 
   
   R_L =  \frac{V_{R_L}}{I_C} = \frac{1.6V}{5mA} =  320 \Omega   \quad (6)


In order to satisfy Eq. (2) it follows that:

.. math:: 

   R_E = R_L, \quad  \text{i.e.} \quad R_E = \frac{V_{R_L}}{I_C} = 320  \Omega. \quad (7)

Now we can calculate :math:`R_{in}` i.e :math:`R_{B}` value as:


.. math:: 

   R_{B} = \beta \frac{R_L}{A} = 100 \frac{320 \Omega }{5} = 6.4k \Omega. \quad (8)


The last step is to calculate values of DC bias resistors
:math:`R_1` and :math:`R_2`. :math:`R_2` can be obtained from
"cookbook" relation given in Eq. (9) and therefore :math:`R_1`
can be calculated from Eq. (10). 


.. math:: 

   R_2 &\approx 10 R_E  \quad (9)

   R_2 &= 3.2 k \Omega     


.. math:: 

   R_1 = \frac{V_{CC} - (v_{BE}+V_{R_E})}{\frac{(v_{BE}+V_{R_E})}{R_2}}  \quad (10)

where :math:`v_{BE} = 0.6 V` 

.. math::
   
   R_1 = \frac{5V - (0.6V+1.6V)}{ \frac{(0.6V + 1.6V)}{3.2k \Omega}} = 4.0k \Omega     

 
.. note::
   Above shown calculation of the common emitter amplifier should be
   use as a guideline and not as a definitive design blueprint. The
   reason for this is that in majority of cases calculated values of
   the resistors will be outside of the resistors values available on
   the market. Therefore resistor values should be rounded or changed
   in order to fit them to the closes values of commonly available
   resistors. It is a good practice to set :math:`R_1` and
   :math:`R_B` as potentiometer since with this two resistors we can
   manually tune the amplifier. Tuning the amplifier is necessary
   since transistors can differ from each other.

   Selecting the values of capacitors :math:`C_1`, :math:`C_2` and
   :math:`C_E` is done by using high value capacitors while the
   maximum voltage rating of the capacitors must be larger than
   :math:`V_{CC}`. Commonly an electrolytic capacitors are used
   in ranges of :math:`\mu F`. If we want to bring (emitter - gnd)
   impedance (for AC) close to zero then :math:`C_E` must be large as
   possible. Also :math:`C_1` , :math:`C_2`  should be large to
   prevent large voltage drops across them. 

   
Materials
---------

- Red Pitaya STEMlab
  
- 2x 470Ω Resistor
  
- 2x 10kΩ Resistor
  
- 1x 10kΩ Trimer
  
- 1x 1kΩ Resistor
  
- 1x 10uF Capacitor
  
- 2x 4.7uF Capacitor
  
- 1x small signal npn transistor (2N3904_)
  
- 1x Solder-less Breadboard

  
Procedure
---------

Following calculations and guidelines above we have built common
emitter amplifier shown in figure 2. We had an :math:`470 \Omega`
resistors available and those resistors where used for :math:`R_L` and
:math:`R_E`. After selecting the :math:`R_L` and :math:`R_E` the other
components have been calculated and selected. 


.. figure:: img/Activity_26_Fig_02.png

Figure 2: Common emitter amplifier with components values


1. Build the circuit on from figure 2 on the breadboard.

.. figure:: img/Activity_26_Fig_03.png

Figure 3: Common emitter amplifier on the breadboard

2. Start the Oscilloscope & Signal generator application
   
3. In the OUT1 settings menu set Amplitude value to 0.1V, DC offset to
   0 V  and frequency to 10kHz to apply the input voltage. From the
   waveform menu select SINE, deselect SHOW button and select enable.
   
4. On the left bottom of the screen be sure that  IN1 and IN2 V/div
   are set to 200mV/div (You can set V/div by selecting the desired
   channel and using vertical +/- controls)
   
5. Set t/div value to 20us/div (You can set t/div using horizontal +/-
   controls)
   
6. In the trigger menu settings and select NORMAL
   
7. In the measurements menu select P2P for IN1 and IN2
   

.. figure:: img/Activity_26_Fig_04.png

Figure 4: Common emitter amplifier measurements

On figure 3 the measurements of the common emitter amplifier is
shown. From the P2P measurements we can calculate achieved gain and it
is approximately  :math:`A \approx 9`.


Questions
---------

1. Try to change value of :math:`R_{B_{pot}}` and observe the change
   in the gain?
   
2. What is the maximum voltage swing of the output signal?
   
3. Increase OUT1 frequency and try to measure amplifier bandwidth.
   

For question 2 follow next:

Set the **IN2 scope probe to x10, in the IN2 menu set probe
attenuation to 10**  and increase OUT1 amplitude to 0.2V. What is the
P2P value of the IN2? 


With gain :math:`A = 9`, input signal P2P amplitude 0.4V the output
P2P(IN2) value should be :math:`0.4 \times 9 = 3.6 V` ! But it is not?
Signal is cut off! Can you explain why?  

.. hint::
   
   Check the calculations above and voltages across :math:`V_{CE}`











        

