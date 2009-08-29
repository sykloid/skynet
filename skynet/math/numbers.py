'''Tools for basic number theoretical manipulations.'''

from functools import reduce
from operator import mul

## Factorial

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

## GCD

def recursive_gcd(m, n) :
    '''Computes the GCD (Greatest Common Divisor) of two numbers.'''

    return m if n == 0 else recursive_gcd(n, m % n)

def iterative_gcd(m, n) :
    '''Computes the GCD (Greatest Common Divisor) of two numbers.'''

    while n :
        m, n = n, m % n

    return m

gcd = iterative_gcd

## Extended GCD

def iterative_xgcd(m, n) :
    '''Returns numbers x, y and g such that g = gcd(m, n) and x*m + y*n == g.'''

    x = last_y = 0
    y = last_x = 1

    while n :
        m, n, q = n, m % n, m // n

        last_x, x = x, last_x - q * x
        last_y, y = y, last_y - q * y

    return (last_x, last_y, m)

def recursive_xgcd(m, n) :
    '''Returns numbers x, y and g such that g = gcd(m, n) and x*m + y*n == g.'''

    if n == 0 :
        return (1, 0, m)

    last_x, last_y, g = recursive_xgcd(n, m % n)

    return last_y, last_x - (m // n) * last_y, g

xgcd = iterative_xgcd
