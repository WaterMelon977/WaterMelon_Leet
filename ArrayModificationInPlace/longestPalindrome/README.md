# Longest Palindromic Substring

## LeetCode Problem Link
[Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

## Approach

A palindrome mirrors around its center.

- For every index `i`, treat it as a center and expand outward to check palindrome length.
- Handle two cases: odd-length (center = `i,i`) and even-length (center = `i,i+1`).
- Expand while left and right characters match.
- Track the longest palindrome boundaries seen so far.
- Return the substring using those stored indices.

## Why Efficient?
Instead of checking all substrings (`O(n^3)`), expanding from centers checks only possible palindromes, reducing work significantly.

## Python Solution
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand_from_center(left, right):
            # expand while valid palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        start = end = 0

        for i in range(len(s)):
            # odd length palindrome
            l1, r1 = expand_from_center(i, i)
            # even length palindrome
            l2, r2 = expand_from_center(i, i + 1)
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
        return s[start:end + 1]
```

## Complexity Analysis
- **Time:** `O(n^2)` — each center expansion may scan the string.
- **Space:** `O(1)` — only constant variables used to track indices.