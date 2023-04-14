==========================
Transistors
==========================

Introductions
-------------------------
The objective of this activity is to introduce readers to the world of transistors. We will be looking at the different types of transistors and how they function.


Background
------------------------
Transistors are one of the most important inventions of the 20th century and have been instrumental in the development of modern electronics. They are semiconductor devices that can act as switches or amplifiers, and they have replaced bulky and inefficient vacuum tubes in many electronic applications. Today, transistors are found in almost every electronic device, from smartphones and computers to medical equipment and automobiles. They have enabled the development of smaller, more efficient, and more powerful electronic devices, and their impact on modern technology cannot be overstated.


What is a transistor?
----------------------
A transistor is a fundamental electronic component that is used to amplify and switch electronic signals. It is a three-terminal device that is composed of a collector, a base, and an emitter. Transistors can be found in almost every electronic device, from smartphones and computers to medical equipment and automobiles. They have enabled the development of smaller, more efficient, and more powerful electronic devices, and their impact on modern technology cannot be overstated.

Transistors work by controlling the flow of electric current through a semiconductor material, which is typically made of silicon or germanium. The base terminal is used to control the flow of current between the collector and the emitter terminals. When a small current is applied to the base terminal, it allows a larger current to flow between the collector and the emitter, which makes it possible to amplify a signal. The ability to control the flow of current through a transistor makes it an essential component in electronic circuits. There are two main types of transistors that we will cover:

Bipolar junction transistors
---------------------
Bipolar junction transistors (BJTs) are an essential component of many electronic circuits. They are widely used for their amplification properties and for switching signals. BJTs are formed by doping semiconductor material with impurities to create regions with different electrical properties. The resulting transistor structure consists of two PN junctions. One junction is between the collector and base regions, and the other is between the base and emitter regions.

The operation of a BJT is based on the flow of electrons across the junctions. When a voltage is applied across the base-emitter junction, it creates a flow of electrons from the emitter to the base region. The flow of electrons creates a current in the base region, which in turn causes a larger current to flow from the collector to the emitter. This current amplification effect is what makes BJTs useful in electronic circuits.

There are two types of BJTs: NPN and PNP. In an NPN BJT, the base is made of P-type material and the collector and emitter are made of N-type material. In contrast, in a PNP BJT, the base is made of N-type material, and the collector and emitter are made of P-type material. The behavior of the transistor depends on the direction of the current flow, which can be controlled by the voltage applied to the base.


Field-effect transistors
------------
FETs can be classified into several types, including metal-oxide-semiconductor FETs (MOSFETs), junction FETs (JFETs), and insulated-gate bipolar transistors (IGBTs). MOSFETs are widely used in modern electronic devices and are particularly useful in digital circuits because they can be easily switched on and off. JFETs are commonly used as voltage-controlled resistors or in low-noise amplifier applications. IGBTs are used in high-power applications such as motor control and power electronics.

One of the advantages of FETs is that they have a very high input impedance, which means that they draw very little current from the circuit they are connected to. This property makes FETs particularly useful in applications where the input signal is weak, as in sensor applications or in high-impedance microphone preamplifiers.

Another advantage of FETs is that they can be made smaller than BJTs, which makes them ideal for use in miniaturized electronic devices. FETs are also less susceptible to radiation damage, making them suitable for use in space and other harsh environments.


Hands-on Experiment: Measuring Transistor Noise with Red Pitaya
============================

Transistor noise is a crucial factor in the design and optimization of electronic circuits, as it can impact the performance of the system. In this experiment, we will measure the noise characteristics of a selected transistor using the Red Pitaya. We will analyze the noise contributions, such as thermal, shot, and flicker noise, and their impact on the total noise power spectral density (PSD).


Experimental Setup
-------------------
For this experiment, we will be using a simple circuit consisting of a 1k resistor connected to the transistor's output. We will be measuring the noise characteristics of the transistor using the Red Pitaya's Spectrum Analyzer function. To power the circuit, we will use a low-noise power supply to minimize external noise contributions.

To set up the circuit, you can refer to the picture below:

.. image:: img/transistor_noise_setup.jpg
:name: Circuit
:align: center


