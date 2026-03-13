**LeetCode Link**
[https://leetcode.com/problems/flatten-binary-tree-to-linked-list/](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)

**Approach**

* The final structure must follow **preorder traversal order**: `root → left → right`.
* Recursively flatten the **left subtree** and **right subtree**.
* If a left subtree exists:

  * Find the **rightmost node of the left subtree**.
  * Attach the original right subtree to this node.
  * Move the left subtree to the right side of the root.
  * Set `root.left = None`.
* Continue this process for every node.

**Key Insight**
The flattened tree must follow **preorder order**, so the left subtree should appear between the root and the original right subtree.

**Why efficient**
Each node is visited once, and pointer adjustments are constant-time except for finding the rightmost node.

**Python Solution**

```python
from typing import Optional

class Solution:
    def flatten(self, root: Optional['TreeNode']) -> None:
        if not root:
            return
        
        self.flatten(root.left)
        self.flatten(root.right)
        
        if root.left:
            rightmost = root.left
            while rightmost.right:
                rightmost = rightmost.right
            
            rightmost.right = root.right
            root.right = root.left
            root.left = None
```

**Explain any tricky part of the code**

Finding the **rightmost node of the left subtree** ensures the original right subtree is attached at the correct place in the preorder sequence.

Edge-case handling: If `root.left` is `None`, no restructuring is needed and the recursion simply continues.

**Complexity**
Time: **O(n)** average, though worst-case skewed trees may approach O(n²) due to repeated rightmost searches.
Space: **O(h)** recursion stack proportional to tree height.
