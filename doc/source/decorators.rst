================================================================
 :mod:`decorators` -- Helpful decorators to make code prettier. 
================================================================

.. module:: decorators
    :synopsis: Helpful decorators to make code prettier.
.. sectionauthor:: P.C. Shyamshankar

This module defines some decorators that can be used as syntactic sugar to make
code prettier.

.. function:: memoize(function)

    Decorates the given function to produce a caching version. Can only be used
    for deterministic functions.
