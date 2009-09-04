=============================================================================
 :mod:`math.sequences` -- Interesting sequences and tools to deal with them. 
=============================================================================

.. module:: math.sequences
    :synopsis: Interesting sequences and tools to deal with them.
.. sectionauthor:: P.C. Shyamshankar <sykora@lucentbeing.com>

This module defines various tools, especially generators and iterators to work
with some common and interesting sequences.

.. function:: Fibonacci()

    A generator for the sequence of Fibonacci Numbers, ``0, 1, 1, 2, 3, 5, 8,
    ...``, where the first two terms are 0 and 1, and each subsequent term is
    the sum of the two previous terms.

.. function:: fibonacci(n)

    Computes the nth Fibonacci number. The 0th term is defined as 0, first term
    as 1.
