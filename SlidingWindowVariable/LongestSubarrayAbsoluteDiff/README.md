# LeetCode Problem: Longest Continuous Subarray with Absolute Diff Less Than or Equal to Limit

[Problem Link](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)

---

## Approach

- We need the longest subarray where `max(nums) - min(nums) <= limit`, which suggests a **sliding window**.
- As the window expands with `right`, we must efficiently track the **current maximum and minimum** values.
- Use two **monotonic deques**:

  - `maxDeque` → decreasing order to keep track of the maximum.
  - `minDeque` → increasing order to keep track of the minimum.
- For each `right`, push the element into both deques while maintaining their monotonic properties.
- If `maxDeque[0] - minDeque[0] > limit`, the window becomes invalid → move `left` forward and remove outdated elements from deques.
- Track the maximum window length during traversal.

---

## Key Insight

The difficulty is maintaining the **window's min and max in O(1)** time; monotonic deques allow us to keep the extremes at the front while supporting efficient updates.

---

## Why Efficient?

Instead of recomputing min and max each time (`O(n)` per window), monotonic deques maintain them in **amortized O(1)** time, enabling a full sliding window solution.

---

## Python Solution
```python
from collections import deque

class Solution:
    def longestSubarray(self, nums, limit):
        max_deque = deque()  # decreasing -> front is max
        min_deque = deque()  # increasing -> front is min
        
        left = 0
        max_length = 0
        
        for right in range(len(nums)):
            
            # maintain decreasing max deque
            while max_deque and nums[max_deque[-1]] < nums[right]:
                max_deque.pop()
            max_deque.append(right)
            
            # maintain increasing min deque
    while min_deque and nums[min_deque[-1]] > nums[right]:
    min_deque.pop()
    min_deque.append(right)
    
    # shrink window if invalid
    while nums[max_deque[0]] - nums[min_deque[0]] > limit:
    	
    	if max_deque[0] == left:
    		max_deque.popleft()
    	if min_deque[0] == left:
    		min_deque.popleft()
    	
    	left += 1
    
    max_length = max(max_length, right - left + 1)
    
return max_length
```
---
## Explain any tricky part of the code
*Monotonic deque maintenance*
When inserting a new element:
to `maxDeque`, remove all smaller elements from the back because they can never become the max again.
to `minDeque`, remove all larger elements from the back because they can never become the min again.
This guarantees that **the front always holds the current window's max/min**.
eEdge-case handling: When shrinking the window, we must remove deque elements whose **index equals `left`**, because they leave the window.
---
## Complexity
Time: **O(n)** — each element enters and leaves each deque at most once.
Space: **O(n)** — deques can store up to ` n` indices in worst case.