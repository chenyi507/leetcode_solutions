from typing import Optional, List
from collections import deque
import unittest

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        d = deque()
        d.append(0)
        res = [0 for i in range(len(temperatures))]

        for i in range(1, len(temperatures)):
            if temperatures[i] <= temperatures[d[-1]]:
                d.append(i)
            else:
                while len(d) > 0 and temperatures[i] > temperatures[d[-1]]:
                    idx = d.pop()
                    res[idx] = i - idx
        
        return res

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        temperatures = [73,74,75,71,69,72,76,73]
        target = [1,1,4,2,1,1,0,0]
        self.assertEqual(self.solution.dailyTemperatures(temperatures), target)

    def test_example_2(self):
        temperatures = [30,40,50,60]
        target = [1,1,1,0]
        self.assertEqual(self.solution.dailyTemperatures(temperatures), target)
    
    def test_example_3(self):
        temperatures = [30,60,90]
        target = [1,1,0]
        self.assertEqual(self.solution.dailyTemperatures(temperatures), target)

if __name__ == '__main__':
    unittest.main()