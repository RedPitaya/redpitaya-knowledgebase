Transient Response of RC Circuit
################################


Objective
_________

The objective of this Lab activity is to study the transient response of a series RC circuit and understand the time constant concept using pulse waveforms.

Notes
_____

.. _hardware: http://redpitaya.readthedocs.io/en/latest/doc/developerGuide/125-10/top.html

In this tutorials we use the terminology taken from the user manual when referring to the connections to the Red Pitaya STEMlab board hardware_.
Oscilloscope & Signal generator application is used for generating and observing signals on the circuit. 


Background
__________

In this lab activity you will apply a pulse waveform to the RC circuit to analyses the transient response of the circuit. The pulse-width relative to a circuit's time constant determines how it is affected by an RC circuit. 

Time Constant (t): A measure of time required for certain changes in voltages and currents in RC and RL circuits. Generally, when the elapsed time exceeds five time constants (5t) after switching has occurred, the currents and voltages have reached their final value, which is also called steady-state response. 

The time constant of an RC circuit is the product of equivalent capacitance and the Thévenin resistance as viewed from the terminals of the equivalent capacitor. 

.. math::
	
	t = R \cdot C 

A Pulse is a voltage or current that changes from one level to another and back again. If a waveform's high time equals its low time it is called a square wave. The length of each cycle of a pulse is its period (T). 

The pulse width (tp) of an ideal square wave is equal to half the time period. 

The relation between pulse width and frequency is then given by, 

.. math::
	
	f = \frac{1}{2t_p} 

.. figure:: img/Activity_06_Fig_01.png

Figure 1: Series RC circuit.

From Kirchhoff's laws, it can be shown that the charging voltage V\ :sub:`C`\ (t) across the capacitor is given by: 

.. math::	
	V_C (t) = V( 1- e^{- \frac{t}{RC}})  ;t >= 0 

where, V is the applied source voltage to the circuit for t = 0. RC = t is the time constant. The response curve is increasing and is shown in figure 2. 

.. figure:: img/Activity_06_Fig_02.png

Figure 2: Capacitor charging for Series RC circuit to a step input with time axis normalized by t

The discharge voltage for the capacitor is given by: 

.. math::

	V_C (t) = V_o e^{-\frac{t}{RC}} ;t >= 0 

Where V\ :sub:`0`\  is the initial voltage stored in capacitor at t = 0, and RC = t is time constant. The response curve is a decaying exponential as shown in figure 3. 

.. figure:: img/Activity_06_Fig_03.png

Figure 3: Capacitor Discharging for Series RC circuit

Materials
_________

Red Pitaya STEMlab 125-14 or STEMlab 125-10 

Resistors: 
	2.2 KΩ, 
	10 KΩ

Capacitors: 
	1 µF, 
	0.01 µF 

Procedure
_________

1. Set up the circuit shown in figure 4 on your solderless breadboard with the component values R\ :sub:`1`\ = 2.2 KΩ and C\ :sub:`1`\ = 1 µF. 

	-Connect the Oscilloscope & Signal generator probes as is shown in figure 5.
	-Set the oscilloscope attenuation to x1.

.. figure::   img/Activity_06_Fig_04.png

Figure 4. Breadboard diagram of RC circuit  R\ :sub:`1`\ = 2.2 KΩ and C\ :sub:`1`\ = 1 µF. 


.. figure::   img/Activity_06_Fig_05.png

Figure 5. Breadboard RC circuit R\ :sub:`1`\ = 2.2 KΩ and C\ :sub:`1`\ = 1 µF. 

Start the Oscilloscope & Signal Generator application. 

2. In the OUT1 settings menu set DC offset value to 0.5 and Amplitude  value to 0.5V to apply a 1Vp-p square wave centered on 0.5 V as the input voltage to the circuit. From the waveform menu select SQUARE signal, deselect SHOW button and select enable. 
On the left bottom of the screen be sure that IN1 V/div and IN2 V/div are both set to 200mV/div (You can set V/div by selecting the desired channel and using vertical +/- controls)
In the IN1 and IN2 settings menu set the value of Vertical Offset to -500mV 
For the stable acquisition set the trigger level in TRIGGER menu to 0.5V and select NORMAL.

3. Observe the response of the circuit for the following three cases and record the results. 

a. Pulse width larger than 5t (for example 15t) : Set the frequency of OUT1 output such that the capacitor has enough time to fully charge and discharge during each cycle of the square wave. So let the pulse width be 15t and set the frequency according to equation (2). The value you have found should be approximately 15 Hz. 

Notice: Calculate frequency of OUT1 so that the pulse width of OUT1 is equal to desired 
value of x*t by equation (2):

.. math::

	f_out = \frac{1}{2 \cdot x \cdot t} 

For example: If we want to have pulse width of your OUT1 square signal equals 5*t 
(t - time constant of RC circuit  t = R * C)

.. math::

	t = R \cdot C = 2.2E3 \cdot 1E-6 = 2.2E-3

.. math::

	f_out  = \frac{1}{2 \cdot 5 \cdot 2.2E-3} = 45Hz

Determine the time constant from the waveforms obtained on the screen if you can. If you cannot obtain the time constant easily, explain possible reasons. 

For determining time constant use “CURSOR” option.
Open CURSOR menu and select all four cursors: X1, X2, Y1, Y2. 
For Y cursor select IN2 for source.
Control/Move cursors using an left click+hold mouse control on the cursor marker(an arrow on the end of the cursor line).



Adjust the **time base** using **horizontal +/-** control until you have at approximately two cycles of the square wave on the display grid. 

.. figure::   img/Activity_06_Fig_06.png

Figure 6. Oscilloscope interface and signals IN1 and IN2 on  RC circuit 

In order to set cursors more accurately adjust the time base  until you have approximately  one or  half of the cycle of the square wave on the display grid. 

.. figure::   img/Activity_06_Fig_07.png

Figure 7: Measuring the time constant t for OUT1 pulse width >> 5t . 

Set cursor as is shown in figure 2 readout  delta values and calculate time constant.


b. Pulse width =  5t : Set the frequency of OUT1 such that the pulse width = 5t (this should be approximately 45 Hz). Since the pulse width is 5t, the capacitor should just be able to fully charge and discharge during each pulse cycle. Using cursor tool determine t.

.. figure::   img/Activity_06_Fig_08.png

Figure 8: Measuring the time constant t for OUT1 pulse width =  5t


c. Pulse width less than 5t (for example 1t): In this case the capacitor does not have time to charge significantly before it is switched to discharge, and vice versa. Let the pulse width be only 1.0t in this case and set the frequency accordingly (this should be approximately 240 Hz). 

.. figure::   img/Activity_06_Fig_09.png

Figure 9: Measuring the time constant t for OUT1 pulse width =  1t


4. Repeat the procedure using  R\ :sub:`1`\ = 10 KΩ and C\ :sub:`1`\= 0.01 µF and record the measurements.
Questions:

	1. Calculate the time constant using equation (1) and compare it to the measured value from 3a. Repeat this for other set of R and C values.

	2. Discuss the effects of changing component values.


