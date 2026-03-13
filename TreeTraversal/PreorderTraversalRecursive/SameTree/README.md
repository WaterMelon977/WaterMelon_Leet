**LeetCode Link**
[https://leetcode.com/problems/same-tree/](https://leetcode.com/problems/same-tree/)

**Approach**

* The trees are the same if **structure and node values match at every position**.
* Use **DFS recursion** to compare corresponding nodes in both trees.
* Base case: if both nodes are `None`, they are identical at that position.
* If one node is `None` and the other is not, trees differ.
* If node values differ, return `False`.
* Recursively check the **left subtrees and right subtrees**.

**Key Insight**
Two trees are identical only if:

* current node values match
* left subtrees are identical
* right subtrees are identical

**Why efficient**
Each node pair is compared exactly once.

**Python Solution**

```python
from typing import Optional

class Solution:
    def isSameTree(self, p: Optional['TreeNode'], q: Optional['TreeNode']) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
```

**Explain any tricky part of the code**

The condition `if not p or not q` ensures that if only one node exists at that position, the trees are structurally different.

Edge-case handling: When both nodes are `None`, recursion returns `True`, correctly handling leaf boundaries.

**Complexity**
Time: **O(n)** — each node is compared once.
Space: **O(h)** — recursion stack proportional to tree height (worst case `n`, balanced tree `log n`).
