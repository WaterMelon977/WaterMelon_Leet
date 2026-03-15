**LeetCode Link**
[https://leetcode.com/problems/diameter-of-binary-tree/](https://leetcode.com/problems/diameter-of-binary-tree/)

**Approach**

* The **diameter** of a tree is the **number of edges in the longest path between any two nodes**.
* For each node, the longest path passing through it is:
  **height(left subtree) + height(right subtree)**.
* Use **DFS recursion** to compute subtree heights.
* While computing heights, update a global `diameter`.
* Return the height of each subtree as `1 + max(left_height, right_height)`.
* The maximum value of `left_height + right_height` across all nodes is the answer.

**Key Insight**
The longest path in a tree **always passes through some node**, so checking `left_height + right_height` at every node finds the diameter.

**Why efficient**
We compute **height and diameter in a single DFS traversal**, avoiding repeated height calculations.

**Python Solution**

```python
class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = 0
        
        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # update diameter
            diameter = max(diameter, left_height + right_height)
            
            # return height
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return diameter
```

**Explain any tricky part of the code**

The key calculation:

```
diameter = max(diameter, left_height + right_height)
```

`left_height + right_height` represents the **longest path that passes through the current node**, connecting the deepest nodes of its left and right subtrees.

Edge-case handling:
If the tree has only one node, both subtree heights are `0`, so the diameter correctly becomes `0`.

**Complexity**

Time: **O(n)** — every node is visited once.
Space: **O(h)** — recursion stack where `h` is the tree height.
