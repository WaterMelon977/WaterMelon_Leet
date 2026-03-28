"""
LeetCode #743: Network Delay Time

https://leetcode.com/problems/network-delay-time/
"""

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