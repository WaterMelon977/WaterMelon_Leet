"""
LeetCode #438: Find All Anagrams in a String

https://leetcode.com/problems/find-all-anagrams-in-a-string/
"""

class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(p) > len(s):
            return []
        
        result = []
        p_count = [0] * 26
        window = [0] * 26
        
        for c in p:
            p_count[ord(c) - ord('a')] += 1
        
        left = 0
        
        for right in range(len(s)):
            window[ord(s[right]) - ord('a')] += 1
            
            if right - left + 1 > len(p):
                window[ord(s[left]) - ord('a')] -= 1
                left += 1
            
            if window == p_count:
                result.append(left)
        
        return result