# LeetCode Problem: Longest Subarray of 1s After Deleting One Element

[Problem Link](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/)

## Approach

We need to find the longest subarray of 1s after deleting exactly one element.

This is equivalent to finding the longest window containing at most one 0.

- Use a sliding window with a non-shrinkable pattern: maintain a window where zeros ≤ 1.
- Expand the window with `right`. If we see a 0, increment the zero count.
- If zeros > 1, move `left` forward until only one zero remains.
- Since one element must be deleted, the effective length becomes `window_size - 1`.

## Key Insight

Deleting one element means we can tolerate one zero inside the window because deleting that zero connects the surrounding 1s.

## Why Efficient?

Each element enters and leaves the window at most once, so the sliding window processes the array in linear time.

## Python Solution
```python
class Solution:
    def longestSubarray(self, nums):
        left = 0
        zeros = 0
        max_length = 0
        
        for right in range(len(nums)):
            
            if nums[right] == 0:
                zeros += 1
            
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            max_length = max(max_length, right - left)
        
        return max_length
```

## Explanation of Tricky Part of Code
**Why `right - left` instead of `right - left + 1`?**
- The window allows one zero, but since we are required to delete one element, the effective length after deletion is `window_size - 1`.
- The window size is `(right - left + 1)`; subtracting one gives us `(right - left)` which accounts for this deletion.
- **Edge-case Handling:** If all elements are ones, we still delete one element; thus, answer becomes `len(nums) - 1`, which this formula naturally produces.

## Complexity Analysis
- **Time:** O(n) — each element is processed once by the sliding window.
- **Space:** O(1) — only counters and pointers are used.