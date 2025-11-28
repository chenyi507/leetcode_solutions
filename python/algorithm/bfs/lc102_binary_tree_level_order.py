from typing import Optional, List
import queue
import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from algorithm.util.tree_node import TreeNode

class Solution:    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return res
        
        q = queue.Queue()
        q.put(root)

        while q.qsize() > 0:
            level = []
            for i in range(q.qsize()):
                cur_node = q.get()
                level.append(cur_node.val)
                if not cur_node.left is None:
                    q.put(cur_node.left)
                if not cur_node.right is None:
                    q.put(cur_node.right)
            res.append(level)
        
        return res
        

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)

        target = [[3],[9,20]]        
        self.assertEqual(self.solution.levelOrder(root), target)

if __name__ == '__main__':
    unittest.main()