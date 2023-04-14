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
============================
A transistor is a fundamental electronic component that is used to amplify and switch electronic signals. It is a three-terminal device that is composed of a collector, a base, and an emitter. Transistors can be found in almost every electronic device, from smartphones and computers to medical equipment and automobiles. They have enabled the development of smaller, more efficient, and more powerful electronic devices, and their impact on modern technology cannot be overstated.

.. image:: img/14.1.jpg
        :name: Transistors
        :align: center

Transistors work by controlling the flow of electric current through a semiconductor material, which is typically made of silicon or germanium. The base terminal is used to control the flow of current between the collector and the emitter terminals. When a small current is applied to the base terminal, it allows a larger current to flow between the collector and the emitter, which makes it possible to amplify a signal. The ability to control the flow of current through a transistor makes it an essential component in electronic circuits. There are two main types of transistors that we will cover:

Bipolar junction transistors
===============================
Bipolar junction transistors (BJTs) are versatile electronic components that play a vital role in many electronic circuits. Their primary function is to amplify electrical signals and to act as switches in various applications. BJTs are manufactured by introducing impurities into semiconductor materials, resulting in regions with distinct electrical properties. These regions form the basis of the transistor structure, consisting of two PN junctions: one between the collector and base regions, and another between the base and emitter regions.

.. image:: img/14.2.jpg
        :name: NPN/PNP
        :align: center

The functionality of a BJT relies on the movement of electrons across these junctions. When a voltage is applied to the base-emitter junction, it induces electron flow from the emitter region to the base region. This flow of electrons generates a current within the base region, consequently prompting a larger current to flow from the collector to the emitter. The ability to amplify current is what makes BJTs invaluable in electronic circuits.

There are two main types of BJTs: NPN and PNP. The NPN BJT features a base region made from P-type material, while the collector and emitter regions are made from N-type material. In contrast, the PNP BJT has a base region made from N-type material, and both the collector and emitter regions are made from P-type material. The behavior of the transistor is contingent upon the direction of current flow, which can be manipulated by adjusting the voltage applied to the base.

.. image:: img/14.3.jpg
        :name: BJT
        :align: center

BJTs have numerous applications in modern electronics. They can be found in a wide array of devices, such as amplifiers, oscillators, and voltage regulators. Additionally, BJTs are used in digital circuits for logic gates and flip-flops. The versatility of bipolar junction transistors, along with their ability to amplify and switch signals, make them a fundamental component in the design and operation of electronic circuits.


BJT Circuit Configurations: Common Emitter, Common Collector, and Common Base
--------------------------------------------
Transistor circuits can be configured in various ways depending on the desired functionality. The three most common configurations for bipolar junction transistors (BJTs) are the common emitter, common collector, and common base configurations. Each configuration has its own unique properties and applications in electronic circuits. In this section, we will discuss the characteristics and uses of these configurations.

**Common Emitter Configuration**

In the common emitter configuration, the emitter terminal of the transistor is shared or "common" between the input and output. This configuration is widely used in amplifier circuits because of its high voltage gain and high current gain. Some key features of the common emitter configuration are:

*Inverting amplifier: The output signal is 180 degrees out of phase with the input signal.*

*High voltage and current gain: The common emitter configuration has both high voltage and current gain, making it suitable for various amplification applications.*

*Medium input and output impedance: This configuration has a moderate input impedance and output impedance, making it suitable for interfacing with other circuits.*

*Common emitter circuits are often used in audio amplifiers, oscillators, and other applications requiring signal amplification.*

**Common Collector Configuration**

In the common collector configuration, also known as the emitter follower or voltage follower, the collector terminal of the transistor is shared or "common" between the input and output. This configuration is used primarily for impedance matching and buffering applications. Some key features of the common collector configuration are:

*Non-inverting amplifier: The output signal is in phase with the input signal.*

*Unity voltage gain: The voltage gain of the common collector configuration is close to 1, meaning there is little voltage amplification.*

*High input impedance and low output impedance: This configuration has a high input impedance and low output impedance, making it ideal for impedance matching and buffering applications.*

*Common collector circuits are often used in voltage regulators, impedance matching circuits, and as buffers for driving low-impedance loads.*

**Common Base Configuration**

In the common base configuration, the base terminal of the transistor is shared or "common" between the input and output. This configuration is less commonly used compared to the common emitter and common collector configurations. Some key features of the common base configuration are:

*Non-inverting amplifier: The output signal is in phase with the input signal.*

*High voltage gain and low current gain: The common base configuration has a high voltage gain but a low current gain, making it suitable for specific amplification applications.*

*Low input impedance and high output impedance: This configuration has a low input impedance and high output impedance.*

*Common base circuits are often used in high-frequency amplifiers, such as radio frequency (RF) amplifiers, due to their high voltage gain and good frequency response characteristics.*

Field-effect transistors
=========================
Field-effect transistors (FETs) are a crucial class of electronic components with a diverse range of applications in modern electronics. These devices can be categorized into several types, including metal-oxide-semiconductor FETs (MOSFETs), junction FETs (JFETs), and insulated-gate bipolar transistors (IGBTs).

.. image:: img/14.4.png
        :name: JFET/MOS
        :align: center

