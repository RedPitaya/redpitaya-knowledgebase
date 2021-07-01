
Basic OP Amp Configurations
############################

Objective
__________

In this lab we introduce the operational amplifier (op amp), an active
circuit that is designed with certain characteristics (high input
resistance, low output resistance, and a large differential gain) that
make it a nearly ideal amplifier and useful building-block in many
circuits applications. In this lab you will learn about DC biasing for
active circuits and explore a few of the basic functional op amp
circuits. We will also use this lab to continue developing skills with
the lab hardware.


Notes
_____

.. _hardware: http://redpitaya.readthedocs.io/en/latest/doc/developerGuide/125-10/top.html
.. _here: http://redpitaya.readthedocs.io/en/latest/doc/developerGuide/125-14/extent.html#extension-connector-e2
.. _Oscilloscope: http://redpitaya.readthedocs.io/en/latest/doc/appsFeatures/apps-featured/oscSigGen/osc.html
.. _Signal: http://redpitaya.readthedocs.io/en/latest/doc/appsFeatures/apps-featured/oscSigGen/osc.html
.. _generator: http://redpitaya.readthedocs.io/en/latest/doc/appsFeatures/apps-featured/oscSigGen/osc.html

In this tutorials we use the terminology taken from the user manual
when referring to the connections to the Red Pitaya STEMlab board
hardware_.

Oscilloscope_ & Signal_ generator_ application is used for generating
and observing signals on the circuit.

Extension connector pin used as 5V voltage source are show in the
documentation here_.


Materials
_________

- Red Pitaya STEMlab 125-14 or STEMlab 125-10 
- OPAMP:  1x AD8541 ( CMOS rail to rail amplifier )
- LED: 1x
- Resistor:  4x 1 :math:`k \Omega`
- Resistor:  3x 4.7 :math:`k \Omega`
- Resistor:  2x 10 :math:`k \Omega`
- Resistor:  1x 20 :math:`k \Omega`
- Capacitor: 1x 1 :math:`\mu F`

Op-Amp Basics
_____________

.. _LM317: http://www.ti.com/lit/ds/symlink/lm317.pdf
.. _adjustable: http://www.ti.com/lit/ds/symlink/lm317.pdf
.. _regulator: http://www.ti.com/lit/ds/symlink/lm317.pdf
.. _E2: http://redpitaya.readthedocs.io/en/latest/doc/developerGuide/125-14/extent.html#extension-connector-e2
.. _connector: http://redpitaya.readthedocs.io/en/latest/doc/developerGuide/125-14/extent.html#extension-connector-e2


First Step: Connecting DC Power
-------------------------------
Op amps must always be supplied with DC power and therefore it is best
to configure these connections first before adding any other circuit
components. Figure 1 shows one possible power arrangement on your
solder-less breadboard. We use two of the long rails for the positive
supply voltage and ground. Using LM317_ adjustable_ regulator_ we
provide 2.5 V mid supply rail that may be required.


.. note::

   STEMlab boards do not have 2.5V DC output pin so we are using LM317
   adjustable regulator to provide 2.5V DC rail from 5V one.
   
   Connection of LM317 is very simple and described below. Equation
   for calculating output voltage is given as:
   
     
   .. math::

      V_{out} = 1.25 \bigg( 1+\frac{R_2}{R_1} \bigg) \quad (1). 


Included are the so-called “supply de-coupling” capacitor connected
between the power-supply and ground rails. It is too early to discuss
in great detail the purpose of these capacitors, but they are used to
reduce noise on the supply lines and avoid parasitic oscillations. It
is considered good practice in analog circuit design to always include
small bypass capacitors close to the supply pins of each op amp in
your circuit.


.. figure:: img/Activity_13_Fig_01.png

Figure 1: Power connections using 5V power pin from E2_ connector_ and LM317_ adjustable_ regulator_

It is good practice to have power suply indication. For that we use
LED connected to the 2.5V rail. If the voltage is present on this rail
the LED will be ON. Since 2.5V is provided from 5V rail the same  LED
will also indicate “OK” status of 5V power supply. Insert the LM317
and op amp into your breadboard and add the wires,resistors,led and
supply capacitors as shown in figure 1. To avoid problems later you
may want to attach a small label to the breadboard to indicate which
rails correspond to +5 V, +2.5V and GND.


