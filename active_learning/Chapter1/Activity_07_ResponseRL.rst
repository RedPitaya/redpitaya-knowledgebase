Transient Response of an RL Circuit
###################################

Objective
_________

The objective of this Lab activity is to study the transient response of inductor circuits using a series RL configuration and understand the time constant concept.

Notes
_____

.. _hardware: http://redpitaya.readthedocs.io/en/latest/doc/developerGuide/125-10/top.html

In this tutorials we use the terminology taken from the user manual when referring to the connections to the Red Pitaya STEMlab board hardware_.
Oscilloscope & Signal generator application is used for generating and observing signals on the circuit. 

Background
__________

This lab activity is similar to the RC Lab activity 5, except that the capacitor is replaced by an inductor. In this experiment, you will apply a square waveform to the RL circuit to analyze the transient response of the circuit. The pulse width relative to the circuit's time constant determines how it is affected by the RL circuit. 

Time Constant (t): It is a measure of time required for certain changes in voltages and currents in RC and RL circuits. Generally, when the elapsed time exceeds five time constants (5t) after switching has occurred, the currents and voltages have reached their final value, which is also called steady-state response. 
 
The time constant of an RL circuit is the equivalent inductance divided by the Thévenin resistance as viewed from the terminals of the equivalent inductor. 

.. math::
	f=\frac{L}{R} 



A Pulse is a voltage or current that changes from one level to another and back again. If a waveform's high time equals its low time, it is called a square wave. The length of each cycle of a pulse train is its period (T). The pulse width (tp) of an ideal square wave is equal to half the time period. 

The relation between pulse width and frequency for the square wave is given by: 
 
.. math::

	f=\frac{1}{2t_p} 
	

.. figure:: img/Activity_07_Fig_01.png

Figure 1: Series RL circuit

In an R-L circuit, voltage across the inductor decreases with time while in the RC circuit the voltage across the capacitor increased with time. Thus, current in an RL circuit has the same form as voltage in an RC circuit: they both rise to their final value exponentially.

The expression for the current in the Inductor is given by:

.. math::
	
	I_L(t) = RV( 1 - e^{-\frac{R}{L}t} )  ; t >= 0

where, V is the applied source voltage to the circuit for t = 0. The response curve is increasing and is shown in figure 2. 

.. figure:: img/Activity_07_Fig_02.png

Figure 2: Current in Inductor increasing in a Series RL circuit.

(Time axis normalized by t) 

The expression for the current decay across the Inductor is given by: 
 
.. math:: 
 
	I_L(t) = I_0 e^{- \frac{R}{L}t} ; t >= 0 

where,  I :sub: `0` is the initial current stored in the inductor at t = 0  
L/R = t is time constant. 
 
The response curve is a decaying exponential and is shown in figure 3. 

.. figure:: img/Activity_07_Fig_03.png

Since it is not possible to directly measure the current through the Inductor ( current supplied by driving source OUT1 ) with the STEMlab, we will measure output voltage across the Resistor in series with the Inductor. The resistor waveform will be same shape as the inductor current since from Ohm’s law we know that current and voltage through resistor are related with  V :sub:`R` = I :sub:`R` * R. Our circuit has two elements (Resistor and Inductor) in series which means same current is flowing through both components I :sub:`circuit` = I :sub:`L` = I :sub:`R` 
We know that signal on input IN2 is voltage across resistor V :sub:`R` which is in fact current through inductor multiplied by resistance R.

.. math::
	
	IN2 = R \cdot I_L 

From that it follows that when observing signal IN2 we are observing current through inductor, and only thing we need to have in mind is scaling factor - resistance R.
     
From the waveforms on the scope, we should be able to measure the time constant t which should be equal to t = L / R :sub:`total` .
Here, R :sub:`total` is the total resistance and can be calculated from R :sub:`total` = R :sub:`inductance`  + R.
R inductance is the measured value of inductor resistance and can be measured by using Multimeter  prior to running the experiment. (Measure R inductance same as you would measure normal resistor.)


Materials
_________

Red Pitaya STEMlab 125-14 or STEMlab 125-10 

Resistor 220 Ω

Inductor 20 mH ( 2x10 mH in series )

Procedure
_________

1. Measure the combined inductor and resistor resistance R \ :sub:`total` \ by using a Multimeter.




.. figure::   img/Activity_07_Fig_04.png

2. Set up the circuit shown in figure 5 on your solderless breadboard with the component values R :sub:`1` = 220 Ω and L :sub:`1` = 20mH. 
-Connect the Oscilloscope & Signal generator probes as is shown in Figure 5.
-Set the oscilloscope attenuation to x1.

Figure 5: Experiment Set-Up 

Start the Oscilloscope & Signal Generator application. 

3. In the OUT1 settings menu set DC offset value to 0.5 and Amplitude  value to 0.5V to apply a 1Vp-p square wave centered on 0.5 V as the input voltage to the circuit. From the waveform menu select SQUARE signal, deselect SHOW button and select enable. 
On the left bottom of the screen be sure that IN1 V/div and IN2 V/div are both set to 200mV/div (You can set V/div by selecting the desired channel and using vertical +/- controls)
In the IN1 and IN2 settings menu set the value of Vertical Offset to -500mV 
For the stable acquisition set the trigger level in TRIGGER menu to 0.5V and select NORMAL.

Calculate the applied frequency using equation (2) for tp = 5t . In the OUT1 settings menu set frequency according to the calculation.

Adjust the time base using horizontal +/- control until you have at approximately two cycles of the square wave on the display grid. 


4. The VR (IN2) waveform has the same shape as IL(t) waveform. From VR waveform measure time constant t and compare with the one that you calculated from L/R :sub:`total`. 

.. hint:: 
	
	When measuring RC transient effect we used cursor to find 0.63*Vc, here we are interested in current I :sub:`L` = IN2/R and not voltage. 
	According to the Figure 3 you should put cursor Y1 to the maximum value of IN2 and cursor Y2 to the 0.37*IN2. 
	Set the X1 and X2 cursors to the crossing points and measure time constant.


For determining time constant use “CURSOR” option.
Open CURSOR menu and select all four cursors: X1,X2,Y1,Y2. 
For  Y cursor select  IN2 for source.
Control/Move cursors using an left click+hold mouse control on the cursor marker(an arrow on the end of the cursor line).

In order to set cursors more accurately adjust the time base  until you have approximately  one or  half of the cycle of the square wave on the display grid. 


5. Observe the response of the circuit and record the results again for tp = 25t, and tp = 0.5t.

Questions
_________

• Include plots of IL and VR for different tp values given above in Procedure 4.
• A Capacitor stores charge. What do you think an Inductor stores? Answer in brief.



