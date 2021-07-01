Diodes and Jupyter Notebook example
===================================

Objective
---------

The purpose of this activity is to investigate the current vs. voltage
characteristics of various solid state PN junction diodes such as the
conventional Si diode, the Schottky barrier diode, the Zener diode and
Light emitting diode (LED).

Notes
-----

.. _hardware: http://redpitaya.readthedocs.io/en/latest/doc/developerGuide/125-10/top.html
.. _here: http://redpitaya.readthedocs.io/en/latest/doc/developerGuide/125-14/extent.html#extension-connector-e2
.. _Oscilloscope: http://redpitaya.readthedocs.io/en/latest/doc/appsFeatures/apps-featured/oscSigGen/osc.html
.. _Signal: http://redpitaya.readthedocs.io/en/latest/doc/appsFeatures/apps-featured/oscSigGen/osc.html
.. _generator: http://redpitaya.readthedocs.io/en/latest/doc/appsFeatures/apps-featured/oscSigGen/osc.html
.. _Jupyter: http://jupyter.org/index.html
.. _Notebook: http://jupyter.org/index.html


In this tutorials we use the terminology taken from the user manual
when referring to the connections to the Red Pitaya STEMlab board
hardware_.

Extension connector pins used for **-3.3V** and **+3.3V** voltage
supply are show in the documentation here_.

Oscilloscope_ & Signal_ generator_ application is used for generating
and observing signals on the circuit.


Background
----------

The PN junction diode is a device which is commonly used in circuit
applications such as rectification where current is allowed to flow in
only one direction. When the diode is fabricated in silicon, the
forward voltage drop is typically 0.7 V and the :math:`{V_D}`
vs. :math:`{I_D}` characteristic relating diode voltage and current
can be described by an exponential relationship:

.. math::

   I_D = I_S \bigg( e^{\frac{V_Dq}{nkT}} - 1  \bigg)   \quad (1)

where :math:`I_{S}` and n are scale factors, and :math:`kT/q` (25.4 mV
at room temperature) is the so called thermal voltage :math:`{V_T}`.


Diode schematic symbols
-----------------------

Each type of diode has a specific schematic symbol which are
variations of the conventional diode symbol shown on the left in
figure 1. A sort of “Z” shaped cathode denotes a zener diode as in the
second symbol in figure 1. An “S” shaped cathode denotes a Schottky
diode as in the next symbol. The arrows pointing away from the diode
denotes an LED as in the symbol on the right. Arrows pointing toward
the diode would represent a photo diode light detector.


.. figure:: img/Activity_19_Fig_01.png

Figure 1: Diode schematic symbols 

Zener Diode Fundamentals
------------------------

A Zener diode is similar in construction and operation to an ordinary
diode. Unlike a conventional diode where the intended use is to
prevent current in the reverse direction, a zener diode is mostly used
in the reverse region above the breakdown voltage. Its :math:`I` vs,
:math:`V` characteristic curve is similar to ordinary diode. By
adjusting the doping of the P and N sides of the junction, it is
possible to design a Zener diode that breaks down at anywhere
from a few volts to a few hundred volts. See Figure 2. In this
breakdown or zener region the diode voltage will remain
approximately constant over a wide range of currents. The
maximum reverse-bias potential that can be applied before
entering the Zener region is called the Peak Inverse Voltage
(PIV) or the Peak Reverse Voltage (PRV).  

.. figure:: img/Activity_19_Fig_02.png

Figure 2: Forward and reverse zener diode :math:`I/V` characteristic

At voltages above the onset of breakdown, an increase in applied
voltage will cause more current to flow in the diode, but the voltage
across the diode will stay very nearly at :math:`V_Z`. A Zener diode
operated in reverse breakdown can provide a reference voltage for
systems like voltage regulators or voltage comparators.


Schottky Diode Fundamentals
---------------------------

A Schottky barrier diode uses a rectifying metal-semiconductor
junction formed by plating, evaporating or sputtering one of a variety
of metals onto n-type or p-type semiconductor material. Generally,
n-type silicon and n-type GaAs are used in commercially available
Schottky diodes. The properties of a forward biased Schottky barrier
diode are determined by majority carrier phenomena. A conventional PN
junction diode's properties are determined by minority
carriers. Schottky diodes are majority carrier devices that can be
switched rapidly from forward to reverse bias without minority carrier
storage effects. 

