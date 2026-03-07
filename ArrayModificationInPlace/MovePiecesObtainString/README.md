# Leetcode 2337

[Insert Leetcode Link](https://leetcode.com/problems/move-pieces-to-obtain-a-string/)

## Approach

- Remove `'_'` from both start and target. If the remaining sequences of `L` and `R` differ, return `False`.
- Use two pointers `i` and `j` to scan `start` and `target`.
- Skip `'_'` in both strings to align the next piece.
- If the aligned characters differ → return `False`.
- If the piece is `L`, ensure `i >= j` (because `L` can only move left).
- If the piece is `R`, ensure `i <= j` (because `R` can only move right).
- Continue until both strings are processed.

## Why efficient?

We only scan both strings once while skipping blanks, verifying movement constraints in a single pass.

## Python Solution
```python
def canChange(self, start: str, target: str) -> bool:
    # First ensure order of L and R is identical
    if start.replace('_', '') != target.replace('_', ''):
        return False

    i = j = 0
    n = len(start)

    while i < n and j < n:
        # skip blanks
        while i < n and start[i] == '_':
            i += 1
        while j < n and target[j] == '_':
            j += 1

        if i == n or j == n:
            break

        # check movement rules
        if start[i] == 'L' and i < j:
            return False
        if start[i] == 'R' and i > j:
            return False

        i += 1
        j += 1 
    
    return True
```


## Alternate Solution

```python

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        i, j = 0, 0

        while i < n or j < n:
            # 1. Skip underscores in start
            while i < n and start[i] == '_':
                i += 1
            
            # 2. Skip underscores in target
            while j < n and target[j] == '_':
                j += 1

            # 3. Check if one reached end and the other didn't
            if i == n or j == n:
                return i == n and j == n

            # 4. Pieces must be the same character
            if start[i] != target[j]:
                return False

            # 5. Movement constraints
            # L can only move left (i >= j)
            if start[i] == 'L' and i < j:
                return False
            # R can only move right (i <= j)
            if start[i] == 'R' and i > j:
                return False

            # Move to next characters
            i += 1
            j += 1

        return True
```

## Complexity 
- Time: O(n) single traversal of both strings 
- Space: O(1) only pointer variables used, no extra data structures