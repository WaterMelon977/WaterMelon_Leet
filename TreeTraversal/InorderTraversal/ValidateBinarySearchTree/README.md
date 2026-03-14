**LeetCode Link**
[https://leetcode.com/problems/validate-binary-search-tree/](https://leetcode.com/problems/validate-binary-search-tree/)

**Approach**

* A valid BST requires **left subtree < node < right subtree for every node**.
* Pass **valid value ranges (lower, upper)** during DFS.
* Initially, the root has range **(-∞, +∞)**.
* For each node, check if `lower < node.val < upper`.
* Recurse left with updated **upper = node.val**.
* Recurse right with updated **lower = node.val**.

**Key Insight**
Each node must satisfy **global constraints from all ancestors**, not just its immediate parent. Passing bounds during DFS enforces this.

**Why efficient**
Each node is validated exactly once while maintaining constraints through recursion.

**Python Solution**

```python
class Solution:
    def isValidBST(self, root):
        
        def dfs(node, lower, upper):
            if not node:
                return True
            
            # check BST constraint
            if not (lower < node.val < upper):
                return False
            
            # validate left and right subtrees
            return (dfs(node.left, lower, node.val) and
                    dfs(node.right, node.val, upper))
        
        return dfs(root, float('-inf'), float('inf'))
```

**Explain any tricky part of the code**

The range update:

```
dfs(node.left, lower, node.val)
dfs(node.right, node.val, upper)
```

This ensures all nodes in the left subtree remain **less than the current node**, and all nodes in the right subtree remain **greater**, preserving constraints from all ancestors.

Edge-case handling:
Duplicate values violate the condition because the check uses **strict inequality (`<`)**, ensuring duplicates invalidate the BST.

**Complexity**

Time: **O(n)** — every node is visited once.
Space: **O(h)** — recursion stack where `h` is tree height.
