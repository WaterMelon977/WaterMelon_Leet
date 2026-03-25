"""
LeetCode #1254: Number of Closed Islands

https://leetcode.com/problems/number-of-closed-islands/
"""

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] == 1:
                return
            
            # Mark visited
            grid[r][c] = 1
            
            # Explore neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # Step 1: Remove border-connected islands
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)
        
        # Step 2: Count remaining closed islands
        closed_islands = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    closed_islands += 1
                    dfs(r, c)
        
        return closed_islands