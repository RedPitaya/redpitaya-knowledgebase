Resonance in RLC Circuits
=========================

Objective
---------

The objective of this Lab activity is to study the phenomenon of
resonance in RLC circuits. Determine the resonant frequency and
bandwidth of the given network using the amplitude response to a
sinusoidal source. 

Notes
-----

.. _hardware: http://redpitaya.readthedocs.io/en/latest/doc/developerGuide/125-10/top.html
.. _Bode: http://redpitaya.readthedocs.io/en/latest/doc/appsFeatures/apps-featured/bode/bode.html

In this tutorials we use the terminology taken from the user manual
when referring to the connections to the Red Pitaya STEMlab board
hardware_.

Oscilloscope & Signal generator application is used for generating and
observing signals on the circuit. Bode_ analyzer application is used
to measure frequency response of RLC circuit. 


Background
----------

A resonant circuit, also called a tuned circuit consists of an
inductor and a capacitor together with a voltage or current source. It
is one of the most important circuits used in electronics. For
example, a resonant circuit, in one of many forms, allows us to tune
into a desired radio or television station from the vast number of
signals that are around us at any time.

A network is in resonance when the voltage and current at the network
input terminals are in phase and the input impedance of the network is
purely resistive.  

.. figure:: img/Activity_08_Fig_01.png

   Figure 1: Parallel Resonance Circuit

   
Consider the parallel RLC circuit of Fig. 1. The steady-state admittance offered by the circuit is: 

.. math::

   Y = \frac{1}{R} + j \left( \omega C - \frac{1}{\omega L} \right) 

Resonance occurs when the voltage and current at the input terminals
are in phase. This corresponds to a purely real admittance, so that
the necessary condition is given by:

.. math::

   \omega C - \frac{1}{\omega L} = 0

   
The resonant condition may be achieved by adjusting L, C, or
:math:`\omega`. Keeping L and C constant, the resonant frequency
:math:`\omega_0` is given by:   


.. math::

   \omega_0 = \frac{1}{\sqrt{LC}} \, rad/s (1)

or 

.. math::

   f_0 = \frac {1}{2 \pi \sqrt{LC}} \, Hz  (2)

Frequency Response: It is a plot of the magnitude of the output
Voltage of a resonance circuit as function of frequency. The response
of course starts at zero, reaches a maximum value in the vicinity of
the natural resonant frequency, and then drops again to zero as ω
becomes infinite. The frequency response is shown in figure 2.  

.. figure:: img/Activity_08_Fig_02.png

   Figure 2: Frequency Response of Parallel Resonant Circuit

   
The two additional frequencies ω :sub: `1` and ω :sub:`2` are also
indicated which are called half-power frequencies. These frequencies
locate those points on the curve at which the voltage response is :math:`1/sqrt(2)`
or 0.707 times the maximum value. They are used to measure
the band-width of the response curve. This is called the half-power
bandwidth of the resonant circuit and is defined as:  

.. math::

   \beta = \omega_2 - \omega_1	(3)

   
.. figure:: img/Activity_08_Fig_03.png

   Figure 3: Series Resonance Circuit

   
Materials
---------


Red Pitaya STEMlab 125-14 or STEMlab 125-10 
Resistors 100 Ω, 1 KΩ
Capacitors 0.01 µF
Inductors 4.7 mH


Procedure
---------

Additional Calculation: 
Using one of the sw tools such is Matlab or Python we can calculate
the impedance of the parallel RLC circuit from Figure 1.

The admittance(Y) of the parallel circuit is given in equation 1 above
where impedance Z  is given as Z = 1 / Y.
       
       
.. note:: 
	
   In this calculation we take into account series resistance of the
   inductor. This resistance will affect the phase response of the RLC
   circuit at lower frequencies. Equation above are used for ideal
   components without parasitic elements. In practice (measurements)
   we only have real elements and we need to take into account that
   inductor is not a pure inductance but also has an effective series
   resistance :math:`R_{esr}`, hence

   .. math::

      Y_{L} = \frac{1}{(R_{esr} + j 2 \pi f L)}.


      
.. _impedance: https://en.wikipedia.org/wiki/Electrical_impedance
.. _antiresonators: https://en.wikipedia.org/wiki/Antiresonance


.. note::

   The resonance frequency is defined as the frequency at which the
   impedance_ of the circuit is at a minimum. Equivalently, it can be
   defined as the frequency at which the impedance is purely real
   (that is, purely resistive). This occurs because the impedances of
   the inductor and capacitor at resonance are equal but of opposite
   sign and cancel out. Circuits where L and C are in parallel rather
   than series actually have a maximum impedance rather than a minimum
   impedance. For this reason they are often described as
   antiresonators_, it is still usual, however, to name the frequency
   at which this occurs as the resonance frequency.

   
Matlab code for calculation of :math:`Z` is given below.

