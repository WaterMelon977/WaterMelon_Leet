# 1. Core idea
Repeatedly replace the number with the sum of squares of its digits. If it becomes 1, it’s happy; if it enters a cycle, it’s not. Use Floyd’s cycle detection (slow/fast pointers) to detect a loop without extra space.

# 2. Why optimal (time/space intuition)
Each transformation reduces the number to a bounded range, so cycle detection is sufficient. Floyd’s algorithm avoids a hash set and uses constant space. Time is small and bounded due to digit contraction.

# 3. Python code

```python
class Solution:
    def isHappy(self, n):
        def f(x):
            s = 0
            while x:
                x, d = divmod(x, 10)
                s += d * d
            return s
        
        slow = n
        fast = f(n)
        while fast != 1 and slow != fast:
            slow = f(slow)
            fast = f(f(fast))
        return fast == 1
```

# 4. Time & Space: O(log n) / O(1)