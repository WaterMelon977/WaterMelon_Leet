**Thinking through this:**

- We need to find the time for a signal to reach **all nodes** from source `k` — this is just the **maximum shortest path** from `k` to every other node
- Since edge weights are positive, **Dijkstra's algorithm** is the natural fit (Bellman-Ford would work but is O(VE), overkill here)
- Naive approach — BFS won't work because edges have weights; we need a priority queue to always process the closest unvisited node first
- If after running Dijkstra any node is unreachable (distance still infinity), return `-1`
- The answer is `max(dist.values())` — the last node to receive the signal determines total delay

---

**LeetCode Link**
https://leetcode.com/problems/network-delay-time/

**Approach**
- Build an **adjacency list** from the edge list so we can efficiently look up all neighbors of any node
- Initialize a `dist` dictionary with infinity for all nodes except the source `k`, which starts at `0` — we know it takes 0 time to reach yourself
- Use a **min-heap (priority queue)** seeded with `(0, k)` — always process the node with the currently smallest known distance next, which guarantees we finalize distances in optimal order
- When we pop a node, **skip it if we already found a shorter path** (stale entry in the heap) — this avoids reprocessing
- For each neighbor, if going through the current node gives a shorter path, update `dist` and push the new `(cost, neighbor)` into the heap
- After the heap empties, if any node still has distance infinity it's unreachable → return `-1`, otherwise return the `max` of all distances

**Key Insight**
Because all weights are positive, the first time Dijkstra pops a node from the min-heap, that distance is already optimal — no need to revisit it.

**Why efficient**
Dijkstra with a binary heap runs in O((V + E) log V), far better than Bellman-Ford's O(VE); the heap ensures we always extend the shortest known path first without scanning all edges repeatedly.

**Python Solution**
```python
import heapq
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # --- Build adjacency list: node -> list of (neighbor, travel_time) ---
        graph = defaultdict(list)
        for source, destination, travel_time in times:
            graph[source].append((destination, travel_time))

        # --- Initialize distances: all nodes unreachable except the source ---
        dist = {node: float('inf') for node in range(1, n + 1)}
        dist[k] = 0

        # --- Min-heap: (cumulative_time, node) — always process cheapest node next ---
        min_heap = [(0, k)]  # start at source with cost 0

        while min_heap:
            current_time, current_node = heapq.heappop(min_heap)

            # Skip if we already found a better path to this node (stale heap entry)
            if current_time > dist[current_node]:
                continue

            # --- Relax all outgoing edges from current node ---
            for neighbor, edge_weight in graph[current_node]:
                new_time = current_time + edge_weight

                # Only push to heap if this path improves the known best distance
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    heapq.heappush(min_heap, (new_time, neighbor))

        # --- Determine result: max delay, or -1 if any node was unreachable ---
        max_delay = max(dist.values())
        return max_delay if max_delay < float('inf') else -1
```

**Explain any tricky part of the code**
The `if current_time > dist[current_node]: continue` guard handles **stale heap entries** — when we find a better path to a node, we push a new entry but can't remove the old one from the heap. So when the old (worse) entry is eventually popped, we just skip it since `dist[node]` already holds a smaller value.

Edge-case handling: If a node has no incoming edges from `k`'s reachable component, its distance stays `inf` — `max(dist.values())` will be `inf`, and the final check correctly returns `-1`.

**Complexity**
Time: O((V + E) log V) — each node and edge is processed at most once, with heap operations costing log V each
Space: O(V + E) — adjacency list stores all edges, heap and dist map store at most V entries each