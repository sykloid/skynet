'''Tools for basic number theoretical manipulations.'''

from functools import reduce
from operator import mul
from random import randint

import re

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

def recursive_xgcd(m, n) :
    '''Returns numbers x, y and g such that g = gcd(m, n) and x*m + y*n == g.'''

    if n == 0 :
        return (1, 0, m)

    last_x, last_y, g = recursive_xgcd(n, m % n)

    return last_y, last_x - (m // n) * last_y, g

def iterative_xgcd(m, n) :
    '''Returns numbers x, y and g such that g = gcd(m, n) and x*m + y*n == g.'''

    x = last_y = 0
    y = last_x = 1

    while n :
        m, n, q = n, m % n, m // n

        last_x, x = x, last_x - q * x
        last_y, y = y, last_y - q * y

    return (last_x, last_y, m)

xgcd = iterative_xgcd

## Primality Testing

# Deterministic Algorithms.

# Standard test, checks every factor to the square root.
def is_prime_vanilla(n) :
    '''Tests if the given number is prime.'''
    if n < 2 :
        return False

    if n == 2 :
        return True

    if n % 2 == 0 :
        return False

    # TODO: Condense loop into any + comprehension.
    for i in range(3, int(n ** 0.5) + 1, 2) :
        if n % i == 0 :
            return False

    return True

# About as fast a deterministic test you're going to get.
def is_prime_6k1(n) :
    '''Tests if the given number is prime.'''

    if n in (0, 1) :
        return False

    if n in (2, 3) :
        return True

    if n % 2 == 0 or n % 3 == 0 :
        return False

    # TODO: Condense loop into any + comprehension.
    for i in range(6, int(n ** 0.5) + 2, 6) :
        if n % (i - 1) == 0 or n % (i + 1) == 0 :
            return False

    return True

def is_prime_regex(n) :
    '''Tests if the given number is prime.'''
    return not re.match(r"^1?$|^(11+?)\1+$", "1" * n)

# Probabilistic Algorithms.

def is_prime_fermat_pseudoprime(n) :
    '''Tests if a number is a base 2 Fermat Pseudoprime.'''

    if n < 2 :
        return False

    if n == 2 :
        return True

    return pow(2, n - 1, n) == 1

def miller_rabin_witness(a, n, t, u) :
    '''Determines if the number 'a' is a witness to the compositeness of the
    number 'n', where (n - 1) == u*2**t.
    '''

    x = pow(a, u, n)

    for i in range(t) :
        y = x*x % n

        if y == 1 and x != 1 and x != n - 1 :
            return True

        x = y

    if y != 1 :
        return True

    return False

def is_prime_miller_rabin(n, s = 25) :
    '''Tests if a the given number is prime.'''

    if n < 2 :
        return False

    if n == 2 :
        return True

    if n % 2 == 0 :
        return False

    # Express n - 1 in the form u * 2 ** t
    b = bin(n - 1)[2:]
    u = b.rstrip('0')
    t = len(b) - len(u)
    u = int(u, 2)

    # Ask each witness.
    # TODO: Condense loop into any + comprehension.
    for i in range(s) :
        a = randint(2, n - 1)
        if miller_rabin_witness(a, n, t, u) :
            return False

    return True
