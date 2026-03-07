class Solution:
    def countSubstrings(self, s: str) -> int:
        def number_of_substrings(left, right):
            # expand while valid palindrome
            num=0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                num += 1 
                left -= 1
                right += 1
                
            return num
        ans=0
        for i in range(len(s)):
            ans += number_of_substrings(i,i)
            ans += number_of_substrings(i,i+1)
        return ans 
        