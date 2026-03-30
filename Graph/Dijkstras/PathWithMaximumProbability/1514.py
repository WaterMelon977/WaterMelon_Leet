"""
LeetCode #1514: Path with Maximum Probability

https://leetcode.com/problems/path-with-maximum-probability/
"""
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