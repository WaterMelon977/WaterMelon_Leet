**LeetCode Link**
[https://leetcode.com/problems/binary-tree-maximum-path-sum/](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

**Approach**

* Use **postorder DFS** to compute max contribution from left and right subtrees.
* For each node, compute:

  * `left_gain = max(dfs(left), 0)` → ignore negative paths
  * `right_gain = max(dfs(right), 0)`
* The **path passing through current node** = `node.val + left_gain + right_gain`
  → update global maximum.
* Return to parent the **max single path**:

  * `node.val + max(left_gain, right_gain)`
* Maintain a global variable to track the maximum path sum.

**Key Insight**
At each node, we consider it as the **highest point (turning point)** of a path and try combining both left and right gains.

**Why efficient**
We compute everything in a single DFS traversal → no recomputation.

**Python Solution**

```python
class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            # Compute max gain from left and right (ignore negatives)
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # Path passing through current node
            current_path_sum = node.val + left_gain + right_gain

            # Update global max
            self.max_sum = max(self.max_sum, current_path_sum)

            # Return max gain to parent (only one side)
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.max_sum
```

**Explain any tricky part of the code**

The key distinction:

* `current_path_sum` uses **both left + right** (complete path through node)
* Return value uses **only one side** (since parent path can't split)

Edge-case handling: Negative values are handled using `max(..., 0)` so we never include harmful paths.

**Complexity**
Time: O(n) — visit each node once
Space: O(h) — recursion stack height
