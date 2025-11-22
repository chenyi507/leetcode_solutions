from typing import Optional, List
import unittest
from .util.tree_node import TreeNode

import queue

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


if __name__ == '__main__':
    unittest.main()