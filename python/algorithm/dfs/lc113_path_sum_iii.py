from typing import Optional, List
import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from algorithm.util.tree_node import TreeNode

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        path = []
        self.helper(res, path, root, targetSum)
        return res

    def helper(self, res: List[List[int]], path: List[int], root: Optional[TreeNode], targetSum: int):
        if root is None:
            return
        
        path.append(root.val)
        if root.left is None and root.right is None:
            if targetSum == root.val:                
                res.append(path[:])
            path.pop()
            return
        
        self.helper(res, path, root.left, targetSum - root.val)
        self.helper(res, path, root.right, targetSum - root.val)        
        path.pop()

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right = TreeNode(8)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.left = TreeNode(5)
        root.right.right.right = TreeNode(1)
        targetSum = 22
        target = [[5,4,11,2],[5,8,4,5]]
        self.assertEqual(self.solution.pathSum(root, targetSum), target)
    
if __name__ == '__main__':
    unittest.main()