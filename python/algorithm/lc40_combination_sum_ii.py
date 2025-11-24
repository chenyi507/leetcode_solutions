import unittest
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
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
            if i > idx and candidates[i] == candidates[i - 1]:
                continue
            lst.append(candidates[i])
            self.helper(res, lst, candidates, target - candidates[i], i + 1)
            lst.pop()

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    # Test cases will be added here
    def test_example_1(self):
        nums = [10,1,2,7,6,1,5]
        sum = 8
        target = [[1,1,6],[1,2,5],[1,7],[2,6]]
        self.assertEqual(self.solution.combinationSum(nums, sum), target)


if __name__ == '__main__':
    unittest.main()