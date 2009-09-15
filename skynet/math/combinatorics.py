'''Combinatorial functions.'''

from functools import reduce
from operator import mul

def C(n, r) :
    '''Computes the number of combinations of n items taken r at a time.'''

    if r < 0 or r > n :
        raise ValueError("Cannot choose {} items from {}".format(r, n))
    return reduce(mul, range(n - r + 1, n + 1), 1) // reduce(mul, range(1, r + 1), 1)

def P(n, r) :
    '''Computes the number of permutations of n items taken r at a time.'''

    if r < 0 or r > n :
        raise ValueError("Cannot permute {} items from {}".format(r, n))
    return reduce(mul, range(n - r + 1, n + 1), 1)
