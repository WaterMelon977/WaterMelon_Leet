# Insert Leetcode Link
[Sort Colors](https://leetcode.com/problems/sort-colors/)

## Approach

Use the Dutch National Flag algorithm with three pointers: `low`, `mid`, and `high`.

- `low` tracks where the next 0 should go.
- `high` tracks where the next 2 should go.
- Traverse using `mid`.

**Algorithm steps:**
1. If `nums[mid] == 0`, swap with `low`, increment both.
2. If `nums[mid] == 2`, swap with `high`, decrement `high` (do not move `mid` yet).
3. If `nums[mid] == 1`, just move `mid`.

## Why it is efficient
Single pass with constant extra space while placing 0s, 1s, and 2s in correct partitions.

## Python Solution
```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Three pointers for Dutch National Flag algorithm
        low = 0        # position for next 0
        mid = 0        # current element
        high = len(nums) - 1  # position for next 2

        while mid <= high:
            if nums[mid] == 0:
                # place 0 at correct position
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # 1 is already in correct middle region
                mid += 1
            else:  # nums[mid] == 2:
                # place 2 at the end
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                # do not increment mid because swapped value must be checked
```

## Complexity Analysis
dTime: O(n) — each element is processed once in a single traversal.
Space: O(1) — in-place sorting using constant pointers.