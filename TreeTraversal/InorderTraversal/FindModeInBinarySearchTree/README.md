**LeetCode Link**
[https://leetcode.com/problems/find-mode-in-binary-search-tree/](https://leetcode.com/problems/find-mode-in-binary-search-tree/)

**Approach**

* In a **BST, inorder traversal produces values in sorted order**.
* While doing DFS inorder, track the **current value frequency**.
* Maintain `prev` to know if the current value continues the same streak.
* Update `count` for the current value and track `max_count`.
* If `count > max_count`, reset the modes list; if `count == max_count`, append the value.
* Continue DFS through the entire tree.

**Key Insight**
Because inorder traversal of a BST gives **sorted values**, equal values appear **consecutively**, allowing frequency counting in one pass.

**Why efficient**
We compute frequencies **during traversal**, avoiding extra maps or multiple passes.

**Python Solution**

```python
class Solution:
    def findMode(self, root):
        modes = []
        prev = None
        count = 0
        max_count = 0
        
        def dfs(node):
            nonlocal prev, count, max_count
            
            if not node:
                return
            
            # inorder traversal
            dfs(node.left)
            
            # update frequency
            if prev == node.val:
                count += 1
            else:
                count = 1
            
            prev = node.val
            
            # update modes
            if count > max_count:
                max_count = count
                modes.clear()
                modes.append(node.val)
            elif count == max_count:
                modes.append(node.val)
            
            dfs(node.right)
        
        dfs(root)
        return modes
```

**Explain any tricky part of the code**

The frequency update logic:

```python
if prev == node.val:
    count += 1
else:
    count = 1
```

Because values appear **consecutively in inorder traversal**, this correctly counts duplicates without using a hashmap.

Edge-case handling:
The first node has `prev = None`, so the code resets `count = 1`, correctly initializing the first value.

**Complexity**

Time: **O(n)** — every node is visited once during DFS.
Space: **O(h)** — recursion stack where `h` is the tree height.
