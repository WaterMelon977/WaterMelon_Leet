# Minimum Size Subarray Sum

[LeetCode Problem Link](https://leetcode.com/problems/minimum-size-subarray-sum/)

## Approach

- Use a sliding window with two pointers `left` and `right`.
- Expand the window by moving `right` and adding `nums[right]` to the current sum.
- Once the sum becomes ≥ target, try shrinking the window from the left to minimize its size.
- Update the minimum length each time the condition is satisfied.
- Continue shrinking until the sum becomes `< target`, then expand again.
- If no valid subarray is found, return 0.

## Key Insight

Since all numbers are positive, expanding the window always increases the sum and shrinking always decreases it, making the sliding window valid.

## Why Efficient?

Each element enters and leaves the window at most once, enabling a linear traversal.

## Python Solution
```python
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return 0 if min_length == float('inf') else min_length
```

## Complexity Analysis
- **Time:** O(n) — each element is added and removed from the window at most once.
- **Space:** O(1) — only constant variables are used for pointers and sums.