'''Tools for basic number theoretical manipulations.'''

from functools import reduce
from itertools import product
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

_gcd = iterative_gcd

def chained_gcd(*numbers) :
    '''Computes the GCD (Greatest Common Divisor) of two or more numbers.'''
    if len(numbers) < 2 :
        raise TypeError(
            "gcd() takes at least 2 positional arguments, {} given.".format(
                len(numbers)
            )
        )

    first, *rest = numbers
    return reduce(_gcd, rest, first)

gcd = chained_gcd

def _lcm(m, n) :
    '''Computes the LCM (Least Common Multiple) of two numbers.'''
    return m * n // gcd(m, n)

def chained_lcm(*numbers) :
    if len(numbers) < 2 :
        raise TypeError(
            "lcm() takes at least 2 positional arguments, {} given.".format(
                len(numbers)
            )
        )

    first, *rest = numbers
    return reduce(_lcm, rest, first)

lcm = chained_lcm

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

# A cache for primality testing. Improves speeds dramatically.
prime_cache = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
               43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# Standard test, checks every factor to the square root.
def is_prime_vanilla(n) :
    '''Tests if the given number is prime.'''
    if n < 2 :
        return False

    if n == 2 :
        return True

    if n % 2 == 0 :
        return False

    return all(n % i for i in range(3, int(n ** 0.5) + 1, 2))

# About as fast a deterministic test you're going to get.
def is_prime_6k1(n) :
    '''Tests if the given number is prime.'''

    if n in (0, 1) :
        return False

    if n in (2, 3) :
        return True

    if n % 2 == 0 or n % 3 == 0 :
        return False

    return all(n % (i - 1) and n % (i + 1) for i in range(6, int(n**0.5) + 2, 6))

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
    '''Tests if the given number is prime.'''

    if n < 2 :
        return False

    if n in prime_cache :
        return True

    if any((n % i) == 0 for i in prime_cache) :
        return False

    # Express n - 1 in the form u * 2 ** t
    b = bin(n - 1)[2:]
    u = b.rstrip('0')
    t = len(b) - len(u)
    u = int(u, 2)

    # Ask each witness.
    return not any(miller_rabin_witness(randint(2, n - 1), n, t, u) for i in range(s))

def is_prime(n) :
    '''Tests if the given number is prime.'''
    return is_prime_miller_rabin(n) if n >> 25 else is_prime_6k1(n)

is_prime_deterministic = is_prime_6k1

## Factorization

def prime_factors_trial_division(n) :
    '''Factorizes a number into prime factors and corresponding exponents.'''

    if is_prime(n) or n == 1 :
        yield (n, 1)
        return

    exponent = 0
    while n % 2 == 0:
        exponent += 1
        n //= 2

    if exponent :
        yield(2, exponent)

    i = 3
    while n != 1 :
        exponent = 0
        while n % i == 0 :
            exponent += 1
            n //= i

        if exponent :
            yield (i, exponent)
        i += 2

    return

prime_factors = prime_factors_trial_division

def divisors_cartesian_product(n) :
    '''Generates all the divisors of the given number. Does not yield in order.'''

    if n == 1 :
        return [1]

    return (
        reduce(mul, factors, 1)
        for factors in product(
            *[[p**i for i in range(e + 1)] for (p, e) in prime_factors(n)]
        )
    )

divisors = divisors_cartesian_product

## Multiplicative functions.

def phi(n) :
    '''Returns the Euler Totient function of the given number.

    This is the number of positive integers less than and relatively prime to
    the given number.
    '''

    return reduce(mul, (p**(e - 1) * (p - 1) for p, e in prime_factors(n)), 1)

def sigma(n, k = 1) :
    '''Returns the sum of the kth powers of the divisors of the given number.'''

    if n == 1 :
        return 1

    return reduce(
        mul,
        (sum(p**(j*k) for j in range(e + 1)) for (p, e) in prime_factors(n)),
        1
    )

# Equivalent do sigma(n, 0), but this method is faster.
def tau(n) :
    '''Returns the number of divisors of the given number.'''

    if n == 1 :
        return 1

    return reduce(mul, (e + 1 for p, e in prime_factors(n)), 1)

## Digits, and related.

def digits(n) :
    '''Returns the sequence of digits of the given number.'''

    return tuple(int(i) for i in str(n))

def is_palindrome(n) :
    '''Determines if the given number is a palindrome.'''

    d = tuple(digits(n))
    return d == d[::-1]

## Square Testing.

square_endings = {0x00, 0x01, 0x04, 0x09, 0x10, 0x11, 0x19, 0x21, 0x24, 0x29,
                   0x31, 0x39}

def is_square(n) :
    '''Determines if the given umber is a square.'''

    if n & 0x3f not in square_endings :
        return False

    root = int(n**0.5)
    return root*root == n