Next, attach the +5 V supply and GND connections from the STEMlab
board to the terminals on your breadboard. Use jumper wires to power
the rails. Remember, the power-supply GND terminal will be our circuit
“ground” reference. Once you have your supply connections you may want
to use a DMM to probe the IC pins directly to insure that pin 7 is
at +5 V, pin 4 at 0 V (ground) and check 2.5 power rail.

Remember you must have the STEMlab powered up before measuring the
voltages with the volt meter.


.. figure:: img/Activity_13_Fig_02.png

Figure 2: Power connections 

First Step: Unity-Gain Amplifier (Voltage Follower)
----------------------------------------------------

Our first op amp circuit is a simple one, shown in figure 3. This is
called a unity-gain buffer, or sometimes just a voltage follower,
defined by the transfer function :math:`V_{out} = V_{in}`. At first
glance it may seem like a useless device, but as we will show later it
finds use because of its high **input resistance** and **low output
resistance**.


.. figure:: img/Activity_13_Fig_03.png

Figure 3: Unity Gain Follower

Using your breadboard and the STEMlab power supplies, construct the
circuit shown in figure 3. Note that the power connections have not
been explicitly shown here; it is assumed that those connections must
be made in any real circuit (as you did in the previous step), so it
is unnecessary to show them in the schematic from this point on. Use
jumper wires to connect input and output to the waveform generator
output, OUT1 and oscilloscope inputs IN1 an IN2.


1. Start the Oscilloscope & Signal Generator application.
   
2. In the OUT1 settings menu set DC offset value to 0.5 and Amplitude
   value to 0.45V to apply a 1Vp-p sine wave centered on 0.5 V as the
   input voltage to the circuit. From the waveform menu select SINE
   signal deselect SHOW button and select enable. On the left bottom
   of the screen be sure that IN1 V/div and IN2 V/div are both set to
   200mV/div (You can set V/div by selecting the desired channel and
   using vertical +/- controls) In the IN1 and IN2 settings menu set
   the value of Vertical Offset to -500mV For the stable acquisition
   set the trigger level in TRIGGER menu to 0.5V and select NORMAL.
    
3. In the measurement menu select “P2P” , select IN1 and press DONE,
   select IN2 and press DONE
   
4. In the measurement menu select “FREQ” , select IN1 and press DONE,
   select IN2 and press DONE
   

.. figure:: img/Activity_13_Fig_04.png

Figure 4: Unity Gain Follower measurements with an Oscilloscope & Signal Generator application.

Our measurements have confirmed that circuit in figure 3 is indeed a
voltage follower. This configuration is widely used for example if our
signal generator, connected to the “+” pin of the OPAMP, needs to be
separated from influence of the circuit connected to the output of the
voltage follower (pin 6).

In reality a voltage follower shown in figure 3 has its limitations in
case of performances. Mainly this is the capability of voltage
follower to preserve :math:`V_{out}=V_{in}` characteristic in case of
high frequencies of :math:`V_{in}` (IN1=OUT1, look at figure 3).

Try to increase Signal generator (OUT1) frequency up to 100kHz or 1MHz
and observe signals IN1 and IN2.  Certain delay of signal IN2 will
appear indicating that voltage follower is inserting time delay
between input (IN1) and output (IN2) signals.


Buffering Example
-------------------
The high input resistance of the op-amp (zero input current) means
there is very little loading on the generator; i.e., no current is
drawn from the source circuit and therefore no voltage drops on any
internal (Thevenin) resistance. Thus in this configuration the op-amp
acts like a “buffer” to shield the source from the loading effects
from other parts of the system. From the perspective of the load
circuit the buffer transforms a non-ideal voltage source into a nearly
ideal source. figure 5 describes a simple circuit that we can use to
demonstrate this feature of a unity-gain buffer. Here the buffer is
inserted between a voltage-divider circuit and some “load” resistance,
the 10K resistor.


.. figure:: img/Activity_13_Fig_05.png

Figure 5: Buffer Example 

Using your breadboard and the STEMlab power supplies, construct the
circuit shown in figure 5, case 1.


**Case 1**
    Simultaneously observe :math:`V_{in}` (IN1) and :math:`V_{out}`
    (IN2) and record the amplitudes (P2P).
    

