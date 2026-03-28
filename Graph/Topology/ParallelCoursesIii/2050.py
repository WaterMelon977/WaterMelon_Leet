"""
LeetCode #2050: Parallel Courses III

https://leetcode.com/problems/parallel-courses-iii/
"""

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
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
        