import unittest
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        lst = []
        nums.sort()
        self.helper(res, lst, nums, 0)

        return res
    
    def helper(self, res: List[List[int]], lst: List[int], nums: List[int], idx: int):
        res.append(lst[:])

        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i - 1]:
                continue
            lst.append(nums[i])
            self.helper(res, lst, nums, i + 1)
            lst.pop()

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    # Test cases will be added here
    def test_example_1(self):
        nums = [1,2,2]
        target = [[],[1],[1,2],[1,2,2],[2],[2,2]]
        self.assertEqual(self.solution.subsets(nums), target)


if __name__ == '__main__':
    unittest.main()