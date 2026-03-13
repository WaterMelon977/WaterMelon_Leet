**LeetCode Link**
[https://leetcode.com/problems/invert-binary-tree/](https://leetcode.com/problems/invert-binary-tree/)

**Approach**

* The goal is to **swap the left and right child of every node** in the tree.
* Use **DFS recursion** to traverse the tree.
* At each node, swap `node.left` and `node.right`.
* Recursively call the function on the new left and right children.
* Continue until reaching `None` nodes.

**Key Insight**
The inversion is local: **each node only needs its children swapped**, and recursion ensures the operation propagates to the entire tree.

**Why efficient**
Each node is visited exactly once and performs a constant-time swap.

**Python Solution**

```python
from typing import Optional

class Solution:
    def invertTree(self, root: Optional['TreeNode']) -> Optional['TreeNode']:
        if not root:
            return None
        
        # swap children
        root.left, root.right = root.right, root.left
        
        # recurse on children
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
```

**Explain any tricky part of the code**

The line
`root.left, root.right = root.right, root.left`
performs the swap in one operation before recursion continues on the swapped children.

Edge-case handling: If `root` is `None`, the function immediately returns `None`.

**Complexity**
Time: **O(n)** — each node is visited once.
Space: **O(h)** — recursion stack depends on tree height.
