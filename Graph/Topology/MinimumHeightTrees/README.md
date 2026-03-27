Thinking through this:

- The roots that produce minimum height trees are always the **midpoint(s)** of the longest path in the graph (the tree's diameter)
- Key realization: trim leaf nodes layer by layer from outside in — exactly like topological sort but on an undirected graph
- At most 2 nodes can ever be the answer (the 1–2 center nodes of the diameter)
- Use degree array: leaves have degree 1. Repeatedly peel them, reduce neighbors' degrees, new leaves emerge
- Stop when ≤ 2 nodes remain — those are the centers

**LeetCode Link**
https://leetcode.com/problems/minimum-height-trees/

---

**Approach**
- Build an undirected adjacency list and a `degree` array for all nodes
- Initialize queue with all current leaves (nodes with `degree == 1`)
- Iteratively trim leaves: reduce each neighbor's degree by 1; if neighbor becomes a new leaf (`degree == 1`), add to next wave
- Shrink `remaining_nodes` count each wave; stop trimming when `remaining_nodes <= 2`
- Whatever nodes remain are the centroid(s) — return them as the answer

---

**Key Insight**
The center of a tree (minimizing max depth) is always the **midpoint of its longest path**. Peeling leaves inward layer by layer converges exactly to that midpoint — the last 1 or 2 surviving nodes are always the answer, guaranteed.

---

**Why efficient**
Every node and edge is visited at most once across all trimming waves, giving true linear time. No need to BFS/DFS from every node candidate, which would be O(N²).

---

**Python Solution**

```python
from collections import deque, defaultdict

def findMinHeightTrees(n: int, edges: list[list[int]]) -> list[int]:
    # edge case: single node has no edges
    if n == 1:
        return [0]

    # build undirected adjacency list and degree count
    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    degree = [len(adj[node]) for node in range(n)]

    # initialize queue with all leaf nodes (degree == 1)
    queue = deque([node for node in range(n) if degree[node] == 1])
    remaining_nodes = n

    # trim leaves inward until 1 or 2 center nodes remain
    while remaining_nodes > 2:
        leaf_count = len(queue)
        remaining_nodes -= leaf_count

        # process all current leaves simultaneously (one full wave)
        for _ in range(leaf_count):
            leaf = queue.popleft()
            for neighbor in adj[leaf]:
                degree[neighbor] -= 1
                # neighbor is now exposed as a new leaf
                if degree[neighbor] == 1:
                    queue.append(neighbor)

    return list(queue)
```

---

**Explain any tricky part of the code**

**Wave-by-wave processing (the `leaf_count` snapshot):** We must process all leaves of the *current wave together* before moving to the next — similar to BFS level-order traversal. Capturing `leaf_count = len(queue)` at the start of each iteration freezes the current frontier, preventing newly added leaves from being consumed in the same wave, which would corrupt the layer counting.

**Edge-case handling:** `n == 1` is handled upfront because with no edges, the degree list is empty and the leaf-initialization step would produce an empty queue — returning `[0]` explicitly avoids that silent failure.

---

**Complexity**
Time: O(N) — each node is enqueued and dequeued exactly once across all trimming waves
Space: O(N) — adjacency list, degree array, and queue each hold at most N entries