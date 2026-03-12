**LeetCode Link**
[https://leetcode.com/problems/find-largest-value-in-each-tree-row/](https://leetcode.com/problems/find-largest-value-in-each-tree-row/)

**Approach**

* Use **BFS level-order traversal** with a queue.
* Push the root node into the queue.
* For each level, compute `level_size = len(queue)` to isolate that level.
* Track a variable `max_val` initialized to `-inf` for that level.
* Process all nodes of the level, updating `max_val` with `max(max_val, node.val)`.
* Append children to the queue and add `max_val` to the result after finishing the level.

**Key Insight**
Since BFS processes nodes **level by level**, we can compute the maximum value while scanning nodes of the same level.

**Why efficient**
Each node is visited once and compared once, giving optimal linear time complexity.

**Python Solution**

```python
from collections import deque
from typing import List, Optional

class Solution:
    def largestValues(self, root: Optional['TreeNode']) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            max_val = float('-inf')
            
            for _ in range(level_size):
                node = queue.popleft()
                max_val = max(max_val, node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(max_val)
        
        return result
```

**Explain any tricky part of the code**

Initializing `max_val = float('-inf')` ensures the maximum is correctly updated even if all node values in the level are negative.

Edge-case handling: If the tree is empty (`root is None`), return an empty list.

**Complexity**
Time: **O(n)** — every node is processed once.
Space: **O(n)** — queue may hold up to one full level of the tree.
