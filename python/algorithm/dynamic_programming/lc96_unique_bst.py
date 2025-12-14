import unittest

class Solution:
    def numTrees(self, n: int) -> int:
        uniq_num = [1] * (n + 1)

        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                total += uniq_num[root - 1] * uniq_num[nodes - root]
            uniq_num[nodes] = total
        
        return uniq_num[-1]
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        n = 5
        target = 42
        self.assertEqual(self.solution.numTrees(n), target)

if __name__ == '__main__':
    unittest.main()