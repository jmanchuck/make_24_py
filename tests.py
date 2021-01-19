import unittest
import math
from game import *


class TestAll(unittest.TestCase):

    def test_get_pair(self):
        arr = [1, 2, 3, 4]
        pair_list = set()
        for x, y, lst in get_pair_and_remaining(arr):
            tpl = (x, y, lst[0], lst[1])
            pair_list.add(tpl)

        self.assertEqual(len(pair_list), math.comb(len(arr), 2))

    def test_pair_operations(self):
        x, y = 2, 4
        answer = [2, 2, 8, 6]
        results = [z for z in all_operations(x, y)]

        self.assertEqual(results, answer)


if __name__ == "__main__":
    unittest.main()
