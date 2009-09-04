from itertools import islice, count

def Fibonacci() :
    '''A Generator for the Fibonacci numbers.'''
    p, q = 0, 1

    while True :
        yield p
        p, q = q, p + q

def fibonacci(n) :
    '''Computes the nth Fibonacci number.'''

    if n in (0, 1) :
        return n

    if n % 2 :
        return fibonacci((n - 1) // 2) ** 2 + fibonacci((n + 1) // 2) ** 2
    else :
        return (2 * fibonacci((n // 2) - 1) + fibonacci(n // 2)) * fibonacci(n // 2)

def primes_until(n) :
    '''Generates all prime numbers below a given upper bound.'''

    if n < 2 :
        return []

    length = n // 2 - 1 + (n % 2)

    sieve = [True] * (length + 1)

    for i in range(int(n**0.5) >> 1) :
        if not sieve[i] :
            continue

        start = 3 + (i * (i + 3) << 1)
        step = 3 + (i << 1)

        div, mod = divmod(length - start, step)
        sieve[start:length:step] = [False] * (div + bool(mod))

    primes = [2]
    primes.extend([(i << 1) + 3 for i in range(length) if sieve[i]])

    return primes
