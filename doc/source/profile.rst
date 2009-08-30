======================================
 :mod:`profile` -- Tools to time code 
======================================

.. module:: profile
    :synopsis: Tools to time code.
.. sectionauthor:: P.C. Shyamshankar <sykora@lucentbeing.com>

This module defines various simple utility tools to time pieces of code.

.. class:: BasicTimer(function[, setup[, runs = 1000]])

    Instances of :class:`BasicTimer` represent a proxy to a callable, which when
    called, performs several runs through the callable and prints the time per
    pass. The actual returned results of the callable are discarded.
