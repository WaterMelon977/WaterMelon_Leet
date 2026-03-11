"""
LeetCode #2516: Take K of Each Character From Left and Right

https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/
"""

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