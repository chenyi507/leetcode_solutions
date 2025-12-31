from typing import Optional, List
from collections import deque
import unittest

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        res = 0
        d = deque()        
        d.append(0)

        for i in range(1, len(height)):
            if height[i] < height[d[-1]]:
                d.append(i)
            elif height[i] == height[d[-1]]:
                d.pop()
                d.append(i)
            else:
                while len(d) > 0 and height[i] > height[d[-1]]:
                    idx = d.pop()
                    if len(d) > 0:
                        w = i - d[-1] - 1
                        h = min(height[i], height[d[-1]]) - height[idx]
                        res += + w * h 
                d.append(i)
        
        return res

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        target = 6
        self.assertEqual(self.solution.trap(height), target)

    def test_example_2(self):
        height = [4,2,0,3,2,5]
        target = 9
        self.assertEqual(self.solution.trap(height), target)

if __name__ == '__main__':
    unittest.main()