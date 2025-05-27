https://colab.research.google.com/drive/1V5Afu8zDQLJpPXQLMyocMm93GB2qdOJV

# 🌐 Python Quick Review: Graphs

Quick reference for solving graph-related Leetcode problems in Python.

---

## 🔌 Graph Representation

```python
from collections import defaultdict

graph = defaultdict(list)

# Undirected graph
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

# Directed graph
for u, v in edges:
    graph[u].append(v)
```

---

## ✅ Find if Path Exists in Graph

Use DFS/BFS to check if destination can be reached.

```python
def validPath(n, edges, source, destination):
    from collections import defaultdict, deque
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = set()
    queue = deque([source])
    while queue:
        node = queue.popleft()
        if node == destination:
            return True
        if node in visited:
            continue
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                queue.append(nei)
    return False
```

---

## 🏝️ Number of Islands (DFS)

```python
def numIslands(grid):
    def dfs(r, c):
        if (r < 0 or r >= len(grid) or
            c < 0 or c >= len(grid[0]) or
            grid[r][c] != '1'):
            return
        grid[r][c] = '0'
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1
    return count
```

---

## 📐 Max Area of Island (DFS)

```python
def maxAreaOfIsland(grid):
    def dfs(r, c):
        if (r < 0 or r >= len(grid) or
            c < 0 or c >= len(grid[0]) or
            grid[r][c] == 0):
            return 0
        grid[r][c] = 0
        return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

    max_area = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            max_area = max(max_area, dfs(r, c))
    return max_area
```

---

## 🎓 Course Schedule (Cycle Detection using DFS)

```python
def canFinish(numCourses, prerequisites):
    graph = defaultdict(list)
    for a, b in prerequisites:
        graph[a].append(b)

    visited = set()
    cycle = set()

    def dfs(crs):
        if crs in cycle:
            return False
        if crs in visited:
            return True
        cycle.add(crs)
        for pre in graph[crs]:
            if not dfs(pre):
                return False
        cycle.remove(crs)
        visited.add(crs)
        return True

    return all(dfs(c) for c in range(numCourses))
```

---

## 🧾 Course Schedule II (Topological Sort)

```python
def findOrder(numCourses, prerequisites):
    graph = defaultdict(list)
    for a, b in prerequisites:
        graph[a].append(b)

    visited = set()
    cycle = set()
    res = []

    def dfs(crs):
        if crs in cycle:
            return False
        if crs in visited:
            return True
        cycle.add(crs)
        for pre in graph[crs]:
            if not dfs(pre):
                return False
        cycle.remove(crs)
        visited.add(crs)
        res.append(crs)
        return True

    for c in range(numCourses):
        if not dfs(c):
            return []
    return res
```

---

## 🌊 Pacific Atlantic Water Flow (BFS or DFS from edges)

```python
def pacificAtlantic(heights):
    if not heights:
        return []

    ROWS, COLS = len(heights), len(heights[0])
    pac, atl = set(), set()

    def dfs(r, c, visit, prev_height):
        if ((r, c) in visit or r < 0 or c < 0 or r >= ROWS or c >= COLS or
            heights[r][c] < prev_height):
            return
        visit.add((r, c))
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            dfs(r+dr, c+dc, visit, heights[r][c])

    for c in range(COLS):
        dfs(0, c, pac, heights[0][c])
        dfs(ROWS-1, c, atl, heights[ROWS-1][c])
    for r in range(ROWS):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, COLS-1, atl, heights[r][COLS-1])

    return list(pac & atl)
```

---

## 📌 Notes

- Use **DFS/BFS** for graph traversal.
- Track visited nodes with `set()` or boolean matrix.
- **Topological sort** is used for ordering tasks in DAG (Course Schedule II).
- **Cycle detection** is key in DFS with a `cycle` set.
- Graphs may be represented as adjacency lists (defaultdict or dict of lists).
- Use 4-directional DFS for 2D grid traversal problems like islands.

# Graph Interview Patterns

This document outlines Python solutions and core algorithms to revise important graph problems commonly asked in coding interviews.

---

## 1. Clone Graph

**Leetcode:** [https://leetcode.com/problems/clone-graph/](https://leetcode.com/problems/clone-graph/)

**Pattern:** Graph Traversal (DFS/BFS), HashMap for visited

### Algorithm

- Use a hash map to keep track of visited nodes and their corresponding cloned nodes.
- Traverse the graph using DFS (or BFS) and recursively clone neighbors.

### Python Code (DFS)

```python
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]

            clone = Node(node.val)
            visited[node] = clone
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone

        return dfs(node)
```

---

## 2. Rotting Oranges

**Leetcode:** [https://leetcode.com/problems/rotting-oranges/](https://leetcode.com/problems/rotting-oranges/)

**Pattern:** BFS from multiple sources

### Algorithm

- Use BFS and start from all initially rotten oranges.
- Count time (minutes) level by level in BFS.
- Track fresh oranges and decrement as they rot.

### Python Code

```python
from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh += 1

        time = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            r, c, t = q.popleft()
            time = max(time, t)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc, t + 1))

        return time if fresh == 0 else -1
```

---

## 3. Min Cost to Connect All Points (Prim's Algorithm)

**Leetcode:** [https://leetcode.com/problems/min-cost-to-connect-all-points/](https://leetcode.com/problems/min-cost-to-connect-all-points/)

**Pattern:** Minimum Spanning Tree (Prim's)

### Algorithm

- Use Prim's algorithm with a min-heap.
- Maintain a set of visited nodes and push the minimum edge connecting unvisited nodes.

### Python Code

```python
import heapq

class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        visited = set()
        min_heap = [(0, 0)]  # (cost, point index)
        total_cost = 0

        while len(visited) < n:
            cost, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            visited.add(i)
            total_cost += cost

            for j in range(n):
                if j not in visited:
                    dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    heapq.heappush(min_heap, (dist, j))

        return total_cost
```

---

## 4. Network Delay Time (Dijkstra's Algorithm)

**Leetcode:** [https://leetcode.com/problems/network-delay-time/](https://leetcode.com/problems/network-delay-time/)

**Pattern:** Dijkstra's algorithm (single-source shortest path)

### Algorithm

- Use Dijkstra's algorithm with a min-heap.
- Track the shortest time to each node.
- Return max time among all nodes if all are reachable.

### Python Code

```python
import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        min_heap = [(0, k)]  # (time, node)
        dist = {}

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in dist:
                continue
            dist[node] = time
            for nei, wt in graph[node]:
                if nei not in dist:
                    heapq.heappush(min_heap, (time + wt, nei))

        return max(dist.values()) if len(dist) == n else -1
```

---

These problems help reinforce core graph patterns: traversal (DFS/BFS), shortest paths (Dijkstra), and MST construction (Prim's). Practice them to solidify graph fundamentals for interviews.
