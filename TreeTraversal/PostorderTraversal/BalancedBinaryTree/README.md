**LeetCode Link**
[https://leetcode.com/problems/balanced-binary-tree/](https://leetcode.com/problems/balanced-binary-tree/)

**Approach**

* A binary tree is balanced if **for every node** the height difference between left and right subtree is **≤ 1**.
* Use **DFS recursion** that returns the **height of the subtree**.
* If any subtree is already unbalanced, return **-1** as a signal.
* Compute `left_height` and `right_height` from recursive calls.
* If `abs(left_height - right_height) > 1`, return `-1`.
* Otherwise return the subtree height `1 + max(left_height, right_height)`.

**Key Insight**
Use **-1 as a sentinel value** to indicate the subtree is already unbalanced so we can stop further checks early.

**Why efficient**
We compute **height and balance in a single DFS traversal**, avoiding repeated height calculations.

**Python Solution**

```python
class Solution:
    def isBalanced(self, root):
        
        def dfs(node):
            if not node:
                return 0
            
            left_height = dfs(node.left)
            if left_height == -1:
                return -1
            
            right_height = dfs(node.right)
            if right_height == -1:
                return -1
            
            if abs(left_height - right_height) > 1:
                return -1
            
            return 1 + max(left_height, right_height)
        
        return dfs(root) != -1
```

**Explain any tricky part of the code**

The sentinel return:

```python
if left_height == -1:
    return -1
```

If a subtree is already unbalanced, we **propagate `-1` upward**, preventing unnecessary further computation.

Edge-case handling: An empty tree returns height `0`, which is considered balanced.

**Complexity**

Time: **O(n)** — each node is visited once.
Space: **O(h)** — recursion stack where `h` is the tree height.