1. Start the Oscilloscope & Signal Generator application.
   
2. In the OUT1 settings menu set DC offset value to 0 and Amplitude
   value to 1V to apply a 2Vp-p sine wave centered on 0V as the input
   voltage to the circuit. From the waveform menu select SINE
   signal deselect SHOW button and select enable.
   
3. On the left bottom of the screen be sure that IN1 V/div and IN2
   V/div are both set to 200mV/div (You can set V/div by selecting the
   desired channel and using vertical +/- controls)
   
4. In the IN2 settings menu set the value of Vertical Offset to
   -1000mV.
   
5. In the IN1 and IN2 settings menu set probe settings to x10.
   
6. For the stable acquisition set the trigger level in TRIGGER menu to
   1.3V and select NORMAL.
   
7. In the measurement menu select “P2P” , select IN1 and press DONE,
   select IN2 and press DONE
   
8. In the measurement menu select “FREQ” , select IN1 and press DONE,
   select IN2 and press DONE
   

**Case 2**
    Remove the 10kΩ load and substitute a 1kΩ resistor instead and
    record the amplitudes (P2P) of :math:`V_{in}` (IN1) and
    :math:`V_{out}`
	  

**Case 3**
    Move the 1 KΩ load between pin 3 and +2.5 V, so that it is in
    parallel with the 4.7 KΩ resistor. Record the amplitudes (P2P) of
    :math:`V_{in}` (IN1) and :math:`V_{out}`
	  
.. figure:: img/Activity_13_Fig_06.png

Figure 6: Buffer Example case 1

If you have performed measurements in all 3 cases you have noticed
following; In case 1 and 2 there was no difference between
measurements of  :math:`V_{in}` (IN1) and :math:`V_{out}` although we
had different loads (1K and 10K resistors) on the buffer output. From
this fact it is clear that buffer circuit can drive those loads
:math:`V_{out-case-1}=V_{out-case-2}` with the same output voltage
while preventing different loads affecting the :math:`V_{in}`
signal :math:`V_{in-case-1}=V_{in-case-2}`.
      
In case 3 adding 1K resistor between pin 3 (“+”) and 2.5V will affect
the :math:`V_{in}` voltage and since, the circuit is a voltage
follower, an :math:`V_{out}` will change accordingly.



Basics Amplifier Configurations
_______________________________

Inverting Amplifier
--------------------

Figure 7 shows the conventional inverting amplifier configuration with
a 10 KΩ “load” resistor at the output.


.. figure:: img/Activity_13_Fig_07.png

Figure 7: Inverting amplifier configuration 

Now assemble the inverting amplifier circuit shown in figure 7 using
R2 = 4.7kΩ. Remember to disconnect the power supply before assembling
a new circuit. Cut and bend the resistor leads as needed to keep them
flat against the board surface, and use the shortest jumper wires for
each connection Remember, the breadboard gives you a lot of
flexibility. For example, the leads of resistor R2 do not necessarily
have to bridge over the op-amp from pin 2 to pin 6; you could use an
intermediate node and a jumper wire to go around the device instead.


1. Start the Oscilloscope & Signal Generator application.
   
2. In the OUT1 settings menu set DC offset value to -0.5V and
   Amplitude value to 0.45V to apply a offseted sine wave centered on
   -0.5V as the input voltage to the circuit. From the waveform menu
   select SINE signal deselect SHOW button and select enable.
   
3. In the IN1 and IN2 settings menu set probe settings to x10.
   
4. On the left bottom of the screen be sure that IN1 V/div is set to
   200mV/div and IN2 to 1V/div (You can set V/div by selecting the
   desired channel and using vertical +/- controls)
   
5. In the IN1 settings menu set the value of Vertical Offset to
   -500mV, In the IN2 settings menu set the value of Vertical Offset
   to 2.500mV,
   
6. For the stable acquisition set the trigger level in TRIGGER menu to
   -0.5V and select NORMAL.
   
7. In the measurement menu select “P2P” , select IN1 and press DONE,
   select IN2 and press DONE
   
8. In the measurement menu select “MEAN” , select IN1 and press DONE,
   select IN2 and press DONE
   

.. figure:: img/Activity_13_Fig_08.png

Figure 8: Inverting amplifier configuration measurements