The normal current vs. voltage :math:`I/V` curve of a Schottky barrier
diode resembles that of a PN junction diode with the following
exceptions:

1. The reverse breakdown voltage of a Schottky barrier diode is lower
   and the reverse leakage current higher than those of a PN junction
   diode made using the same resistivity semiconductor material.
   
2. The forward voltage at a specific forward current is also lower for
   a Schottky barrier diode than for a PN junction diode. For example,
   at 2 mA forward bias current a low barrier silicon Schottky diode
   will have a forward voltage of ~0.3 volts while a silicon PN
   junction diode will have a voltage of ~0.7 volts. This lower
   forward voltage drop can cut the power dissipated in the diode by
   more than one half. This power savings can be very significant when
   the diodes need to carry large forward currents. The current
   vs. voltage (:math:`I/V`) relationship for a Schottky barrier diode
   is given by the following equation known as the Richardson
   equation. The primary difference from the conventional diode
   equation is in :math:`I_S` with the addition of the modified
   Richardson constant :math:`A^*`.
   

.. math::

   I_D = I_S \bigg( e^{\frac{V_Dq}{nkT}} - 1  \bigg)   \quad (2)

.. math::

   I_S = A A^* T^2 e^{-\frac{q \Phi B}{kT}}   \quad (3)

   
Where:

* :math:`A` = junction area
  
* :math:`A^*` = modified Richardson constant (value varies by material
  and dopant) = :math:`110 A/(°K^2-cm^2)`  for n-type Si
  
* :math:`T` = absolute temperature in :math:`K` (Kelvins)
  
* :math:`q` = electronic charge  = :math:`1.6E-19 \quad C`
  
* :math:`\Phi B` = barrier height in volts k = Boltzman's constant =
  1.37 * 10-23 J/K = :math:`1.37E-23 \quad J/K`
  
* :math:`n` = ideality factor (forward slope factor, determined by metal-semiconductor interface) 


LED Fundamentals
----------------

The LED is a junction diode that emits light when forward
biased. Actually all PN junction diodes emit photons when forward
biased, it is just that the photons are in the infrared band and the
physical shape of the diode does not allow the photons to escape the
package. To achieve the visible light emitting property, it is
necessary to fabricate the LED from materials with larger band-gaps
other than silicon. As a result, the forward voltage drop of the LED
is greater than 0.7V; usually on the order of 1.5 to 2 volts depending
on the wavelength of the emitted light. The LED is also built in a
special transparent package as shown in figure 3.


.. figure:: img/Activity_19_Fig_03.png

Figure 3: Light emitting diodes 

An LED is a semiconductor device that emits electromagnetic radiation
at optical and infrared frequencies. The device is a PN junction diode
made from p-type and n-type semiconductors, usually GaAs, GaP or
SiC. They emit light only when an external applied voltage is used to
forward bias the diode above a minimum threshold value. The gain in
electrical potential energy delivered by this voltage is sufficient to
force electrons to flow out of the n-type material, across the
junction barrier, and into the p-type region. This threshold voltage
for the onset of current flow across the junction and the production
of light is :math:`V_0`. The emission of light occurs after electrons
enter into the p-region (and holes into the n-region). These electrons
are a small minority surrounded by holes (essentially the
anti-particles of the electrons) and they will quickly find a hole to
recombine with. Energetically, the electron relaxes from the excited
state (conduction band) to the ground state (valence band). The diodes
are called light emitting because the energy given up by the electron
as it relaxes is emitted as a photon. Above the threshold value, the
current and light output increases exponentially with the bias voltage
across the diode. The quanta of energy or photon has an energy E =
hf. The relation between the photon energy and the turn-on voltage
:math:`V_0`, is:

.. math::
   
   eV_0 = E_g = hf = \frac{hc}{\lambda} \quad (4)

where:

* :math:`E_g` is the size of the energy gap
  
* :math:`V_0` is the threshold voltage
  
* :math:`f` and :math:`\lambda` are the frequency and wavelength of
  the emitted photons
  
