# 55. Jump Game

[LeetCode link](https://leetcode.com/problems/jump-game/)

# LeetCode Link
[https://leetcode.com/problems/jump-game/](https://leetcode.com/problems/jump-game/)

## Approach

- Traverse the array while maintaining the **farthest index reachable** so far.
- At each index `i`, check if it is **reachable** (`i â¤ farthest`). If not, reaching this index is impossible.
- Update `farthest = max(farthest, i + nums[i])` to extend the reachable range.
- If at any point `farthest` reaches or passes the last index, return `True`.
- If the loop finishes without reaching the end, return `False`.

## Key Insight

You donât need to simulate jumps. Track the **maximum reachable boundary** as you scan the array.

## Why efficient

The greedy approach keeps only the farthest reachable index and processes each element once.

## Python Solution

```python id="c8t0k1"
class Solution:
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

## Explain any tricky part of the code

The check:
```python
def canJump(self, nums):
    if i > farthest:
```
does what?
> It means the current index lies **beyond the reachable boundary**, so we cannot land there, making the goal unreachable.
>
> Edge-case handling: if the array has length `1`, we are already at the last index, so the algorithm correctly returns `True`.

## Complexity
- Time: **O(n)** - each index is processed once.
- Space: **O(1)** - only a variable tracking the farthest reachable index is used.