import unittest
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        lst = []
        used_lst = [False for i in range(len(nums))]

        self.helper(nums, res, lst, used_lst)\

        return res

    def helper(self, nums: List[int], res: List[List[int]], lst: List[int], used_lst: List[bool]):
        if len(lst) == len(nums):
            res.append(lst[:])
            return

        for i in range(len(nums)):
            if (i > 0 and nums[i] == nums[i - 1] and used_lst[i - 1] == False) or (used_lst[i] == True):
                continue
            used_lst[i] = True
            lst.append(nums[i])
            self.helper(nums, res, lst, used_lst)
            lst.pop()
            used_lst[i] = False

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    # Test cases will be added here
    def test_example_1(self):
        nums = [1,1,2]
        target = [[1,1,2],[1,2,1],[2,1,1]]
        self.assertEqual(self.solution.permuteUnique(nums), target)


if __name__ == '__main__':
    unittest.main()