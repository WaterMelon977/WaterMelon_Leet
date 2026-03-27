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



------------------------------------------------

Thinking through this:

- Classic topological sort problem — find a valid ordering of courses given prerequisites
- Khan's Algorithm (BFS-based) is the standard optimal approach: track in-degrees, process nodes with in-degree 0 first
- If a cycle exists, not all nodes will be processed → return empty array
- Build adjacency list + in-degree array, then BFS from all zero in-degree nodes simultaneously
- Append each dequeued node to result order

**LeetCode Link**
https://leetcode.com/problems/course-schedule-ii/

---

**Approach**
- Build a directed adjacency list where `prerequisite → course` (edge direction = dependency order)
- Compute `in_degree[course]` = number of prerequisites each course has
- Initialize a queue with all courses that have `in_degree == 0` (no prerequisites — safe to take first)
- BFS: dequeue a course, append to result, reduce `in_degree` of all its neighbors; enqueue neighbors whose `in_degree` drops to 0
- If result length equals `numCourses`, a valid order exists; otherwise a cycle was detected → return `[]`

---

**Key Insight**
A course can only be scheduled once all its prerequisites are scheduled — this is exactly in-degree 0 in the dependency graph. Cycle detection is free: a cycle means some nodes never reach in-degree 0 and stay stuck.

---

**Why efficient**
Each node and edge is visited exactly once during BFS, avoiding redundant recomputation. No DFS backtracking overhead.

---

**Python Solution**

```python
from collections import deque, defaultdict

def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    # build adjacency list: prereq -> list of courses it unlocks
    adj = defaultdict(list)
    in_degree = [0] * numCourses

    for course, prereq in prerequisites:
        adj[prereq].append(course)
        in_degree[course] += 1

    # start bfs with all courses that have no prerequisites
    queue = deque([c for c in range(numCourses) if in_degree[c] == 0])
    order = []

    while queue:
        course = queue.popleft()
        order.append(course)

        # unlock neighbors by reducing their in-degree
        for neighbor in adj[course]:
            in_degree[neighbor] -= 1
            # this neighbor is now free to be scheduled
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # cycle detected if not all courses were processed
    return order if len(order) == numCourses else []
```

---

**Explain any tricky part of the code**

**Edge direction matters:** The edge goes `prereq → course`, not the other way. This ensures that when we process a prereq and reduce its neighbors' in-degrees, we're saying "this prereq is done, one less blocker for that course." Reversing this breaks the algorithm silently.

**Edge-case handling:** If `prerequisites = []`, all courses start with `in_degree == 0`, the queue fills with all `numCourses` nodes immediately, and the result is simply `[0, 1, ..., numCourses-1]` — handled naturally with no special branching.

---

**Complexity**
Time: O(V + E) — each course (vertex) and prerequisite (edge) is processed exactly once
Space: O(V + E) — adjacency list stores all edges; in-degree array and queue hold at most V entries