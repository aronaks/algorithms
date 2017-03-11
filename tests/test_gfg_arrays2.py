import unittest

from algorithms.gfg_arrays2 import find_leaders


class TesLinkedList(unittest.TestCase):

    def test_(self):
        arr = [16, 17, 4, 3, 5, 2]
        res = find_leaders(arr, len(arr))
        self.assertListEqual([2, 5, 17], res)
