"""
LeetCode #1905: Count Sub Islands

https://leetcode.com/problems/count-sub-islands/
"""

from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid2), len(grid2[0])
        
        def dfs(r, c):
            # Boundary + water
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return True
            if grid2[r][c] == 0:
                return True
            
            # Mark visited
            grid2[r][c] = 0
            
            # Check current cell validity
            is_sub = (grid1[r][c] == 1)
            
            # Explore neighbors
            is_sub &= dfs(r + 1, c)
            is_sub &= dfs(r - 1, c)
            is_sub &= dfs(r, c + 1)
            is_sub &= dfs(r, c - 1)
            
            return is_sub
        
        count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1:
                    if dfs(r, c):
                        count += 1
        
        return count