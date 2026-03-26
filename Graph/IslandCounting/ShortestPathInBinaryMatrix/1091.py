"""
LeetCode #1091: Shortest Path in Binary Matrix

https://leetcode.com/problems/shortest-path-in-binary-matrix/
"""

from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # If start or end is blocked
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1
        
        # 8 directions
        directions = [
            (1,0), (-1,0), (0,1), (0,-1),
            (1,1), (1,-1), (-1,1), (-1,-1)
        ]
        
        queue = deque([(0, 0, 1)])  # (row, col, distance)
        grid[0][0] = 1  # mark visited
        
        while queue:
            r, c, dist = queue.popleft()
            
            # Reached destination
            if r == n - 1 and c == n - 1:
                return dist
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1  # mark visited
                    queue.append((nr, nc, dist + 1))
        
        return -1