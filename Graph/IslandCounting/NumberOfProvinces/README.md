**LeetCode Link**
[https://leetcode.com/problems/number-of-provinces/](https://leetcode.com/problems/number-of-provinces/)

**Approach**

* Treat the adjacency matrix as a graph of `n` nodes (cities).
* Use a `visited` array to track explored cities.
* Iterate through each city:

  * If not visited → it’s a new province → increment count.
  * Run DFS/BFS to mark all directly/indirectly connected cities.
* In DFS, check all neighbors `j` where `isConnected[i][j] == 1`.
* Continue until all cities are visited.

**Key Insight**
Each connected component in the graph = one province.

**Why efficient**
We traverse each connection once → avoids redundant exploration.

**Python Solution**

```python
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        
        def dfs(city):
            for neighbor in range(n):
                # If connected and not visited
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)
        
        provinces = 0
        
        for city in range(n):
            if not visited[city]:
                provinces += 1
                visited[city] = True
                dfs(city)
        
        return provinces
```

**Explain any tricky part of the code**

* Even though it's a matrix, we treat it like a graph and scan all neighbors for each city.

Edge-case handling: Fully disconnected cities → each city becomes its own province.

**Complexity**
Time: O(n²) — scanning adjacency matrix
Space: O(n) — visited array + recursion stack
