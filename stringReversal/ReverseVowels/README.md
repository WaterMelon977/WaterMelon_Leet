# Reverse Vowels of a String

[LeetCode Problem Link](https://leetcode.com/problems/reverse-vowels-of-a-string/)

## Approach

- Use two pointers: `left` at the start and `right` at the end.
- Convert string to a list because Python strings are immutable.
- Move `left` forward until a vowel is found.
- Move `right` backward until a vowel is found.
- Swap the vowels at `left` and `right`.
- Continue until `left >= right`, then join the list to return the string.

## Why Efficient?

Two pointers scan the string only once while swapping vowels in-place.

## Python Solution
```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        chars = list(s)

        left = 0
        right = len(chars) - 1

        while left < right:
            while left < right and chars[left] not in vowels:
                left += 1
            while left < right and chars[right] not in vowels:
                right -= 1
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        return "".join(chars)
```

## Complexity Analysis
- **Time:** O(n), each character is visited at most once by the two pointers.
- **Space:** O(n), conversion of string to list for in-place swaps.