.. note::

   From the measurements shown on figure 8 we can see that amplitude
   of :math:`V_{out}` (IN2) is cca 4.7 time larger than amplitude of
   :math:`V_{in}` (IN1). Also the phase between two signals is 180
   degrees.This is the result of inverting amplifier
   characteristic which is given as:
	 

   .. math::	

      V_{out} = - \bigg( \frac{R2}{R1} \bigg) V_{in}  \quad (2)
      

Non-Inverting Amplifier
------------------------

The non-inverting amplifier configuration is shown in figure 9. Like
the unity-gain buffer, this circuit has the (usually) desirable
property of high input resistance, so it is useful for buffering
non-ideal sources, however with a gain greater than one.


.. figure:: img/Activity_13_Fig_09.png

Figure 9: Non-Inverting amplifier configuration measurements

Assemble the non-inverting amplifier circuit shown in
figure 9. Remember to shut off the power supplies before assembling
the new circuit. Set **R2 = 4.7kΩ**.


1. Start the Oscilloscope & Signal Generator application.
   
2. In the OUT1 settings menu set DC offset value to 0.5V and Amplitude
   value to 0.3V to apply a offseted sine wave centered on 0.5V as the
   input voltage to the circuit. From the waveform menu select
   SINE signal deselect SHOW button and select enable.
   
3. In the IN1 and IN2 settings menu set probe settings to x10.
   
4. On the left bottom of the screen be sure that IN1 V/div is set to
   100mV/div and IN2 to 1V/div (You can set V/div by selecting the
   desired channel and using vertical +/- controls)
   
5. In the IN1 settings menu set the value of Vertical Offset to
   -500mV, In the IN2 settings menu set the value of Vertical Offset
   to -3V.
   
6. For the stable acquisition set the trigger level in TRIGGER menu to
   0.5V and select NORMAL.
   
7. In the measurement menu select “P2P” , select IN1 and press DONE,
   select IN2 and press DONE
   
8. In the measurement menu select “MEAN” , select IN1 and press DONE,
   select IN2 and press DONE
   


.. figure:: img/Activity_13_Fig_10.png

Figure 10: Non-Inverting amplifier configuration measurements

.. note::
   
   From the measurements shown on figure 10 we can see that amplitude
   of :math:`V_{out}` (IN2) is cca 5.7 time larger than amplitude of
   :math:`V_{in}` (IN1). Also the phase between two signals is ~0
   degrees.This is the result of non-inverting amplifier
   characteristic which is given as:
	 

   .. math:: V_{out} =  \bigg( 1 + \frac{R2}{R1} \bigg) V_{in}  \quad (3)


Increase the feedback resistance R2 further until the onset of
clipping, that is, until the peaks of the output signal begin to be
flattened due to output saturation. Record the value of resistance
where this happens. Now increase the feedback resistance to 100
KΩ. Describe and draw waveforms in your notebook. What is the
theoretical gain at this point? How small would the input signal have
to be in order to keep the output level to less than 5V given this
gain? Try to adjust the waveform generator to this value. Describe the
output achieved.

The last step underscores an important consideration for high-gain
amplifiers. High-gain necessarily implies a large output for a small
input level. Sometimes this can lead to inadvertent saturation due to
the amplification of some low-level noise or interference, for example
the amplification of stray 60Hz signals from power-lines that can
sometimes be picked up. Amplifiers will amplify any signals at the
input terminals…whether you want it or not!



Summing Amplifier Circuit
--------------------------

The circuit of figure 11 is a basic inverting amplifier with four inputs, called a “summing” amplifier. 

.. figure:: img/Activity_13_Fig_11.png

Figure 11: Summing Amplifier configuration


With the power disconnected, build circuit as shown in figure 11 and continue with measurements.

.. figure:: img/Activity_13_Fig_12.png

Figure 12: Summing Amplifier circuit on the breadboard

**Set:** :math:`R_{in}` = :math:`R_{in}` = :math:`R_{f}` = 4.7kΩ.

1. Start the Oscilloscope & Signal Generator application.
   
2. In the OUT1 and OUT2 settings menu set DC offset value to -0.5V and
   Amplitude value to 0.3V to apply a offseted sine wave centered on
   -0.5V as the input voltages to the circuit. From the waveform
   menu select SINE signal and select enable.
   
