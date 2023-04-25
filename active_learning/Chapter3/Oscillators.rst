==========================
Oscillators
==========================


Objective
==========================
In this section, we will discuss the basic principles, types, and applications of oscillators in electronic circuits. Oscillators are crucial components in many electronic systems, responsible for generating a continuous waveform of a specific frequency. Oscillators can be broadly classified into two main categories: harmonic oscillators and relaxation oscillators. Understanding the principles and types of oscillators is essential for anyone working with electronic circuits and systems.


Oscillators
==========================
Oscillators are electronic components that generate periodic signals, often in the form of sinusoidal waveforms. They are used in various applications, including signal generation, frequency synthesis, and clock generation. In this introduction to oscillators, we will explore the basic principles, types, and applications of oscillators in electronic circuits.


.. image:: img/3.2/2.1.jpg
:name: oscillators
:align: center

Basic Principles of Oscillators
==========================
An oscillator is a device that converts DC power into AC signals, generating a periodic waveform. Oscillators typically consist of an amplifying component and a feedback network, which shapes the output waveform and determines the oscillation frequency. The feedback network can include passive components, such as resistors, capacitors, and inductors, or active components like transistors and operational amplifiers.

Types of Oscillators
==========================
Oscillators can be categorized into two main groups: harmonic oscillators and relaxation oscillators. Each group has its unique characteristics and applications in electronic circuits.


Harmonic Oscillators
------------------
In electronics, a harmonic oscillator is a circuit that generates a sinusoidal waveform with a specific frequency. The frequency of the oscillator is determined by the values of the circuit components, and the waveform produced is a function of the output voltage and the input signal. One of the most important properties of a harmonic oscillator is its frequency stability. This refers to the ability of the oscillator to maintain a constant frequency over time, even in the presence of changes in temperature, voltage, or other environmental factors. Frequency stability is particularly important in communication systems, where precise frequency control is essential for reliable operation.

Harmonic oscillators are widely used in electronic circuits for a variety of applications, including signal generation, frequency synthesis, and modulation. In signal generation, an oscillator is used to produce a stable and precise waveform that can be used as a reference signal or to generate a carrier signal for modulation. In frequency synthesis, multiple oscillators are combined to generate a range of frequencies, allowing for precise frequency control. In modulation, an oscillator is used to modulate the amplitude, frequency, or phase of a carrier signal, allowing for the transmission of information. The most common types of harmonic oscillators are:


**LC Oscillators**

LC oscillators utilize an LC tank circuit, which is composed of an inductor (L) and a capacitor (C) connected in parallel. The resonant frequency (f) of the LC tank circuit is determined by the following equation:

.. math:: f = \frac{1}{2 \pi \sqrt{LC}}

Where L represents the inductance (in henries) and C represents the capacitance (in farads).

The energy stored within an LC circuit alternates between the inductor and capacitor, resulting in sinusoidal voltage and current waveforms.

There are two common types of LC oscillators: Colpitts and Hartley oscillators. Both of these oscillator types employ an active element, such as a transistor or an operational amplifier, to provide gain and sustain oscillations.

.. image:: img/3.2/2.2.jpg
:name: Colpitts
:align: center

.. image:: img/3.2/2.3.jpg
:name: Hartley
:align: center

**Crystal Oscillators**

Crystal oscillators use a piezoelectric crystal, such as quartz, as the resonant element in the oscillator circuit. Due to the stability and accuracy of the crystal, these oscillators produce highly stable and precise frequencies, making them suitable for applications like timekeeping and frequency synthesis.

.. image:: img/3.2/2.4.jpg
:name: Colpitts
:align: center

**RC Oscillators**

RC oscillators use resistors (R) and capacitors (C) to generate sinusoidal waveforms. The most common type of RC oscillator is the phase-shift oscillator, which utilizes a cascade of RC circuits to create a phase shift that produces oscillation.

.. math:: \tau = RC

Relaxation Oscillators
-------------------------
Relaxation oscillators are electronic circuits that produce a periodic output waveform through the charging and discharging of a capacitor. Unlike other types of oscillators, relaxation oscillators do not require a resonant circuit to determine the frequency of oscillation. Instead, they use the charging and discharging of the capacitor to produce a waveform with a frequency that is determined by the values of the circuit components. Relaxation oscillators are often used in electronic circuits where a simple and low-cost oscillator is required. They are commonly used in applications such as clocks, timers, and tone generators. The waveform produced by a relaxation oscillator can be tailored to meet the specific needs of the application, such as a square wave, sawtooth wave, or other periodic waveform.

