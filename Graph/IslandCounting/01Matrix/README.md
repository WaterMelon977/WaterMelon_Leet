**LeetCode Link**
[https://leetcode.com/problems/01-matrix/](https://leetcode.com/problems/01-matrix/)

**Approach**

* Use **multi-source BFS** starting from all `0` cells.
* Initialize a queue with all positions where `mat[r][c] == 0`.
* Set all `1`s to a large value (unvisited distance).
* Perform BFS:

  * For each cell, update neighbors with `dist + 1` if smaller.
* Traverse in 4 directions.
* This ensures shortest distance to nearest `0`.

**Key Insight**
Start BFS from all `0`s simultaneously → guarantees shortest distance (like wave expansion).

**Why efficient**
Each cell is processed once → avoids repeated BFS from every `1`.

**Python Solution**

```python id="9c3r3n"
from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        queue = deque()
        
        # Initialize queue with all 0s, mark 1s as unvisited
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = float('inf')
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # Multi-source BFS
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Relaxation step
                    if mat[nr][nc] > mat[r][c] + 1:
                        mat[nr][nc] = mat[r][c] + 1
                        queue.append((nr, nc))
        
        return mat
```

**Explain any tricky part of the code**

* The **relaxation condition** ensures we only update when we find a shorter distance.

Edge-case handling: If all cells are `0`, BFS runs but no updates needed → matrix unchanged.

**Complexity**
Time: O(m * n) — each cell processed once
Space: O(m * n) — queue in worst case
