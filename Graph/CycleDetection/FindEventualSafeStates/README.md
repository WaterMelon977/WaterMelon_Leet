**LeetCode Link**
[https://leetcode.com/problems/find-eventual-safe-states/](https://leetcode.com/problems/find-eventual-safe-states/)

**Approach**

* Reverse the graph: for every edge `u → v`, create `v → u` (store parents).
* Compute **indegree** = number of outgoing edges in original graph.
* Nodes with `outdegree = 0` (terminal nodes) are **safe** → push into queue.
* Use BFS (Kahn’s Algorithm):

  * Pop safe node, mark it safe.
  * Reduce indegree of its parents.
  * If any parent’s indegree becomes 0 → it becomes safe.
* Sort and return all safe nodes.

**Key Insight**
A node is safe if all its paths lead to terminal nodes → reverse thinking: remove terminal nodes and propagate safety backward.

**Why efficient**
Instead of DFS cycle detection for every node, we process each edge once using BFS → avoids repeated work.

**Python Solution**

```python
from collections import deque, defaultdict

class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        
        # Reverse graph: child -> list of parents
        reverse_graph = defaultdict(list)
        
        # Outdegree (original graph)
        outdegree = [0] * n
        
        for node in range(n):
            for nei in graph[node]:
                reverse_graph[nei].append(node)
            outdegree[node] = len(graph[node])
        
        # Queue for terminal nodes (safe nodes)
        queue = deque()
        
        for node in range(n):
            if outdegree[node] == 0:
                queue.append(node)
        
        safe = [False] * n
        
        # BFS (Kahn’s Algorithm)
        while queue:
            curr = queue.popleft()
            safe[curr] = True
            
            for parent in reverse_graph[curr]:
                outdegree[parent] -= 1
                
                if outdegree[parent] == 0:
                    queue.append(parent)
        
        # Collect safe nodes in sorted order
        return [i for i in range(n) if safe[i]]
```

**Explain any tricky part of the code**

* Reversing graph is key: instead of checking “where node goes”, we track “who depends on this node”.
* When a node becomes safe, we reduce outdegree of its parents → simulates removing unsafe edges gradually.

Edge-case handling: Nodes in cycles never reach outdegree 0, so they are naturally excluded.

**Complexity**
Time: O(V + E) → each node and edge processed once
Space: O(V + E) → for reverse graph and queue
