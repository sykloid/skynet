'''Tools for basic number theoretical manipulations.'''

from functools import reduce
from operator import mul

# Implementation of standard recursive definition.
# Slow, and subject to hitting the recursion limit.
def recursive_factorial(n) :
    '''Computes the factorial of a number.'''

    if n < 0 :
        raise ValueError("Factorial is not defined for negative values.")

    return 1 if n == 0 else n * recursive_factorial(n - 1)

# This one is faster, since the overhead of recursive calls is way too high.
def iterative_factorial(n) :
    '''Computes the factorial of a number.'''

    if n < 0 :
        raise ValueError("Factorial is not defined for negative values.")

    return 1 if n == 0 else reduce(mul, range(1, n + 1), 1)

# The fastest one is the one I didn't write, of course.
from math import factorial as builtin_factorial

# Use the fastest one.
factorial = builtin_factorial

def recursive_gcd(m, n) :
    '''Computes the GCD (Greatest Common Divisor) of two numbers.'''

    return m if n == 0 else recursive_gcd(n, m % n)

def iterative_gcd(m, n) :
    '''Computes the GCD (Greatest Common Divisor) of two numbers.'''

    while n :
        m, n = n, m % n

    return m

gcd = iterative_gcd
