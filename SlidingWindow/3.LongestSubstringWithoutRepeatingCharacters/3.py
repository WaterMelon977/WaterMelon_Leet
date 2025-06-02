class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length=0
        n=len(s)
        left=0
        sett=set()

        for right in range(n):
            while s[right] in sett:
                sett.remove(s[left])
                left+=1
            sett.add(s[right])
            max_length=max(max_length,right-left+1)
        return max_length



        