# Insert Leetcode Link
[https://leetcode.com/problems/longest-repeating-character-replacement/](https://leetcode.com/problems/longest-repeating-character-replacement/)

## Approach

- Use a **sliding window** with pointers `left` and `right`.
- Maintain a **frequency map** of characters inside the window.
- Track `max_freq`, the count of the **most frequent character** in the window.
- The number of replacements needed for the window is `window_size - max_freq`.
- If replacements needed **> k**, shrink the window from the left.
- Update the maximum valid window length while expanding `right`.

## Key Insight
A window is valid if we can replace all non-majority characters with the most frequent character:
`window_size - max_freq ≤ k`.

## Why efficient
The window expands and shrinks while each character is processed once, giving a linear-time solution.

## Python Solution

```python

def characterReplacement(s: str, k: int) -> int:
    freq = {}
    left = 0
    max_freq = 0
    max_length = 0

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1
        # track most frequent character in window
        max_freq = max(max_freq, freq[s[right]])
        # if window invalid, shrink it
        while (right - left + 1) - max_freq > k:
            freq[s[left]] -= 1 
            left += 1 
        max_length = max(max_length, right - left + 1)
    return max_length
```

## Complexity
Time: O(n) each character enters and leaves the sliding window at most once
Space: O(1) frequency map holds at most 26 uppercase letters
