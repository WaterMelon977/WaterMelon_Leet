**LeetCode Link**
[https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

**Approach**

* Perform **BFS level-order traversal** using a queue (same base idea as problem 102).
* Maintain a boolean flag `left_to_right` to track the traversal direction of the current level.
* For each level, process `level_size = len(queue)` nodes.
* Append node values normally if `left_to_right` is `True`.
* If `left_to_right` is `False`, reverse the order by inserting values at the front of the level list.
* After finishing a level, flip the direction flag to create the zigzag pattern.

**Key Insight**
Level order traversal stays the same as BFS; the only change is **how values are added to the current level list** depending on traversal direction.

**Why efficient**
Each node is visited once. The zigzag ordering is handled during insertion, avoiding extra traversal of the tree.

**Python Solution**

```python
from collections import deque
from typing import List, Optional

class Solution:
    def zigzagLevelOrder(self, root: Optional['TreeNode']) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        left_to_right = True
        
        while queue:
            level_size = len(queue)
            level = deque()
            
            for _ in range(level_size):
                node = queue.popleft()
                
                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(list(level))
            left_to_right = not left_to_right
        
        return result
```

**Explain any tricky part of the code**

Using a **deque for `level`** allows `appendleft()` in O(1). This avoids reversing the list after building the level.

Edge-case handling: If the tree is empty (`root is None`), return an empty list immediately.

**Complexity**
Time: **O(n)** — every node is processed exactly once.
Space: **O(n)** — queue stores nodes of the widest level in the tree.

