"""
LeetCode #310: Minimum Height Trees

https://leetcode.com/problems/minimum-height-trees/
"""


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