import unittest
from skynet.math import sequences
from skynet.math.numbers import is_prime
from itertools import takewhile

class FibonacciTest(unittest.TestCase) :
    known_values = {
        0 : 0,
        1 : 1,
        2 : 1,
        3 : 2,
        10 : 55,
        20 : 6765,
        30 : 832040,
        40 : 102334155,
        50 : 12586269025,
        100 : 354224848179261915075,
    }

    def test_fibonnaci_ordinal_known_values(self) :
        for n, f in self.known_values.items() :
            self.assertEqual(f, sequences.fibonacci(n))

    def test_fibonacci_sequence(self) :
        f = sequences.Fibonacci()
        self.assertEqual(next(f), 0)
        self.assertEqual(next(f), 1)
        self.assertEqual(next(f), 1)

        p = q = 1
        for i in range(3, 101) :
            x = next(f)
            if i in self.known_values :
                self.assertEqual(self.known_values[i], x)

            self.assertEqual(x, p + q)

            p, q = q, x

class PrimeTest(unittest.TestCase) :
    ranges = {
        (1, 10) : [i for i in range(1, 10) if is_prime(i)],
        (10, 100) : [i for i in range(10, 100) if is_prime(i)],
        (100, 1000) : [i for i in range(100, 1000) if is_prime(i)],
        (1000, 100000) : [i for i in range(1000, 10000) if is_prime(i)],
    }

    bound = 100000

    ref = [i for i in range(bound) if is_prime(i)]

    def test_primes_between(self) :
        for lower, upper in self.ranges :
            ref = [i for i in range(lower, upper) if is_prime(i)]
            self.assertEqual(ref, list(sequences.primes_between(lower, upper)))

    def test_primes_until(self) :
        self.assertEqual(self.ref, list(sequences.primes_until(self.bound)))

    def test_prime_generator(self) :
        g = sequences.prime_generator()
        self.assertEqual(
            self.ref,
            list(takewhile(lambda n: n < self.bound, sequences.prime_generator()))
        )

if __name__ == '__main__':
    unittest.main()
