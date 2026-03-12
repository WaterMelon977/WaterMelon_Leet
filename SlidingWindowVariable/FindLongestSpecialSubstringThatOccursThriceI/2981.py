"""
LeetCode #2981: Find Longest Special Substring That Occurs Thrice I

https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/
"""

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
            
            # try candidate lengths
            for x in range(max_run, 0, -1):
                count = 0
                for L in lengths:
                    if L >= x:
                        count += L - x + 1
                
                if count >= 3:
                    ans = max(ans, x)
                    break
        
        return ans
