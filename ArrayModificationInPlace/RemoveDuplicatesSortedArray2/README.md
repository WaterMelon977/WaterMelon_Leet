# Problem Link
[Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

## Approach

Since the array is sorted, duplicates appear consecutively.

- Maintain a write pointer `insert_pos` to place valid elements.
- Traverse the array with a read pointer `i`.
- Allow at most two occurrences of each number.
- If `insert_pos < 2` (first two elements) OR `nums[i] != nums[insert_pos - 2]`, copy the element to `insert_pos`.
- Increment `insert_pos` whenever an element is written.

## Why efficient
The algorithm scans the array once while modifying it in-place, avoiding extra memory and unnecessary shifts.

## Python Solution
```python
class Solution:
    def removeDuplicates(self, nums):
        # position where next valid element should be placed
        insert_pos = 0
        
        for i in range(len(nums)):
            # allow first two elements or ensure no more than 2 duplicates
            if insert_pos < 2 or nums[i] != nums[insert_pos - 2]:
                nums[insert_pos] = nums[i]
                insert_pos += 1
        
        return insert_pos
```

## Complexity
- **Time:** O(n) — single pass through the array
- **Space:** O(1) — modifies the array in-place without extra memory