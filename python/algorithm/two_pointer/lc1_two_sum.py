import unittest

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i, num in enumerate(nums):
            if target - num in dict:
                return [dict[target - num], i]            
            dict[num] = i

        return []

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [2,7,11,15]
        target = 9
        self.assertEqual(self.solution.twoSum(nums, target), [0,1])
    
if __name__ == '__main__':
    unittest.main()