**LeetCode Link**
[https://leetcode.com/problems/pacific-atlantic-water-flow/](https://leetcode.com/problems/pacific-atlantic-water-flow/)

**Approach**

* Instead of flowing from each cell → oceans (costly), **reverse the thinking**:

  * Start DFS/BFS from oceans and move inward.
* Maintain two visited sets:

  * `pacific_reachable` (top row + left column)
  * `atlantic_reachable` (bottom row + right column)
* From ocean borders, traverse to neighbors **only if height increases or stays same** (`next >= current`).
* After both traversals, collect cells present in **both sets**.
* Use DFS or BFS (both valid).

**Key Insight**
Water flows downhill, so reverse flow: from ocean → climb to all cells that *can reach* that ocean.

**Why efficient**
Each cell is visited at most twice (once per ocean) → avoids repeated DFS from every cell.

**Python Solution**

```python id="jztnpt"
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        rows, cols = len(heights), len(heights[0])
        
        pacific = set()
        atlantic = set()
        
        def dfs(r, c, visited):
            visited.add((r, c))
            
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                
                if (0 <= nr < rows and 0 <= nc < cols and 
                    (nr, nc) not in visited and 
                    heights[nr][nc] >= heights[r][c]):
                    
                    dfs(nr, nc, visited)
        
        # Pacific (top row + left column)
        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)
        
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols - 1, atlantic)
        
        # Intersection of both reachable sets
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])
        
        return result
```

**Explain any tricky part of the code**

* The condition `heights[nr][nc] >= heights[r][c]` ensures reverse flow:
  we only climb to cells from which water could flow down to the ocean.

Edge-case handling: Single cell grid → it touches both oceans → included in result.

**Complexity**
Time: O(m * n) — each cell visited twice (2 DFS)
Space: O(m * n) — visited sets + recursion stack
