# 1. Core idea
Use a write pointer `k`. Iterate through the array and copy every element that is not equal to `val` to position `k`, then increment `k`. This compacts all valid elements at the start of the array.

# 2. Why optimal (time/space intuition)
Each element is processed once, giving linear time. The operation is done in-place with a single pointer and no extra memory. This satisfies the problem’s requirement of modifying the array without extra space.

# 3. Python code

```python
class Solution:
    def removeElement(self, nums, val):
        k = 0
        for n in nums:
            if n != val:
                nums[k] = n
                k += 1
        return k
```

# 4. Time & Space: O(n) / O(1)