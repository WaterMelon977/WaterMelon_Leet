# 1. Core idea
Scan the array and compact all non-zero elements to the front using a write pointer. After placing all non-zeros, fill the remaining positions with zeros. This preserves the relative order of non-zero elements.

# 2. Why optimal (time/space intuition)
Each element is processed once to shift non-zeros and once more to fill zeros, both linear passes. The operation is in-place and uses only a few variables. This satisfies the O(1) extra space requirement.

# 3. Python code
```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        last_nonZero_index = -1

        for i in range(n):
            if nums[i] != 0:
                last_nonZero_index += 1
                nums[last_nonZero_index] = nums[i]

        for i in range(last_nonZero_index + 1, n):
            nums[i] = 0
```

# 4. Time & Space: O(n) / O(1)

Time & Space: O(n) / O(1)