**LeetCode Link**
[https://leetcode.com/problems/course-schedule/](https://leetcode.com/problems/course-schedule/)

**Approach**

* Build graph as: `course → prerequisites` (`graph[course].append(prereq)`).
* Now DFS means: “to take this course, can I finish all its prerequisites?”
* Use 3-state DFS:

  * `0 = unvisited`
  * `1 = visiting` (cycle detection)
  * `2 = visited` (already safe)
* For each course:

  * Recursively check all its prerequisites.
  * If any prerequisite leads to a cycle → return False.
* If all courses are valid → return True.

**Key Insight**
Cycle means a course indirectly depends on itself → impossible to complete.

**Why efficient**
Each node is processed once due to memoization (`state=2`).

**Python Solution**

```python id="q6l7yb"
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
```

**Explain any tricky part of the code**

* Here DFS direction is **reversed mentally**:

  * Instead of “what courses depend on me?”
  * We ask: **“what do I depend on?”**
* Cycle example:

  ```
  0 → 1 → 2 → 0
  ```

  While checking course `0`, DFS goes:

  ```
  0 → 1 → 2 → 0 (already visiting → cycle)
  ```

Edge-case handling: Course with no prerequisites → DFS returns True immediately.

**Complexity**
Time: O(V + E) — each course and dependency processed once
Space: O(V + E) — graph + recursion stack
