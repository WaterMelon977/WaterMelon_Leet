**LeetCode Link**
[https://leetcode.com/problems/surrounded-regions/](https://leetcode.com/problems/surrounded-regions/)

**Approach**

* Key idea: Only capture regions **not connected to border**.
* Traverse all border cells; whenever you see `'O'`, run DFS/BFS and mark all connected `'O'` as **safe** (e.g., mark as `'T'`).
* After marking, iterate the entire board:

  * Convert remaining `'O'` → `'X'` (these are surrounded).
  * Convert temporary `'T'` → `'O'` (restore safe ones).
* Use 4-direction traversal (up, down, left, right).
* This avoids checking each region individually → single pass marking strategy.

**Key Insight**
Any `'O'` connected to the boundary can **never be surrounded**, so we protect them first.

**Why efficient**
Instead of checking every region separately, we eliminate invalid candidates in one traversal → linear scan.

**Python Solution**

```python
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c):
            # Boundary + only process 'O'
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if board[r][c] != 'O':
                return
            
            # Mark as safe
            board[r][c] = 'T'
            
            # Explore neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # Step 1: Mark all border-connected 'O's
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)
        
        # Step 2: Flip surrounded + restore safe
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'   # surrounded
                elif board[r][c] == 'T':
                    board[r][c] = 'O'   # restore safe
```

**Explain any tricky part of the code**

* Instead of trying to detect surrounded regions directly, we **reverse the thinking**:
  mark *non-surrounded* first (border-connected), then flip the rest.

Edge-case handling: Small boards (like 1 row/col) → all cells are border, so nothing gets flipped.

**Complexity**
Time: O(m * n) — each cell processed at most once
Space: O(m * n) — recursion stack in worst case (DFS)
