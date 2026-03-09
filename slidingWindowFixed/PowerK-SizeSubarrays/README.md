# Insert Leetcode Link
[Find the Power of K Size Subarrays I](https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/)

## Approach

We want each window of size `k` to be strictly consecutive increasing by 1.

- Maintain a sliding window and track `streak` = length of current consecutive chain.
- While iterating the array:
  - If `nums[i] == nums[i-1] + 1`, increase `streak`.
  - Otherwise, reset `streak = 1`.
- When `streak >= k`, the subarray ending at `i` is valid.
- Append `nums[i]` as the power, otherwise append `-1`.

## Why Efficient?

Instead of checking every window separately (`O(nk)`), we track consecutive runs once and reuse that information.

## Python Solution
```python

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # Edge case: If k is 1, every element is its own valid subarray
        if k == 1:
            return nums
            
        n = len(nums)
        result = []

        streak = 1

        for i in range(1, n):
            if nums[i] == nums[i-1] + 1:
                streak += 1
            else:
                streak = 1

            if i >= k - 1:
                if streak >= k:
                    result.append(nums[i])
                else:
                    result.append(-1)

        return result
```

## Complexity
- **Time:** O(n) — each element processed once while maintaining the consecutive streak.
- **Space:** O(1) — only constant variables used besides the output array.