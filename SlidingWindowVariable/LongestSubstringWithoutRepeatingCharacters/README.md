# Longest Substring Without Repeating Characters

[LeetCode Problem Link](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## Approach

- Use a sliding window with two pointers `left` and `right`.
- Maintain a set (or hashmap) storing characters currently in the window.
- Expand `right` to include new characters.
- If a duplicate appears, move `left` forward while removing characters until the duplicate is removed.
- Update the maximum window length after each expansion.
- Continue until `right` reaches the end of the string.

## Key Insight

Instead of restarting the search whenever a duplicate appears, maintain a dynamic sliding window that always contains unique characters.

## Why Efficient?

Each character is added and removed from the window at most once, enabling a linear scan.

## Python Solution
```python
def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        # shrink window until duplicate removed
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

## Complexity Analysis
- **Time:** O(n), each character enters and leaves the sliding window at most once.
- **Space:** O(min(n, charset)), where set stores characters currently in the window.