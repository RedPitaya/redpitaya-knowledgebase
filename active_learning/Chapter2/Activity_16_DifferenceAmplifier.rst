Difference Amplifier
#####################

Objective
__________

Adding and/or subtracting analog signals is potentially the most common function performed by an op-amp. This activity will investigate single op-amp circuits for subtracting two analog signals. 
We have already discussed Summing_ Amplifier_ circuit;  a single op-amp circuits for adding two (or more) analog signals. Same behaviour we also expect here while signals in the opamp inputs should be subtracted and not summed together.

Notes
______

.. _hardware: http://redpitaya.readthedocs.io/en/latest/doc/developerGuide/125-10/top.html
.. _here: http://redpitaya.readthedocs.io/en/latest/doc/developerGuide/125-14/extent.html#extension-connector-e2
.. _Oscilloscope: http://redpitaya.readthedocs.io/en/latest/doc/appsFeatures/apps-featured/oscSigGen/osc.html
.. _Signal: http://redpitaya.readthedocs.io/en/latest/doc/appsFeatures/apps-featured/oscSigGen/osc.html
.. _generator: http://redpitaya.readthedocs.io/en/latest/doc/appsFeatures/apps-featured/oscSigGen/osc.html
.. _Bode: http://redpitaya.readthedocs.io/en/latest/doc/appsFeatures/apps-featured/bode/bode.html 
.. _Summing: http://red-pitaya-active-learning.readthedocs.io/en/latest/Activity13_BasicOPAmpConfigurations.html#summing-amplifier-circuit
.. _Amplifier: http://red-pitaya-active-learning.readthedocs.io/en/latest/Activity13_BasicOPAmpConfigurations.html#summing-amplifier-circuit
.. _OP484: http://www.analog.com/media/en/technical-documentation/data-sheets/OP184_284_484.pdf

In this tutorials we use the terminology taken from the user manual when referring to the connections to the Red Pitaya STEMlab board hardware_.
Extension connector pins used for **-3.3V** and **+3.3V** voltage supply are show in the documentation here_. 
Oscilloscope_ & Signal_ generator_ application is used for generating and observing signals on the circuit.

Short Background
_________________

The basic difference opamp circuit is shown in figure 1.  To solve for the transfer function :math:`V_{out} = f(V_1,V_2)` of the difference amplifier we can use a superposition principle.

.. figure:: img/Activity_16_Fig_01.png

Figure 1: Basic Difference Amplifier

In the first step consider circuit from figure 1 where noninverting input (pin 3) is set to the GND.
We get familiar inverting amplifier circuit which transfer function is given as

.. math::	
	        V_{out} = - V_1 \bigg( \frac{R_f}{R_i} \bigg)   \quad (1)

In second step consider the circuit from figure 1 where :math:`V_1` input is set to the GND. 
We get familiar non-inverting amplifier circuit which transfer function is given as 

.. math::	
	        V_{out} = V_2 \bigg( 1 + \frac{R_f}{R_i} \bigg) \quad (2)
  
Following superposition principle we get 

.. math::	
	        V_{out} = V_{out_{step_1}}+V_{out_{step_2}}=V_2 \bigg( 1+ \frac{R_f}{R_i} \bigg) - V_1 \bigg(\frac{R_f}{R_i} \bigg) \quad (3)

From the equation above we can clearly see that circuit from figure 1 is indeed a difference amplifier where output signal :math:`V_{out}` is the  difference of the input signals :math:`V_2-V_1` amplified by factor :math:`\frac{R_f}{R_1}`.

For :math:`R_f = R_i`  we get: 

.. math::	
	        V_{out} = 2V_2 -V_1 \quad (4)
  


Materials
__________

- Red Pitaya STEMlab 
- OPAMP:  1x OP484 
- Resistor:  4x 10 :math:`k \Omega`

Procedure
___________

Build the difference amplifier shown in figure 2. R3 and R4 are added as a voltage divider in order to attenuate :math:`V_2^*` input signal by half. 
With voltage divider (R3, R4) added, for circuit shown on figure 2 and from equation (4) we get 

.. math::	
	        V_{out} = 2V_2 - V_1 = \frac{1}{2} 2 V_2^* - V_1 = V_2^* - V_1 = OUT_2 - OUT_1  \quad (5)

.. figure:: img/Activity_16_Fig_02.png

Figure 2: Difference Amplifier

.. warning::
      Before connecting the circuit to the STEMlab -3.3V and +3.3V  pins double check your circuit. The  -3.3V and +3.3V  voltage supply pins do not have  short circuit handling and they can be damaged in case of short circuit.

.. figure:: img/Activity_16_Fig_03.png

Figure 3: Difference Amplifier on the breadboard

1. Start the Oscilloscope & Signal Generator application.
2. In the IN1 settings menu deselect SHOW button.
3. In the OUT1 settings menu set Amplitude value to 0.2V to apply a 0.4Vp-p sine wave centered on 0V as the input voltage :math:`V_1`. From the waveform menu select SINE and select enable.
4. In the OUT2 settings menu set Amplitude value to 0.6V to apply a 1.2Vp-p sine wave centered on 0V as the input voltage :math:`V_2^*`. From the waveform menu select SINE and select enable.
5. For the stable acquisition set the trigger source to IN2
6. On the left bottom of the screen be sure that  IN2 V/div is set to 200mV/div (You can set V/div by selecting the desired channel and using vertical +/- controls) 
7. On the left bottom of the screen be sure that OUT1 V/div and OUT2 V/div are both set to 200mV/div (You can set V/div by selecting the desired channel and using vertical +/- controls) 
8. In the measurement menu select “MAX” , select IN2 and press DONE

.. figure:: img/Activity_16_Fig_04.png

Figure 4: Difference Amplifier measurements

.. note::
     As we can see from the measurements shown on the figure 4 our circuit behaves as a voltage difference amplifier since IN2 amplitude is equal to the difference between OUT2 and OUT1 amplitudes as it is predicted by equation (5).

Since both input signals are sinusoidal the only artefact of the difference amplifier circuit on the output signal is the difference in amplitude. But what happens when we have different waveforms of OUT1 and OUT2. 

1. In the OUT2 settings menu select SQUARE waveform and observe results

.. figure:: img/Activity_16_Fig_05.png

Figure 5: Difference Amplifier measurements - Different waveforms of OUT1 and OUT2

From figure 5 we can observe a difference amplifier output signal (IN2) which has a strange waveform shape given as IN2(waveform)=OUT2(SQUARE) - OUT1(SINE). 
This observation is absolutely confirming that circuit shown on figure 2 is a difference amplifier.

.. note:: 
     Try different OUT1 and OUT2 waveforms and observe results.
      