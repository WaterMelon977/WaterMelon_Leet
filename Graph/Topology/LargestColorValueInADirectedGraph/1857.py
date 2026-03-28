"""
LeetCode #1857: Largest Color Value in a Directed Graph

https://leetcode.com/problems/largest-color-value-in-a-directed-graph/
"""
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
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
        