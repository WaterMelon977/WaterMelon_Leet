# 1. Core idea
Treat the array as a linked list where index → next index (`nums[i]`). Since numbers are in `[1, n]`, a duplicate creates a cycle. Use Floyd’s Tortoise and Hare to detect the cycle and find its entry point (the duplicate).

# 2. Why optimal (time/space intuition)
We cannot modify the array and must use constant extra space. Cycle detection gives linear time and `O(1)` space, which meets constraints optimally. No sorting or hashing needed.

# 3. Python code

```python
class Solution:
    def findDuplicate(self, nums):
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
```

# 4. Time & Space: `O(n)` / `O(1)`