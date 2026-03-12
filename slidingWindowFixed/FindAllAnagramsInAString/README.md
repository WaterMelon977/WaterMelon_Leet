**LeetCode Link**
[https://leetcode.com/problems/find-all-anagrams-in-a-string/](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

**Approach**

* We need all starting indices where a substring of `s` is an **anagram of `p`**.
* An anagram has the **same character frequency** as `p`.
* Use a **fixed-size sliding window** of length `len(p)`.
* Maintain frequency arrays for `p` and the current window in `s`.
* Expand the window with `right`, updating counts.
* If the window size exceeds `len(p)`, shrink from the left.
* Whenever the two frequency arrays match, record the starting index `left`.

**Key Insight**

All anagrams share the **same character frequency distribution**, so matching frequency arrays guarantees an anagram.

**Why efficient**

Instead of sorting each substring (`O(k log k)` per window), frequency arrays allow constant-time comparisons.

**Python Solution**

```python
class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(p) > len(s):
            return []
        
        result = []
        p_count = [0] * 26
        window = [0] * 26
        
        for c in p:
            p_count[ord(c) - ord('a')] += 1
        
        left = 0
        
        for right in range(len(s)):
            window[ord(s[right]) - ord('a')] += 1
            
            if right - left + 1 > len(p):
                window[ord(s[left]) - ord('a')] -= 1
                left += 1
            
            if window == p_count:
                result.append(left)
        
        return result
```

**Explain any tricky part of the code**

The window size is always kept equal to `len(p)`.
When the window grows larger:

```python
window[ord(s[left]) - ord('a')] -= 1
left += 1
```

removes the left character so the window remains fixed length.

Edge-case handling: if `len(p) > len(s)`, no anagram substring can exist.

**Complexity**

Time: **O(n)** — sliding window processes each character once.
Space: **O(1)** — two arrays of size 26 for character frequencies.
