**LeetCode Link**
[https://leetcode.com/problems/max-area-of-island/](https://leetcode.com/problems/max-area-of-island/)

**Approach**

* Traverse the grid; whenever you find a `'1'`, start DFS to compute that island’s area.
* During DFS, count current cell and explore 4 directions.
* Mark visited cells by converting `'1' → '0'` to avoid revisiting.
* Track the maximum area across all DFS runs.
* Return the largest area found.

**Key Insight**
Each DFS computes the size of one connected component; take the maximum.

**Why efficient**
Each cell is visited once and “sunk” → no repeated work.

**Python Solution**

```python id="l1r8bq"
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            # Boundary + only process land
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if grid[r][c] == 0:
                return 0
            
            # Mark visited
            grid[r][c] = 0
            
            # Count this cell + neighbors
            area = 1
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)
            
            return area
        
        max_area = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area
```


```python

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(r, c):
            # 1. Base Case: Out of bounds or water (0)
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            
            # 2. Mark as visited by sinking the island (turning 1 to 0)
            grid[r][c] = 0
            
            # 3. Sum up the current cell (1) + all 4 neighbors
            return (1 + dfs(r + 1, c) + 
                        dfs(r - 1, c) + 
                        dfs(r, c + 1) + 
                        dfs(r, c - 1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Update the global maximum with the area of the found island
                    max_area = max(max_area, dfs(r, c))

        return max_area
```

**Explain any tricky part of the code**

* DFS returns the area of the island, so we accumulate using `1 + neighbors`.

Edge-case handling: No land (`all 0s`) → DFS never runs → max_area stays 0.

**Complexity**
Time: O(m * n) — each cell visited once
Space: O(m * n) — recursion stack in worst case


-----------------


