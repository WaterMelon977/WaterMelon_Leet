# Reverse String II

[LeetCode Problem Link](https://leetcode.com/problems/reverse-string-ii/)

## Approach

- Convert the string into a list because strings are immutable.
- Process the string in blocks of size `2k`.
- For each block, reverse the first `k` characters.
- Use slicing or two pointers to reverse from `i` to `i + k - 1`.
- Move to the next block by increasing index by `2k`.
- Join the list back into a string.

## Why Efficient?

We only traverse the string once and reverse segments in-place.

## Python Solution

```python
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)
        n = len(chars)

        for i in range(0, n, 2 * k):
            left = i
            right = min(i + k - 1, n - 1)

            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        return "".join(chars)
```

## Complexity Analysis
- **Time:** O(n) — each character is visited at most once during segment reversals.
- **Space:** O(n) — due to conversion of string to list for modification.