import unittest
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        lst = []
        self.helper(res, lst, s, 0)

        return res
    
    def helper(self, res, lst, s, start_idx):
        if len(lst) == 4:
            if start_idx == len(s):
                res.append(".".join(lst))
            return

        for i in range(1, 4):
            if start_idx + i > len(s):
                return                
            cur_str = s[start_idx:start_idx + i]
            # validate numbers for ip
            if cur_str.startswith("0") and len(cur_str) > 1:
                return
            if int(cur_str) > 255:
                return

            lst.append(cur_str)
            self.helper(res, lst, s, start_idx + i)
            lst.pop()

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    # Test cases will be added here
    def test_example_1(self):
        s = "25525511135"
        target = ["255.255.11.135","255.255.111.35"]
        self.assertEqual(self.solution.restoreIpAddresses(s), target)


if __name__ == '__main__':
    unittest.main()