* :math:`c` is the velocity of light
  
* :math:`e` is the electronic charge
  
* :math:`h` is Planck's constant 

  
Experiments
___________

PN junction diode VI characteristic
-----------------------------------

The current vs. voltage characteristics of the PN junction diode can
be measured using the STEMlab and the following connections shown in
figure 4. Set up the breadboard with the generator OUT1 channel output
attached to one end of the resistor. The other end of the resistor is
connected to one end of the diode being measured as shown in the
diagram. The inputs channels IN1 and IN2 are also connected different
ends the resistor, therefore diode current and voltage will be given
as: 

.. math::

   I_d = (IN_1 - IN_2) / R_1
      
   .

   V_d = IN_2

.. figure:: img/Activity_19_Fig_04.png

Figure 4: Connection diagram for diode I vs. V curves 

For measuring current vs. voltage characteristics of the PN junction
diode OUT1 generator should be configured as 1kHz triangle wave with 1
V max and 0 V min values. For measuring :math:`VI` curve an "XY" plot
is required where x-axis will represent diode voltage
:math:`IN_2` and y-axis a diode current :math:`(IN_1 - IN_2) / R_1`.
For this task we will use Jupyter Notebook Web application. 

.. note::
   The Jupyter_ Notebook_ is a web application that allows you to
   create and share documents that contain live code, equations,
   visualizations and explanatory text. They have also ensured support
   for the Jupyter application with Red Pitaya libraries enabling
   control of all features of the STEMlab boards such as: signal
   acquisition, signal generation, digital signal control,
   communication etc. The Jupyter Notebook is started on the same way
   as any other applications. After starting Jupyter application a web
   based notebook is opened.  This combination of the notebook,
   STEMlab and Python features makes the STEMlab an excellent tool for
   prototyping and quick programing. Since Jupyter Notebook enables
   text, equation and picture editing this is a perfect tool for
   tutorials, examples etc.

But before measuring :math:`VI` curve you should check voltages
signals using Oscilloscope & Signal generator application.



Materials
---------

- Solder-less Breadboard
  
- Resistor 10 Ω
  
- Conventional diode (1N4001 or similar)
  

Procedure - time domain measurements
------------------------------------

1. Build the circuit from figure 4 on the breadboard 

.. figure:: img/Activity_19_Fig_05.png

Figure 5: Connections on the breadboard  

2. Start the Oscilloscope & Signal generator application
   
3. In the OUT1 settings menu set Amplitude value to 0.5V, DC offset to
   0.5V to apply a triangle wave as the input voltage. From the
   waveform menu select TRIANGLE, deselect SHOW button and select
   enable.
   
4. On the left bottom of the screen be sure that  IN1 V/div is set to
   200mV/div (You can set V/div by selecting the desired channel and
   using vertical +/- controls)
   
5. On the left bottom of the screen be sure that  IN2 V/div is set to
   200mV/div (You can set V/div by selecting the desired channel and
   using vertical +/- controls)
   
6. Set t/div value to 200us/div (You can set t/div using horizontal
   +/- controls)
   
7. In the MATH settings menu set IN1-IN2 and select enable. **Math
   trace scaled by factor R1 represent diode current**
   


.. figure:: img/Activity_19_Fig_06.png

Figure 6: Voltages and current on the diode (Time dependent)  

From figure 6 we can see that diode start conducting when the voltage
on it exceed diode threshold voltage which is around 0.6V.

Also, diode current represented with MATH trace is observable. We can
clearly see that when the diode voltage is below 0.6 the diode current
is 0A. At point when the diode voltage exceed 0.6V diode starts
conducting and the path current is only limited by resistor R1. 


Procedure - VI characteristics measurements
-------------------------------------------

For this task we will use Jupyter Notebook Web application. 
How to start Jupyter Notebook and create new project is shown on figure 7 flow chart.

.. figure:: img/Activity_19_Fig_07.png

Figure 7: Creating new Jupyter notebook

If you have successfully created new Jupyter notebook then copy-paste
code bellow and run it. Code bellow will generate same signal as from
figure 6 but it will plot them in XY graph. For measuring :math:`VI`
curve an "XY" plot is required where x-axis will represent diode
voltage :math:`IN_2` and y-axis a diode current :math:`(IN_1 - IN_2) / R_1`.

