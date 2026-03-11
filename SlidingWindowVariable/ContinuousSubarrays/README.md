# 2762. Continuous Subarrays

[LeetCode link](https://leetcode.com/problems/continuous-subarrays/)

# LeetCode Problem: Continuous Subarrays

[Problem Link](https://leetcode.com/problems/continuous-subarrays/)

## Approach

A subarray is valid if `max(nums) - min(nums) <= 2`.

- Use a sliding window and maintain the current windowâs maximum and minimum using two monotonic deques.
- `maxDeque` keeps elements in decreasing order (`front = max of window`).
- `minDeque` keeps elements in increasing order (`front = min of window`).
- Expand the window with `right`. If the condition `max - min > 2` becomes invalid, shrink the window from the left.
- For each valid `right`, the number of valid subarrays ending at `right` is `right - left + 1`.

## Key Insight

For a valid sliding window, all subarrays ending at `right` and starting from `[left ... right]` are valid. Therefore, we add `right - left + 1` to the answer.

## Why Efficient?

Maintaining min and max using monotonic deques allows the window to update in **O(1)** amortized time, resulting in a linear scan.

## Python Solution
```python
from collections import deque

class Solution:
    def continuousSubarrays(self, nums):
        maxDeque = deque()
        minDeque = deque()
        
        left = 0
        result = 0
        
        for right in range(len(nums)):
            
            # Maintain decreasing max deque
            while maxDeque and nums[maxDeque[-1]] < nums[right]:
                maxDeque.pop()
            maxDeque.append(right)
            
            # Maintain increasing min deque
            while minDeque and nums[minDeque[-1]] > nums[right]:
                minDeque.pop()
            minDeque.append(right)
            
            # Shrink if invalid
            while nums[maxDeque[0]] - nums[minDeque[0]] > 2:
                if maxDeque[0] == left:
                    maxDeque.popleft()
                if minDeque[0] == left:
                    minDeque.popleft()
                
                left += 1
            
            result += right - left + 1
        
        return result
```

## Explanation of Tricky Part of Code
The line:
'this line: result += right - left + 1'
does the following:
to count all valid subarrays ending at 'right':
a) [right]
b) [left+1 ... right]
c) [left ... right]
every starting point inside this window forms a valid subarray because the window is maintained as valid.
'the shrinking process involves removing indices from deques when they leave the current window (index == left).'

## Complexity Analysis
- **Time:** O(n) — each index enters and leaves each deque once.
- **Space:** O(n) — deques may hold up to n indices in worst case.