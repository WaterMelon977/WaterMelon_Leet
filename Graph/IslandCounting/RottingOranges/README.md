**LeetCode Link**
[https://leetcode.com/problems/rotting-oranges/](https://leetcode.com/problems/rotting-oranges/)

**Approach**

* Use **multi-source BFS** starting from all initially rotten oranges (`2`).
* Count total fresh oranges (`1`).
* Push all rotten cells into a queue with time `0`.
* Perform BFS level by level:

  * For each rotten orange, infect adjacent fresh ones.
  * Decrease fresh count and push them with `time + 1`.
* Track the maximum time taken.
* If fresh oranges remain at the end → return `-1`.

**Key Insight**
Rot spreads in waves → BFS naturally models minimum time (shortest distance in grid).

**Why efficient**
Each cell is processed once → no repeated infection attempts.

**Python Solution**

```python id="qg3n9f"
from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        
        # Initialize queue and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, time)
                elif grid[r][c] == 1:
                    fresh += 1
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        time = 0
        
        # BFS
        while queue:
            r, c, t = queue.popleft()
            time = max(time, t)
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # make rotten
                    fresh -= 1
                    queue.append((nr, nc, t + 1))
        
        return time if fresh == 0 else -1
```

**Explain any tricky part of the code**

* We store `time` in the queue to track how long it takes for each orange to rot.

Edge-case handling: If no fresh oranges initially → return 0 immediately (handled naturally since `fresh == 0`).

**Complexity**
Time: O(m * n) — each cell processed once
Space: O(m * n) — queue in worst case
