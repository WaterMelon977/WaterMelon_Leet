**LeetCode Link**
[https://leetcode.com/problems/minimum-absolute-difference-in-bst/](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)

**Approach**

* In a **BST, inorder traversal produces sorted values**.
* The **minimum absolute difference** must occur between **two consecutive values in this sorted order**.
* Perform **DFS inorder traversal**.
* Track the **previous visited value (`prev`)**.
* For each node, compute `node.val - prev` and update the minimum difference.
* Continue traversal across the tree.

**Key Insight**
Because inorder traversal of a BST gives **sorted values**, the minimum difference will always be between **adjacent nodes in inorder order**, not arbitrary nodes.

**Why efficient**
We compute differences **during traversal** without storing all values or sorting.

**Python Solution**

```python
class Solution:
    def getMinimumDifference(self, root):
        prev = None
        min_diff = float('inf')
        
        def dfs(node):
            nonlocal prev, min_diff
            if not node:
                return
            
            # inorder traversal
            dfs(node.left)
            
            # compute difference with previous node
            if prev is not None:
                min_diff = min(min_diff, node.val - prev)
            
            prev = node.val
            
            dfs(node.right)
        
        dfs(root)
        return min_diff
```

**Explain any tricky part of the code**

The key step:

```
node.val - prev
```

Since inorder traversal yields **sorted node values**, `prev` is always the **immediate predecessor**, making this difference the only candidate needed to track the minimum.

Edge-case handling:
For the **first visited node**, `prev` is `None`, so we skip computing the difference.

**Complexity**

Time: **O(n)** — each node is visited once.
Space: **O(h)** — recursion stack where `h` is the height of the tree.
