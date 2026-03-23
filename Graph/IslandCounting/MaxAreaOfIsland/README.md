**LeetCode Link**
[https://leetcode.com/problems/max-area-of-island/](https://leetcode.com/problems/max-area-of-island/)

**Approach**

* Traverse the grid; whenever you find a `'1'`, start DFS to compute that island’s area.
* During DFS, count current cell and explore 4 directions.
* Mark visited cells by converting `'1' → '0'` to avoid revisiting.
* Track the maximum area across all DFS runs.
* Return the largest area found.

**Key Insight**
Each DFS computes the size of one connected component; take the maximum.

**Why efficient**
Each cell is visited once and “sunk” → no repeated work.

**Python Solution**

```python id="l1r8bq"
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            # Boundary + only process land
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if grid[r][c] == 0:
                return 0
            
            # Mark visited
            grid[r][c] = 0
            
            # Count this cell + neighbors
            area = 1
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)
            
            return area
        
        max_area = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area
```


```python

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(r, c):
            # 1. Base Case: Out of bounds or water (0)
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            
            # 2. Mark as visited by sinking the island (turning 1 to 0)
            grid[r][c] = 0
            
            # 3. Sum up the current cell (1) + all 4 neighbors
            return (1 + dfs(r + 1, c) + 
                        dfs(r - 1, c) + 
                        dfs(r, c + 1) + 
                        dfs(r, c - 1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Update the global maximum with the area of the found island
                    max_area = max(max_area, dfs(r, c))

        return max_area
```

**Explain any tricky part of the code**

* DFS returns the area of the island, so we accumulate using `1 + neighbors`.

Edge-case handling: No land (`all 0s`) → DFS never runs → max_area stays 0.

**Complexity**
Time: O(m * n) — each cell visited once
Space: O(m * n) — recursion stack in worst case


-----------------


This is one of those quirks of Python that trips up almost everyone at first. It comes down to how Python handles **immutable** vs. **mutable** objects when you nest functions.

### 1. Why `current_island_size[0]` works (but `int` doesn't)

In Python, integers are **immutable**. When you do `x = 5` and then `x += 1`, you aren't actually changing the number 5; you are creating a brand-new integer (6) and telling the label `x` to point to it instead.

* **The Problem:** In your `dfs` function, if you just had `current_island_size = 0`, the moment you try to do `current_island_size += 1`, Python thinks, *"Oh, you're creating a **new local variable** inside `dfs` named `current_island_size`."* It loses the connection to the one you defined outside.
* **The List Hack:** A list is **mutable**. When you use `current_island_size = [0]`, you aren't changing the *list* itself when you modify its contents; you’re just reaching inside the box and changing what's there. Because you aren't reassigning the variable name (you aren't saying `current_island_size = ...`), Python doesn't try to create a local copy. All recursive calls are reaching into the **same box**.

---

### 2. What is `nonlocal`?

The `nonlocal` keyword is the "official" way to solve the problem above without using the "List Hack." 

It tells Python: *"Hey, when I mention this variable, don't create a new local one. Look in the parent function's scope and use that one instead."*

**Here is how your code would look using `nonlocal`:**

```python
def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    max_island = 0
    current_island_size = 0 # Just a plain integer!

    def dfs(i, j):
        # We need to declare both as nonlocal to modify them inside here
        nonlocal current_island_size 
        
        if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
            return
        
        grid[i][j] = 0
        current_island_size += 1 # This now updates the variable in the outer scope
        
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                current_island_size = 0 
                dfs(i, j)
                max_island = max(max_island, current_island_size)

    return max_island
```

### Summary Table

| Feature | Using a List `[0]` | Using `nonlocal` |
| :--- | :--- | :--- |
| **Mechanism** | Modifies a shared object in memory. | Points the variable name to the outer scope. |
| **Pros** | Works in older versions of Python (pre-3.0). | More readable and "standard" Python. |
| **Cons** | Feels a bit "hacky" to some. | Only works for nested functions (not global scope). |



Would you like me to explain how the **global** keyword differs from **nonlocal**, or are you good with the nested function scope?