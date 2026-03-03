# 1. Core idea
Use two pointers. Traverse `t` once while advancing pointer `i` in `s` whenever characters match. If `i` reaches the end of `s`, it is a subsequence.

# 2. Why optimal (time/space intuition)
Each character of `t` is processed once, and `s` is scanned implicitly through pointer movement. No backtracking or extra data structures required. This is the minimal linear scan solution.

# 3. Python code
```python
class Solution:
    def isSubsequence(self, s, t):
        i = 0
        for c in t:
            if i < len(s) and s[i] == c:
                i += 1
        return i == len(s)
```

# 4. Time & Space Complexity
- Time: O(n)
- Space: O(1)