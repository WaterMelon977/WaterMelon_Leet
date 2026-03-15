**LeetCode Link**
[https://leetcode.com/problems/binary-search-tree-iterator/](https://leetcode.com/problems/binary-search-tree-iterator/)

**Approach**

* We need an iterator that returns the **next smallest element** each time.
* Since **BST inorder traversal gives sorted order**, simulate inorder traversal.
* Maintain a **stack** storing the path to the next smallest node.
* During initialization, push the entire **left chain from root** onto the stack.
* `next()` pops the top node (next smallest) and then pushes the **left chain of its right subtree**.
* `hasNext()` simply checks if the stack still contains nodes.

**Key Insight**
The stack always stores the **next nodes that would appear in inorder traversal**, so the top of the stack is always the next smallest element.

**Why efficient**
Each node is pushed and popped **once**, giving amortized constant time per operation.

**Python Solution**

```python
class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        # push all left descendants
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        # next smallest element
        node = self.stack.pop()
        
        # process right subtree
        if node.right:
            self._push_left(node.right)
        
        return node.val

    def hasNext(self):
        return len(self.stack) > 0
```

**Explain any tricky part of the code**

The helper function:

```python
def _push_left(node):
    while node:
        stack.append(node)
        node = node.left
```

This ensures the **smallest unvisited node is always on top of the stack**, exactly mimicking inorder traversal.

Edge-case handling:
If the tree is empty, the stack stays empty and `hasNext()` correctly returns `False`.

**Complexity**

Time: **O(1) amortized per operation** — each node is pushed and popped once.
Space: **O(h)** — stack stores at most the height of the tree.
