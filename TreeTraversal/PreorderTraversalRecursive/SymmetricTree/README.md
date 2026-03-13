**LeetCode Link**
[https://leetcode.com/problems/symmetric-tree/](https://leetcode.com/problems/symmetric-tree/)

**Approach**

* A tree is symmetric if the **left subtree is a mirror of the right subtree**.
* Define a recursive function `isMirror(left, right)` to compare two nodes.
* Base case: if both nodes are `None`, they are symmetric.
* If only one is `None`, symmetry breaks.
* Check if node values are equal.
* Recursively compare:

  * `left.left` with `right.right`
  * `left.right` with `right.left`

**Key Insight**
Symmetry means **mirror equality**, not direct equality. The comparison must cross-match children.

**Why efficient**
Each node pair is checked once while verifying the mirror structure.

**Python Solution**

```python id="h2ezt4"
from typing import Optional

class Solution:
    def isSymmetric(self, root: Optional['TreeNode']) -> bool:
        def isMirror(left, right):
            if not left and not right:
                return True
            
            if not left or not right:
                return False
            
            if left.val != right.val:
                return False
            
            return (isMirror(left.left, right.right) and
                    isMirror(left.right, right.left))
        
        return isMirror(root.left, root.right)
```

**Explain any tricky part of the code**

The recursive comparison swaps sides: `left.left` with `right.right` and `left.right` with `right.left`. This ensures mirror symmetry rather than identical structure.

Edge-case handling: If the root has no children (`root.left` and `root.right` are `None`), the tree is symmetric.

**Complexity**
Time: **O(n)** — every node is visited once.
Space: **O(h)** — recursion stack proportional to tree height.
