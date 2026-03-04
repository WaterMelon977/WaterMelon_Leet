# Sort Array by Parity

[Problem Link](https://leetcode.com/problems/sort-array-by-parity/)

## Approach

- Use two pointers: `left` at start and `right` at end.
- Move `left` forward while elements are even.
- Move `right` backward while elements are odd.
- When `nums[left]` is odd and `nums[right]` is even, swap them.
- Continue until `left >= right`.

This partitions the array so all even numbers appear before odd numbers.

## Why Efficient?

It rearranges elements in a single pass using in-place swaps, avoiding extra memory.

## Python Solution
```python
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            # move left pointer until an odd number is found
            while left < right and nums[left] % 2 == 0:
                left += 1
            
            # move right pointer until an even number is found
            while left < right and nums[right] % 2 == 1:
                right -= 1
            
            # swap misplaced elements
            nums[left], nums[right] = nums[right], nums[left]

        return nums
```

```python
# Alternate Solution
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd_index_to_replace = 0
        n= len(nums)

        for i in range(n):
            if nums[i]%2 == 0:
                c= nums[odd_index_to_replace]
                
                nums[odd_index_to_replace] =nums[i]
                nums[i]=c
                odd_index_to_replace += 1 

        return nums
            



```

## Complexity
- **Time:** O(n) — each element is visited at most once by the two pointers.
- **Space:** O(1) — sorting is done in-place without extra data structures.