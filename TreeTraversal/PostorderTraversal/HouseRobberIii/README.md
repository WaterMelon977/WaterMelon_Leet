**LeetCode Link**
[https://leetcode.com/problems/house-robber-iii/](https://leetcode.com/problems/house-robber-iii/)

**Approach**

* If we rob a node, we **cannot rob its direct children**.
* For each node we track two values:

  * **rob_this** → money if we rob this node.
  * **skip_this** → money if we skip this node.
* Use **DFS recursion** and return these two values for each subtree.
* If we rob the current node:
  `rob_this = node.val + left.skip + right.skip`
* If we skip the current node:
  `skip_this = max(left.rob, left.skip) + max(right.rob, right.skip)`
* The final answer is `max(rob_root, skip_root)`.

**Key Insight**
Each node returns **two states** (rob or skip). This avoids recomputing overlapping cases and naturally models the constraint that **adjacent nodes cannot both be robbed**.

**Why efficient**
Every node is processed once, and each DFS call returns constant-sized information.

**Python Solution**

```python
class Solution:
    def rob(self, root):
        
        def dfs(node):
            if not node:
                return (0, 0)  # (rob_this, skip_this)
            
            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)
            
            # if we rob this node
            rob_this = node.val + left_skip + right_skip
            
            # if we skip this node
            skip_this = max(left_rob, left_skip) + max(right_rob, right_skip)
            
            return (rob_this, skip_this)
        
        rob_root, skip_root = dfs(root)
        return max(rob_root, skip_root)
```

**Explain any tricky part of the code**

The two-state return:

```
(rob_this, skip_this)
```

* `rob_this` → value if this node is robbed (children must be skipped).
* `skip_this` → value if this node is skipped (children can be robbed or skipped).

This converts the problem into **tree dynamic programming**.

Edge-case handling:
If the node is `None`, return `(0,0)` so it contributes nothing to the robbery.

**Complexity**

Time: **O(n)** — each node is processed once.
Space: **O(h)** — recursion stack where `h` is the tree height.
