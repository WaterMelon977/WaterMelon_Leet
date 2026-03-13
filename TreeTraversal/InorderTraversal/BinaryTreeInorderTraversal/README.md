**LeetCode Link**
[https://leetcode.com/problems/binary-tree-inorder-traversal/](https://leetcode.com/problems/binary-tree-inorder-traversal/)

**Approach**

* Inorder traversal follows **Left → Root → Right**.
* Use **DFS recursion** to naturally follow this order.
* Recursively traverse the **left subtree** first.
* Record the **current node value**.
* Recursively traverse the **right subtree**.
* Maintain a result list to collect values in order.

**Key Insight**
Recursion naturally matches the **tree structure**, so performing DFS in the order **left → node → right** directly produces inorder traversal.

**Why efficient**
Each node is visited exactly once. The recursion stack only grows up to the tree height.

**Python Solution**

```python
class Solution:
    def inorderTraversal(self, root):
        result = []
        
        def dfs(node):
            if not node:
                return
            
            # traverse left subtree
            dfs(node.left)
            
            # process current node
            result.append(node.val)
            
            # traverse right subtree
            dfs(node.right)
        
        dfs(root)
        return result
```

**Explain any tricky part of the code**

The recursive order:

```python
dfs(node.left)
result.append(node.val)
dfs(node.right)
```

This enforces the **inorder rule**: visit the entire left subtree first, then the node itself, then the right subtree.

Edge-case handling:
If `root` is `None`, the DFS immediately returns and the result remains an empty list.

**Complexity**

Time: **O(n)** — every node is visited once.
Space: **O(h)** — recursion stack where `h` is the tree height.

---------------------------------------------------------------------------

**LeetCode Link**
[https://leetcode.com/problems/binary-tree-inorder-traversal/](https://leetcode.com/problems/binary-tree-inorder-traversal/)

**Approach**

* Inorder traversal follows the order **left → root → right**.
* Use an **iterative approach with a stack** to simulate recursion.
* Start with the root and keep pushing nodes while moving **left**.
* When no left child exists, **pop from the stack**, record the value.
* Move to the **right subtree** and repeat the process.
* Continue until both the current node is `None` and the stack is empty.

**Key Insight**
The stack keeps track of nodes whose **left subtree has been explored but whose value has not yet been processed**.

**Why efficient**
Each node is pushed and popped **once**, so traversal happens in linear time without recursion overhead.

**Python Solution**

```python
class Solution:
    def inorderTraversal(self, root):
        stack = []
        result = []
        curr = root
        
        while curr or stack:
            
            # go as left as possible
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # process node
            curr = stack.pop()
            result.append(curr.val)
            
            # visit right subtree
            curr = curr.right
        
        return result
```

**Explain any tricky part of the code**

The inner loop:

```python
while curr:
    stack.append(curr)
    curr = curr.left
```

This pushes the entire **left chain** of nodes onto the stack so the **leftmost node** (which should be visited first in inorder) is processed first.

Edge-case handling:
If `root` is `None`, both `curr` and `stack` are empty, so the loop never runs and the function correctly returns an empty list.

**Complexity**

Time: **O(n)** — every node is pushed and popped once.
Space: **O(h)** — stack holds at most the height of the tree.
