from typing import List
import unittest

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        if intervals is None or len(intervals) == 0:
            return res
        intervals.sort(key = lambda x: x[0])        

        left_bound, right_bound = intervals[0][0], intervals[0][1]
        for i in range (1, len(intervals)):
            interval = intervals[i]

            if right_bound < interval[0]:
                res.append([left_bound, right_bound])
                left_bound, right_bound = interval[0], interval[1]
            else:
                right_bound = max(right_bound, interval[1])
                
            if i == len(intervals) - 1:
                res.append([left_bound, right_bound])

        return res

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    # Test cases will be added here
    def test_example_1(self):
        intervals = [[4,7],[1,4]]
        target = [[1,7]]
        self.assertEqual(self.solution.merge(intervals), target)

if __name__ == '__main__':
    unittest.main()