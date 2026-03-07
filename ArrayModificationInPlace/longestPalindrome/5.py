class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand_from_center(left, right):
            # expand while valid palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        start = end = 0

        for i in range(len(s)):
            # odd length palindrome
            l1, r1 = expand_from_center(i, i)

            # even length palindrome
            l2, r2 = expand_from_center(i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1

            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]