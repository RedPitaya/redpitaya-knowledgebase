Karnaugh Map
############

This is a graphical method to simplify Boolean functions. It consists of grouping the terms of a truth table and its simplification to use least possible amount of terms. Let’s start with the OR function.

f(a,b) = a + b 


.. table:: Truth Table
    :align: center
    
    +-------+-------+----------------+
    |a      |b      |c = a OR b      |
    +=======+=======+================+
    |0      |0      |0               |
    +-------+-------+----------------+
    |0      |1      |1               |
    +-------+-------+----------------+
    |1      |0      |1               |
    +-------+-------+----------------+
    |1      |1      |1               |
    +-------+-------+----------------+



The function in canonical form is:

f = (!a X b) + (a X !b) + (a X b)     

---   repeating (a X b) because of a + a = a

f = (!a X b) + (a X !b) + (a X b) + (a X b)   

=b X (!a + a) + a X (!b + b) = b + a

The Karnaugh map is formed with the terms of the truth table:


.. figure:: ./../img/karnaughOR.png
    :height: 200px
    :align: center

    Karnaugh Map

Grouping the terms in red gives: !a X b + a X b = b

Grouping the terms in green gives: a X !b + a X b = a

The result is f = a + b .

The terms/ones must be grouped in multiples of power of two (2, 4, 8, 16, …) and the objective is the simplification of the function. The bigger the group the better the simplification is. All ones should be in one group and it is better not to repeat terms. The simplification of a function is better, if it is possible to make a group. Let’s do the example of the function f(a,b,c) = (a X b) + c

.. table:: Truth table of the function
    :align: center

    +-----+-----+-----+---------------+
    |a    |b    |c    |f(a,b,c)       |
    +=====+=====+=====+===============+
    |0    |0    |0    |0              |
    +-----+-----+-----+---------------+
    |0    |0    |1    |1              |
    +-----+-----+-----+---------------+
    |0    |1    |0    |0              |
    +-----+-----+-----+---------------+
    |0    |1    |1    |1              |
    +-----+-----+-----+---------------+
    |1    |0    |0    |0              |
    +-----+-----+-----+---------------+
    |1    |0    |1    |1              |
    +-----+-----+-----+---------------+
    |1    |1    |0    |1              |
    +-----+-----+-----+---------------+
    |1    |1    |1    |1              |
    +-----+-----+-----+---------------+

|
|
|  

.. figure:: ./../img/karnaughfunction.png
    :height: 200px
    :align: center

    Karnaugh Map

!a X b X c is repeated twice.

Grouping the terms in green gives: a X b X c + a X b X !c = a X b

Grouping the terms in red gives: !a X !b X c + !a X b X c + a X !b X c + a X b X c  = c 

The result is f = (a X b) + c .

The next truth table represents a function with four input variables. The Karnaugh map will be a 4x4 square with 16 terms.

.. table:: Truth table of the function
    :align: center
    
    +-----+-----+-----+-----+---------------+
    |a    |b    |c    |d    |f(a,b,c,d)     |
    +=====+=====+=====+=====+===============+
    |0    |0    |0    |0    |0              |
    +-----+-----+-----+-----+---------------+
    |0    |0    |0    |1    |0              |
    +-----+-----+-----+-----+---------------+
    |0    |0    |1    |0    |0              |
    +-----+-----+-----+-----+---------------+
    |0    |0    |1    |1    |0              |
    +-----+-----+-----+-----+---------------+
    |0    |1    |0    |0    |1              |
    +-----+-----+-----+-----+---------------+
    |0    |1    |0    |1    |0              |
    +-----+-----+-----+-----+---------------+
    |0    |1    |1    |0    |1              |
    +-----+-----+-----+-----+---------------+
    |0    |1    |1    |1    |0              |
    +-----+-----+-----+-----+---------------+
    |1    |0    |0    |0    |0              |
    +-----+-----+-----+-----+---------------+
    |1    |0    |0    |1    |1              |
    +-----+-----+-----+-----+---------------+
    |1    |0    |1    |0    |1              |
    +-----+-----+-----+-----+---------------+
    |1    |0    |1    |1    |1              |
    +-----+-----+-----+-----+---------------+
    |1    |1    |0    |0    |0              |
    +-----+-----+-----+-----+---------------+
    |1    |1    |0    |1    |1              |
    +-----+-----+-----+-----+---------------+
    |1    |1    |1    |0    |1              |
    +-----+-----+-----+-----+---------------+
    |1    |1    |1    |1    |1              |
    +-----+-----+-----+-----+---------------+

|
|
|

.. figure:: ./../img/karnaughfunction4var.png
    :height: 300px
    :align: center

    Karnaugh Map

Grouping the terms in green gives: !a X b X !d

Grouping the terms in red gives: a X d

Grouping the terms in blue gives: a X c

The result is f = (!a X b X !d) + (a X d) + (a X c)
