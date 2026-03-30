**Thinking through this:**

- We want the path from `start` to `end` that maximizes the product of edge probabilities — feels like shortest path but inverted (maximize instead of minimize)
- Naive: enumerate all paths — exponential, clearly too slow for large graphs
- Key observation: probabilities are between 0 and 1, so multiplying them always decreases the value — Dijkstra's works here if we flip to "maximum probability" using a max-heap instead of min-heap
- Standard Dijkstra's uses a min-heap on cost; here we use a max-heap on probability (negate in Python since `heapq` is min-heap), and relax edges greedily
- Bellman-Ford would also work but O(V·E) is worse — Dijkstra's with max-heap is O((V + E) log V), which is optimal here since all probabilities are positive (no "negative weights" analog)

---

**LeetCode Link**
https://leetcode.com/problems/path-with-maximum-probability/

**Approach**
- Build an adjacency list where each entry stores `(neighbor, probability)` for both directions, since the graph is undirected
- Use a max-heap initialized with `(-1.0, start)` — we negate probabilities because Python's `heapq` is a min-heap, so negating turns it into a max-heap
- Pop the node with the highest current probability; if it's `end`, return it immediately (first time we reach `end` via max-heap is guaranteed to be the best path)
- For each neighbor, compute the new probability as `current_prob * edge_prob`; if this beats the best known probability to that neighbor, push it onto the heap and update the record
- Use a stale-entry guard: if the popped probability is worse than what we've already recorded for that node, skip it — this avoids reprocessing outdated heap entries
- If the heap empties without reaching `end`, return `0.0` (no path exists)

**Key Insight**
Dijkstra's works here because all probabilities are in `(0, 1]` — multiplying them is monotonically decreasing, which mirrors the non-negative weight requirement. Swapping min for max lets us greedily always extend the most promising path first.

**Why efficient**
Naive DFS/BFS explores all possible paths (exponential); Dijkstra's with a max-heap processes each edge at most once per relaxation, giving O((V + E) log V) — tractable for the given constraints (up to 10⁴ nodes, 2×10⁴ edges).

**Python Solution**
```python
import heapq
from collections import defaultdict
from typing import List

def maxProbability(
    n: int,
    edges: List[List[int]],
    succProb: List[float],
    start_node: int,
    end_node: int
) -> float:

    # Build undirected adjacency list: node -> list of (neighbor, probability)
    graph = defaultdict(list)
    for (u, v), prob in zip(edges, succProb):
        graph[u].append((v, prob))
        graph[v].append((u, prob))  # undirected: add both directions

    # best_prob[node] tracks the highest probability found so far to reach that node
    best_prob = [0.0] * n
    best_prob[start_node] = 1.0  # probability of reaching start from itself is 1

    # Max-heap using negated probabilities (Python heapq is min-heap by default)
    # Each entry: (-probability, node)
    max_heap = [(-1.0, start_node)]

    # Dijkstra's main loop: always process the highest-probability frontier node first
    while max_heap:
        neg_prob, node = heapq.heappop(max_heap)
        curr_prob = -neg_prob  # convert back to positive probability

        # Reached the destination — first pop is always the best (greedy guarantee)
        if node == end_node:
            return curr_prob

        # Stale entry guard: if this probability is outdated, skip processing
        if curr_prob < best_prob[node]:
            continue

        # Relax edges: try to improve probability for each neighbor
        for neighbor, edge_prob in graph[node]:
            new_prob = curr_prob * edge_prob  # probability of path through this edge

            # Only push to heap if we found a better path to neighbor
            if new_prob > best_prob[neighbor]:
                best_prob[neighbor] = new_prob
                heapq.heappush(max_heap, (-new_prob, neighbor))

    # end_node was never reached — no valid path exists
    return 0.0
```

**Explain any tricky part of the code**
The max-heap trick: Python only provides a min-heap via `heapq`. To simulate a max-heap, we store **negated** probabilities — pushing `-0.8` means `0.8` will be popped before `0.6` (since `-0.8 < -0.6`). We negate again on pop to get the real probability back. This is the standard Python idiom for any "greedy pick the largest" problem.

Edge-case handling: If `start_node == end_node`, the heap pops `(-1.0, start)` immediately and returns `1.0` correctly — no special case needed since the early return triggers on the first pop.

**Complexity**
Time: O((V + E) log V) — each node is pushed to the heap at most once per edge relaxation, and each heap operation costs log V
Space: O(V + E) — adjacency list stores all edges, heap and best_prob array are O(V) in the worst case