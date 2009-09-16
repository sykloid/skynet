'''Combinatorial functions.'''

from functools import reduce
from operator import mul

from skynet.decorators import memoize

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

def next_permutation(items) :
    '''Returns the next lexicographical permutation of the given items.'''

    items = list(items)
    j = len(items)
    i = j - 1

    while items[i - 1] >= items[i] :
        i -= 1

    while items[j - 1] <= items[i - 1] :
        j -= 1

    items[i - 1], items[j - 1] = items[j - 1], items[i - 1]

    i += 1
    j = len(items)

    while i < j :
        items[i - 1], items[j - 1] = items[j - 1], items[i - 1]
        i += 1
        j -= 1

    return items

@memoize
def number_of_partitions(n) :
    '''Counts the number of ways in which the given number can be expressed as
    the sum of positive integers.'''

    if n < 0 :
        return 0
    if n == 0 :
        return 1

    total = 0

    for k in range(1, int(n**0.5) + 1) :
        p = n - k * (3*k - 1) // 2
        q = n - k * (3*k + 1) // 2

        a = number_of_partitions(p)
        b = number_of_partitions(q)

        total += (a + b) if k % 2 else -(a + b)

    return total
