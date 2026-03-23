"""
LeetCode #547: Number of Provinces

https://leetcode.com/problems/number-of-provinces/
"""

from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        
        def dfs(city):
            for neighbor in range(n):
                # If connected and not visited
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)
        
        provinces = 0
        
        for city in range(n):
            if not visited[city]:
                provinces += 1
                visited[city] = True
                dfs(city)
        
        return provinces