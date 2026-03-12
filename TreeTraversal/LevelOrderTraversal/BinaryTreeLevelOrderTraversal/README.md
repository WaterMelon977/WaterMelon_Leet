**LeetCode Link**
[https://leetcode.com/problems/binary-tree-level-order-traversal/](https://leetcode.com/problems/binary-tree-level-order-traversal/)

**Approach**

* This is a classic **Breadth-First Search (BFS)** traversal of a binary tree.
* Use a **queue** to process nodes level by level.
* Start by pushing the root node into the queue.
* For each level, record the current queue size (number of nodes in that level).
* Process exactly that many nodes, adding their values to the level list and pushing their children into the queue.
* Append the level list to the result and continue until the queue becomes empty.

**Key Insight**
BFS naturally processes nodes **level-by-level**, and using the queue size allows us to isolate nodes belonging to the same level.

**Why efficient**
Each node is processed exactly once and inserted into the queue once, giving optimal linear complexity.

**Python Solution**

```python
from collections import deque
from typing import List, Optional

class Solution:
    def levelOrder(self, root: Optional['TreeNode']) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)
        
        return result
```

**Explain any tricky part of the code**

The key technique is capturing `level_size = len(queue)` before the loop. This ensures we process **only nodes from the current level**, even though new child nodes are added to the queue during the loop.

Edge-case handling: If `root` is `None`, the function immediately returns an empty list.

**Complexity**
Time: **O(n)** — every node is visited exactly once.
Space: **O(n)** — queue may store up to one full level of the tree in the worst case.
