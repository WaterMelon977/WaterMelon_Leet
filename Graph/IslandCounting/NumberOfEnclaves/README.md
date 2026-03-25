**LeetCode Link**
[https://leetcode.com/problems/number-of-enclaves/](https://leetcode.com/problems/number-of-enclaves/)

**Approach**

* Enclaves are land cells (`1`) **not connected to the boundary**.
* First, eliminate all land connected to borders:

  * Traverse boundary cells; for every `1`, run DFS and mark connected land as `0`.
* After removal, remaining `1`s are enclaves.
* Count all remaining `1`s in the grid.
* Use 4-direction traversal.

**Key Insight**
Same pattern as “closed islands”: remove border-connected land → what remains cannot reach boundary.

**Why efficient**
Each cell is visited at most once → no redundant DFS calls.

**Python Solution**

```python id="qg0jka"
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
```

**Explain any tricky part of the code**

* We don’t check “can reach boundary” explicitly; we **delete all such land first**, then just count leftovers.

Edge-case handling: If all land touches boundary → everything removed → result is 0.

**Complexity**
Time: O(m * n) — each cell processed once
Space: O(m * n) — recursion stack in worst case