Once the circuit is set up, you can run the Spectrum Analyzer app on the Red Pitaya's home page and set up the frequency range and resolution bandwidth to cover both low-frequency flicker noise and higher-frequency thermal and shot noise contributions (e.g., 10 Hz to 100 kHz).

To perform the measurement, power the transistor biasing circuit and observe the noise power spectral density (PSD) on the Spectrum Analyzer app. You should get a result similar to the picture below, with a spectrum displaying the noise contributions at various frequencies:

.. image:: img/transistor_noise_spectrum.png
:name: Spectrum
:align: center

To analyze the noise contributions, you can use the cursor function on the Spectrum Analyzer app, which displays the frequency and PSD (in W/Hz) value of the desired point.

.. image:: img/transistor_noise_cursor.png
:name: Cursor
:align: center



Calculations
--------------------

With the obtained noise PSD data, you can calculate the individual noise contributions, such as thermal, shot, and flicker noise, and their impact on the total noise PSD. Here are some key equations to consider when calculating noise contributions:

The following measured values were obtained from the Spectrum Analyzer app at various frequencies:

At 10 Hz: PSD = 1.50 x 10^-10 W/Hz
At 1 kHz: PSD = 5.00 x 10^-11 W/Hz
At 10 kHz: PSD = 2.00 x 10^-11 W/Hz
At 100 kHz: PSD = 1.00 x 10^-11 W/Hz
Now, let's use the equations the different noise contributions.

Thermal noise:
Assuming a room temperature of 25°C (298 K) and a resistor value of 1kΩ:

.. math:: v_t^2 = 4k_BTR\Delta f = 4 * 1.38 * 10^{-23} J/K * 298 K * 1000 \Omega * 1 Hz = 1.65 * 10^{-20} W/Hz

where v_t^2 is the thermal noise PSD, k_B is the Boltzmann constant, T is the temperature in Kelvin, R is the resistance, and Δf is the bandwidth.

Shot noise:
Assume a DC current of 1 mA (1 x 10^-3 A) through the transistor:

.. math:: i_s^2 = 2qI_\text{DC}\Delta f = 2 * 1.6 * 10^{-19} C * 1 * 10^{-3} A * 1 Hz = 3.2 * 10^{-19} W/Hz

where i_s^2 is the shot noise PSD, q is the elementary charge, I_DC is the DC current through the device, and Δf is the bandwidth.

Flicker noise:
Using the measured PSD value at 10 Hz (1.50 x 10^-10 W/Hz) and subtracting the calculated thermal and shot noise contributions:

.. math:: v_f^2 = 1.50 * 10^{-10} W/Hz - 1.65 * 10^{-20} W/Hz - 3.2 * 10^{-19} W/Hz = 1.48 * 10^{-10} W/Hz

where v_f^2 is the flicker noise PSD, K is a process-dependent constant, α and β are exponents typically close to 1, and f is the frequency.

Now, we have to calculate the individual noise contributions at different frequencies:

.. list-table::
   :header-rows: 1
   :widths: 15 25 25 25

   * - Frequency
     - Thermal Noise (W/Hz)
     - Shot Noise (W/Hz)
     - Flicker Noise (W/Hz)
   * - 10 Hz
     - 1.65 x 10^-20
     - 3.2 x 10^-19
     - 1.48 x 10^-10
   * - 1 kHz
     - 1.65 x 10^-20
     - 3.2 x 10^-19
     - negligible
   * - 10 kHz
     - 1.65 x 10^-20
     - 3.2 x 10^-19
     - negligible
   * - 100 kHz
     - 1.65 x 10^-20
     - 3.2 x 10^-19
     - negligible

Conclusion
----------------------------
In conclusion, the Red Pitaya proved to be a reliable and accurate tool for measuring and analyzing transistor noise. By measuring the noise PSD of the transistor and using the appropriate formulas, we were able to obtain the noise contributions with good precision. This experiment not only provided us with an understanding of the transistor noise characteristics, but also with the opportunity to practice using the Red Pitaya's spectrum analyzer and oscilloscope features. These skills are essential for any electronics engineer or hobbyist who works with transistors and other electronic components.

Written by Andraž Pirc

This teaching material was created by `Red Pitaya https://www.redpitaya.com/
