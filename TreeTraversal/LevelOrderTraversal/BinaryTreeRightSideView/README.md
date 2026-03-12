**LeetCode Link**
[https://leetcode.com/problems/binary-tree-right-side-view/](https://leetcode.com/problems/binary-tree-right-side-view/)

**Approach**

* Use **BFS level-order traversal** with a queue.
* For each level, determine `level_size = len(queue)` to process nodes of that level.
* Traverse nodes in the level from left to right.
* The **last node processed in that level** represents the node visible from the right side.
* Record the value of this last node into the result.
* Continue until all levels are processed.

**Key Insight**
In level-order traversal, the **last node of each level** is the one visible when viewing the tree from the right side.

**Why efficient**
Each node is processed exactly once using BFS, avoiding redundant traversal.

**Python Solution**

```python
from collections import deque
from typing import List, Optional

class Solution:
    def rightSideView(self, root: Optional['TreeNode']) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                if i == level_size - 1:
                    result.append(node.val)
        
        return result
```

**Explain any tricky part of the code**

The condition `if i == level_size - 1` captures the **last node of the level**, which is the visible node from the right side.

Edge-case handling: If the tree is empty (`root is None`), return an empty list.

**Complexity**
Time: **O(n)** — each node is visited once.
Space: **O(n)** — queue may contain a full level of the tree.
