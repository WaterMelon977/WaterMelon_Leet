**LeetCode Link**
[https://leetcode.com/problems/detonate-the-maximum-bombs/](https://leetcode.com/problems/detonate-the-maximum-bombs/)

**Approach**

* Model bombs as a directed graph:

  * Edge `i → j` exists if bomb `i` can detonate bomb `j`.
* For each pair `(i, j)`:

  * Check if distance between centers ≤ radius of `i`.
  * Use squared distance to avoid sqrt.
* Build adjacency list for the graph.
* For each bomb, run DFS/BFS to count how many bombs can be detonated.
* Track the maximum count across all starting bombs.

**Key Insight**
This reduces to finding the **maximum reachable nodes** in a directed graph starting from each node.

**Why efficient**
Graph construction is O(n²), and DFS from each node is O(n + e), which is acceptable for constraints.

**Python Solution**

```python
from typing import List

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        
        # Build graph
        graph = [[] for _ in range(n)]
        
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, _ = bombs[j]
                
                # Check if j is within i's radius
                if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r1 ** 2:
                    graph[i].append(j)
        
        def dfs(node, visited):
            visited.add(node)
            count = 1
            
            for nei in graph[node]:
                if nei not in visited:
                    count += dfs(nei, visited)
            
            return count
        
        max_bombs = 0
        
        for i in range(n):
            visited = set()
            max_bombs = max(max_bombs, dfs(i, visited))
        
        return max_bombs
```

**Explain any tricky part of the code**

* Use squared distance comparison to avoid floating-point errors:
  `(x1 - x2)^2 + (y1 - y2)^2 <= r^2`

Edge-case handling: Bombs with no neighbors → DFS returns 1 (itself only).

**Complexity**
Time: O(n² + n*(n + e)) ≈ O(n³) worst case, but acceptable for constraints
Space: O(n²) — adjacency list in worst case
