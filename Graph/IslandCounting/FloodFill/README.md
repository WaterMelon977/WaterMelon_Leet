**LeetCode Link**
[https://leetcode.com/problems/flood-fill/](https://leetcode.com/problems/flood-fill/)

**Approach**

* Use DFS/BFS to traverse all connected pixels with the same starting color.
* Store the original color at `(sr, sc)` and avoid processing if it's already equal to `color`.
* From the starting cell, explore 4 directions (up, down, left, right).
* Only visit cells that are within bounds and match the original color.
* Change each valid visited cell to the new `color`.
* Continue until all connected same-color pixels are updated.

**Key Insight**
This is a classic graph traversal on a grid where connected components are defined by same-color neighbors.

**Why efficient**
Each cell is visited at most once → linear time relative to grid size.

**Python Solution**

```python
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        original_color = image[sr][sc]
        
        # If the starting pixel already has the target color, no work needed
        if original_color == color:
            return image
        
        def dfs(r, c):
            # Check boundaries and color match
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if image[r][c] != original_color:
                return
            
            # Change color
            image[r][c] = color
            
            # Explore 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        dfs(sr, sc)
        return image
```

**Explain any tricky part of the code**

* The early check `if original_color == color` prevents infinite recursion (since we’d keep revisiting same cells).

Edge-case handling: Starting cell already has the target color → return immediately to avoid unnecessary traversal.

**Complexity**
Time: O(m * n) — each cell visited once
Space: O(m * n) — recursion stack in worst case (full grid DFS)
<!--  -->