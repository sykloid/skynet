import unittest
from skynet.math import sequences

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

if __name__ == '__main__':
    unittest.main()
