**LeetCode Link**
[https://leetcode.com/problems/permutation-in-string/](https://leetcode.com/problems/permutation-in-string/)

**Approach**

* We must check if **any permutation of `s1` appears as a substring in `s2`**.
* A permutation means the **character frequencies must match exactly**.
* Use a **fixed-size sliding window of length `len(s1)`** on `s2`.
* Maintain frequency arrays for `s1` and the current window in `s2`.
* Expand the window with `right`, updating the frequency.
* If the window size exceeds `len(s1)`, shrink from the left.
* If the frequency arrays match at any step, a permutation exists.

**Key Insight**

All permutations of a string share the **same frequency distribution**, so we only need to compare character counts.

**Why efficient**

Instead of generating all permutations (`O(n!)`), we check windows using constant-size frequency arrays.

**Python Solution**

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1 = [0] * 26
        count2 = [0] * 26
        
        for c in s1:
            count1[ord(c) - ord('a')] += 1
        
        left = 0
        
        for right in range(len(s2)):
            count2[ord(s2[right]) - ord('a')] += 1
            
            if right - left + 1 > len(s1):
                count2[ord(s2[left]) - ord('a')] -= 1
                left += 1
            
            if count1 == count2:
                return True
        
        return False
```

**Explain any tricky part of the code**

The arrays:

```
count1[26]
count2[26]
```

store frequencies of characters `'a'` to `'z'`.
Comparing these arrays checks whether the current window is a **permutation of `s1`**.

Edge-case handling: if `len(s1) > len(s2)`, it is impossible to form a permutation substring.

**Complexity**

Time: **O(n)** — each character in `s2` is processed once.
Space: **O(1)** — two fixed arrays of size 26.
