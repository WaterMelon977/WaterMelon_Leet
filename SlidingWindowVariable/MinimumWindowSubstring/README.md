# 76. Minimum Window Substring

[LeetCode link](https://leetcode.com/problems/minimum-window-substring/)

# LeetCode Problem: Minimum Window Substring

[LeetCode Link](https://leetcode.com/problems/minimum-window-substring/)

## Approach

- Count the frequency of characters in `t` using a hashmap `need`.
- Use a **sliding window** with pointers `left` and `right`.
- Expand the window by moving `right`, updating counts in a `window` hashmap.
- Track how many required characters are satisfied using a `formed` counter.
- When `formed == required` (all characters covered), try shrinking the window from the left to find the **minimum valid window**.
- Update the smallest window length during this process.

## Key Insight

A window is valid when **all required character counts are satisfied**, not just when all characters appear once.

## Why Efficient?

Instead of checking every substring (`O(n^2)`), the sliding window expands and shrinks each pointer at most `n` times.

## Python Solution
```python
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = {}
        
        required = len(need)
        formed = 0
        
        left = 0
        min_len = float('inf')
        result = (0, 0)
        
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            
            if char in need and window[char] == need[char]:
                formed += 1
            
            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = (left, right)
                
                left_char = s[left]
                window[left_char] -= 1
                
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                
                left += 1
        
l, r = result
        return "" if min_len == float('inf') else s[l:r+1]
def explain_tricky_part():
description: |
dThe variable `formed` tracks how many characters meet their **required frequency**. We only increment it when:
a```
windo[c] == need[c]
def`
dnot when `window[c] > need[c]`. Edge-case handling: if no valid window exists, `min_len` stays `inf`, so we return an empty string.
def complexity():
type: explanation
time: O(n) â both pointers move at most ` n` times.
space: O(k) â hashmap stores counts for characters in `t`.