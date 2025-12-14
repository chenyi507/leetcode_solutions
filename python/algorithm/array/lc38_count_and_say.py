import unittest
from typing import List

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        turn = 1
        last_word = "1"

        while turn < n:
            idx = 0
            cur_word = ""
            cur_count = 1
            while idx < len(last_word):
                if idx > 0:
                    if last_word[idx] == last_word[idx - 1]:
                        cur_count += 1                    
                    else:
                        cur_word += str(cur_count) + last_word[idx - 1]
                        cur_count = 1
                idx += 1
            cur_word += str(cur_count) + last_word[-1]
            last_word = cur_word
            turn += 1
        
        return last_word
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    # Test cases will be added here
    def test_example_1(self):
        n = 4
        target = "1211"
        self.assertEqual(self.solution.countAndSay(n), target)
    
    def test_example_2(self):
        n = 10
        target = "13211311123113112211"
        self.assertEqual(self.solution.countAndSay(n), target)

if __name__ == '__main__':
    unittest.main()