3. In the IN1 and IN2 settings menu set probe settings to x10.
   
4. On the left bottom of the screen be sure that IN1 V/div is set to
   100mV/div and IN2 to 1V/div (You can set V/div by selecting the
   desired channel and using vertical +/- controls)
   
5. For the stable acquisition set the trigger level in TRIGGER menu to
   -0.5V and select NORMAL.
   
6. In the measurement menu select “P2P” , select IN1 and press DONE,
   select IN2 and press DONE
   

.. figure:: img/Activity_13_Fig_13.png

Figure 13: Summing Amplifier measurements

.. note::
   
   From measurement above we can see that output voltage is sum of the two input voltages.
   Also the phase between two signals is ~0 degrees.
   This is the result of inverting summing amplifier characteristic which is given as: 

   .. math:: 

      -V_{out} =  \frac{R_f}{R_{in}} \bigg( V_{in1} + V_{in2} \bigg) \quad (4)

      
   In general :math:`R_{in}` can be different for each input voltage so it follows:

     
   .. math::
     
      -V_{out} =  \frac{R_f}{R_{in1}} V_{in1} + \frac{R_f}{R_{in2}} V_{in2} + ... + \frac{R_f}{R_{inN}} V_{inN}  \quad (5)

To prove equation above try to disable OUT2 and observe IN2 P2P value. Also try to change OUT2 amplitude and observe measurements.  What happens if you set OUT2 phase to 180deg?  Can you explain the result in that case?


Using an Op-Amp as a Comparator
---------------------------------

The high intrinsic gain of the op-amp and the output saturation effects can be exploited by configuring the op-amp as a comparator as in figure 14. This is essentially a binary-state decision-making circuit: if the voltage at the “+” terminal is greater than the voltage at the “-” terminal, :math:`V_{in}` > :math:`V_{ref}` , the output goes “high” (saturates at its maximum value). Conversely if :math:`V_{in}` < :math:`V_{ref}` the output goes “low”. The circuit compares the voltages at the two inputs and generates an output based on the relative values. Unlike all the previous circuits there is no feedback between the input and output; we say that the circuit is operating “open-loop”. 

.. figure:: img/Activity_13_Fig_14.png

Figure 14: Op-Amp as Comparator 

With the power disconnected, build circuit as shown in figure 14 and continue with measurements.

1. Start the Oscilloscope & Signal Generator application.
2. In the OUT1 set Amplitude value to 0.45V, and DC offset value to 0.5V to apply a offseted sine wave centered on 0.5V as the input voltage to the circuit. From the waveform 
   menu select SINE signal deselect SHOW button. Set frequency to 100Hz and select enable (ON). 
   In the OUT2 select DC signal, deselect SHOW button set Amplitude value to 0.5V to apply a DC voltage as the REFERENCE value :math:`V_{ref}` . Select enable (ON). 
3. In the IN2 settings menu set probe settings to x10.
4. On the left bottom of the screen be sure that IN1 V/div is set to 200mV/div and IN2 to 2V/div (You can set V/div by selecting the desired channel and using vertical +/- controls) 
5. For the stable acquisition set the trigger level in TRIGGER menu to 0.25V and select NORMAL.

.. figure:: img/Activity_13_Fig_15.png

Figure 15: Op-Amp as Comparator measurements

.. note::

     For comparator shown on figure 14 it follows:

     .. math:: 
          if \quad  V_{in} > V_{ref}  \quad  ; \quad V_{out} = V_{+} \quad (5)

     .. math:: 
          if \quad  V_{in} < V_{ref} \quad  ; \quad V_{out} = V_{-}

Questions
--------------

- Slew rate: discuss how you measured and computed the slew rate in the unity-gain buffer configuration, and compare this with the value listed in the OP97 data sheet.
- Buffering: explain why the buffer amplifier in figure 5 allowed the voltage divider circuit to function perfectly with differently load resistances.
- Output saturation: explain your observations of output voltage saturation in the inverting amplifier configuration and your estimate of the internal voltages drops. How close does the output come to
   the supply rails in this experiment and also later when used as a comparator with different power-supply voltages? Can you guess what the output voltage swing would be for an op-amp that is advertised as a “rail-to-rail” device?
- Comparator: discuss your measurements and what would happen if the polarity of Vref is reversed. 
