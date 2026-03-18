**LeetCode Link**
[https://leetcode.com/problems/delete-nodes-and-return-forest/](https://leetcode.com/problems/delete-nodes-and-return-forest/)

**Approach**

* Use **postorder DFS** (left → right → node) so we process children before deciding on current node deletion.
* Maintain a `to_delete` set for O(1) lookup.
* Recursive function returns the **updated node** (or `None` if deleted).
* If current node is deleted:

  * Its non-null children become **new roots** → add to result.
  * Return `None` to parent.
* If current node is NOT deleted:

  * Reconnect its left and right children from recursion.
* Initially, if root is not deleted → include it in result.

**Key Insight**
Postorder traversal ensures we **clean children first**, so when deleting a node, its children are already correctly processed and can safely become new roots.

**Why efficient**
Each node is visited exactly once → no redundant work.

**Python Solution**

```python
class Solution:
    def delNodes(self, root, to_delete):
        to_delete_set = set(to_delete)
        forest = []

        def dfs(node):
            if not node:
                return None

            # Process children first (postorder)
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            # If current node needs to be deleted
            if node.val in to_delete_set:
                # Add children as new roots if they exist
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)
                return None  # delete this node

            return node  # keep this node

        # Start DFS
        root = dfs(root)

        # If root is not deleted, add it
        if root:
            forest.append(root)

        return forest
```

**Explain any tricky part of the code**

The key trick is:

```python
node.left = dfs(node.left)
node.right = dfs(node.right)
```

This ensures when we decide to delete `node`, its children are already **fully processed and valid roots** if needed.

Edge-case handling: When the root itself is deleted, we avoid adding it and only return its valid children as forest roots.

**Complexity**
Time: O(n) — each node visited once
Space: O(h) — recursion stack (h = height of tree)
