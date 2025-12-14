import unittest
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        lst = []
        
        self.helper(res, lst, k, n, 1)

        return res

    def helper(self, res: List[List[int]], lst: List[int], k: int, n: int, idx: int):
        if len(lst) == k:
            if n == 0:
                res.append(lst[:])
            return

        if n < 0:
            return

        for i in range(idx, 10):
            if i > 9 - (k - len(lst)) + 1:
                return
            lst.append(i)
            self.helper(res, lst, k, n - i, i + 1)
            lst.pop()

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        k = 3
        n = 9
        target = [[1,2,6],[1,3,5],[2,3,4]]
        self.assertEqual(self.solution.combinationSum3(k, n), target)


if __name__ == '__main__':
    unittest.main()