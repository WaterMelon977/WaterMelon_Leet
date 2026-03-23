"""
LeetCode #695: Max Area of Island

https://leetcode.com/problems/max-area-of-island/
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        max_island = 0

        # We use a list to make it mutable across recursive calls
        current_island_size = [0] 

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return
            
            # Found land! Mark it as visited (0) so we don't count it twice
            grid[i][j] = 0
            # Increment the shared counter
            current_island_size[0] += 1
            
            # Explore all neighbors
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    current_island_size[0] = 0 # Reset for the new island
                    dfs(i, j)
                    # After DFS finishes exploring the whole island:
                    max_island = max(max_island, current_island_size[0])

        return max_island


        