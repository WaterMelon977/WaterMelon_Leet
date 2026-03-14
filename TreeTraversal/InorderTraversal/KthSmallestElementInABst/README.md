**LeetCode Link**
[https://leetcode.com/problems/kth-smallest-element-in-a-bst/](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

**Approach**

* In a **BST, inorder traversal produces values in sorted order**.
* The **k-th smallest element** corresponds to the **k-th node visited in inorder traversal**.
* Perform **DFS inorder traversal (left → root → right)**.
* Maintain a counter that increments whenever a node is visited.
* When the counter reaches `k`, record the node value.
* Stop traversal once the answer is found.

**Key Insight**
Because BST inorder traversal yields **sorted order**, the **k-th visited node** directly gives the **k-th smallest element**.

**Why efficient**
We avoid storing all node values; traversal stops as soon as the `k`-th element is found.

**Python Solution**

```python
class Solution:
    def kthSmallest(self, root, k):
        count = 0
        result = None
        
        def dfs(node):
            nonlocal count, result
            if not node or result is not None:
                return
            
            dfs(node.left)
            
            count += 1
            if count == k:
                result = node.val
                return
            
            dfs(node.right)
        
        dfs(root)
        return result
```

**Explain any tricky part of the code**

The early stop condition:

```python
if not node or result is not None:
    return
```

Once the `k`-th element is found, further traversal is unnecessary, so recursion exits immediately.

Edge-case handling:
If `k = 1`, the algorithm returns the **leftmost node**, which is the smallest element in the BST.

**Complexity**

Time: **O(h + k)** — traverse down the tree and visit `k` nodes in inorder.
Space: **O(h)** — recursion stack where `h` is the tree height.
