Thinking through this:

- We need to find the maximum frequency of any single color along any path in a directed graph — classic topological sort + DP problem
- Naive approach (DFS every path) is exponential — we need to propagate color counts forward through the graph efficiently
- Key DP state: `dp[node][color]` = max count of `color` along any path ending at `node`
- Process nodes in topological order (Khan's BFS) — when we process a node, all its predecessors are already finalized, so we can safely inherit and update color counts
- If a cycle exists, not all nodes will be processed → return -1 (infinite path, no valid answer)
- Track global max across all `dp[node][color]` values as we go

**LeetCode Link**
https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

---

**Approach**
- Build a directed adjacency list and compute `in_degree` for every node, exactly like Khan's algorithm setup
- Create a 2D DP table `dp[node][color]` initialized to 0 — this will store the best (max) count of each color on any path reaching that node
- Seed the queue with all nodes of `in_degree == 0` (no incoming edges — valid path starting points); for each such node, set `dp[node][its_own_color] = 1`
- BFS: dequeue a node, update the global max from its color counts, then for each neighbor push the best color counts forward: `dp[neighbor][c] = max(dp[neighbor][c], dp[node][c])`, and additionally increment the neighbor's own color
- Decrement neighbor's `in_degree`; if it hits 0, set its own color count to at least 1 and enqueue it
- If total processed nodes < `n`, a cycle was detected — return -1

---

**Key Insight**
`dp[node][color]` accumulates the maximum number of times `color` appears on any path arriving at `node`. When pushing to a neighbor, we inherit the parent's counts and add 1 only for the neighbor's own color — this cleanly separates "what came before" from "what this node contributes."

---

**Why efficient**
Each node and edge is visited exactly once during BFS, and each update is O(26) for the color propagation — giving O(26 × (N + E)) which simplifies to O(N + E). The naive all-paths DFS would be exponential.

---

**Python Solution**

```python
from collections import deque, defaultdict

def largestPathValue(colors: str, edges: list[list[int]]) -> int:
    n = len(colors)
    NUM_COLORS = 26

    # build directed graph and track how many edges point into each node
    adj = defaultdict(list)
    in_degree = [0] * n

    for src, dst in edges:
        adj[src].append(dst)
        in_degree[dst] += 1

    # dp[node][c] = max count of color c on any path ending at node
    # initialized to 0 meaning no path has reached this node yet
    dp = [[0] * NUM_COLORS for _ in range(n)]

    # seed queue with nodes that have no prerequisites (in_degree == 0)
    # these are valid starting points of paths
    queue = deque()
    for node in range(n):
        if in_degree[node] == 0:
            queue.append(node)
            # this node contributes 1 count of its own color
            dp[node][ord(colors[node]) - ord('a')] = 1

    processed_count = 0  # tracks how many nodes we've finalized
    global_max = 0        # best color frequency found across all paths

    # process nodes in topological order
    while queue:
        node = queue.popleft()
        processed_count += 1

        # update global max with the best color count at this node
        global_max = max(global_max, max(dp[node]))

        # propagate this node's color counts forward to each neighbor
        for neighbor in adj[node]:
            neighbor_color = ord(colors[neighbor]) - ord('a')

            for c in range(NUM_COLORS):
                # inherit the best count of color c from this path so far
                inherited_count = dp[node][c]

                # if neighbor's own color matches c, this node adds 1 more
                if c == neighbor_color:
                    inherited_count += 1

                # keep the maximum across all paths reaching this neighbor
                dp[neighbor][c] = max(dp[neighbor][c], inherited_count)

            # one fewer incoming edge to satisfy before neighbor is ready
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # if we didn't process all nodes, a cycle exists — no valid answer
    return global_max if processed_count == n else -1
```

---

**Explain any tricky part of the code**

**The `inherited_count + 1` pattern:** When pushing color counts from `node` to `neighbor`, we copy all 26 color counts as-is — except for the neighbor's own color, which gets +1. This is the cleanest way to say "everything your ancestors accumulated stays the same, but you add one count for yourself." Doing it inline inside the loop avoids a separate post-increment step that's easy to forget.

**Edge-case handling:** A self-loop like `edges = [[0, 0]]` creates a cycle where `in_degree[0]` never reaches 0 — `processed_count` will be less than `n` and the function correctly returns -1.

---

**Complexity**
Time: O(26 × (N + E)) → O(N + E) — each node and edge is processed once, with a constant 26-color inner loop per edge
Space: O(26 × N) → O(N) — the DP table dominates; adjacency list and queue are O(N + E)
