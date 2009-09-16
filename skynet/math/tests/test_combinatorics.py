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

class NextPermutationTest(unittest.TestCase) :
    known_values = {
        (9, 1, 0) : (1, 0, 9),
        (0, 1, 2, 3) : (0, 1, 3, 2),
        (5, 7, 2, 1) : (7, 1, 2, 5),
        (1, 6, 5, 3, 2) : (2, 1, 3, 5, 6),
        (9, 1, 4, 8, 7, 2, 0) : (9, 1, 7, 0, 2, 4, 8),
    }

    def test_next_permutation(self) :
        for p, n in self.known_values.items() :
            self.assertEqual(n, tuple(combinatorics.next_permutation(p)))

class PartitionsTest(unittest.TestCase) :
    known_values = {
        0 : 1,
        1 : 1,
        2 : 2,
        3 : 3,
        4 : 5,
        5 : 7,
        6 : 11,
        7 : 15,
        8 : 22,
        9 : 30,
        10 : 42,
        20 : 627,
        50 : 204226,
        100 : 190569292,
        200 : 3972999029388,
    }

    def test_number_of_partitions(self) :
        for i, p in self.known_values.items() :
            self.assertEqual(p, combinatorics.number_of_partitions(i))

if __name__ == '__main__' :
    unittest.main()
