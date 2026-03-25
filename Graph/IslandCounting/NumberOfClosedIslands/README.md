**LeetCode Link**
[https://leetcode.com/problems/number-of-closed-islands/](https://leetcode.com/problems/number-of-closed-islands/)

**Approach**

* A closed island is a group of `0`s **not touching the border**.
* First, eliminate all islands connected to the border:

  * Traverse boundary cells; for every `0`, run DFS and mark all connected `0`s as visited (convert to `1`).
* Now, iterate through the grid:

  * For every remaining `0`, it's a **closed island** → increment count.
  * Run DFS to mark the entire island as visited.
* Use 4-direction traversal.

**Key Insight**
Remove all border-connected land first; remaining islands are guaranteed closed.

**Why efficient**
Each cell is visited at most once → avoids repeated checks.

**Python Solution**

```python id="7m0p5g"
from typing import List

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
```

**Explain any tricky part of the code**

* Instead of checking if an island is closed during DFS, we **pre-remove invalid ones (border-connected)** to simplify logic.

Edge-case handling: If all land touches border → everything removed → result is 0.

**Complexity**
Time: O(m * n) — each cell visited once
Space: O(m * n) — recursion stack in worst case
