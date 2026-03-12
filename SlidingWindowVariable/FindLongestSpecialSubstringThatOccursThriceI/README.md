# 2981. Find Longest Special Substring That Occurs Thrice I

[LeetCode link](https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/)

# LeetCode Problem: Find Longest Special Substring Occurring Thrice

**Link:**
[https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/](https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/)

## Approach

- A **special substring** consists of the **same character repeated** (e.g., `"aaa"`, `"bbbb"`).
- First, compress the string into **runs of consecutive identical characters** and record their lengths.
- For each character `'a'â'z'`, collect the lengths of its runs.
- For a run of length `L`, it contributes substrings of length `1..L`. A substring of length `x` appears `(L - x + 1)` times inside that run.
- We need a length `x` such that the total occurrences across runs of that character are **â¥ 3**.
- For each character, check candidate lengths derived from its run lengths (largest first) and track the maximum valid `x`.

## Key Insight

If a run has length `L`, it contributes **multiple overlapping substrings**, so one run can already produce up to `L - x + 1` occurrences.

## Why Efficient?

Instead of generating all substrings (`O(n^2)`), we analyze **run lengths**, reducing the work to linear preprocessing plus small per-character checks.

## Python Solution
```python
class Solution:
    def maximumLength(self, s: str) -> int:
        from collections import defaultdict
        
        runs = defaultdict(list)
        
        # build runs
        i = 0
        n = len(s)
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs[s[i]].append(j - i)
            i = j
        
        ans = -1
        
        # check each character
        for char in runs:
            lengths = runs[char]
            
            max_run = max(lengths)
            
            # try candidate lengths from largest to smallest
            for x in range(max_run, 0, -1):
                count = 0
                for L in lengths:
                    if L >= x:
                        count += L - x + 1
                if count >= 3:
                    ans = max(ans, x)
                    break
        
        return ans
```

## Explanation of Tricky Part of Code:
The occurrence count:
```python
L - x + 1

```
means how many substrings of length x can be formed from a run of length L.

Example:
```python
run = "aaaa" (L=4)
x=2 → substrings: aa, aa, aa → 3 occurrences

```

Edge-case handling: if no substring appears at least three times, the answer remains -1.

**Complexity**

Time: O(n + 26·n) worst case (small constant since only 26 characters).
Space: O(n) for storing run lengths.
