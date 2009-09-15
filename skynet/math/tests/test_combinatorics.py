import unittest
from skynet.math import combinatorics

class EnumerationTest(unittest.TestCase) :
    known_combinations = {
        (0, 0) : 1,
        (2, 0) : 1,
        (5, 5) : 1,
        (6, 3) : 20,
        (8, 2) : 28,
        (9, 5) : 126,
        (11, 5) : 462,
        (23, 4) : 8855,
        (36, 21) : 5567902560,
        (79, 42) : 46261812817306682205610,
    }

    known_permutations = {
        (0, 0) : 1,
        (1, 0) : 1,
        (5, 5) : 120,
        (8, 3) : 336,
        (13, 2) : 156,
        (15, 7) : 32432400,
        (16, 4) : 43680,
        (12, 10) : 239500800,
        (11, 9) : 19958400,
        (10, 7) : 604800,
    }


    def test_combinations(self) :
        for (n, r), c in self.known_combinations.items() :
            self.assertEqual(c, combinatorics.C(n, r))

    def test_permutations(self) :
        for (n, r), c in self.known_permutations.items() :
            self.assertEqual(c, combinatorics.P(n, r))

if __name__ == '__main__' :
    unittest.main()
