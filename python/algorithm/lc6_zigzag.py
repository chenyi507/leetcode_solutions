import unittest

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        char_list = [[] for _ in range(numRows)]
        cur_row = 0
        going_down = True
        for c in s:
            char_list[cur_row].append(c)
            if cur_row == 0:
                going_down = True
            elif cur_row == numRows - 1:
                going_down = False
            
            cur_row += 1 if going_down else -1
        
        return ''.join([''.join(row) for row in char_list])

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    # Test cases will be added here
    def test_example_1(self):
        s = "PAYPALISHIRING"
        numRows = 3
        target = "PAHNAPLSIIGYIR"
        self.assertEqual(self.solution.convert(s, numRows), target)

    def test_example_2(self):
        s = "AB"
        numRows = 1
        target = "AB"
        self.assertEqual(self.solution.convert(s, numRows), target)

if __name__ == '__main__':
    unittest.main()