.. code-block:: matlab

   close all
   clear all
   clc
   Rs = 100;
   R1 = 1E3;
   L1 = 4.7E-3;
   C1 = 0.1E-6;
   Resr = 6.5;       % inductor series resistance in Ohms
   Vin = 1;
   f = 100:100:1E6;  % frequency range for calculation

   %% calculation of Z
   Y1 = 1/R1;
   Y2 = i*2*pi.*f*C1;
   Y3 = 1./(Rind+i*2*pi.*f*L1);
   Y = Y1 + Y2 + Y3;
   Z = 1./Y;

   %% Plotting
   ax = plotyy(f,real(Z),f,imag(Z),'semilogx','semilogx');
   ylabel(ax(1), 'Real part of  Z / Ohms');
   ylabel(ax(2), 'Real part of  Z / Ohms');
   xlabel('Frequency / Hz');
   grid on

   
By running code above we get following results shown on picture bellow.

.. figure::   img/Activity_08_Fig_04.png
 
   Figure 4: Calculation of the Impedance Z of parallel RLC circuit.
   Blue trace real/resistive part of Z, green trace imaginary/reactive
   part of Z. 

   
We can also calculate absolute value of Z which is the combined
impedance of RLC circuit from Figure 1.  Absolute value of Impedance Z
is the parameter form which we can predict what the measurements
should look like.


We can model the circuit from Figure 8 as is shown on figure below
where  Z = 1/Y and Y is given in equation 1. 

.. figure::   img/Activity_08_Fig_05.png

   Figure 5: Representing parallel RLC circuit as a complex impedance Z

From figure 5 above we can clearly see that our circuit is simple
voltage divider where Vout=Vin*Z/(Rs+Z). But since the Z is frequency
dependent the ratio between Z and Rs will be frequency dependent and
with that the Vin/Vout ratio.

At some frequency f: where the value of  Z  is much smaller than value
of Rs the output voltage amplitude will be much smaller than input
voltage amplitude.

At some frequency f: where value of Z is much higher than value of Rs
the output voltage amplitude will be close to the input voltage
amplitude

At some frequency f:  where Z=Rs the Vout will be ½ Vin.  

At some frequency f: where Z is maximal the Vout will be also
maximal. This is the resonant frequency.


.. figure::   img/Activity_08_Fig_06.png

   Figure 6: Calculation of absolute value of impedance Z for the circuit shown on figure 3. 


Using

.. math::

   V_{out} = V_{in} \frac{Z}{R_s + Z}

we can calculate the frequency response of our RLC circuit shown in
Figs. 5 and 8.

.. note::

   Magnitude repsponse in decibel (dB)
   
   .. math::

      H_v = 20 \cdot \log_{10}\left\lvert \frac{V_{out}}{V_{in}} \right\lvert.



.. figure::   img/Activity_08_Fig_07.png

   Figure 7: Calculation of frequency response (Vout/Vin) for circuit on figure 5.


Procedure:

1. Set up the RLC circuit as shown in figure 8 on your solderless
   breadboard, with the component values RS = 100 Ω, R1 = 1 KΩ, C1 =
   0.1 µF and L1= 4.7 mH.

.. figure::   img/Activity_08_Fig_08.png

   Figure 8: Parallel RLC circuit for the measurements.


2. Open the Bode analyzer application. In “Settings” menu set start
   frequency to 100Hz, end frequency to 1MHz and number of steps
   to 50. And Click “RUN” button. 

.. figure::   img/Activity_08_Fig_09.png

   Figure 9: Bode analyzer application

   
After the measurements are done you should get the frequency response of your circuit as is shown on Figure 10q.

.. figure::   img/Activity_08_Fig_10.png

    Figure 10: Frequency response of circuit from Figure 8 take by Bode analyzer application.



- Compare measurements and calculation. If there is any difference try to explain why.

.. hint:: parasitic


The Bode analyzer application will make a frequency sweep in such way
it will generate sine signal on OUT1 within frequency range selected
by us(in settings menu).

IN1 input signal is directly connected to OUT1 following that
IN1=Vin. IN2 is connected on the other side of the RLC circuit and
from that IN2=Vout. Bode analyzer application will then for each
frequency step take the ratio of IN1/IN2 and calculate frequency
response.  

2. On order to see how Vout/IN2 signal amplitude is changing in
   respect to OUT1 start the Oscilloscope application, in OUT1
   settings enable OUT1, deselect SHOW button and look at the signal
   amplitudes of IN1 and IN2. 


   Change the OUT1  frequency, adjust t/div value so you have 2 cycles of
   the IN1 and observe the amplitudes of IN1 and IN2. 


   Repeat this step for OUT1 frequency from 100Hz to 1MHz and you should observe 
   same amplitude response as it is measured by Bode analyzer application.


   Bode analyzer is also measuring phase between IN1 and IN2. Phase is
   also frequency dependent.  You can see that easily wit the
   Oscilloscope application. 


3. Repeat the experiment using for the series resonant circuit in
   figure 3, and use L1 = 20 mH and C1 = 0.01 uF and R1 = 1 KΩ. The Vo
   voltage on the resistor is proportional to the series RLC circuit
   current. 

   
Questions
---------

Plot the voltage response of the circuit and obtain the bandwidth from
the half-power frequencies using equation (3). 




