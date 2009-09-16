=================================================
 :mod:`math.combinatorics` -- Tools for counting 
=================================================

.. module:: math.combinatorics
    :synopsis: Tools for counting
.. sectionauthor:: P.C. Shyamshankar <sykora@lucentbeing.com>

This module provides tools to help counting various things, like permutations,
combinations, partitions, etc.

.. function:: C(n, r)

    Computes the number of ways in which ``r`` items can be selected from ``n``
    items.

.. function:: P(n, r)
    
    Computes the number of ways in which ``r`` items can be arranged from ``n``
    items.

.. function:: next_permutation(items)

    Generates the next lexicographical permutation of the given items,
    following the given one. ``items`` must be a finite iterable consisting of
    items which are comparable.

.. function:: number_of_partitions(n)

    Computes the number of ways in which the given number ``n`` can be
    expressed as the sum of positive integers. 
