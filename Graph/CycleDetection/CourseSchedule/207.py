"""
LeetCode #207: Course Schedule

https://leetcode.com/problems/course-schedule/
"""

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # graph[course] = list of its prerequisites
        graph = [[] for _ in range(numCourses)]
        
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        state = [0] * numCourses  # 0=unvisited, 1=visiting, 2=visited
        
        def dfs(course):
            if state[course] == 1:
                return False  # cycle detected
            if state[course] == 2:
                return True   # already processed
            
            state[course] = 1  # mark as visiting
            
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            
            state[course] = 2  # mark as safe
            return True
        
        for course in range(numCourses):
            if state[course] == 0:
                if not dfs(course):
                    return False
        
        return True