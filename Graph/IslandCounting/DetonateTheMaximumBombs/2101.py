"""
LeetCode #2101: Detonate the Maximum Bombs

https://leetcode.com/problems/detonate-the-maximum-bombs/
"""


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        
        # Build graph
        graph = [[] for _ in range(n)]
        
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, _ = bombs[j]
                
                # Check if j is within i's radius
                if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r1 ** 2:
                    graph[i].append(j)
        
        def dfs(node, visited):
            visited.add(node)
            count = 1
            
            for nei in graph[node]:
                if nei not in visited:
                    count += dfs(nei, visited)
            
            return count
        
        max_bombs = 0
        
        for i in range(n):
            visited = set()
            max_bombs = max(max_bombs, dfs(i, visited))
        
        return max_bombs