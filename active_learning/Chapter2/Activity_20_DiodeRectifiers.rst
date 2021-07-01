Diode Rectifiers
##################

Objective
__________


The objective of this experiment is to investigate half wave and full wave diode rectifiers used to convert AC to DC. 

Notes
______

.. _hardware: http://redpitaya.readthedocs.io/en/latest/doc/developerGuide/125-10/top.html
.. _Oscilloscope: http://redpitaya.readthedocs.io/en/latest/doc/appsFeatures/apps-featured/oscSigGen/osc.html
.. _Signal: http://redpitaya.readthedocs.io/en/latest/doc/appsFeatures/apps-featured/oscSigGen/osc.html
.. _generator: http://redpitaya.readthedocs.io/en/latest/doc/appsFeatures/apps-featured/oscSigGen/osc.html

In this tutorials we use the terminology taken from the user manual when referring to the connections to the Red Pitaya STEMlab board hardware_.
Oscilloscope_ & Signal_ generator_ application is used for generating and observing signals on the circuit.

Materials
___________

- Red Pitaya STEMlab 
- Resistor:  1x 1 :math:`k \Omega`
- Small signal diode: 4x (1N914 or similar) 



Half wave rectifier
____________________

Directions
-----------

Set up the breadboard with OUT1 and IN2 channels attached to one end of the diode. The other end of the diode is connected to one end of the 1kΩ load resistor as shown in figure 2. The other end of the resistor is connected to the GND rail. Input of scope channel IN2 is connected to the end of the resistor not connected to the GND rail.

.. figure:: img/Activity_20_Fig_01.png

Figure 1: Connection diagram for half wave diode rectifierc

From the configuration above it follows that input ac voltage and rectified "dc" voltage are represented on scope application as :math:`V_{AC} = IN_1` and :math:`V_{rec} = IN_2`. 


1. Build the circuit from figure 1 on the breadboard 

.. figure:: img/Activity_20_Fig_02.png

Figure 2: Connections on the breadboard  

2. Start the Oscilloscope & Signal generator application
3. In the OUT1 settings menu set Amplitude value to 0.9V, DC offset to 0 V to apply the input voltage. From the waveform menu select SINE, 
   deselect SHOW button and select enable.
