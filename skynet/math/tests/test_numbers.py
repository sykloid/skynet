import unittest
from skynet.math import numbers
from random import randint
from operator import mul
from functools import reduce

class FactorialTest(unittest.TestCase) :
    known_values = {
        0 : 1,
        1 : 1,
        2 : 2,
        3 : 6,
        5 : 120,
        8 : 40320,
        13 : 6227020800,
    }

    wrong_values = [-1, -2, -3, -5, -8]

    def test_recursive_factorial_known_values(self) :
        for n, factorial in self.known_values.items() :
            self.assertEqual(factorial, numbers.recursive_factorial(n))

    def test_iterative_factorial_known_values(self) :
        for n, factorial in self.known_values.items() :
            self.assertEqual(factorial, numbers.iterative_factorial(n))

    def test_builtin_factorial_known_values(self) :
        for n, factorial in self.known_values.items() :
            self.assertEqual(factorial, numbers.builtin_factorial(n))

    def test_recursive_factorial_wrong_values(self) :
        for n in self.wrong_values :
            self.assertRaises(ValueError, numbers.recursive_factorial, n)

    def test_iterative_factorial_wrong_values(self) :
        for n in self.wrong_values :
            self.assertRaises(ValueError, numbers.iterative_factorial, n)

    def test_builtin_factorial_wrong_values(self) :
        for n in self.wrong_values :
            self.assertRaises(ValueError, numbers.builtin_factorial, n)

class GCDTest(unittest.TestCase) :
    known_values = {
        (2, 3) : 1,
        (8, 20) : 4,
        (5, 2) : 1,
        (42, 91) : 7,
        (5, 0) : 5,
        (2, 1) : 1,
        (64, 16) : 16,
        (97, 33) : 1,
        (91, 78) : 13,
        (10**10, 2**12) : 2**10,
    }

    known_chains = dict(known_values)

    known_chains.update({
        (2, 4, 6, 8) : 2,
        (1, 2, 5, 10) : 1,
        (100, 200, 225, 500) : 25,
        (21, 56, 42, 91) : 7,
        (8, 128, 1000) : 8,
    })

    def test_recursive_gcd(self) :
        for (m, n), g in self.known_values.items() :
            self.assertEqual(g, numbers.recursive_gcd(m, n))
            self.assertEqual(g, numbers.recursive_gcd(n, m))

    def test_iterative_gcd(self) :
        for (m, n), g in self.known_values.items() :
            self.assertEqual(g, numbers.iterative_gcd(m, n))
            self.assertEqual(g, numbers.iterative_gcd(n, m))

    def test_chained_gcd(self) :
        for chain, g in self.known_chains.items() :
            self.assertEqual(g, numbers.chained_gcd(*chain))

class LCMTest(unittest.TestCase) :
    known_values = {
        (2, 3) : 6,
        (8, 20) : 40,
        (5, 2) : 10,
        (5, 0) : 0,
        (2, 1) : 2,
        (64, 16) : 64,
        (97, 33) : 3201,
        (91, 78) : 546,
        (10**10, 2**12) : 4*10**10,
        (2, 4, 6, 8) : 24,
        (1, 2, 5, 10) : 10,
        (100, 200, 225, 500) : 9000,
        (21, 56, 42, 91) : 2184,
        (8, 128, 1000) : 16000,
    }

    def test_chained_lcm(self) :
        for chain, lcm in self.known_values.items() :
            self.assertEqual(lcm, numbers.chained_lcm(*chain))

class XGCDTest(unittest.TestCase) :
    known_values = {
        (2, 3) : 1,
        (8, 20) : 4,
        (5, 2) : 1,
        (42, 91) : 7,
        (75, 275) : 25,
        (5, 0) : 5,
        (2, 1) : 1,
        (64, 16) : 16,
        (97, 33) : 1,
        (91, 78) : 13,
        (10**10, 2**12) : 2**10,
    }

    def test_iterative_xgcd(self) :
        for (m, n), g in self.known_values.items() :
            x, y, h = numbers.iterative_xgcd(m, n)
            self.assertEqual(g, h)
            self.assertEqual(x*m + y*n, h)

    def test_recursive_xgcd(self) :
        for (m, n), g in self.known_values.items() :
            x, y, h = numbers.recursive_xgcd(m, n)
            self.assertEqual(g, h)
            self.assertEqual(x*m + y*n, h)

