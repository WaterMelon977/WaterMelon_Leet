**LeetCode Link**
[https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

**Approach**

* Use **BST property**: left < root < right.
* Start from root and compare with `p` and `q`.
* If both `p` and `q` are **smaller than root**, move left.
* If both are **greater than root**, move right.
* Otherwise, current node is the **split point → LCA**.
* Iterate until LCA is found.

**Key Insight**
The first node where `p` and `q` go in **different directions (or one equals root)** is the LCA.

**Why efficient**
We avoid traversing entire tree → only follow one path from root.

**Python Solution**

```python
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        current = root
        
        while current:
            # If both nodes are smaller → go left
            if p.val < current.val and q.val < current.val:
                current = current.left
            
            # If both nodes are greater → go right
            elif p.val > current.val and q.val > current.val:
                current = current.right
            
            # Split point found
            else:
                return current
```

**Explain any tricky part of the code**

The key condition:

```python
else:
    return current
```

This handles:

* `p` on left, `q` on right
* OR one of them is exactly `current`

Edge-case handling: Works even if one node is ancestor of the other.

**Complexity**
Time: O(h) — traverse height of tree
Space: O(1) — iterative, no recursion
