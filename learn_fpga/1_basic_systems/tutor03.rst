Mathematical Operations with the Binary Base
############################################


Operations in the binary base are equal to those in the decimal base. The difference is when we need to store numbers with a finite amount of bits. Let’s do some operations with 8 bits, where the MSB is the sign bit and the other 7 bits hold the magnitude of the number. We should be careful to operate with MSB separately as we do with plus and minus signs in the decimal base.

Sum
===

104\ :sub:`10`\ + 2\ :sub:`10`\ = 0110 1000\ :sub:`2`\ + 0000 0010\ :sub:`2`\ = 0110 1010\ :sub:`2`\ = 106\ :sub:`10`\  

As both summands are positive (their MSBs are 0), the most significant bit of the result is also 0. The result also isn’t greater than the maximum possible number we can write with 7 numerical bits 0111 1111\ :sub:`2`\ – so an overflow didn’t occur.

104\ :sub:`10`\ + 24\ :sub:`10`\ = 0110 1000\ :sub:`2`\ + 0001 1000\ :sub:`2`\ =  1000 0000\ :sub:`2`\ = 0\ :sub:`10`\  

In this example the second number is bigger than in the first example, but the result is unusually small – that is because an overflow occurred: we only have enough bits to store binary numbers with 7 digits, but our result has 8 digits (not counting the MSB, as it is used to store the sign) and due to that the highest, eight, digit gets cut off, as we do not have enough space to store it – this is called an overflow and the result we get is incorrect.

Subtraction
===========

-104\ :sub:`10`\ - 2\ :sub:`10`\ = -(104\ :sub:`10`\ + 2\ :sub:`10`\ )= -(0110 1000\ :sub:`2`\ + 0000 0010\ :sub:`2`\) = 1110 1010\ :sub:`2`\= - 106\ :sub:`10`\    

Here we subtracted two negative numbers so the result is negative (MSB of the result is 1). The overflow can also occur with negative numbers as seen in the following example:

-104\ :sub:`10`\ - 24\ :sub:`10`\ = -(104\ :sub:`10`\ + 24\ :sub:`10`\ ) = -(0110 1000\ :sub:`2`\ + 0001 1000\ :sub:`2`\) = 1000 0000\ :sub:`2`\   

The next example shows a subtraction of a positive and a negative number.

-104\ :sub:`10`\ + 24\ :sub:`10`\ = -(104\ :sub:`10`\ - 24\ :sub:`10`\ ) = -(0110 1000\ :sub:`2`\ - 0001 1000\ :sub:`2`\) = 1101 0000\ :sub:`2`\   

Multiplication
==============

2\ :sub:`10`\ * 60\ :sub:`10`\ = 0000 0010\ :sub:`2`\ * 0011 1100\ :sub:`2`\ = 0111 1000\ :sub:`2`\ = 120\ :sub:`10`\

-2\ :sub:`10`\ * 60\ :sub:`10`\ = -0000 0010\ :sub:`2`\ * 0011 1100\ :sub:`2`\ = -0111 1000\ :sub:`2`\ = 1111 1000\ :sub:`2`\ = - 120\ :sub:`10`\

In none of the cases shown above did an overflow occur.

Division
========

60\ :sub:`10`\/2\ :sub:`10`\ = 0011 1100\ :sub:`2`\ / 0000 0010\ :sub:`2`\ = 0001 1110\ :sub:`2`\ = 30\ :sub:`10`\

If the division results in a decimal number, the decimal places are discarded.

Two Complement
==============

The way we do arithmetic operations on paper, like carrying numbers over and deciding which number is greater to influence the sign of the result, when performing a subtraction, is difficult to implement in a digital system. To overcome that there is another way to represent finite binary numbers and it’s called two complement. It is easier to perform calculations of sum and subtraction using two complement representation.

