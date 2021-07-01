BJT transistor as a switch
############################

Objective
__________

A bipolar junction transistor (BJT) can be used in many circuit configurations such as an amplifier, oscillator, filter, rectifier or just used as an on-off switch. If the transistor is biased into the linear region, it will operate as an amplifier or other linear circuit, if biased alternately in the saturation and cut-off regions, then it is being used as a switch, allowing current to flow or not to flow in other parts of the circuit. This experiment describes the BJT when operated as a switch. 


Notes
______

.. _hardware: http://redpitaya.readthedocs.io/en/latest/doc/developerGuide/125-10/top.html
.. _Oscilloscope: http://redpitaya.readthedocs.io/en/latest/doc/appsFeatures/apps-featured/oscSigGen/osc.html
.. _Signal: http://redpitaya.readthedocs.io/en/latest/doc/appsFeatures/apps-featured/oscSigGen/osc.html
.. _generator: http://redpitaya.readthedocs.io/en/latest/doc/appsFeatures/apps-featured/oscSigGen/osc.html
.. _here: http://redpitaya.readthedocs.io/en/latest/doc/developerGuide/125-14/extent.html#extension-connector-e2
.. _datasheet: https://www.sparkfun.com/datasheets/Components/2N3904.pdf

In this tutorials we use the terminology taken from the user manual when referring to the connections to the Red Pitaya STEMlab board hardware_.
Oscilloscope_ & Signal_ generator_ application is used for generating and observing signals on the circuit.
Extension connector pins used for **+5V**  voltage supply are show in the documentation here_. 


Background
___________

Switching circuits are significantly different than linear circuits. They are also easier to understand. Before investigating more complex circuits, we will begin by introducing discrete solid-state switching circuits: those built around BJTs.

A switch consists of a BJT transistor that is alternately driven between the saturation and cutoff regions. A simple version of the switch is shown in figure 1. When the input equals :math:`-V_{in}` , the base-emitter junction is reverse biased or off so no current flows in the collector. This is illustrated by the red load line shown in the figure. When the BJT is in cutoff, the circuit (ideally) has the following values: 

.. math::
  
    V_{CE} = V_{CC} \quad \text{and} \quad I_C = 0  A \quad (1)

This state is similar to an open switch.
When the input equals :math:`+V_{in}`, the transistor is driven into saturation and the following conditions occur: 

.. math::
  
    V_{CE} \approx 0 \quad \text{and} \quad I_{C_{sat}} = \frac{V_{CC}}{R_C} A \quad (2)

This state is similar to a closed switch connecting the bottom of :math:`R_C` to ground. 

.. figure:: img/Activity_24_Fig_01.png

Figure 1: NPN BJT switch and its load line

The characteristics for a BJT switch assume that:

1. :math:`-V_{in}` is low enough to drive the transistor into cutoff.
2. :math:`+V_{in}` must produce enough base current through RB to drive the transistor into saturation.
3. The transistor is an ideal component.

These conditions can be assured by designing the circuit so that:

1. :math:`-V_{in}=V_{BE}`
2. :math:`+V_{in} = V_{BE} + I_B R_B`  (:math:`V_{CC}` is a good maximum)
3. :math:`I_B > I_{C_{sat}} / \beta`    

Condition 1 guarantees that the circuit is driven into the cutoff region by the input. Conditions 2 and 3 assure that the transistor will be driven into the saturation region. An actual BJT switch differs from the ideal switch in several aspects. In practice, even in cutoff there is some small leakage current through the transistor. Also, in saturation, there is always some voltage dropped across the transistor's internal resistance. Typically, this will be between 0.2 and 0.4 V in saturation depending on the collector current and size of the device. These variations from the ideal are generally minor with a properly sized device, so we can assume near ideal conditions when analyzing or designing a BJT switch circuit. 

.. figure:: img/Activity_24_Fig_02.png

Figure 2: NPN LED switch 

Materials
__________

- Red Pitaya STEMlab 
- 1x 1kΩ Resistor
- 1x 100Ω Resistor
- 1x 5mm LED (any color)
- 1x small signal NPN transistor (2N3904)
- 1x Solder-less Breadboard

Procedure
___________

1. Build the circuit from figure 2 on the breadboard. Set :math:`R_B` = 1kΩ, :math:`R_C` = 100Ω 

.. figure:: img/Activity_24_Fig_03.png

Figure 3:  NPN LED switch on the breadboard 

2. Start the Oscilloscope & Signal generator application
3. In the OUT1 settings menu set Amplitude value to 0.5V, DC offset to 0.5 V, Frequency to 10Hz to apply the input voltage. 
   From the waveform menu select SQUARE, deselect SHOW and select enable.
4. On the left bottom of the screen be sure that  IN1 V/div is set to 200mV/div and  IN2 is set to 1V/div (You can set V/div by selecting the desired 
   channel and using vertical +/- controls)
5. Set t/div value to 20ms/div (You can set t/div using horizontal +/- controls)
6. Under IN2 menu settings set probe to x10 and vertical offset to 0.
7. Under IN1 set vertical offset to 0.

.. figure:: img/Activity_24_Fig_04.png

Figure 4:  NPN as a switch measurements

From figure 4 we can observe NPN transistor behavior when it is operating as a switch. When the base voltage is "high" the transistor is "turned on" enabling current flow from +5V voltage rail trough diode to the GND. When current starts flowing the LED will blink.
In this "turned on" state we can see that IN2 (LED voltage do not goes to 0 V). This is is the affect of the forward drop down voltages of the LED diode and Q1 transistor. From figure 4 we can measure this drop down voltage do be ~2.2V. Try to measure what amount of drop down voltage is caused by Q1 and what amount by LED. When base voltage is "low" transistor is "turned off" disabling current flow therefore the LED voltage will be same as R1 i.e 5V. 


Questions
__________

1. How much current is flowing in resistors :math:`R_C` and :math:`R_B` when the LED is on and when the LED is off?
2. Calculate the :math:`\beta` when Q1 is saturated. How does this value compare to the spec listed in the datasheet_?
