**LeetCode Link**
[https://leetcode.com/problems/find-leaves-of-binary-tree/](https://leetcode.com/problems/find-leaves-of-binary-tree/)

**Approach**

* Leaves are nodes with **no children**.
* After removing leaves, new leaves are formed → this repeats level by level.
* Instead of physically removing nodes, compute each node’s **height**:

  * Leaf node → height = 0
  * Parent → height = `1 + max(left, right)`
* Nodes with the same height belong to the same “removal round”.
* Use DFS to compute heights and group nodes by height.

**Key Insight**
A node’s **height equals the round in which it becomes a leaf**.

**Why efficient**
We compute heights in a single DFS and group nodes without modifying the tree.

**Python Solution**

```python
class Solution:
    def findLeaves(self, root):
        res = []
        
        def dfs(node):
            if not node:
                return -1  # base for height calculation
            
            left_h = dfs(node.left)
            right_h = dfs(node.right)
            
            curr_h = 1 + max(left_h, right_h)
            
            # ensure list exists
            if curr_h == len(res):
                res.append([])
            
            res[curr_h].append(node.val)
            
            return curr_h
        
        dfs(root)
        return res
```

**Explain any tricky part of the code**

The base case:

```
return -1
```

This ensures that a **leaf node gets height 0**:

```
1 + max(-1, -1) = 0
```

So leaves naturally fall into the first group.

Edge-case handling:
If the tree is empty, DFS returns immediately and the result is an empty list.

**Complexity**

Time: **O(n)** — each node is visited once.
Space: **O(h)** — recursion stack where `h` is tree height.