class PrimalityTest(unittest.TestCase) :
    known_values = [2, 3, 127, 953, 881, 743, 409, 311, 317, 43]
    wrong_values = [1, 703, 608, 705, 764, 837, 949, 210, 336, 81]

    pseudoprimes = [561, 1105, 1729]

    def test_is_prime_vanilla_known_values(self) :
        for p in self.known_values :
            self.assertTrue(numbers.is_prime_vanilla(p))

    def test_is_prime_vanilla_wrong_values(self) :
        for q in self.wrong_values :
            self.assertFalse(numbers.is_prime_vanilla(q))

    def test_is_prime_6k1_known_values(self) :
        for p in self.known_values :
            self.assertTrue(numbers.is_prime_6k1(p))

    def test_is_prime_6k1_wrong_values(self) :
        for q in self.wrong_values :
            self.assertFalse(numbers.is_prime_6k1(q))

    def test_is_prime_regex_known_values(self) :
        for p in self.known_values :
            self.assertTrue(numbers.is_prime_regex(p))

    def test_is_prime_regex_wrong_values(self) :
        for q in self.wrong_values :
            self.assertFalse(numbers.is_prime_regex(q))

    def test_is_prime_fermat_pseudoprime_known_values(self) :
        for p in self.known_values :
            self.assertTrue(numbers.is_prime_fermat_pseudoprime(p))

    def test_is_prime_fermat_pseudoprime_wrong_values(self) :
        for q in self.wrong_values :
            self.assertFalse(numbers.is_prime_fermat_pseudoprime(q))

    def test_is_prime_fermat_pseudoprime_pseudoprimes(self) :
        for q in self.pseudoprimes :
            self.assertTrue(numbers.is_prime_fermat_pseudoprime(q))

    def test_is_prime_miller_rabin_known_values(self) :
        for p in self.known_values :
            self.assertTrue(numbers.is_prime_miller_rabin(p))

    def test_is_prime_miller_rabin_wrong_values(self) :
        for q in self.wrong_values :
            self.assertFalse(numbers.is_prime_miller_rabin(q))

    def test_is_prime(self) :
        for p in self.known_values :
            self.assertTrue(numbers.is_prime(p))

    def test_is_prime(self) :
        for q in self.wrong_values :
            self.assertFalse(numbers.is_prime(q))

class DigitsTest(unittest.TestCase) :
    known_values = [
        0,
        1,
        9,
        21,
        78,
        233,
        571,
        2347984,
        22938479238472,
        2**32,
    ]

    def test_digits_known_values(self) :
        for n in self.known_values :
            self.assertEqual(
                n,
                sum(
                    i*10**index
                    for index, i in enumerate(reversed(tuple(numbers.digits(n))))
                )
            )

class PalindromeTest(unittest.TestCase) :
    known_values = [
        1,
        9,
        11,
        99,
        121,
        919,
        1310131,
        12345654321,
        9878789,
        11011,
    ]

    wrong_values = [
        17,
        21,
        911,
        131071,
        225,
        567,
        436759384,
        102944,
        85492,
        2034
    ]

    def test_palindrome_known_values(self) :
        for p in self.known_values :
            self.assertTrue(numbers.is_palindrome(p))

    def test_palindrome_wrong_values(self) :
        for n in self.wrong_values :
            self.assertFalse(numbers.is_palindrome(n))

class FactorizationTest(unittest.TestCase) :
    known_values = [1, 2] + [randint(3, 2**5) for i in range(18)]

    def test_prime_factors_trial_division(self) :
        for n in self.known_values :
            self.assertEqual(
                n,
                reduce(mul, (p**e for p, e in
                             numbers.prime_factors_trial_division(n)), 1)
            )

class DivisorsTest(unittest.TestCase) :
    known_values = {
        1 : [1],
        2 : [1, 2],
        10 : [1, 2, 5, 10],
        45 : [1, 3, 5, 9, 15, 45],
        200 : [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 200],
        900 : [1, 2, 3, 4, 5, 6, 9, 10, 12, 15, 18, 20, 25, 30, 36, 45, 50, 60,
               75, 90, 100, 150, 180, 225, 300, 450, 900],
        1001 : [1, 7, 11, 13, 77, 91, 143, 1001],
        9996 : [1, 2, 3, 4, 6, 7, 12, 14, 17, 21, 28, 34, 42, 49, 51, 68, 84,
                98, 102, 119, 147, 196, 204, 238, 294, 357, 476, 588, 714, 833,
                1428, 1666, 2499, 3332, 4998, 9996],
        65536 : [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192,
                 16384, 32768, 65536],
        131073 : [1, 3, 43691, 131073],
    }

    def test_divisors_cartesian_product(self) :
        for n, d in self.known_values.items() :
            self.assertEqual(d, sorted(list(numbers.divisors_cartesian_product(n))))

class PhiTest(unittest.TestCase) :
    known_values = {
        1 : 0,
        2 : 1,
        5 : 4,
        9 : 6,
        27 : 18,
        336 : 96,
        1000 : 400,
        2520 : 576,
        27182 : 13590,
        131071 : 131070,
    }

    def test_phi(self) :
        for n, phi in self.known_values.items() :
            self.assertEqual(phi, numbers.phi(n))

class SigmaTest(unittest.TestCase) :
    known_values = [
        1,
        2,
        5,
        9,
        27,
        336,
        1000,
        2520,
        27182,
        131071,
    ]

    power_bound = 10

    def test_sigma(self) :
        for n in self.known_values :
            for k in range(1, self.power_bound) :
                self.assertEqual(
                    sum(i ** k for i in numbers.divisors(n)),
                    numbers.sigma(n, k)
                )

class TauTest(unittest.TestCase) :
    known_values = [
        1,
        2,
        5,
        9,
        27,
        336,
        1000,
        2520,
        27182,
        131071,
    ]

    def test_tau(self) :
        for n in self.known_values :
            self.assertEqual(len(list(numbers.divisors(n))), numbers.tau(n))

if __name__ == '__main__' :
    unittest.main()
