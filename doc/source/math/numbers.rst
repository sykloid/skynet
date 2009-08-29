====================================================================
 :mod:`math.numbers` -- Basic number theoretic manipulations 
====================================================================

.. module:: math.numbers
    :synopsis: Basic number theoretic manipulations.
.. sectionauthor:: P.C. Shyamshankar <sykora@lucentbeing.com>

This module defines some basic functions required for number theory, such as:

.. function:: factorial(n)
    
    Computes the factorial of the given number. Factorials are not defined for
    negative or non-integral numbers.

.. function:: gcd(m, n)

    Computes the GCD (Greatest Common Divisor) of the two given numbers.

.. function:: xgcd(m, n)

    Computes the GCD ``g`` of the numbers ``m`` and ``n``, as well as two
    numbers ``x`` and ``y`` such that ``m*x + n*y == g``. Returns ``(x, y,
    g)``.
