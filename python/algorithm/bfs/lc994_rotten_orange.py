from typing import Optional, List
import queue
import unittest

class Solution:
    def __init__(self):
        self.dx = [1, 0, -1, 0]
        self.dy = [0, 1, 0, -1]


    def orangesRotting(self, grid: List[List[int]]) -> int:
        day = 0
        rotten_cnt, total_cnt = 0, 0
        w, h = len(grid[0]), len(grid)        
        q = queue.Queue()
        visited = [[False for j in range(w)] for i in range(h)]
        for j in range(h):
            for i in range(w):
                if grid[j][i] != 0:
                    total_cnt += 1
                if grid[j][i] == 2:
                    visited[j][i] = True
                    rotten_cnt += 1
                    q.put((j, i))
                           
        while q.qsize() > 0:
            size = q.qsize()
            for i in range(size):
                cur_cell = q.get()
                for k in range(4):
                    x, y = cur_cell[0] + self.dx[k], cur_cell[1] + self.dy[k]
                    if not self.is_cell_valid(x, y, w, h):
                        continue
                    if grid[x][y] != 1 or visited[x][y]:
                        continue
                    visited[x][y] = True
                    grid[x][y] = 2
                    rotten_cnt += 1
                    q.put((x, y))
            if q.qsize() > 0:
                day += 1
        
        return day if rotten_cnt == total_cnt else -1


    def is_cell_valid(self, x, y, w, h):
        if x < 0 or x >= h:
            return False
        if y < 0 or y >= w:
            return False                

        return True

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        grid = [[1,2]]
        target = 1   
        self.assertEqual(self.solution.orangesRotting(grid), target)

if __name__ == '__main__':
    unittest.main()