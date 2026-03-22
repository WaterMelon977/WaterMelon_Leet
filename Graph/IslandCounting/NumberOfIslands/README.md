**LeetCode Link**
[https://leetcode.com/problems/number-of-islands/](https://leetcode.com/problems/number-of-islands/)

**Approach**

* Treat the grid as a graph where each `'1'` is land and connected horizontally/vertically.
* Iterate through every cell:

  * When you find a `'1'`, it means a new island → increment count.
  * Run DFS/BFS from that cell to **mark entire island as visited** (convert `'1'` → `'0'`).
* Use 4-direction traversal to explore connected land.
* Continue until all cells are processed.

**Key Insight**
Each DFS/BFS call “sinks” one entire island, so counting DFS calls = number of islands.

**Why efficient**
Each cell is visited once and turned into water → no repeated work.

**Python Solution**

```python
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        def dfs(r, c):
            # Boundary + only process land
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] != '1':
                return
            
            # Mark as visited (sink island)
            grid[r][c] = '0'
            
            # Explore 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)
        
        return islands
```

**Explain any tricky part of the code**

* We **modify the grid in-place** (`'1' → '0'`) to avoid using a separate visited array.

Edge-case handling: Grid with all `'0'` → loop runs but DFS never triggers → returns 0.

**Complexity**
Time: O(m * n) — each cell visited once
Space: O(m * n) — recursion stack in worst case (full grid DFS)