.. note:: Copy code from below into cell 1

.. code-block:: python

   # Import libraries 
   from redpitaya.overlay.mercury import mercury as overlay

   from bokeh.io import push_notebook, show, output_notebook
   from bokeh.models import HoverTool, Range1d, LinearAxis, LabelSet, Label
   from bokeh.plotting import figure, output_file, show
   from bokeh.resources import INLINE 
   output_notebook(resources=INLINE)

   import numpy as np
      
   # Initialize fpga modules
   fpga = overlay()
   gen0 = fpga.gen(0)
   osc = [fpga.osc(ch, 1.0) for ch in range(fpga._MNO)]
   
   # Configure OUT1 generator channel 
   gen0.amplitude = 0.5
   gen0.offset = 0.5
   gen0.waveform = gen0.sawtooth(0.5)
   gen0.frequency = 2000
   gen0.start()
   gen0.enable = True
   gen0.trigger()
    
   # R1 resistor value
   R1 = 10

   # Configure IN1 and IN2 oscilloscope input channels
   for ch in osc:
   ch.filter_bypass = True
   # data rate decimation 
   ch.decimation = 10
   # trigger timing [sample periods]
   N = ch.buffer_size
   ch.trigger_pre  = 0
   ch.trigger_post = N
   # osc0 is controlling both channels
   ch.sync_src = fpga.sync_src["osc0"]
   ch.trig_src = fpga.trig_src["osc0"]
   # trigger level [V], edge ['neg', 'pos'] and holdoff time [sample periods]
   ch.level = 0.5
   ch.edg = 'pos'
   ch.holdoff = 0
       
   # Initialize diode current and voltage
   V = I = np.zeros(N)

   # Plotting
   hover = HoverTool(mode = 'vline', tooltips=[("V", "@x"), ("I", "@y")])
   tools = "wheel_zoom,box_zoom,reset,pan" 
   p = figure(plot_height=500, plot_width=900,
	      title="XY plot of diodes VI characteristic",
	      toolbar_location="right",
	      tools=(tools, hover))
   p.xaxis.axis_label = 'Voltage [V]'
   p.yaxis.axis_label = 'Current [mA]'
   r = p.line(V,I, line_width=1, line_alpha=0.7, color="blue")
		
   # get and explicit handle to update the next show cell 
   target = show(p,notebook_handle=True)

 
Create new cell (Insert -> Cell Below) and copy code from below into
it.

.. code-block:: python

   # Measuring I, V and re-plotting
   while True:
   # reset and start
   osc[0].reset()
   osc[0].start()
   # wait for data
   while (osc[0].status_run()): pass
   V0 = osc[0].data(N-100)  # IN1 signal
   V1 = osc[1].data(N-100)  # IN2 signal
   I=((V0-V1)/R1)*1E3     # 1E3 convert to mA
   r.data_source.data['x'] = V0
   r.data_source.data['y'] = I
   push_notebook(handle=target)

   
Run Cell 1 and Cell 2. Notice cell 2 is a main loop for the
acquisition and re-plotting. If you stop the acquisition just run
only cell 2 for starting measurements again.   


After running the code above you should get diode VI characteristic as
is shown on figure 8. 

.. figure:: img/Activity_19_Fig_08.png

Figure 8: Didoes VI characteristic measured using  Jupyter Notebook

From the figure 8 the typical diode VI characteristic is shown. From
the figure 8 we can see that, as the voltage on the diode is
increasing (from 0-0.5V) the diode current stays near zero until
voltage reaches values near threshold voltage (~0.6V). At this point
diode is "turned on" and the path current (diode current) is only
limited by resistor R1. In case when the diode voltage is decreasing
the VI curve is not the same, resulting in the diode hysteresis. Upper
curve from figure 8 shows that once the diode was "turned on" the
lower diode voltage will cause higher current than in the case when
the diode was previously "turned off". An ideal diode would not have
hysteresis i.e the diode current would be independent of previous
diode states but only on the diode voltage.

.. note::
   Try to answer on what is causing diode hysteresis? 