MOSFETs are prevalent in contemporary electronic devices, especially in digital circuits, due to their easy on-off switching capabilities. JFETs, on the other hand, are typically employed as voltage-controlled resistors or in low-noise amplifier applications. IGBTs find use in high-power applications, such as motor control and power electronics, where they help to manage large amounts of current and voltage. One significant advantage of FETs is their high input impedance, which results in minimal current draw from the connected circuit. This characteristic makes FETs particularly beneficial in situations where the input signal is weak, such as in sensor applications or high-impedance microphone preamplifiers.

The structure of a field-effect transistor (FET) is distinct from that of a bipolar junction transistor (BJT). An FET is built using a semiconductor material, typically silicon, with a thin insulating layer, usually silicon dioxide or other metal oxide, deposited on top. This insulating layer is called the gate oxide. The gate electrode, which is typically made of metal or highly doped polysilicon, is then placed on top of the insulating layer. The gate electrode is insulated from the semiconductor material, hence the name "insulated-gate."

.. image:: img/14.5.jpg
        :name: FET
        :align: center

The semiconductor material is also doped to create source and drain regions, which are typically N-type or P-type, depending on the desired transistor type (N-channel or P-channel). These regions are created on either side of the gate electrode, separated by a narrow channel. In the case of a MOSFET, the conductivity of this channel can be controlled by the voltage applied to the gate electrode, which in turn modulates the flow of charge carriers (electrons or holes) between the source and drain regions.

The unique construction of FETs enables them to offer several advantages over BJTs, such as high input impedance, smaller device size, and better radiation tolerance. Their distinct structure allows them to be efficiently utilized in a variety of electronic applications, from digital circuits and low-noise amplifiers to high-power motor control and power electronics.

FET Circuit Configurations: Common Source, Common Drain, and Common Gate
=================================
Field-Effect Transistors (FETs) are another type of transistor that can be configured in various ways. The three most common configurations for FETs are the common source, common drain, and common gate configurations. Each configuration has its own unique properties and applications in electronic circuits.

**Common Source Configuration**

In the common source configuration, the source terminal of the FET is shared or "common" between the input and output. This configuration is widely used in amplifier circuits because of its high voltage gain and high input impedance. Some key features of the common source configuration are:

*Inverting amplifier: The output signal is 180 degrees out of phase with the input signal.*

*High voltage gain: The common source configuration has a high voltage gain, making it suitable for various amplification applications.*

*High input impedance: This configuration has a high input impedance, making it suitable for interfacing with other high-impedance circuits.*

*Common source circuits are often used in audio amplifiers, oscillators, and other applications requiring signal amplification.*

**Common Drain Configuration**

In the common drain configuration, also known as the source follower or voltage follower, the drain terminal of the FET is shared or "common" between the input and output. This configuration is used primarily for impedance matching and buffering applications. Some key features of the common drain configuration are:

*Non-inverting amplifier: The output signal is in phase with the input signal.*

*Unity voltage gain: The voltage gain of the common drain configuration is close to 1, meaning there is little voltage amplification.*

*High input impedance and low output impedance: This configuration has a high input impedance and low output impedance, making it ideal for impedance matching and buffering applications.*

*Common drain circuits are often used in voltage regulators, impedance matching circuits, and as buffers for driving low-impedance loads.*

**Common Gate Configuration**

In the common gate configuration, the gate terminal of the FET is shared or "common" between the input and output. This configuration is less commonly used compared to the common source and common drain configurations. Some key features of the common gate configuration are:

*Non-inverting amplifier: The output signal is in phase with the input signal.*

*High voltage gain and low input impedance: The common gate configuration has a high voltage gain and a low input impedance, making it suitable for specific amplification applications.*

*High output impedance: This configuration has a high output impedance.*

*Common gate circuits are often used in high-frequency amplifiers, such as radio frequency (RF) amplifiers, due to their high voltage gain and good frequency response characteristics.*

Aplication of Transistors
=======================

Transistors are versatile and fundamental components in modern electronic devices and systems. They have various applications across numerous fields, owing to their amplification, switching, and signal processing capabilities. Here are some of the primary uses of transistors:

**Switching:**
Transistors can function as electronic switches, allowing or blocking the flow of current based on the input signal. This feature is crucial in digital circuits and logic gates, which form the basis of digital electronics, microprocessors, and memory devices.

**Voltage regulation:**
Transistors can be employed in voltage regulation circuits, such as linear voltage regulators or switching regulators, to maintain a stable output voltage despite variations in input voltage or load current.

**Signal processing:**
Transistors are used in various signal processing applications, including filters, oscillators, and modulators. They can shape, generate, or modify signals in both analog and digital domains.

**Power electronics:**
Transistors, particularly power transistors and MOSFETs, play a critical role in power electronics, where they control and convert electrical energy in devices like power supplies, motor drives, and inverters.

**Sensors and instrumentation:**
Transistors are often used in sensor circuits and instrumentation amplifiers to process signals from sensors, such as temperature, pressure, or light sensors, and convert them into a usable output.

**Telecommunication:**
Transistors are vital in telecommunication systems, where they are used for signal amplification, frequency conversion, and modulation. They can be found in various devices, such as mobile phones, radio transmitters, and satellite communication systems.

**Medical equipment:**
Transistors are employed in medical devices, such as hearing aids, pacemakers, and medical imaging equipment, where they help process and control electronic signals.

**Automotive electronics:**
Transistors are utilized in various automotive electronic systems, including engine control units (ECUs), fuel injection systems, and electronic stability control (ESC) systems.

The wide range of applications demonstrates the versatility and importance of transistors in modern electronics. They have revolutionized the electronics industry and continue to be a fundamental building block in the development of innovative devices and systems.






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
