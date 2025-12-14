from typing import Optional, List
import queue
import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from algorithm.util.tree_node import TreeNode

class Solution:

    class ResultType:
        def __init__(self, depth: int, is_valid: bool):
            self.depth = depth
            self.is_valid = is_valid

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = self.helper(root)
        return result.is_valid
    
    def helper(self, root: Optional[TreeNode]) -> ResultType:
        if root is None:
            return self.ResultType(0, True)

        left_result = self.helper(root.left)
        right_result = self.helper(root.right)

        if not left_result.is_valid or not right_result.is_valid:
            return self.ResultType(-1, False) 

        if abs(left_result.depth - right_result.depth) > 1:
            return self.ResultType(-1, False)

        return self.ResultType(max(left_result.depth, right_result.depth) + 1, True)
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        target = True
        self.assertEqual(self.solution.isBalanced(root), target)
    
if __name__ == '__main__':
    unittest.main()