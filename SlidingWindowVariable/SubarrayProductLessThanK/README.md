# Subarray Product Less Than K

[LeetCode Problem Link](https://leetcode.com/problems/subarray-product-less-than-k/)

## Approach

- Use a sliding window with pointers `left` and `right`.
- Maintain the product of the current window.
- Expand the window by multiplying `nums[right]`.
- If the product becomes ≥ `k`, shrink the window from the left until the product becomes < `k`.
- At each step, the number of valid subarrays ending at `right` is `right - left + 1`.
- Add this count to the answer.

## Key Insight

For a valid window `[left…right]`, every subarray ending at `right` and starting between `left` and `right` is valid. So we can count multiple subarrays at once instead of enumerating them, reducing complexity from O(n²) to O(n).

## Why Efficient?

The sliding window ensures each element is multiplied and divided at most once.

## Python Solution
```python
def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    if k <= 1:
        return 0

    left = 0
    product = 1
    count = 0

    for right in range(len(nums)):
        product *= nums[right]

        while product >= k:
            product //= nums[left]
            left += 1

        count += right - left + 1

    return count```

## Complexity Analysis
- **Time:** O(n), each element enters and leaves the sliding window at most once.
- **Space:** O(1), only constant variables are used for pointers and product tracking.