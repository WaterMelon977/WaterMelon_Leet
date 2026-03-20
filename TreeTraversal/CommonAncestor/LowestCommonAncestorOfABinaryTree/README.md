**LeetCode Link**
[https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

**Approach**

* Use **postorder DFS** (left → right → node).
* Base case:

  * If node is `None` → return `None`
  * If node is `p` or `q` → return that node
* Recurse on left and right.
* If **both left and right return non-null** → current node is LCA.
* Otherwise, return the **non-null child result** upward.
* Final answer is the node returned from root.

**Key Insight**
The first node where **p and q appear in different subtrees** (one left, one right) is the LCA.

**Why efficient**
Single traversal of tree → no extra structures needed.

**Python Solution**

```python
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def dfs(node):
            if not node:
                return None
            
            # If current node is p or q
            if node == p or node == q:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If both sides found → this is LCA
            if left and right:
                return node
            
            # Otherwise return whichever side found something
            return left if left else right
        
        return dfs(root)
```

**Explain any tricky part of the code**

The key logic:

```python
if left and right:
    return node
```

Means:

* One target found in left subtree
* One target found in right subtree
  → current node is the lowest meeting point.

Edge-case handling: If one node is ancestor of the other, it gets returned early and bubbles up as LCA.

**Complexity**
Time: O(n) — visit each node once
Space: O(h) — recursion stack
