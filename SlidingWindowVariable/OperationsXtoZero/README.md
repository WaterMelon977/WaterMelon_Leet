# LeetCode Problem: Minimum Operations to Reduce X to Zero

## [Problem Link](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/)

## Approach

- Removing elements from the **left or right** is equivalent to **keeping a middle subarray** whose sum is `total_sum - x`.
- Let `target = total_sum - x`. We need the **longest subarray with sum = target**.
- Use a **sliding window** since all numbers are positive.
- Expand `right` and keep a running `window_sum`.
- If `window_sum > target`, shrink the window from the left until it becomes ≤ target.
- Whenever `window_sum == target`, update the maximum subarray length. Final answer = `n - max_length`.

## Key Insight

Instead of deciding which elements to remove from both ends, convert the problem into **finding the longest subarray to keep**.

## Why Efficient?

Brute forcing left/right removals is exponential, but converting to a **longest subarray sum problem** allows a linear sliding window solution.

## Python Solution
```python
def minOperations(self, nums, x):
    total_sum = sum(nums)
    target = total_sum - x
    
    if target < 0:
        return -1
    
    left = 0
    window_sum = 0
    max_len = -1
    
    for right in range(len(nums)):
        window_sum += nums[right]
        
        while window_sum > target and left <= right:
            window_sum -= nums[left]
            left += 1
        
        if window_sum == target:
            max_len = max(max_len, right - left + 1)
    
    if max_len == -1:
        return -1
    
    return len(nums) - max_len
```

## Explanation of Tricky Part of the Code
The transformation: Instead of choosing elements to remove from both ends, we **keep the longest middle segment whose sum equals `total_sum - x`**. Removing everything else gives the minimum operations.

Edge-case handling: if `target < 0` or no subarray equals `target`, then operation is impossible so return `-1`.

## Complexity Analysis
- Time: **O(n)** — each element enters and leaves the sliding window at most once.
- Space: **O(1)** — only pointers and counters are used.