**LeetCode Link**
[https://leetcode.com/problems/binary-tree-postorder-traversal/](https://leetcode.com/problems/binary-tree-postorder-traversal/)

**Approach**

* Postorder traversal follows **Left → Right → Root**.
* Use **DFS recursion** to naturally follow this order.
* Recursively traverse the **left subtree**.
* Recursively traverse the **right subtree**.
* After both children are processed, **append the current node value**.
* Store results in a list.

**Key Insight**
The node is processed **only after both subtrees are explored**, which defines postorder traversal.

**Why efficient**
Each node is visited exactly once while recursion follows the natural structure of the tree.

**Python Solution**

```python
class Solution:
    def postorderTraversal(self, root):
        result = []
        
        def dfs(node):
            if not node:
                return
            
            # traverse left subtree
            dfs(node.left)
            
            # traverse right subtree
            dfs(node.right)
            
            # process current node
            result.append(node.val)
        
        dfs(root)
        return result
```

**Explain any tricky part of the code**

The traversal order:

```
dfs(node.left)
dfs(node.right)
result.append(node.val)
```

The node value is appended **after visiting both children**, ensuring the correct **postorder sequence**.

Edge-case handling: If `root` is `None`, DFS immediately returns and the result list remains empty.

**Complexity**

Time: **O(n)** — every node is visited once.
Space: **O(h)** — recursion stack where `h` is the tree height.
