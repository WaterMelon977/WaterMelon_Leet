Thinking through this:

- We need to place numbers `1..k` in a `k×k` matrix such that row and column ordering constraints are satisfied
- Row conditions define a relative vertical ordering of numbers; column conditions define horizontal ordering — these are **two independent topological sorts**
- Run toposort on row conditions → get the row position of each number; run toposort on column conditions → get the column position
- If either toposort detects a cycle → return empty matrix
- Once we have `row_pos[num]` and `col_pos[num]` for every number, place `num` at `matrix[row_pos[num]][col_pos[num]]`
- Two completely separate Khan's BFS runs, then one placement pass — clean and elegant

**LeetCode Link**
https://leetcode.com/problems/build-a-matrix-with-conditions/

---

**Approach**
- Run Khan's topological sort on `rowConditions` — the order in which numbers are processed gives their relative row index (first processed = row 0, second = row 1, etc.)
- If the toposort doesn't process all `k` numbers, a cycle exists in row constraints → return `[]`
- Run the exact same Khan's topological sort independently on `colConditions` → get column indices for each number
- If cycle detected in column constraints → return `[]`
- Build a `k×k` zero matrix; for each number `1..k`, place it at `matrix[row_pos[num]][col_pos[num]]`
- Return the filled matrix

---

**Key Insight**
Row and column ordering constraints are **completely independent problems** — solving them as two separate topological sorts decouples the complexity entirely. The position of a number in the toposort output directly maps to its row (or column) index in the matrix.

---

**Why efficient**
Two independent O(K + E) topological sorts plus one O(K) placement pass — linear in constraints. A brute-force search over all permutations of positions would be factorial.

---

**Python Solution**

```python
from collections import deque, defaultdict

def buildMatrix(k: int,
                rowConditions: list[list[int]],
                colConditions: list[list[int]]) -> list[list[int]]:

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
```

---

**Explain any tricky part of the code**

**Index-in-order = position in matrix:** The position of a number in the toposort output list directly becomes its row (or column) index. `enumerate(row_order)` gives `(0, first_num), (1, second_num), ...` — we invert this into `row_pos[num] = idx`. This works because toposort guarantees that if `a` must come before `b`, `a` appears earlier in the list, so `row_pos[a] < row_pos[b]` — the constraint is automatically satisfied.

**Edge-case handling:** A number that appears in no condition still gets a valid position because Khan's seeds all nodes with `in_degree == 0` — isolated numbers are processed first and assigned some valid index.

---

**Complexity**
Time: O(K + E) — two independent toposorts each O(K + E) where E = number of conditions, plus O(K) placement
Space: O(K + E) — adjacency list and in-degree array across both toposorts; output matrix is O(K²)