4. On the left bottom of the screen be sure that  IN1 V/div is set to 200mV/div (You can set V/div by selecting the desired channel and using vertical +/- controls
5. On the left bottom of the screen be sure that  IN2 V/div is set to 200mV/div (You can set V/div by selecting the desired channel and using vertical +/- controls)
6. Set t/div value to 200us/div (You can set t/div using horizontal +/- controls)

.. figure:: img/Activity_20_Fig_03.png

Figure 3:  Half wave diode rectifier measurements

As we can see from figure 3 the positive half-period of the input signal is transfered to the load. This means that negative half-period is not participating in the power transfer.

Questions
----------

1. Why is the peak value of the rectified output less than the peak value of the AC input and by how much?
2. At what point in the input waveform does the rectified waveform become positive i.e. something other than zero?
3. What happens if the direction of the diode is reversed? Repeat the experiment with the direction of the diode reversed. 


Full wave rectifier
____________________

Here we will investigate the use of two diodes as a full wave rectifier. 

Again using 1N914 diodes, set up the breadboard with OUT1 attached to one end of the first diode, D1, and OUT2 to one end of the second diode, D2. Both diodes should face in the same direction as shown in figure 5. The other end of each diode is connected to one end of the 1kΩ load resistor RL. The other end of the resistor is connected to the GND V rail. 

.. figure:: img/Activity_20_Fig_04.png

Figure 4: Connection diagram for full wave diode rectifier 

Procedure
----------

1. Build the circuit from figure 4 on the breadboard 

.. figure:: img/Activity_20_Fig_05.png

Figure 5: Connections on the breadboard

2. Start the Oscilloscope & Signal generator application
3. In the OUT1 settings menu set Amplitude value to 0.9V, DC offset to 0 V to apply the input voltage. From the waveform menu select SINE and select enable.
4. In the OUT2 settings menu set Amplitude value to 0.9V, DC offset to 0 V, **Phase to 180 deg** to apply the input voltage. From the waveform menu 
   select SINE and select enable.
5. In the IN1 settings menu deselect SHOW    
6. On the left bottom of the screen be sure that  IN2,OUT1 and OUT2 V/div are set to 200mV/div (You can set V/div by selecting the desired 
   channel and using vertical +/- controls
7. Set t/div value to 200us/div (You can set t/div using horizontal +/- controls)
8. In the Trigger settings menu set trigger source to IN2, trigger level to 0.2V, trigger mode to normal and trigger offset to -0.12ms


If both 0 degree and 180 degree phases of the AC inputs signal (OUT1 and OUT2) are available, then a second diode can fill in the missing half-wave of the input and produce the full-wave rectified signal. Again the forward voltage of the diodes will be apparent and the output waveform will not come to a sharp point at the zero crossing due to the non-zero turn on voltage of the diodes. 

.. figure:: img/Activity_20_Fig_06.png

Figure 6: Full wave rectifier measurements

Questions
----------

1. What happens if the direction of the diodes is reversed? Repeat experiment with the direction of both diodes reversed.
2. What happens if the direction of one diode is opposite of the other? Repeat experiment with the direction of one diode (D1) reversed.
3. How could both 0 degree and 180 degree phases be created from a single source? (how about a transformer?)


Bridge rectifier
_________________

Here we will investigate the use of four diodes as a bridge rectifier.
Bridge rectifier is a full wave rectifier and we should expect same signals as shown on figure 6. The difference here is that
bridge rectifier fill in the negative half-wave without using additional voltage source shifted by 180 deg. Instead of that 
bridge rectifier use 4 diodes in order to make full wave rectifier without need for additional voltage source.

.. figure:: img/Activity_20_Fig_07.png

Figure 7: Bridge full wave diode rectifier 

.. note:: 
    In bridge diode configuration the "AC" side needs to be floating i.e we can't bring DC ground reference from our Signal generator output (OUT1) to the 
    AC side of the diodes configuration. If we do that the points 3 and 4 (figure 7) will be on the same GND reference effectively shortcutting D3. Shortcutting of D3 will in case of negative OUT1 half-wave simply, trough at that point forward polarized D4, bypass current flow directly trough D4 and not the load resistor RL. Because of that an isolation transformer is needed to separate common ground of "DC" side of the diode bridge.

On figure 8 the bridge rectifier configuration using transformer is shown. This is the most common usage of the bridge rectifier. As we can see from the figure 8 the points 1 and 3 of the bridge rectifier are exposed to the transformer differential voltage enabling correct operation of the rectifier. Point 3 will not be put to the GND when IN2 probe is connected and D3 will not be bypassed since "AC" (transformer) side is isolated.  


.. figure:: img/Activity_20_Fig_08.png

Figure 8: Bridge full wave diode rectifier using transformer

.. note:: 
     Here we have used 1:6 transformer. Transformer selection is dependent on voltage levels and etc. Here we use 1:6 ratio transformer in order to increase supply voltage OUT1(+/- 1V). This voltage increase i.e transformer ratio is not affecting the bridge operation itself. You can use 1:1,1:2 or different ratio transformers. 

Procedure
----------

1. Build the circuit from figure 8 on the breadboard 

.. figure:: img/Activity_20_Fig_09.png

Figure 9: Bridge rectifier on the breadboard

2. Set IN2 probe attenuation to x10
3. Start the Oscilloscope & Signal generator application
4. In the OUT1 settings menu set Amplitude value to 0.9V, DC offset to 0 V and Frequency to 100Hz to apply the input voltage. From the waveform menu select SINE, 
   deselect SHOW and select enable.
5. In the IN2 input menu set probe attenuation to x10
6. On the left bottom of the screen be sure that  IN1 is to 200mV/div (You can set V/div by selecting the desired 
   channel and using vertical +/- controls
7. On the left bottom of the screen be sure that IN2 is to 2V/div (You can set V/div by selecting the desired 
   channel and using vertical +/- controls
8. Set t/div value to 2ms/div (You can set t/div using horizontal +/- controls)

.. figure:: img/Activity_20_Fig_10.png

Figure 10: Bridge rectifier measurements

.. note::
   
   IN1 signal shown on figure 10 is the voltage signal on the primary
   side of the transformer(figure 8) therefor, this voltage (IN1)
   multiplied by transformer ratio and shifted for 180 deg is the
   actual AC signal on the bridge rectifier. Why we haven't put IN1
   probe to the secondary side of the transformer? Look at the figure
   7 and its explanation.
   

As we can see from figure 10, the bridge configuration is indeed a
full wave rectifier using just one voltage source. Although when using
STEMlab additional transformer was needed. When using transformer with
the central tap we can make a full wave rectifier using only two
diodes. Explore how!

The disadvantage of this circuit is that now two diode drops are in
series with the load and the peak value of the rectified output is
less than the AC input by 1.2 Volts rather than the 0.6 V in the
previous circuits. Try to measure this voltage drop.

