Insert Leetcode Link
https://leetcode.com/problems/palindromic-substrings/

Approach

Every palindrome expands around a center.

For each index i, consider two centers:

Odd length: center at (i, i)

Even length: center at (i, i+1)

Expand outward while characters match.

Each successful expansion corresponds to one palindromic substring.

Accumulate the count during expansion.

Why efficient
Instead of checking all substrings (O(n³)), we expand around centers and count palindromes in O(n²).

Python Solution

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def expand_from_center(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        
        total = 0
        
        for i in range(len(s)):
            total += expand_from_center(i, i)     # odd length
            total += expand_from_center(i, i + 1) # even length
        
        return total

Complexity
Time: O(n²) each center expansion may scan the string
Space: O(1) only constant variables used for counting and pointers