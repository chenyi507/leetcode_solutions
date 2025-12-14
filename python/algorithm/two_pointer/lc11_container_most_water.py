import unittest
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_height, r_height = height[0], height[-1]
        res = 0

        while l < r:            
            while l < r and height[l] < l_height:
                l += 1
            l_height = height[l]
            while l < r and height[r] < r_height:
                r -= 1
            r_height = height[r]
            
            res = max(res, (r - l) * min(height[r], height[l]))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return res
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        height = [1,8,6,2,5,4,8,3,7]
        target = 49
        self.assertEqual(self.solution.maxArea(height), target)

    def test_example_2(self):
        height = [1,1000,1000,6,2,5,4,8,3,7]
        target = 1000
        self.assertEqual(self.solution.maxArea(height), target)
    
if __name__ == '__main__':
    unittest.main()