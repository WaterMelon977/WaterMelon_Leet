"""
LeetCode #2392: Build a Matrix With Conditions

https://leetcode.com/problems/build-a-matrix-with-conditions/
"""
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topological_sort(num_nodes: int, edges: list[list[int]]) -> list[int]:
            """
            Khan's BFS toposort on nodes 1..num_nodes.
            Returns the ordered list of nodes if no cycle, else empty list.
            """
            # build adjacency list and in-degree for nodes 1..k
            adj = defaultdict(list)
            in_degree = [0] * (num_nodes + 1)  # 1-indexed

            for src, dst in edges:
                adj[src].append(dst)
                in_degree[dst] += 1

            # start with all nodes that have no constraints blocking them
            queue = deque([node for node in range(1, num_nodes + 1)
                        if in_degree[node] == 0])
            order = []

            while queue:
                node = queue.popleft()
                order.append(node)

                for neighbor in adj[node]:
                    in_degree[neighbor] -= 1
                    # neighbor is now unblocked — all its predecessors are placed
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

            # if not all nodes processed, a cycle exists
            return order if len(order) == num_nodes else []

        # get the relative row ordering of numbers 1..k
        row_order = topological_sort(k, rowConditions)
        if not row_order:
            return []  # cycle in row constraints — no valid matrix exists

        # get the relative column ordering of numbers 1..k
        col_order = topological_sort(k, colConditions)
        if not col_order:
            return []  # cycle in column constraints — no valid matrix exists

        # map each number to its row index and column index
        # position in toposort output = its index in the matrix dimension
        row_pos = {num: idx for idx, num in enumerate(row_order)}
        col_pos = {num: idx for idx, num in enumerate(col_order)}

        # place each number at the intersection of its row and column position
        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            matrix[row_pos[num]][col_pos[num]] = num

        return matrix