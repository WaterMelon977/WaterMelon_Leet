# Contains Duplicate II

[LeetCode Problem Link](https://leetcode.com/problems/contains-duplicate-ii/)

## Approach

- Use a hash map to store the last seen index of each number.
- Traverse the array with index `i`.
- If the number has been seen before, check the distance between indices.
  - If `i - last_index <= k`, return `True`.
  - Otherwise, update the index of that number in the map.
- If traversal finishes without finding such a pair, return `False`.

## Why Efficient?

Hash map allows constant-time lookup of previously seen indices, enabling a single-pass solution.

## Python Solution
```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}

        for i, num in enumerate(nums):
            if num in last_seen and i - last_seen[num] <= k:
                return True

            last_seen[num] = i

        return False
```
```python

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for i, num in enumerate(nums):
            # 1. Check if we found a duplicate within the current window
            if num in window:
                return True
            
            # 2. Add the current number to our window
            window.add(num)
            
            # 3. Maintain the window size: if the window is too large, 
            # remove the element that is more than k steps behind
            if len(window) > k:
                window.remove(nums[i - k])
                
        return False
```
## Complexity
- **Time:** O(n) — We traverse the array once and each lookup in the map is O(1).
- **Space:** O(n) — In the worst case, the hash map stores all elements.