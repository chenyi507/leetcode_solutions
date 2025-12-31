from typing import Optional, List
import queue
import unittest

class Solution:
    def __init__(self):
        self.dx = [1, 0, -1, 0]
        self.dy = [0, -1, 0, 1]        

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):                
                if grid[i][j] == 0 or visited[i][j] == True:
                    continue
                area = self.calc_area(i, j, grid, visited)
                res = max(res, area)
        
        return res
        
    
    def calc_area(self, x, y, grid, visited):
        q = queue.Queue()
        q.put((x, y))
        visited[x][y] = True
        area = 0
        
        while q.qsize() > 0:
            cur_loc = q.get()
            cur_x, cur_y = cur_loc[0], cur_loc[1]            
            area += 1
            
            for i in range(4):
                neighbor_x, neighbor_y = cur_x + self.dx[i], cur_y + self.dy[i]
                neighbor_loc = (neighbor_x, neighbor_y)                
                if self.is_valid_island_cell(neighbor_x, neighbor_y, grid, visited):
                    q.put(neighbor_loc)  
                    visited[neighbor_x][neighbor_y] = True                              
        
        return area


    def is_valid_island_cell(self, x, y, grid, visited):
        if x < 0 or x >= len(grid):
            return False
        if y < 0 or y >= len(grid[0]):
            return False        
        if grid[x][y] != 1:
            return False
        if visited[x][y] == True:
            return False        
        
        return True

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
        target = 4   
        self.assertEqual(self.solution.maxAreaOfIsland(grid), target)

if __name__ == '__main__':
    unittest.main()