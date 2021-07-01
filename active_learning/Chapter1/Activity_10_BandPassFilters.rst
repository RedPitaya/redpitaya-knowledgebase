Band Pass Filters
=================

Objective
---------

The objective of this Lab activity is to: 

1. Construct a Band Pass Filter by cascading a low pass filter and a high pass filter. 

2. Obtain the frequency response of the filter using Bode_ analyzer application.


Notes
-----

.. _hardware: http://redpitaya.readthedocs.io/en/latest/index.html
.. _Bode: http://redpitaya.readthedocs.io/en/latest/doc/appsFeatures/apps-featured/bode/bode.html 

In this tutorials we use the terminology taken from the user manual
when referring to the connections to the Red Pitaya STEMlab board
hardware_.

Bode_ analyzer application is used to measure frequency response of
Low Pass and High Pass Filters.

The Bode analyzer is an ideal application for measuring frequency
responses of the passive/active filters, complex impedances and any
other electronic circuit. The Gain/Phase frequency response can be
used to characterize any device under test completely, you can perform
linear and logarithmic sweeps. Gain and Phase can be measured from 1Hz
to 60MHz. The basic user interface enables quick interaction and
parameter settings. The Bode analyzer can be used for the measurement
of Stability of control circuits such as the DC/DC converters in power
supplies, Influence of termination on amplifiers or filters,
Ultrasonic and piezo electric systems and similar.


Background
----------

A Band Pass Filter allows a specific range of frequencies to pass,
while blocking or attenuating lower and higher frequencies. It passes
frequencies between the two cut-off frequencies while attenuating
frequencies outside the cut-off frequencies. One typical application
of a band pass filter is in Audio Signal Processing, where a specific
range of frequencies of sound are desired while attenuating the
rest. Another application is in the selection of a specific signal
from a range of signals in communication systems. A band pass filter
may be constructed by cascading a High Pass RL filter with a roll-off
frequency :math:`f_L` and a Low Pass RC filter with a roll-off
frequency :math:`f_H`, such that:

.. math::	

   f_L < f_H 

The Lower cut-off frequency is given as: 

.. math::	

   f_L = \frac{R}{2 \pi L} \quad (1)

The higher cut-off frequency is given as: 

.. math::

   f_H = \frac{1}{2 \pi RC} \quad (2) 

The **Band Width** of frequencies passed is given by: 

.. math::

   BW = f_L < f_{BW} < f_H \quad (3) 

All signal frequencies :math:`f` below :math:`f_L` and above
:math:`f_H` are attenuated and the frequencies between are passed by
the filter.
      

.. figure:: img/Activity_10_Fig_01.png

   Figure 1: Band Pass Filter circuit 

   
Frequency Response
------------------

To show how a circuit responds to a range of frequencies a plot of the
magnitude ( amplitude ) of the output voltage of the filter as a
function of the frequency can be drawn. It is generally used to
characterize the range of frequencies in which the filter is designed
to operate within. Figure 2 shows a typical frequency response of a
Band Pass filter.


.. figure:: img/Activity_10_Fig_02.png

   Figure 2: Band Pass Filter Frequency Response

   
Materials:
----------


- Red Pitaya STEMlab 125-14 or STEMlab 125-10 

- Resistor: 	1 KΩ 

- Capacitor:    0.047 µF

- Inductor: 	22 mH 


Procedure
---------


1. Set up the filter circuit as shown in figure 1 and figure 3 on your
   solderless breadboard, with the component values R1 = 1 KΩ, C1 =
   0.047 µF, L1 =22 mH.

   .. figure:: img/Activity_10_Fig_03.png

   Figure 3: Band Pass Filter on solderless breadboard

2. Start the Bode analyzer application. The Bode analyzer application
   will make a frequency sweep in such way it will generate sine
   signal on :math:`OUT1` within frequency range selected by us(in
   settings menu). :math:`IN1` input signal is directly connected to
   :math:`OUT_1` following that :math:`IN1=V_{in}`. :math:`IN2` is
   connected on the other side of the filter and from that
   :math:`IN2=V_{out}`. Bode analyzer application will then for
   each frequency step take the ratio of :math:`IN1/IN2`
   (:math:`V_{in}/V_{out}`) and calculate frequency
   response.  

3. In the Bode analyzer settings menu set for:

   - start frequency:  500 Hz

   - end frequency: 30 kHz

   - number of steps: 50

   - scale: Log 

   - select RUN button

   .. figure:: img/Activity_10_Fig_04.png

   Figure 4: Band Pass Filter **measured** Frequency Response

   
Questions:
----------

1. Compute the cut-off frequencies for each Band Pass filter
   constructed using the formula in equations (1) and (2). Compare
   these theoretical values to the ones obtained from the experiment
   and provide suitable explanation for any differences. 

