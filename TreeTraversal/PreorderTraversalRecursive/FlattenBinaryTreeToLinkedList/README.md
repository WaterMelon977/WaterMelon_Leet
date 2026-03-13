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


**LeetCode Link**
[https://leetcode.com/problems/flatten-binary-tree-to-linked-list/](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)

**Approach**

* We must transform the binary tree **in-place** into a linked list following **preorder traversal (root → left → right)**.
* For every node, if it has a left child, the left subtree must be inserted between the node and its right subtree.
* Find the **rightmost node of the left subtree** (preorder predecessor).
* Attach the original **right subtree** to this rightmost node.
* Move the **left subtree to the right**, and set `left = None`.
* Continue traversing using `curr = curr.right` until the tree is flattened.

**Key Insight**
The **rightmost node of the left subtree** is the last node visited in preorder for that subtree, so the original right subtree must be attached there.

**Why efficient**
This approach modifies the tree **in-place** and processes each node once, avoiding recursion or extra stacks.

**Python Solution**

```python
class Solution:
    def flatten(self, root):
        curr = root
        
        while curr:
            if curr.left:
                # find rightmost node of left subtree
                predecessor = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                
                # attach original right subtree
                predecessor.right = curr.right
                
                # move left subtree to right
                curr.right = curr.left
                curr.left = None
            
            # move to next node in the list
            curr = curr.right
```

**Explain any tricky part of the code**

The tricky step is finding the **rightmost node of the left subtree**:

```python
while predecessor.right:
    predecessor = predecessor.right
```

This node is the **last node visited in preorder within the left subtree**, so we attach the original right subtree there to preserve preorder order.

Edge-case handling:
If a node has no left child, we simply move to `curr.right`, ensuring nodes with only right children remain unchanged.

**Complexity**

Time: **O(n)** — each node is visited a constant number of times.
Space: **O(1)** — tree is modified in-place without recursion or extra structures.
