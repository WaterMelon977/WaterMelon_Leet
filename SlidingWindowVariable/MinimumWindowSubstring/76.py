"""
LeetCode #76: Minimum Window Substring

https://leetcode.com/problems/minimum-window-substring/
"""


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