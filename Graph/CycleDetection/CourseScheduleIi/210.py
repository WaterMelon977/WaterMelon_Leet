"""
LeetCode #210: Course Schedule II

https://leetcode.com/problems/course-schedule-ii/
"""

from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # graph[course] = prerequisites
        graph = [[] for _ in range(numCourses)]
        
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        state = [0] * numCourses  # 0=unvisited, 1=visiting, 2=visited
        order = []
        
        def dfs(course):
            if state[course] == 1:
                return False  # cycle
            if state[course] == 2:
                return True
            
            state[course] = 1
            
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            
            state[course] = 2
            order.append(course)  # add after dependencies
            
            return True
        
        for course in range(numCourses):
            if state[course] == 0:
                if not dfs(course):
                    return []
        
        return order