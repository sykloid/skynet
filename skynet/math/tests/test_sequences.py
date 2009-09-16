import unittest
from skynet.math import sequences
from skynet.math.numbers import is_prime
from itertools import takewhile, islice
from fractions import Fraction

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

class PolygonalNumbersTest(unittest.TestCase) :
    known_triangular_numbers = {
        1 : 1,
        2 : 3,
        3 : 6,
        4 : 10,
        5 : 15,
        6 : 21,
        7 : 28,
        8 : 36,
        9 : 45,
        10 : 55,
        50 : 1275,
        100 : 5050,
        500 : 125250,
        729 : 266085,
        911 : 415416,
    }

    known_pentagonal_numbers = {
        1 : 1,
        2 : 5,
        3 : 12,
        4 : 22,
        5 : 35,
        6 : 51,
        7 : 70,
        8 : 92,
        9 : 117,
        10 : 145,
        50 : 3725,
        100 : 14950,
        500 : 374750,
        729 : 796797,
        911 : 1244426,
    }

    known_hexagonal_numbers = {
        1 : 1,
        2 : 6,
        3 : 15,
        4 : 28,
        5 : 45,
        6 : 66,
        7 : 91,
        8 : 120,
        9 : 153,
        10 : 190,
        50 : 4950,
        100 : 19900,
        500 : 499500,
        729 : 1062153,
        911 : 1658931,
    }

    TEST_BOUND = 1000

    def test_triangular_number_ordinal(self) :
        for k, t in self.known_triangular_numbers.items() :
            self.assertEqual(t, sequences.triangular_number(k))

    def test_pentagonal_number_ordinal(self) :
        for k, t in self.known_pentagonal_numbers.items() :
            self.assertEqual(t, sequences.pentagonal_number(k))

    def test_hexagonal_number_ordinal(self) :
        for k, t in self.known_hexagonal_numbers.items() :
            self.assertEqual(t, sequences.hexagonal_number(k))

    def test_triangular_number_sequence(self) :
        t = sequences.triangular_numbers()
        for i in range(self.TEST_BOUND) :
            n = next(t)
            if i in self.known_triangular_numbers :
                self.assertEqual(self.known_triangular_numbers[i], n)

    def test_pentagonal_number_sequence(self) :
        t = sequences.pentagonal_numbers()
        for i in range(self.TEST_BOUND) :
            n = next(t)
            if i in self.known_pentagonal_numbers :
                self.assertEqual(self.known_pentagonal_numbers[i], n)

    def test_hexagonal_number_sequence(self) :
        t = sequences.hexagonal_numbers()
        for i in range(self.TEST_BOUND) :
            n = next(t)
            if i in self.known_hexagonal_numbers :
                self.assertEqual(self.known_hexagonal_numbers[i], n)

class RationalsTest(unittest.TestCase) :
    known_values = (
        Fraction(1, 1),
        Fraction(1, 2),
        Fraction(2, 1),
        Fraction(1, 3),
        Fraction(3, 2),
        Fraction(2, 3),
        Fraction(3, 1),
        Fraction(1, 4),
        Fraction(4, 3),
        Fraction(3, 5),
        Fraction(5, 2),
        Fraction(2, 5),
        Fraction(5, 3),
        Fraction(3, 4),
        Fraction(4, 1),
    )

    def test_rationals(self) :
        self.assertEqual(self.known_values, tuple(islice(sequences.rationals(), 15)))

class CoprimePairsTest(unittest.TestCase) :
    known_values = {
        5 : [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 5), (3, 4),
             (3, 5), (4, 5)],
        7 : [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 3),
             (2, 5), (2, 7), (3, 4), (3, 5), (3, 7), (4, 5), (4, 7), (5, 6),
             (5, 7), (6, 7)],
    }

    def test_coprime_pairs_known_values(self) :
        for n, pairs in self.known_values.items() :
            p = sorted(tuple(sorted(i)) for i in sequences.coprime_pairs(n))
            self.assertEqual(pairs, p)

if __name__ == '__main__':
    unittest.main()
