"""
LeetCode #802: Find Eventual Safe States

https://leetcode.com/problems/find-eventual-safe-states/
"""

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
