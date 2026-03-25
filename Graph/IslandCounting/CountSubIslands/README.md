**LeetCode Link**
[https://leetcode.com/problems/count-sub-islands/](https://leetcode.com/problems/count-sub-islands/)

**Approach**

* Traverse `grid2`; whenever you find a `1`, start DFS to explore that island.
* During DFS, check if **all corresponding cells in `grid1` are also `1`**.
* Maintain a flag `is_sub_island = True`.
* For each cell in the DFS:

  * If `grid1[r][c] == 0`, mark `is_sub_island = False`.
* Continue DFS to fully explore the island in `grid2` (important even if invalid).
* After DFS, if `is_sub_island` is still `True`, increment count.

**Key Insight**
An island in `grid2` is valid only if **every cell overlaps land in `grid1`**.

**Why efficient**
Each cell in `grid2` is visited once → no redundant work.

**Python Solution**

```python
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
```

**Explain any tricky part of the code**

* DFS **must continue even if one cell fails**, because we need to mark the entire island visited.
* Using `is_sub &= dfs(...)` ensures all parts must be valid.

Edge-case handling: Even if one cell mismatches (`grid1 = 0`), we still fully DFS to avoid revisiting that island again.

**Complexity**
Time: O(m * n) — each cell visited once
Space: O(m * n) — recursion stack in worst case
