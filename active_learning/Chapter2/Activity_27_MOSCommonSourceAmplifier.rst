MOS transistor common source amplifier
######################################

Objective
_________

The purpose of this experimentis to investigate the common source configuration of the MOS transistor. 

Notes
_____

.. _hardware: http://redpitaya.readthedocs.io/en/latest/doc/developerGuide/125-10/top.html
.. _Oscilloscope: http://redpitaya.readthedocs.io/en/latest/doc/appsFeatures/apps-featured/oscSigGen/osc.html
.. _Signal: http://redpitaya.readthedocs.io/en/latest/doc/appsFeatures/apps-featured/oscSigGen/osc.html
.. _generator: http://redpitaya.readthedocs.io/en/latest/doc/appsFeatures/apps-featured/oscSigGen/osc.html
.. _here: http://redpitaya.readthedocs.io/en/latest/doc/developerGuide/125-14/extent.html#extension-connector-e2
.. _BJT common emitter amplifier: http://red-pitaya-active-learning.readthedocs.io/en/latest/Activity26_BJTCommonEmitterAmplifier.html#bjt-common-emitter-amplifier
.. _Wikipedia Common Source: https://en.wikipedia.org/wiki/Common_source
.. _Common Source Amplifier Tutorial 1: http://www.electronics-tutorials.ws/amplifier/amp_3.html
.. _MIT Common Source Amplifier Lecture: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-012-microelectronic-devices-and-circuits-fall-2005/lecture-notes/lecture19annotat.pdf
.. _Common Source Amplifier with Source Degeneration: http://examcrazy.com/Engineering/Electronics-Communication/Common_Source_Amplifier_with_Source_Degeneration.asp
.. _Common Source Amplifier Tutorial 2: https://www.slideshare.net/yordibautista/fet-basics1
.. _Transconductance: https://en.wikipedia.org/wiki/Transconductance
.. _Drain Output Resistance: http://www.ittc.ku.edu/~jstiles/312/handouts/Drain%20Output%20Resistance.pdf



In this tutorials we use the terminology taken from the user manual when referring to the connections to the Red Pitaya STEMlab board hardware_.
Oscilloscope_ & Signal_ generator_ application is used for generating and observing signals on the circuit.
Extension connector pins used for **+5V**, **-3.3V** and **+3.3V** voltage supply are show in the documentation here_. 

Background
___________

The configuration, shown in figure 1, demonstrates the NMOS transistor used as a common source amplifier.To set the transistor :math:`V_{GS}` voltage for self-biased DC operating point the voltage divider :math:`\frac{R_1}{R_2}` is chosen. Resistor :math:`R_G` is used to set the final **gain** of the amplifier. The value of :math:`R_G` resistor in combination with resistor :math:`R_1` and :math:`R_2` will affect what amount of :math:`V_{in}` is added to the :math:`V_{GS}` voltage and therefore directly setting the amplifier **gain**. Output load resistor :math:`R_L` is chosen such that, for the desired nominal drain current :math:`I_D`, the voltage appearing at :math:`V_{DS}` is approximately one third of the :math:`V_{DD}` supply voltage. Resistor :math:`R_S` is used to add source degeneration in order to stabilize the DC operating point. The best approach for selecting the :math:`R_L` and :math:`R_S` is to enable voltage drops across :math:`M_1`, :math:`R_L` and :math:`R_S` equal to the 1/3 of the :math:`V_{DD}` (at DC operating condition). Therefore :math:`R_S` = :math:`R_L`. Adding the source degeneration resistor has improved the stability of the DC operating point at the cost decreased amplifier gain. A higher gain for AC signals can be restored to some extent by adding capacitor :math:`C_S` across the degeneration resistor :math:`R_S` effectively setting the  " :math:`R_S` " value close to zero for AC signals. Capacitor :math:`C_2` is added to block the DC component of the output signal. Due to high input impedance transistor :math:`C_1` can be selected in range of :math:`< \mu F`.

.. note::
   One of the main advantages of MOS common source amplifier  over `BJT common emitter amplifier`_ is an extremely high input impedance along with a low noise output making them ideal for use in amplifier circuits that have very small input signals.
   Input impedance is effectively only dependent on input capacitance :math:`C_{iss}`, resistors :math:`R_1` and :math:`R_2` which can be selected in range of :math:`M \Omega`.

.. figure:: img/Activity_27_Fig_01.png

Figure 1: Common source amplifier configuration 

