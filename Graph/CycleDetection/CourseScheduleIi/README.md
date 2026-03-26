**LeetCode Link**
[https://leetcode.com/problems/course-schedule-ii/](https://leetcode.com/problems/course-schedule-ii/)

**Approach**

* Build graph as: `course → prerequisites` (`graph[course].append(prereq)`).
* We need a **topological order** → use DFS + postorder.
* Use 3-state DFS:

  * `0 = unvisited`
  * `1 = visiting` → cycle detection
  * `2 = visited`
* For each course:

  * DFS all its prerequisites first.
  * Then append the course to result.
* If cycle detected → return `[]`.
* Final result is already in correct order (no reverse needed).

**Key Insight**
Add course **after finishing its prerequisites** → natural topological ordering.

**Why efficient**
Each node processed once due to memoization → linear time.

**Python Solution**

```python
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
```

**Explain any tricky part of the code**

* Since we store `course → prerequisites`, we append **after DFS**, so prerequisites naturally come before the course → no reverse needed.

Edge-case handling: Cycle exists → immediately return empty list.

**Complexity**
Time: O(V + E) — each course and dependency processed once
Space: O(V + E) — graph + recursion stack
