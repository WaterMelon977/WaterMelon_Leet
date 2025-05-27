Recursion
https://colab.research.google.com/drive/1qdUMlMleXTlObv-r-jdJj6tR2Vmes5AF?usp=sharing

Trees
https://colab.research.google.com/drive/1d0z8pA4Swkk-_bKZkaKpuRQvCNYecxNA?usp=sharing

## 🌳 BINARY TREE - PYTHON INTERVIEW REVIEW NOTES

---

## 🔎 TREE TRAVERSALS

### DFS (Depth-First Search)

```python
def dfs(root):
    if not root:
        return
    dfs(root.left)
    dfs(root.right)
```

### BFS (Level Order Traversal)

```python
from collections import deque

def bfs(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

---

## 🔄 Invert Binary Tree (Leetcode 226)

Swap left and right child recursively

```python
def invertTree(root):
    if not root:
        return None
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root
```

---

## 📈 Maximum Depth of Binary Tree (Leetcode 104)

```python
def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
```

---

## 📊 Balanced Binary Tree (Leetcode 110)

Check if left and right subtree height differ by no more than 1

```python
def isBalanced(root):
    def check(node):
        if not node:
            return 0
        left = check(node.left)
        if left == -1:
            return -1
        right = check(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return check(root) != -1
```

---

## 🥰 Diameter of Binary Tree (Leetcode 543)

Longest path between any two nodes

```python
def diameterOfBinaryTree(root):
    diameter = 0
    def depth(node):
        nonlocal diameter
        if not node:
            return 0
        left = depth(node.left)
        right = depth(node.right)
        diameter = max(diameter, left + right)
        return 1 + max(left, right)

    depth(root)
    return diameter
```

---

## 🗳 Same Binary Tree (Leetcode 100)

```python
def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
```

---

## 📎 Symmetric Tree (Leetcode 101)

Check if tree is a mirror of itself

```python
def isSymmetric(root):
    def isMirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2 or t1.val != t2.val:
            return False
        return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

    return isMirror(root, root)
```

---

## 🔹 Path Sum (Leetcode 112)

```python
def hasPathSum(root, targetSum):
    if not root:
        return False
    if not root.left and not root.right:
        return targetSum == root.val
    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)
```

---

## 📌 NOTES:

- Use **DFS** for most recursive solutions
- Use **BFS** (level-order) for symmetry checks or traversal by depth
- Pay attention to **base cases** (null/leaf nodes)
- Recursive post-order traversal is best for depth-related problems
- Use `nonlocal` or return multiple values for helper functions

---

## 🌳 BINARY TREE - PYTHON INTERVIEW REVIEW NOTES

---

## 🔎 TREE TRAVERSALS

### DFS (Depth-First Search)

```python
def dfs(root):
    if not root:
        return
    dfs(root.left)
    dfs(root.right)
```

### BFS (Level Order Traversal)

```python
from collections import deque

def bfs(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

---

## 🔄 Invert Binary Tree (Leetcode 226)

Swap left and right child recursively

```python
def invertTree(root):
    if not root:
        return None
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root
```

---

## 📈 Maximum Depth of Binary Tree (Leetcode 104)

```python
def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
```

---

## 📊 Balanced Binary Tree (Leetcode 110)

```python
def isBalanced(root):
    def check(node):
        if not node:
            return 0
        left = check(node.left)
        if left == -1:
            return -1
        right = check(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return check(root) != -1
```

---

## 🥰 Diameter of Binary Tree (Leetcode 543)

```python
def diameterOfBinaryTree(root):
    diameter = 0
    def depth(node):
        nonlocal diameter
        if not node:
            return 0
        left = depth(node.left)
        right = depth(node.right)
        diameter = max(diameter, left + right)
        return 1 + max(left, right)

    depth(root)
    return diameter
```

---

## 🗳 Same Binary Tree (Leetcode 100)

```python
def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
```

---

## 📎 Symmetric Tree (Leetcode 101)

```python
def isSymmetric(root):
    def isMirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2 or t1.val != t2.val:
            return False
        return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

    return isMirror(root, root)
```

---

## 🔹 Path Sum (Leetcode 112)

```python
def hasPathSum(root, targetSum):
    if not root:
        return False
    if not root.left and not root.right:
        return targetSum == root.val
    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)
```

---

## 📍 Subtree of Another Tree (Leetcode 572)

```python
def isSubtree(root, subRoot):
    if not root:
        return False
    if isSameTree(root, subRoot):
        return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)
```

---

## 🌐 Binary Tree Level Order Traversal (Leetcode 102)

```python
from collections import deque

def levelOrder(root):
    if not root:
        return []
    res, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level)
    return res
```

---

## 🥇 Kth Smallest in BST (Leetcode 230)

Inorder traversal of BST gives sorted order

```python
def kthSmallest(root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right
```

---

## ⬇️ Minimum Absolute Difference in BST (Leetcode 530)

```python
prev = None
res = float('inf')

def getMinimumDifference(root):
    def inorder(node):
        nonlocal prev, res
        if not node:
            return
        inorder(node.left)
        if prev:
            res = min(res, abs(node.val - prev.val))
        prev = node
        inorder(node.right)

    inorder(root)
    return res
```

---

## 🔢 Validate BST (Leetcode 98)

```python
def isValidBST(root):
    def helper(node, low=float('-inf'), high=float('inf')):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return helper(node.left, low, node.val) and helper(node.right, node.val, high)

    return helper(root)
```

---

## 🔍 Lowest Common Ancestor in BST (Leetcode 235)

```python
def lowestCommonAncestor(root, p, q):
    if p.val < root.val and q.val < root.val:
        return lowestCommonAncestor(root.left, p, q)
    if p.val > root.val and q.val > root.val:
        return lowestCommonAncestor(root.right, p, q)
    return root
```

---

## 🔮 Implement Trie (Prefix Tree) (Leetcode 208)

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end = True

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.end

    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
```

---

## 📌 NOTES:

- Use **DFS** for most recursive solutions
- Use **BFS** (level-order) for symmetry or layered traversals
- BST properties help with binary search or ordering
- Trie is used for prefix matching
- Use auxiliary variables like `prev`, `res`, or `stack` as needed for tracking
- Pay attention to **base cases**

---
