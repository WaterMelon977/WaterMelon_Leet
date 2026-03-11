# 2516. Take K of Each Character From Left and Right

[LeetCode link](https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/)

# LeetCode Link
[https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/](https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/)

## Approach

- Instead of directly choosing characters from the **left and right**, think in reverse: keep a **middle substring** that we do **not remove**.
- Count total occurrences of `'a'`, `'b'`, `'c'`. If any count `< k`, it is impossible â return `-1`.
- After removing characters from both ends, we must still leave at most `total[ch] - k` of each character in the middle substring.
- Use a **sliding window** to find the **longest valid middle substring** where each character count does not exceed its allowed limit.
- Expand the window with `right`. If any character count exceeds its allowed limit, shrink from the left.
- The answer is `n - longest_valid_window`.

## Key Insight

Taking characters from both ends is equivalent to **leaving the largest valid middle substring** whose character counts do not exceed `total[ch] - k`.

## Why efficient

Brute forcing left/right combinations is exponential, but converting it into **finding the longest valid substring** allows a linear sliding window solution.

## Python Solution
```python
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        from collections import Counter
        
        total = Counter(s)
        
        if total['a'] < k or total['b'] < k or total['c'] < k:
            return -1
        
        allowed = {
            'a': total['a'] - k,
            'b': total['b'] - k,
            'c': total['c'] - k
        }
        
        left = 0
        window = {'a':0,'b':0,'c':0}
        max_len = 0
        
        for right in range(len(s)):
            window[s[right]] += 1
            
            while window[s[right]] > allowed[s[right]]:
                window[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return len(s) - max_len
```

## Explain any tricky part of the code
The transformation is the key trick: instead of selecting characters from both ends, we **find the longest substring we can keep in the middle** such that removing the rest guarantees at least `k` of each character.

Edge-case handling: if any character occurs fewer than `k` times in the entire string, it's impossible to collect `k` from the ends, so return `-1`.

## Complexity
Time: **O(n)** â each character enters and leaves the sliding window at most once.
Space: **O(1)** â only counts for `'a'`, `'b'`, `'c'` are stored.