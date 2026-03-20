**LeetCode Link**
[https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/](https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/)

**Approach**

* First DFS: compute `subtree_height[node]` = height of subtree rooted at node.
* Second DFS (rerooting idea): compute `up[node]` = max height of tree **excluding** this node’s subtree.
* For root: `up[root] = 0`.
* For each node:

  * For left child:

    * Best height excluding left subtree = `max(up[node], depth + 1 + subtree_height[right])`
  * For right child:

    * Best height excluding right subtree = `max(up[node], depth + 1 + subtree_height[left])`
* Store answers for each node value using `up[node]`.
* Return results for queries.

**Key Insight**
When removing a subtree, the answer depends on the **best alternative path outside that subtree**, which comes from either:

* ancestor paths (`up[node]`)
* sibling subtree paths

**Why efficient**
Precompute all answers in two DFS traversals → each query answered in O(1).

**Python Solution**

```python
class Solution:
    def treeQueries(self, root, queries):
        subtree_height = {}
        
        # Step 1: compute subtree heights
        def get_height(node):
            if not node:
                return -1  # so leaf = 0
            left = get_height(node.left)
            right = get_height(node.right)
            h = 1 + max(left, right)
            subtree_height[node.val] = h
            return h
        
        get_height(root)

        res = {}
        
        # Step 2: reroot DFS to compute "up" values
        def dfs(node, depth, up_val):
            if not node:
                return
            
            res[node.val] = up_val
            
            # Heights of children
            left_h = subtree_height.get(node.left.val, -1) if node.left else -1
            right_h = subtree_height.get(node.right.val, -1) if node.right else -1
            
            # For left child
            if node.left:
                new_up_left = max(
                    up_val,                          # from ancestors
                    depth + 1 + right_h             # via sibling
                )
                dfs(node.left, depth + 1, new_up_left)
            
            # For right child
            if node.right:
                new_up_right = max(
                    up_val,
                    depth + 1 + left_h
                )
                dfs(node.right, depth + 1, new_up_right)
        
        dfs(root, 0, 0)
        
        return [res[q] for q in queries]
```

**Explain any tricky part of the code**

The reroot transition:

```python
new_up_left = max(up_val, depth + 1 + right_h)
```

This means:

* Either we come from ancestors (`up_val`)
* Or we go through current node → sibling subtree

Edge-case handling: Use `-1` height for missing children so leaf height becomes 0 and formulas stay consistent.

**Complexity**
Time: O(n + q) — two DFS + query lookup
Space: O(n) — for storing heights and results
