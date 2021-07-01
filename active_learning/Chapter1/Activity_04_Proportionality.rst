Proportionality and Superposition
=================================

Objective
---------

The objective of this Lab activity is to verify the proportionality
and superposition theorems. 

Notes
-----

.. _E1: http://redpitaya.readthedocs.io/en/latest/doc/developerGuide/125-14/extent.html#extension-connector-e1
.. _E2: http://redpitaya.readthedocs.io/en/latest/doc/developerGuide/125-14/extent.html#extension-connector-e2
.. _hardware: http://redpitaya.readthedocs.io/en/latest/doc/developerGuide/125-10/top.html

In this tutorials we use the terminology taken from the user manual
when referring to the connections to the Red Pitaya STEMlab board
hardware_. Extension connector pins used as 5V and 3.3V voltage source
are show in the documentation for connectors E1_ and E2_. 


Background
----------

In this activity proportionality and superposition theorems are
examined by applying them to the circuits shown in the following
figures. 

1. The Proportionality Theorem states that the response of a circuit
   is proportional to the source acting on the circuit. This is also
   known as *linearity*. The proportionality constant A relates the
   input voltage to the output voltage as: 

   .. math:: 
	
      V_{out} = A \cdot V_{in} 

   The proportionality factor A is sometimes referred to as the
   gain of a circuit. For the circuit in Fig. 1, the source
   voltage is V\ :sub:`in`\. The response V\ :sub:`out`\ is across
   the :math:`4.7 k\Omega` resistor. The most important result of
   linearity is superposition.

   .. figure:: img/Activity_04_Fig_01.png
      :align: center 
	
      Figure 1 : Resistor circuit with 5V voltage source


2. The Superposition Theorem states that the response of a linear
   circuit with multiple independent sources, such as in figure 2, can
   be obtained by adding the individual responses caused by the
   individual sources acting alone. For an independent source acting
   alone, all other independent voltage sources in the circuit are
   replaced by short circuits and all other independent current
   sources are replaced by open circuits, as in figure 3.

   .. figure:: img/Activity_04_Fig_02.png
      :align: center 

      Figure 2. Circuit with two voltage sources 

      
   .. figure:: img/Activity_04_Fig_03.png
      :align: center 
	
      Figure 3. Circuit for response of just one source

      
Materials
---------

- Red Pitaya STEMlab 125-14 or STEMlab 125-10 

- Various Resistors:
  - :math:`1 k\Omega`, 
  - :math:`2.2 k\Omega`, 
  - :math:`4.7 k\Omega`.


Procedure
---------

Verify the proportionality theorem:

- Construct the circuit of figure 1.

- Case 1: For voltage source “V\ :sub:`in`\=5V” shown on the Figure 1
  use the STEMlab voltage pin on extension connector E2_.  
  
- Case 2: For voltage source “V\ :sub:`in`\=3.3V” shown on the Figure
  1 use the STEMlab voltage pin on extension connector E1_. 

- Case 3: For voltage source “V\ :sub:`in`\=-3.3V” shown on the Figure
  1 use the STEMlab voltage pin on extension connector E2_.  

- Set probe attenuation to x10 (on the oscilloscope probe  and on the
  Oscilloscope IN1 menu settings) 

- Accurately measure V\ :sub:`out`\ using the Oscilloscope
  application. 
  
- You should measure and record the actual fixed power supply voltages
  as well. 

  
  .. table:: Table 1
     :widths: auto

     +---------------+----------------+-------+	
     | V\ :sub:`in`\ | V\ :sub:`out`\ | A     |  
     +---------------+----------------+-------+
     |	5.0 V        |                |       |	
     +---------------+----------------+-------+
     |	3.3 V        |                |       |
     +---------------+----------------+-------+
     |      -3.3 V   |                |       |
     +---------------+----------------+-------+


 
- Calculate the value of A in each case using Eq. (1).

- Plot a graph with V\ :sub:`in`\ on x-axis and V\ :sub:`out`\ on y-axis.

- Verifying the Superposition theorem:

  - Construct the circuit of Fig. 2. Measure and record the voltage across the :math:`4.7 k\Omega` resistor.

  - Construct the circuit of Fig. 3. Measure and record the voltage across the :math:`4.7 k\Omega` resistor.

    
.. note:: Measuring voltage drop across desired resistor is done in
	  such way that Oscilloscope probe of IN1 is connected to the
	  one side of the resistor and Oscilloscope probe of IN2 is
	  connected to another side of the resistor. Voltage
	  difference V\ :sub:`in1`\-V\ :sub:`in2`\ will give an
	  voltage on the measured resistor. 


- Calculate the total response “V\ :sub:`out`\” for circuit of figure
  2 by adding the responses from measurement of circuit of figure 1
  and measurement of circuit of figure 3. 

  V\ :sub:`out`\(figure 2) = V\ :sub:`out`\(figure 1) + V\ :sub:`out`\(figure 3) = __________


- Compare your calculated result to what you measured in step 2a. Explain any differences.

  .. figure:: img/Activity_04_Fig_04.png
     :align: center 
     
     Figure 4: Voltages pin on the Red Pitays STEMlab board


Questions
---------

1. Is the graph obtained a straight line? Compute the slope of the
   graph at any point and compare it to the value of K obtained from
   the measurements. Explain any differences.
   
2. For each of the three circuits you built for the superposition
   experiment, how well did the calculated and measured outputs
   compare? Explain any differences. 
