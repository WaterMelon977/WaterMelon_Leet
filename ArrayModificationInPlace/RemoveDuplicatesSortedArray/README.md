# 1. Core idea
Use two pointers. One pointer `i` tracks the position to place the next unique element, while `j` scans the array. Whenever `nums[j]` differs from the previous element, place it at `nums[i]` and increment `i`.

# 2. Why optimal (time/space intuition)
The array is already sorted, so duplicates are adjacent and easy to skip in one pass. We overwrite duplicates in-place without extra memory. This achieves the required in-place modification with linear time.

# 3. Python code
```python
class Solution:
    def removeDuplicates(self, nums):
        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1
        return i
```

# 4. Time & Space: O(n) / O(1)