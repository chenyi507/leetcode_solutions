import unittest
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        lst = []

        self.helper(res, lst, candidates, target, 0)
        
        return res
    
    def helper(self, res: List[List[int]], lst: List[int], candidates: List[int], target: int, idx: int):
        if target == 0:
            res.append(lst[:])
            return

        if target < 0:
            return

        for i in range(idx, len(candidates)):
            lst.append(candidates[i])
            self.helper(res, lst, candidates, target - candidates[i], i)
            lst.pop()

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    # Test cases will be added here
    def test_example_1(self):
        nums = [2,3,6,7]
        sum = 7
        target = [[2,2,3],[7]]
        self.assertEqual(self.solution.combinationSum(nums, sum), target)


if __name__ == '__main__':
    unittest.main()