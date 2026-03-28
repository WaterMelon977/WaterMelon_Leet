Thinking through this:

- We need to find the **minimum time to complete all courses** — this is the length of the **critical path** through the dependency DAG
- Each course can start only after all its prerequisites finish — topological order (Khan's) is the natural fit
- DP state: `earliest_finish[node]` = earliest time this course can finish = `time[node] + max(earliest_finish of all prerequisites)`
- When a node's `in_degree` hits 0, all its prerequisites are finalized — safe to compute its finish time
- The answer is simply `max(earliest_finish)` across all nodes — the bottleneck path
- Cycle detection is implicit — but problem guarantees a DAG, so no need to handle -1

**LeetCode Link**
https://leetcode.com/problems/parallel-courses-iii/

---

**Approach**
- Build a directed adjacency list `prereq → course` and compute `in_degree` for every course
- Maintain `earliest_finish[course]` = the earliest possible completion time for each course, initialized to 0
- Seed the BFS queue with all courses that have `in_degree == 0` — these have no blockers and can start at time 0; set their `earliest_finish = time[course]`
- BFS: dequeue a course, then for each course it unlocks, update `earliest_finish[neighbor] = max(earliest_finish[neighbor], earliest_finish[current] + time[neighbor])` — take the max because the neighbor must wait for the **slowest** prerequisite
- Reduce neighbor's `in_degree`; when it hits 0, all its prerequisites are settled — enqueue it
- Return `max(earliest_finish)` — the last course on the critical path determines total time

---

**Key Insight**
`earliest_finish[node]` must take the **maximum** over all incoming prerequisite finish times, not the sum or minimum — a course cannot start until every single prerequisite is done, so the slowest prerequisite is the true blocker.

---

**Why efficient**
Each node and edge is visited exactly once during BFS, and finish times are computed in a single forward pass — O(N + E) versus a naive O(N²) simulation that repeatedly scans for unblocked courses.

---

**Python Solution**

```python
from collections import deque, defaultdict

def minimumTime(n: int, relations: list[list[int]], time: list[int]) -> int:

    # build directed graph: prereq -> courses it unlocks
    adj = defaultdict(list)
    in_degree = [0] * (n + 1)  # 1-indexed courses

    for prereq, course in relations:
        adj[prereq].append(course)
        in_degree[course] += 1

    # earliest_finish[course] = earliest time this course can be completed
    # accounts for the slowest chain of prerequisites leading into it
    earliest_finish = [0] * (n + 1)

    # seed queue with courses that have no prerequisites
    # they can start immediately at time 0
    queue = deque()
    for course in range(1, n + 1):
        if in_degree[course] == 0:
            queue.append(course)
            # no prerequisites — finish time is just this course's own duration
            earliest_finish[course] = time[course - 1]  # time is 0-indexed

    # process courses in topological order
    while queue:
        course = queue.popleft()

        # push this course's finish time forward to every course it unlocks
        for next_course in adj[course]:

            # next_course must wait for THIS course to finish before starting
            # take max because next_course waits for its SLOWEST prerequisite
            earliest_finish[next_course] = max(
                earliest_finish[next_course],
                earliest_finish[course] + time[next_course - 1]
            )

            # one fewer prerequisite blocking this course
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                # all prerequisites are now finalized — safe to enqueue
                queue.append(next_course)

    # the answer is the finish time of the last course on the critical path
    return max(earliest_finish[1:])
```

---

**Explain any tricky part of the code**

**Why `max` and not `+` when updating `earliest_finish[next_course]`:** A course can have multiple prerequisites arriving at different times. Each prerequisite independently tries to update the neighbor's finish time. Using `max` ensures we always keep the worst-case (latest) arrival — because the course literally cannot start until the very last prerequisite finishes. This accumulates naturally across multiple BFS waves without any extra bookkeeping.

**Edge-case handling:** A course with multiple prerequisites gets updated multiple times before its `in_degree` hits 0 — the `max` on each update ensures the final value reflects the true bottleneck predecessor, not whichever happened to be processed last.

---

**Complexity**
Time: O(N + E) — each course and relation edge is processed exactly once during BFS
Space: O(N + E) — adjacency list stores all edges; `earliest_finish` and `in_degree` arrays are O(N)