One of the main advantages of relaxation oscillators is their simplicity. They typically require only a few components and can be easily implemented using standard integrated circuits. Additionally, relaxation oscillators can be designed to consume very little power, making them ideal for battery-powered applications. However, relaxation oscillators do have some disadvantages. They are generally less stable than other types of oscillators and can be sensitive to changes in temperature, supply voltage, and other environmental factors. Additionally, the waveform produced by a relaxation oscillator may not be as clean or precise as that produced by other types of oscillators. The most common types of relaxation oscillators are:

**Astable Multivibrator**

An astable multivibrator is a type of electronic oscillator that generates a non-sinusoidal waveform, typically a square wave. It is classified as a relaxation oscillator, which is a category of oscillators that generate waveforms through the charging and discharging of capacitors. Astable multivibrators are widely used in applications such as frequency generators, pulse generators, and digital circuits. The astable multivibrator circuit employs two transistors or operational amplifiers (op-amps) in a cross-coupled configuration, where each transistor or op-amp alternately switches on and off. This creates a continuous oscillation, and the resulting output waveform has a specific duty cycle.

.. image:: img/3.2/2.5.jpg
:name: Colpitts
:align: center

The frequency of oscillation (f0) and the duty cycle (D) for an astable multivibrator are determined by the values of the resistors (R1, R2) and the capacitor (C1) connected in the circuit. The equations for calculating these parameters are as follows:

Frequency of the oscillation:

.. math:: f_0 = \frac{1}{\ln(2) \cdot (R_1 + 2R_2)C_1}

Duty cycle:

.. math:: D = \frac{R_1 + R_2}{R_1 + 2R_2}

By adjusting the values of R1, R2, and C1, one can control the frequency and duty cycle of the output waveform, making the astable multivibrator a versatile and widely used circuit in various electronic applications.

**Monostable Multivibrator**

A monostable multivibrator is a type of electronic oscillator that generates a single output pulse in response to an external trigger signal. It is also classified as a relaxation oscillator, which is a category of oscillators that generate waveforms through the charging and discharging of capacitors. Monostable multivibrators are commonly used in applications such as timers, pulse generators, and debounce circuits.

The monostable multivibrator circuit employs a single transistor or operational amplifier (op-amp) in combination with resistors and a capacitor. Upon receiving a trigger signal, the circuit transitions from its stable state to an unstable state, producing a pulse output. After a specific time period determined by the values of the resistor (R) and capacitor (C) in the circuit, the circuit returns to its stable state.

.. image:: img/3.2/2.6.jpg
:name: Monostable_Multivibrator
:align: center

The time duration of the output pulse (T) for a monostable multivibrator is governed by the values of the resistor (R) and the capacitor (C) connected in the circuit. The equation for calculating the pulse duration is as follows:

Time duration of the output pulse:
.. math:: T = R \cdot C \cdot \ln(1 + \frac{V_{CC}}{V_{BE}})

Here, V_CC is the supply voltage, and V_BE is the base-emitter voltage of the transistor.

You can determine the maximum repetitive rate at which the monostable multivibrator can be triggered by considering the time duration of the output pulse (T). This value depends on the resistor (R) and capacitor (C) in the circuit.

The maximum repetitive rate (f_max) can be calculated as the reciprocal of the time duration (T):

.. math:: f_\text{max} = \frac{1}{T}

Keep in mind that this value represents the maximum rate at which the monostable multivibrator can be triggered repeatedly. The actual trigger rate in a specific application may be lower, depending on the input trigger signals and other factors. By adjusting the values of R and C, one can control the duration of the output pulse, making the monostable multivibrator a highly adaptable and widely used circuit in various electronic applications.

**Bistable Multivibrator**

A bistable multivibrator, also known as a flip-flop or latch, is a type of relaxation oscillator that has two stable states. It maintains its output state until a trigger signal is applied, causing it to switch to the other state. Bistable multivibrators use cross-coupled transistors or operational amplifiers in their circuitry.

.. image:: img/3.2/2.7jpg
:name: Bistable
:align: center

Bistable multivibrators are commonly used in digital systems for storing binary information, counting, and various other applications. There are several types of bistable multivibrators, including SR (Set-Reset), D (Data), JK, and T (Toggle) flip-flops, each with unique properties and behavior.

Unlike astable and monostable multivibrators, bistable multivibrators do not have a specific frequency or time duration associated with their operation. Instead, they change their output state in response to specific input trigger signals. The output state is maintained until another trigger signal is applied, allowing for the storage and manipulation of digital information.


Conclusion
===================
Understanding the different types of oscillators and their functions is essential for anyone working with electronic circuits. By exploring the various types of oscillators and their applications, you can expand your knowledge of electronic circuit design and improve your ability to create innovative and efficient solutions in the world of electronics.

Written by Andraž Pirc

This teaching material was created by `Red Pitaya <https://www.redpitaya.com/>`_ & `Zavod 404 <https://404.si/>`_ in the scope of the `Smart4All <https://smart4all.fundingbox.com/>`_ innovation project.
