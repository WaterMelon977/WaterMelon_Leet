# Max Consecutive Ones III

[LeetCode Problem Link](https://leetcode.com/problems/max-consecutive-ones-iii/)

## Approach

- Use a non-shrinkable sliding window.
- Track the number of zeros in the window.
- Expand the window by moving `right`.
- If `nums[right] == 0`, increment the zero count.
- If zeros exceed `k`, move `left` forward by one step and reduce zero count if needed.
- Do not repeatedly shrink the window; just move both pointers forward.
- The window size `right - left + 1` always represents the maximum valid segment seen so far.

## Key Insight

Instead of shrinking the window with a loop, maintain the invariant that the window never grows beyond what `k` flips allow. When invalid, shift the entire window forward by moving `left` once.

## Why Efficient?

Both pointers move forward at most `n` times with no nested shrinking loop.

## Python Solution
```python
def longestOnes(self, nums: List[int], k: int) -> int:
    left = 0
    zeros = 0
    
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1
        
        if zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
    
    return len(nums) - left
```

## Complexity
- **Time:** O(n), each pointer moves forward at most once through the array.
- **Space:** O(1), only constant variables are used.