.. warning::
   Calculating and designing  of a common source amplifier is not straight forward. Common source amplifier design  will be largely dependent on the selected
   transistor(its parameters), desired frequency range and final amplifier gain. In practice many factors as input capacitance will affect the circuit behavior while this factors are largely excluded from available tutorials and theory. For more in depth understanding of common source amplifier links below are suggested:

   - [1] `Wikipedia Common Source`_ 
   - [2] `Common Source Amplifier Tutorial 1`_
   - [3] `MIT Common Source Amplifier Lecture`_ 
   - [4] `Common Source Amplifier with Source Degeneration`_
   - [5] `Common Source Amplifier Tutorial 2`_
   - [6] `Transconductance`_ :math:`g_m` 
   - [7] `Drain Output Resistance`_ :math:`r_o` 


**By making simplifications listed below Approximate Gain relation for common source amplifier shown on figure 1 can be written as shown in equation (2)**.

1. Neglecting voltage drop across :math:`C_1` capacitor. We can neglect voltage drop across capacitor :math:`C_1` in case when  :math:`1/(2 \pi f C_1) << R_G` . 
2. Neglecting :math:`C_S` impedance. If the :math:`C_S` value is selected in range :math:`C_S >> 10 \mu F` 
   its impedance will be neglectable effectively going to :math:`0 \Omega` for any AC signals. 
3. Drain Output Resistance in case of :math:`\lambda = 0` will tend to infinity , :math:`r_o \to \infty` , therefor it can be neglected in equation (1).

.. note::
   Transconductance :math:`g_m` is the change in the drain current divided by the small change in the gate/source voltage with a constant drain/source voltage. Typical values of :math:`g_m` for a small-signal field effect transistor are 1 to 30 :math:`mS` (millisiemens).

.. math::

     A_v \approx - \frac{R_1 || R_2 || Z_{iss} } {R_G + \big(R_1 || R_2 || Z_{iss} \big)} g_m \big(r_o || R_L || R_S \big) \quad (1)

with neglecting the :math:`r_o` ( :math:`r_o \to \infty`  ), we get:

.. math::

     A_v \approx - \frac{R_1 || R_2 || Z_{iss} } {R_G + \big(R_1 || R_2 || Z_{iss} \big)} g_m \big(R_L || R_S \big) \quad (2)

where :math:`Z_{iss}` is the input gate impedance due to input capacitance :math:`C_{iss}` (common-source-circuit input capacitance) of the MOS transistor.

.. math::

     Z_{iss} = \frac{1}{2 \pi f C_{iss}} \quad (3)

**If we suppose that the transistor parameters** :math:`C_{iss}` **and** :math:`g_m` **are constant values from equation (2) it follows that the gain of the common source amplifier is dependent on the peripheral resistors** :math:`R_1 , R_2, R_G, R_L, R_S` **and input signal frequency** :math:`f`. 

**If** :math:`C_{iss}` **goes to zero then the gain is dependent only on peripheral resistors** :math:`R_1 , R_2, R_G, R_L, R_S` **and transistor transconductance**  :math:`g_m` .

.. note:: 
    In practice the common-source-circuit input capacitance :math:`C_{iss}` is not zero and it can be dependent on gate voltage and amplifier gain.
    Here we will suppose that the :math:`C_{iss}` is constant value. :math:`C_{iss}` and :math:`g_m` values are commonly given in the transistor datasheet. 

Materials
__________

- Red Pitaya STEMlab 
- 4x 1MΩ Resistor
- 2x 470Ω Resistor
- 1x 100kΩ Trimer
- 2x 10uF Capacitor
- 1x 1uF Capacitor
- 1x small signal NOMS transistor (ZVN211_)
- 1x Solder-less Breadboard

.. _ZVN211: http://www.redrok.com/MOSFET_ZVN2110A_100V_320mA_4O_Vth2.4_TO-92_ELine.pdf


Procedure
_____________


Suppose that we want to design an amplifier with the gain :math:`A_v = 5` and :math:`I_L = 5mA` using ZVN211_ transistor and voltage supply :math:`V_{DD} = 5V` .
Following calculations and guidelines above we have built common source amplifier shown in figure 2.

First step is to set **DC operating point** by deciding voltages across :math:`R_L`, :math:`R_D` and :math:`M_1`.

.. math::
      
        V_{R_L}+V_{DS}+V_{R_S} = V_{CC}  \quad  (4)

If we take into account 1/3 ratio of voltages on :math:`R_L`, :math:`R_D` and :math:`M_1` we get following:

.. math::
      
        1.5 V + 2.0 V + 1.5 V = 5V  \quad      (5)

:math:`V_{DS}` is the voltage across :math:`M_1` in saturation state. 
From desired value of :math:`I_L` we can calculate :math:`R_L` as.

.. math::
      
        R_L = \frac{V_{R_L}}{I_L} = \frac{1.5V}{5mA} = 300 \Omega \quad   (6)

Following :math:`1/3 V_{DD}` voltages drops across :math:`R_L`, :math:`R_D` and :math:`M_1` we set :math:`R_S = R_L`.

.. note::

    Due to availability of the resistor we have selected :math:`R_S = R_L = 470 \Omega`.

