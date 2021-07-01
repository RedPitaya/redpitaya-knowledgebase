Thévenin Equivalent Circuit and Maximum Power Transfer
######################################################

Objective
_________

The objective of this Lab activity is to verify Thévenin's theorem by obtaining the Thévenin equivalent voltage (V\ :sub:`TH`\) and Thévenin equivalent resistance (R\ :sub:`TH`\) for the given circuit. Verify the Maximum Power Transfer Theorem.

Notes
_____


.. _hardware: http://redpitaya.readthedocs.io/en/latest/doc/developerGuide/125-10/top.html
.. _here: http://redpitaya.readthedocs.io/en/latest/doc/developerGuide/125-14/extent.html#extension-connector-e2
.. _E1: http://redpitaya.readthedocs.io/en/latest/doc/developerGuide/125-14/extent.html#extension-connector-e1

In this tutorials we use the terminology taken from the user manual when referring to the connections to the Red Pitaya STEMlab board hardware_.
Extension connector pin used as 3.3 V voltage source are show in the documentation here_.


Background
__________

Thévenin's Theorem is a process by which a complex circuit is reduced to an equivalent circuit consisting of a single voltage source (V\ :sub:`TH`\) in series with a single resistance (R\ :sub:`TH`\) and a load resistance (R\ :sub:`L`\). After creating the Thévenin Equivalent Circuit, the load voltage V\ :sub:`L`\ or the load current Il may be easily determined. 

One of the principal uses of Thévenin's theorem is to replace a large portion of a circuit, often a more complicated and uninteresting part, by a simple equivalent. The new simpler circuit enables rapid calculations of the voltage, current, and power which the more complicated original circuit is able to deliver to a load. It also helps to choose the optimal value of the load (resistance) for maximum power transfer. 

.. figure::   img/Activity_05_Fig_01.png

	Figure 1.

.. figure::   img/Activity_05_Fig_02.png

	Figure 2: Thévenin Equivalent Circuit of Figure 1

2. The Maximum Power Transfer Theorem states that an independent voltage source in series with a resistance R\ :sub:`s`\ or an independent current source in parallel with a resistance Rs, delivers a maximum power to the load resistance R\ :sub:`L`\ when R\ :sub:`L`\ = R\ :sub:`s`\.

In terms of a Thévenin Equivalent Circuit, maximum power is delivered to the load resistance R\ :sub:`L`\ when R\ :sub:`L`\ is equal to the Thévenin equivalent resistance R\ :sub:`TH`\ of the circuit.

.. figure:: img/Activity_05_Fig_03.png
	
	Figure 3: Maximum Power Transfer
 
Materials
_________

Red Pitaya STEMlab 125-14 or STEMlab 125-10 

Various Resistors:

	100 Ω, 
	
	330 Ω, 
	
	470 Ω, 
	
	1 KΩ, 
	
	1.5 KΩ
	


Procedure
_________

1. Verifying the Thévenin's theorem:

a) Construct the circuit of figure 1 using the following component values:
 
R1 = 330 Ω
 
R2 = 100 Ω
 
R3 = 100 Ω
 
R4 = 330 Ω
 
R5 = 1 KΩ
 
Rl = 1.5 KΩ
 
Vs = +3.3V 

.. note:: 
	Instead of voltage source “V\ :sub:`s`\” shown on the Figure 1 use the STEMlab voltage pin on extension connector E1_. 

b) Accurately measure the voltage V\ :sub:`L`\ across the load resistance using Oscilloscope application.
Set oscilloscope probe attenuation x10
Start Oscilloscope application and in IN1 and IN2 settings menu select Probe attenuation x10


      Use the Oscilloscope application by connecting channel IN1 to the + node of V\ :sub:`L`\ and connect channel IN2 to the - node. V\ :sub:`L`\ will be the difference between IN1 volts and IN2 volts. This value will later be compared to the one you will find using Thevenin Equivalent.


c) Find V\ :sub:`TH`\: Remove the load resistance R\ :sub:`L`\ and measure the open circuit voltage VOC across the terminals. Use the Oscilloscope application by connecting channel IN1 to the + node of V\ :sub:`OC`\ and connect channel IN2 to the - node. V\ :sub:`OC`\ will be the difference between IN1 volts and IN2 volts. This is equal to V\ :sub:`TH`\. See figure 4

.. note:: 
	To get voltage values of IN1 and IN2 select MEAS menu, select MEAN value and select DONE.


.. figure::  img/Activity_05_Fig_04.png
	
	Figure 4: Measuring the Thevenin Voltage

d) Find R\ :sub:`TH`\: Remove the source voltage Vs and construct the circuit as shown in figure 5. Use the Multimeter to measure the resistance looking into the opening where R\ :sub:`L`\ was. This gives R\ :sub:`TH`\. Make sure there is no power applied to the circuit before measuring with the Multimeter and the ground connection has been moved as shown.


.. figure::  img/Activity_05_Fig_05.png

	Figure 5: Measuring the Thevenin Resistance R\ :sub:`TH`\. 
	
e) Obtaining V\ :sub:`TH`\ and R\ :sub:`TH`\, construct the circuit of figure 2. Create the value of R\ :sub:`rh`\ using a series and or parallel combination of resistors from your parts kit. 

Using the Oscilloscope & Signal generator application - connect channel OUT1  for the V\ :sub:`TH`\ source. In the OUT1 settings menu select “DC” signal waveform and in the Amplitude  field set the value to what you measured for V\ :sub:`TH`\ in step c).
Select “enable” button. 

.. figure::  img/Activity_05_Fig_06.png

Figure 6: Thevenin Equivalent Construction 

f) With R\ :sub:`L`  set to the 1.5 KΩ used in step b) measure the V\ :sub:`L` for the equivalent circuit and compare it to the V\ :sub:`L` obtained in step b). This verifies the Thévenin theorem.

g) Optional: Repeat steps 1 b) to 1 f) for R\ :sub:`L` = 2.2 KΩ
	

2. Verifying the Maximum Power Transfer theorem:
	
a) Construct the circuit as in figure 7 using the following values:

Vs = +3.3 V

R\ :sub:`1`\  = R\ :sub:`2`\  = 100 Ω

R\ :sub:`3`\  = 1 KΩ

R\ :sub:`L`\ = combinations of 1 KΩ and 100 Ω resistors ( figure 8 )

.. figure::  img/Activity_05_Fig_07.png

Figure 8. Rl configurations

d) Calculate the power for each load resistor value using;

.. math::
	P_L = \frac{V_L^{2}}{R_L}

Then, interpolate between your measurements to calculate the load resistor value corresponding to the maximum power (P\ :sub:`l max`\). This value should be equal to R\ :sub:`TH` of circuit in figure 7 with respect to load terminals.

Questions
_________

1. Calculate the percentage error difference between the load voltages obtained for circuits of figure 1 and figure 2.
2. Using Voltage Division for circuit of figure 2, calculate V\ :sub:`L`\. Compare it to the measured values. Explain any differences.
3. Calculate the maximum power transmitted to the load Rl obtained for the circuit of figure 3.

