=============================================================================
 :mod:`math.sequences` -- Interesting sequences and tools to deal with them. 
=============================================================================

.. module:: math.sequences
    :synopsis: Interesting sequences and tools to deal with them.
.. sectionauthor:: P.C. Shyamshankar <sykora@lucentbeing.com>

This module defines various tools, especially generators and iterators to work
with some common and interesting sequences.

.. function:: fibonacci(n)

    Computes the nth Fibonacci number. The 0th term is defined as 0, first term
    as 1.

.. function:: Fibonacci()

    A generator for the sequence of Fibonacci Numbers, ``0, 1, 1, 2, 3, 5, 8,
    ...``, where the first two terms are 0 and 1, and each subsequent term is
    the sum of the two previous terms.

.. function:: polygonal_number(n, r)

    Computes the ``n``th ``r``-gonal number.

.. function:: triangular_number(n)

    A special case of :func:`polygonal_number`, when ``r = 3``.

.. function:: pentagonal_number(n)

    A special case of :func:`polygonal_number`, when ``r = 5``.

.. function:: hexagonal_number(n)

    A special case of :func:`polygonal_number`, when ``r = 6``.

.. function:: polygonal_numbers(r)

    A generator for the sequence of ``r``-gonal numbers.

.. function:: triangular_numbers()

    A special case of :func:`polygonal_numbers`, when ``r = 3``.

.. function:: pentagonal_numbers()

    A special case of :func:`polygonal_numbers`, when ``r = 5``.

.. function:: hexagonal_numbers()

    A special case of :func:`polygonal_numbers`, when ``r = 6``.

.. function:: primes_until(n)

    Returns a list of all prime numbers upto ``n``.

.. function:: primes_between(m, n)

    Returns a list of all prime numbers between ``m`` and ``n``.

.. function:: prime_generator()

    A generator for the infinite sequence of prime numbers.

.. function:: primes([[start], stop])

    A convenience function for unifying the various prime number generators.

    * If both ``start`` and ``stop`` are specified, :func:`primes_between` is used.
    * If only ``stop`` is specified, :func:`primes_until` is used.
    * If nothing is specified, :func:`prime_generator` is used.
