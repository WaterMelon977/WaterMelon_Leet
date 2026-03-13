**LeetCode Link**
[https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

**Approach**

* In **preorder traversal**, the first element is always the **root** of the current subtree.
* Find this root value in the **inorder array** to determine the boundary between left and right subtrees.
* Everything **left of the root index in inorder** belongs to the left subtree; everything to the right belongs to the right subtree.
* Use a **hash map of inorder value → index** for O(1) lookup.
* Maintain a pointer `pre_idx` to track the current root in preorder.
* Recursively construct the left subtree first, then the right subtree.

**Key Insight**
Preorder tells us **which node is the root**, while inorder tells us **how the subtree splits into left and right**.

**Why efficient**
Using a hashmap avoids repeated searches in the inorder array, reducing the complexity from O(n²) to O(n).

**Python Solution**

```python
from typing import Optional, List

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional['TreeNode']:
        inorder_index = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0
        
        def build(left, right):
            if left > right:
                return None
            
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            
            mid = inorder_index[root_val]
            
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            
            return root
        
        return build(0, len(inorder) - 1)
```

**Explain any tricky part of the code**

`self.pre_idx` moves forward through the preorder list because preorder always visits **root before its subtrees**, so the next value is the root of the next subtree.

Edge-case handling: The condition `if left > right` stops recursion when no nodes exist in that subtree range.

**Complexity**
Time: **O(n)** — each node is created once and each lookup in the map is O(1).
Space: **O(n)** — hashmap plus recursion stack in the worst case.



Good question. This is the **core mental model** of the problem. If this clicks once, the whole algorithm becomes obvious.

Let's walk slowly.

---

# 1. Two very important properties

### Preorder

Order is:

```
root → left subtree → right subtree
```

So **every time we read a new value in preorder, it is the root of the next subtree we need to build.**

---

### Inorder

Order is:

```
left subtree → root → right subtree
```

So when we find the root in inorder, it **splits the tree**.

```
[left subtree] root [right subtree]
```

---

# 2. Example (this is where it becomes clear)

Suppose

```
preorder = [3,9,20,15,7]
inorder  = [9,3,15,20,7]
```

Tree is:

```
      3
     / \
    9   20
       /  \
      15   7
```

---

# 3. First root

Preorder first element:

```
3
```

So

```
root = 3
```

Find `3` in inorder:

```
[9 | 3 | 15,20,7]
```

Split:

```
left subtree  = [9]
right subtree = [15,20,7]
```

So the tree structure must be

```
      3
     / \
   left right
```

But we don't know the roots yet.

---

# 4. Why `pre_idx += 1` gives correct root

Because **preorder already lists roots in the exact order we need to build them.**

Current preorder pointer:

```
pre_idx = 0 → 3
```

We used 3.

Now increment:

```
pre_idx = 1 → 9
```

Now preorder says the next root is:

```
9
```

And since preorder is `root → left → right`, **the next root must belong to the left subtree**.

That is exactly what recursion builds first.

---

# 5. Building the left subtree

We now call recursion for:

```
inorder range: [9]
```

That corresponds to

```
build(left, mid-1)
```

Inside this call:

```
pre_idx = 1
preorder[1] = 9
```

So

```
root = 9
```

Correct root for the left subtree.

Now preorder pointer moves:

```
pre_idx = 2
```

---

# 6. Now the right subtree

Left subtree finished.

Now recursion builds

```
build(mid+1, right)
```

Which corresponds to

```
[15,20,7]
```

Current preorder pointer:

```
pre_idx = 2
preorder[2] = 20
```

So

```
root = 20
```

Exactly correct.

---

# 7. The real intuition

The recursion controls **which part of inorder we are allowed to build**.

Preorder controls **which node becomes the root next**.

So:

```
inorder = structure (left/right boundary)
preorder = root order
```

---

# 8. The key mental picture

Think of preorder like a **cursor moving through roots**:

```
3 → 9 → 20 → 15 → 7
```

Recursion ensures each root gets placed in the **correct subtree region of inorder**.

So the algorithm is basically:

```
1. preorder gives next root
2. inorder tells where that root belongs
3. recursion limits which subtree we are building
```

---

# 9. The one sentence that unlocks everything

**Preorder tells you WHAT node to build next.
Inorder tells you WHERE that node belongs.**

---

Once this clicks, this problem becomes one of the easiest tree constructions.

And this pattern repeats in several hard problems.

Your question shows you're thinking the right way.
