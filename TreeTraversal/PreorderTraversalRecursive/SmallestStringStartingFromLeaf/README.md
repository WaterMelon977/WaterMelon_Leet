**LeetCode Link**
[https://leetcode.com/problems/smallest-string-starting-from-leaf/](https://leetcode.com/problems/smallest-string-starting-from-leaf/)

**Approach**

* Each node represents a character: `0 → 'a', 1 → 'b', ... 25 → 'z'`.
* We need the **lexicographically smallest string from leaf → root**.
* Perform **DFS traversal**, keeping the current path.
* Append the current node’s character to the path while going down.
* When reaching a **leaf**, reverse the path to form the **leaf → root string** and compare with the smallest result.
* Backtrack after exploring children to maintain the correct path.

**Key Insight**
We build strings **root → leaf during traversal**, but since the problem requires **leaf → root**, we simply **reverse the path at each leaf** before comparison.

**Why efficient**
Each node is visited once during DFS. String operations only occur at leaves, keeping the overall work proportional to the tree size.

**Python Solution**

```python
class Solution:
    def smallestFromLeaf(self, root):
        self.smallest = None
        
        def dfs(node, path):
            if not node:
                return
            
            # append current character
            path.append(chr(node.val + ord('a')))
            
            # if leaf node
            if not node.left and not node.right:
                candidate = ''.join(reversed(path))
                
                if self.smallest is None or candidate < self.smallest:
                    self.smallest = candidate
            
            # continue traversal
            dfs(node.left, path)
            dfs(node.right, path)
            
            # backtrack
            path.pop()
        
        dfs(root, [])
        return self.smallest
```

**Explain any tricky part of the code**

The tricky part is generating the **leaf → root string**:

```python
candidate = ''.join(reversed(path))
```

`path` stores characters in **root → current order**, so reversing gives the required **leaf → root** string for lexicographic comparison.

Edge-case handling:
If the tree has only one node, it is both root and leaf, so the algorithm correctly returns the single character string.

**Complexity**

Time: **O(n · h)** — DFS visits `n` nodes; reversing path of length `h` occurs only at leaves.
Space: **O(h)** — recursion stack and path storage where `h` is tree height.
