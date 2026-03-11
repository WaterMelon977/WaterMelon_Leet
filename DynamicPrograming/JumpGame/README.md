# LeetCode Problem: Jump Game

**Link:** [https://leetcode.com/problems/jump-game/](https://leetcode.com/problems/jump-game/)

## Approach

- Traverse the array while maintaining the **farthest index reachable** so far.
- At each index `i`, check if it is **reachable** (`i ≤ farthest`). If not, reaching this index is impossible.
- Update `farthest = max(farthest, i + nums[i])` to extend the reachable range.
- If at any point `farthest` reaches or passes the last index, return `True`.
- If the loop finishes without reaching the end, return `False`.

## Key Insight

You don’t need to simulate jumps. Track the **maximum reachable boundary** as you scan the array.

## Why Efficient?

The greedy approach keeps only the farthest reachable index and processes each element once.

## Python Solution
```python
def canJump(self, nums):
    farthest = 0
    
    for i in range(len(nums)):
        if i > farthest:
            return False
        
        farthest = max(farthest, i + nums[i])
        
        if farthest >= len(nums) - 1:
            return True
    
    return True
```

## Explanation of Tricky Part of the Code
The check:
```python
def canJump(self, nums):
    ...
    if i > farthest:
```
does **not** mean that we are beyond reach; it indicates that the current index lies **beyond the reachable boundary**, so we cannot land there, making it impossible to reach the last index.

Edge-case handling: if the array has length `1`, we are already at the last index, so the algorithm correctly returns `True`.

## Complexity Analysis
- Time: **O(n)** — each index is processed once.
- Space: **O(1)** — only a variable tracking the farthest reachable index is used.