Digital Information and Numerical Bases
#######################################


Digital Information
===================

The information is represented by numbers written in a digital way. Why digital? When you have finite components to store information, it must be written digitally, that is what your calculator does. It always stores a finite amount of digits, so for numbers with infinite digits like 5.444…, a calculator with 3 significant digits rounds it to 5.44. Otherwise if you represent a number infinitely precise it is represented analogically, as is the case with the number 5.444….

Representation of Numbers
=========================

We commonly store numbers in a decimal base, because of our ten fingers. But the numbers can be represented in other bases like binary, octal and hexadecimal. These bases are multiples of two and have many advantages that can be used. Our computers, processors and digital systems store the numbers in a binary base. In a digital system the bases are represented by voltage levels, like 0, 3.3V, 5V. The further to the left a digit is in a number, the more value it has. The left-most digit has the highest value so it is called the most significant digit, the one on the far right has the least value and is called the least significant digit. The same is true for the binary system, except that digits are bits. In binary base these names are often used – the most significant bit (MSB for short) and the least significant bit (LSB). First let’s start with the decimal base.

Decimal Base
------------

0, 1, 2, 3, 4, 5, 6, 7, 8 and 9 form the symbols of the decimal base. To represent this base in an electrical system we would need ten different voltage levels. Numbers greater than nine and smaller than zero need additional digits/symbols to be represented. For example let’s write the number 11.5.

:math:`1*10^1 + 1*10^0 + 5*10^{-1}` =  11.5\ :sub:`10`\

In base 10 the number is written like this – 11.5\ :sub:`10`\.

Binary Base
-----------

0 and 1 form the symbols of the binary base. Digits in this base are called bits and if a number in this base has n digits, then it is said that it has n bits. To represent this base in an electrical system we would need two different voltage levels/states – which can easily be described as “on/off” (on = 1, off = 0). Numbers greater than one and smaller than zero need additional digits/symbols to be represented. For example 11.5\ :sub:`10`\  in base two is represented as 1011.1\ :sub:`2`\,

:math:`1*2^3+0*2^2+1*2^1+1*2^0 + 1*2^{-1}` = 1011.1\ :sub:`2`\ = 11.5\ :sub:`10`\

Multiplications and divisions by two in this base are very simple (like multiplication and division by 10 in the decimal system). If you multiply by two you rotate the number to the left for one bit and if you divide by two you rotate it to the right for one bit, for example:

:math:`(1*2^3+0*2^2+1*2^1+1*2^0 + 1*2^{-1})*2 = 1*2^4+0*2^3+1*2^2+1*2^1 + 1*2^0 =` 10111\ :sub:`2`\  = 23\ :sub:`10`\

:math:`(1*2^3+0*2^2+1*2^1+1*2^0 + 1*2^{-1})/2 = 1*2^2+0*2^1+1*2^0+1*2^{-1} + 1*2^{-2}` = 101.11\ :sub:`2`\  = 101.11\ :sub:`2`\  = 5.75\ :sub:`10`\

Octal Base 
----------

0, 1, 2, 3, 4, 5, 6 and 7 form the symbols of the octal base. To represent this base in an electrical system we would need eight different voltage levels. Numbers greater than seven and those smaller than zero need additional digits/symbols to be represented. For example 11.5\ :sub:`10`\  in octal base is represented as 13.4\ :sub:`8`\ ,

:math:`1*2^3+0*2^2+1*2^1+1*2^0 + 1*2^{-1} + 0*2^{-2} + 0*2^{-3} =1*8^1 + (2+1)*8^0 + 4*8^{-1} = 1*8^1+3*8^0+4*8^{-1}` = 13.4\ :sub:`8`\  = 11.5\ :sub:`10`\

As 8 is :math:`2^3` you can group three digits/bits of a number written in a binary base to form one digit in the octal base. Example: 

100 001 111\ :sub:`2`\ = 417\ :sub:`8`\

Hexadecimal Base
----------------

0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E and F form the symbols of the hexadecimal base. To represent this base in an electrical system we would need sixteen different voltage levels. Numbers greater than seven and those smaller than zero need additional digits/symbols to be represented. For example 11.5\ :sub:`10`\  in the hexadecimal base is represented as B.8\ :sub:`16`\ ,

:math:`1*2^3+0*2^2+1*2^1+1*2^0 + 1*2^{-1} + 0*2^{-2}+0*2^{-3} + 0*2^{-4} = 11*16^0 + 8*16^{-1}` = B.8\ :sub:`16`\  = 11.5\ :sub:`10`\

In this case B in hexadecimal would be 11 in decimal. As 16 is :math:`2^4` you can group four digits/bits of a number written in a binary base to form one digit in the hexadecimal base. Example:

1000 1111\ :sub:`2`\ = 8F \ :sub:`16`\

Numbers in Different Bases
--------------------------

.. table::
    :align: center

    +------------------+------------------+------------------+----------------+ 
    | Number base 10   | Number base 2    | Number base 8    | Number base 16 |
    +==================+==================+==================+================+
    |0	               | 0000	          | 0                | 0              |
    +------------------+------------------+------------------+----------------+ 
    |1	               | 0001	          | 1                | 1              |
    +------------------+------------------+------------------+----------------+ 
    |2	               | 0010	          | 2                | 2              |
    +------------------+------------------+------------------+----------------+ 
    |3	               | 0011	          | 3                | 3              |
    +------------------+------------------+------------------+----------------+ 
    |4	               | 0100	          | 4                | 4              |
    +------------------+------------------+------------------+----------------+ 
    |5	               | 0101	          | 5                | 5              |
    +------------------+------------------+------------------+----------------+ 
    |6	               | 0110	          | 6                | 6              |
    +------------------+------------------+------------------+----------------+ 
    |7	               | 0111	          | 7                | 7              |
    +------------------+------------------+------------------+----------------+ 
    |8	               | 1000	          | 10               | 8              |
    +------------------+------------------+------------------+----------------+ 
    |9	               | 1001	          | 11               | 9              |
    +------------------+------------------+------------------+----------------+ 
    |10	               | 1010	          | 12               | A              |
    +------------------+------------------+------------------+----------------+ 
    |11	               | 1011	          | 13               | B              |
    +------------------+------------------+------------------+----------------+ 
    |12	               | 1100	          | 14               | C              |
    +------------------+------------------+------------------+----------------+ 
    |13	               | 1101	          | 15               | D              |
    +------------------+------------------+------------------+----------------+ 
    |14	               | 1110	          | 16               | E              |
    +------------------+------------------+------------------+----------------+ 
    |15	               | 1111	          | 17               | F              |
    +------------------+------------------+------------------+----------------+ 


Negative Numbers
----------------

To represent a negative number in any base you only need to add the “-“ symbol in front of the number, but how to store it in a memory? When we store numbers in the binary base we could add one additional bit to the number, one extra element of memory, to say if it is negative or positive. We usually write the minus sign before a number – the same is done in binary where, in case of signed numbers, the MSB gives the sign of the number. If the MSB is 0 then the signal is positive and if MSB is 1 then the signal is negative. For example:

+11.5\ :sub:`10`\ = +1011.1\ :sub:`2`\ = 01011.1\ :sub:`2`\

-11.5\ :sub:`10`\ = -1011.1\ :sub:`2`\ = 11011.1\ :sub:`2`\
