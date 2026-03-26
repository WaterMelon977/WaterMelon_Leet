**LeetCode Link**
[https://leetcode.com/problems/shortest-path-in-binary-matrix/](https://leetcode.com/problems/shortest-path-in-binary-matrix/)

**Approach**

* Use **BFS** to find shortest path in an unweighted grid.
* If start `(0,0)` or end `(n-1,n-1)` is blocked (`1`) → return `-1`.
* Use 8 directions (including diagonals).
* Push `(0,0)` into queue with distance `1`.
* Mark visited cells by setting them to `1` (avoid revisiting).
* For each step, explore all valid neighbors.
* Return distance when reaching `(n-1, n-1)`.

**Key Insight**
BFS guarantees shortest path in an unweighted grid, even with 8 directions.

**Why efficient**
Each cell is visited once → avoids redundant exploration.

**Python Solution**

```python id="3zq2h1"
from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # If start or end is blocked
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1
        
        # 8 directions
        directions = [
            (1,0), (-1,0), (0,1), (0,-1),
            (1,1), (1,-1), (-1,1), (-1,-1)
        ]
        
        queue = deque([(0, 0, 1)])  # (row, col, distance)
        grid[0][0] = 1  # mark visited
        
        while queue:
            r, c, dist = queue.popleft()
            
            # Reached destination
            if r == n - 1 and c == n - 1:
                return dist
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1  # mark visited
                    queue.append((nr, nc, dist + 1))
        
        return -1
```

**Explain any tricky part of the code**

* Using **8 directions** is crucial; missing diagonals gives wrong answer.

Edge-case handling: Single cell grid (`n=1`) → if it's `0`, return `1`.

**Complexity**
Time: O(n²) — each cell visited once
Space: O(n²) — queue in worst case