The main advantage of two complement is that we do not have two numbers representing 0 when working with signed numbers (in signed magnitude notation the numbers 0000\ :sub:`2`\ and 1000\ :sub:`2`\ represent +0 and -0 (written with 4 bits), which makes computer calculations more complex). So the two complement always has one negative number more when written with finite bits (0 is defined as a positive number).

First we define how many bits we are working with. After that we perform an operation to find the two complement of a negative number. If you have to do the complement of a number x of n bits, the operation is this, y\ :sub:`2`\ = ( :math:`2^n` - x)\ :sub:`2`\. For example we are working with 3 bits and we want to know the two complement of -010\ :sub:`2`\, doing the operation,

y\ :sub:`2`\  = 1000\ :sub:`2`\  – 010\ :sub:`2`\  = 110\ :sub:`2`\ , and the result is -010\ :sub:`2`\  represented in two complement.

Adding and subtracting numbers becomes easy.

3\ :sub:`10`\  – 2\ :sub:`10`\  = 011\ :sub:`2`\  – 010\ :sub:`2`\  = 011\ :sub:`2`\  + (1000\ :sub:`2`\  - 010\ :sub:`2`\ ) =011\ :sub:`2`\  + 110\ :sub:`2`\  = 1001\ :sub:`2`\  = 010\ :sub:`2`\, in this case we have to discard the MSB, the result is correct as the operands had different signs.

3\ :sub:`10`\  +2\ :sub:`10`\  = 011\ :sub:`2`\  + 010\ :sub:`2`\  = 101\ :sub:`2`\, the result is wrong as the sign of the operands are equal, but the sign of the result is different => an overflow occurred (maximum positive number is 011\ :sub:`2`\ = 3\ :sub:`10`\).

-3\ :sub:`10`\  – 2\ :sub:`10`\  = 101\ :sub:`2`\  + 110\ :sub:`2`\  = 1011\ :sub:`2`\, the result is wrong as the sign of the operands are equal, but the of the result is different => an overflow occurred (the maximum negative number is 100\ :sub:`2`\ = -4\ :sub:`10`\).

-3\ :sub:`10`\  – 1\ :sub:`10`\  = 101\ :sub:`2`\  + 111\ :sub:`2`\  = 1100\ :sub:`2`\  = 100\ :sub:`2`\ , the result is correct as the sign of the operand are equal and the sign of the result is equal (we still need to discard the MSB).

There exists a way easier way of getting a 2's complement of a number. For example, we want to get the equvalent of -24\ :sub:`10`\ in the binary base, written as a 2's complement with 8 bits:

Firstly we write the negative number as a positive one in the binary base:

24\ :sub:`10`\ = 00011000\ :sub:`2`\

Then, going from LSB to MSB we just copy the digits until we get to the first 1, we also copy the fist 1, afterwards we just negate all the remaining bits and we get:

-24\ :sub:`10`\ = 11101000\ :sub:`2`\

If we calculate -24\ :sub:`10`\ with the previously mentioned formula (y\ :sub:`2`\ = ( :math:`2^n` - x)\ :sub:`2`\) we get:

-24\ :sub:`10`\  = 100000000\ :sub:`2`\  – 00011000\ :sub:`2`\  = 11101000\ :sub:`2`\

    

.. table::
    :align: center

    +-----------------+-----------------+-------------------------+
    |Decimal number   |Binary number    | 3 bits complement two   |
    +=================+=================+=========================+
    | 3               |011              |011                      |
    +-----------------+-----------------+-------------------------+
    | 2               |010              |010                      |
    +-----------------+-----------------+-------------------------+
    | 1               |001              |001                      |
    +-----------------+-----------------+-------------------------+
    | 0               |000              |000                      |
    +-----------------+-----------------+-------------------------+
    | -1              |100              |111                      |
    +-----------------+-----------------+-------------------------+
    | -2              |101              |110                      |
    +-----------------+-----------------+-------------------------+
    | -3              |110              |101                      |
    +-----------------+-----------------+-------------------------+
    | -4              |111              |100                      |
    +-----------------+-----------------+-------------------------+
