import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        if s is None or len(s) == 0:
            return res

        sliding = {}
        left = 0

        for right, c in enumerate(s):
            if c in sliding and sliding[c] >= left:                
                left = sliding[c] + 1
            res = max(res, right - left + 1)
            sliding[c] = right 

        return res

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        s = "pwwkew"
        target = 3        
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), target)
    
    def test_example_2(self):
        s = "bbbbbb"
        target = 1
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), target)
    
    def test_example_2(self):
        s = "dvdf"
        target = 3
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), target)

if __name__ == '__main__':
    unittest.main()        