To set the transistor :math:`V_{GS}` voltage for self-biased DC operating point the voltage divider :math:`\frac{R_1}{R_2}` is chosen such that :math:`V_G` is set above ( :math:`V_{TH} + V_S` ) voltage value (at DC operating condition).


.. math::

   V_G > (V_{TH} + V_{S}) > (2.0 V + 1.6 V) > 3.6 V \quad   (7)

   .

   \text{ 2.0 V is the threshold voltage of ZVN211 , 1.6V is the DC voltage across } R_S 

   .

   V_G = \frac{R_2}{R_1+R_2} V_{DD} \quad  (8)


For selected :math:`V_G  = 3.7 V` and :math:`R_1  = 1 M \Omega` we get (closest value) for :math:`R_2 = 3 M \Omega`   



.. figure:: img/Activity_27_Fig_02.png

Figure 2: Common source amplifier with components values

.. note::
   
  For amplifier from figure 2 and  input signal frequency of :math:`10kHz` we can calculate voltage gain using equation 2.
  For ZVN211_ we take :math:`g_m = 25 mS` and :math:`C_{iss} = 100pF`.
  
  .. math:: 

     R_1 || R_2 || Z_{iss} = 1 / \bigg( \frac{1}{R_1}+\frac{1}{R_2}+\frac{1}{Z_{iss}} = \frac{1}{R_1}+\frac{1}{R_2} + 2 \pi f C_{iss} \bigg)

     .

     = 1 / \bigg( \frac{1}{1 \times 10^6}+\frac{1}{3 \times 10^6} + 2 \cdot \pi \cdot 10 \times 10^3  \cdot 100 \times 10^{-12} \bigg) = 131 k \Omega

     .

     R_L || R_S = \frac{R_S R_L}{R_S + R_L} = \frac{470 \cdot 470}{470 + 470} = 235 \Omega

     .
     
     \text{ setting trimmer value } R_G  \text{ to }  50k \Omega \text{ we get: }  

     .
     
     A_v \approx - \frac{131 k \Omega } {50 k \Omega + 131 k \Omega} \cdot 25 \times 10^{-3} \frac{1}{\Omega} \cdot  235\Omega  

     .
    
     A_v \approx - 4.2  


1. Build the circuit from figure 2 on the breadboard.

.. figure:: img/Activity_27_Fig_03.png

Figure 3: Common source amplifier on the breadboard

2. Start the Oscilloscope & Signal generator application
3. In the OUT1 settings menu set Amplitude value to 0.1V, DC offset to 0 V  and frequency to 10kHz to apply the input voltage. From the waveform menu select SINE, 
   deselect SHOW button and select enable.
4. On the left bottom of the screen be sure that  IN1 and IN2 V/div are set to 200mV/div (You can set V/div by selecting the desired channel and using vertical +/- controls)
5. Set t/div value to 20us/div (You can set t/div using horizontal +/- controls)
6. In the trigger menu settings and select NORMAL
7. In the measurements menu select P2P for IN1 and IN2

.. figure:: img/Activity_27_Fig_04.png

Figure 4: Common source amplifier measurements

On figure 3 the measurements of the common source amplifier are shown. From the P2P measurements we can calculate achieved gain and it is approximately  :math:`A \approx 4` . Why is the difference between calculated and measured gain? This is due to input capacitance which we have assumed to be 100pF but in reality it can be different. Also values of other components and similar are not exact.  

8. In order to see affect of the gain dependency on the input signal frequency set OUT1 frequency to 5kHz and measure amplifier gain.

.. figure:: img/Activity_27_Fig_05.png

Figure 5: Common source amplifier gain at 5kHz frequency of :math:`V_{in}`

.. hint:: 
    We could set :math:`1M \Omega` resistor in series with MOSFET gate input. This would decrease affect of the parasitic capacitance and enable high input impedance regardless of the input signal frequency. As you can see from the equation 2 once the 1M resistor is added the :math:`Z_{iss}` will be "constant" and larger at high frequency therefore less affecting the input divider :math:`R_G / R_2`.
    Input impedance would become:

    .. math::

         Z_{iss} = 1M \Omega + \frac{1}{2 \pi f C_{iss}} 

    and  :math:`Z_{iss}` capacitance affect (part)

    .. math::
 
       \frac{1}{2 \pi f C_{iss}}    

    would have much less affect on the gain. I.e input signal frequency would have less affect on the amplifier gain.

Questions
__________

1. Try to add :math:`1M` resistor in series with transistor gate pin. Measure amplifier gain. What happens when OUT1 frequency is changed?
2. Try to change value of :math:`R_{G_{pot}}` and observe the change in the gain?
3. Try to change :math:`R_1` and :math:`R_2` to :math:`100k \Omega` and :math:`300k \Omega`. What is the gain dependency on :math:`V_{in}` frequency.  
 
