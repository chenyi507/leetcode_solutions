import unittest
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 0 or k >= n:
            return []
        
        res = []
        lst = []

        self.helper(res, lst, n, k, 1)

        return res

    def helper(self, res: List[List[int]], lst: List[int], n: int, k: int, idx: int):
        if (len(lst) == k):
            res.append(lst[:])
            return
        
        for i in range(idx, n + 1):
            lst.append(i)
            self.helper(res, lst, n, k, i + 1)
            lst.pop()

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    # Test cases will be added here
    def test_example_1(self):
        n, k = 4, 2
        target = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
        self.assertEqual(self.solution.combine(4, 2), target)


if __name__ == '__main__':
    unittest.main()