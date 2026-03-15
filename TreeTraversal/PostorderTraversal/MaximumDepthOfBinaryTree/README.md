**LeetCode Link**
[https://leetcode.com/problems/maximum-depth-of-binary-tree/](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

**Approach**

* The **depth of a node** is `1 + max(depth of left subtree, depth of right subtree)`.
* Use **DFS recursion** to compute the depth.
* If the node is `None`, return `0`.
* Recursively compute the **depth of the left and right subtrees**.
* Return `1 + max(left_depth, right_depth)`.

**Key Insight**
The height of a binary tree is determined by the **longest path from root to a leaf**, which naturally fits a recursive definition.

**Why efficient**
Each node is visited exactly once while computing subtree depths.

**Python Solution**

```python id="igun4s"
class Solution:
    def maxDepth(self, root):
        
        def dfs(node):
            if not node:
                return 0
            
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            
            return 1 + max(left_depth, right_depth)
        
        return dfs(root)
```

**Explain any tricky part of the code**

The recursive relation:

```python id="chh3ek"
1 + max(left_depth, right_depth)
```

The `1` counts the **current node**, while `max()` ensures we follow the **longest path to a leaf**.

Edge-case handling:
If `root` is `None`, the function immediately returns `0`, representing an empty tree.

**Complexity**

Time: **O(n)** — each node is visited once.
Space: **O(h)** — recursion stack where `h` is the height of the tree.
