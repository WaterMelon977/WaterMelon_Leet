"""
LeetCode #1020: Number of Enclaves

https://leetcode.com/problems/number-of-enclaves/
"""

from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] == 0:
                return
            
            # Remove land
            grid[r][c] = 0
            
            # Explore neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # Step 1: Remove border-connected land
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)
        
        # Step 2: Count remaining land
        enclave_count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    enclave_count += 1
        
        return enclave_count