**LeetCode Link**
[https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/)

**Approach**

* Use **BFS level-order traversal** with a queue.
* Track the current `level` number starting from 1.
* For each level, compute `level_size = len(queue)` to process nodes belonging to that level.
* Sum all node values in that level using `level_sum`.
* If `level_sum` is greater than the current `max_sum`, update `max_sum` and store the level number.
* Continue until all levels are processed.

**Key Insight**
Since BFS naturally groups nodes by level, we can compute the **sum of each level while traversing**, and track the level with the maximum sum.

**Why efficient**
Each node contributes to exactly one level sum, so the tree is scanned once.

**Python Solution**

```python
from collections import deque
from typing import Optional

class Solution:
    def maxLevelSum(self, root: Optional['TreeNode']) -> int:
        queue = deque([root])
        level = 1
        max_sum = float('-inf')
        answer_level = 1
        
        while queue:
            level_size = len(queue)
            level_sum = 0
            
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if level_sum > max_sum:
                max_sum = level_sum
                answer_level = level
            
            level += 1
        
        return answer_level
```

**Explain any tricky part of the code**

Tracking `level` separately is important because BFS does not inherently give level numbers; we increment it after finishing each level.

Edge-case handling: `max_sum` starts at `-inf` to correctly handle trees where node values might be negative.

**Complexity**
Time: **O(n)** — each node is processed once.
Space: **O(n)** — queue stores up to the width of the tree.
