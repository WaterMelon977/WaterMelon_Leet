class Solution:
    def reverseVowels(self, s: str) -> str:
        # 1. Use a set for faster O(1) lookups
        vowels = set("aeiouAEIOU")
        c = list(s)
        L, R = 0, len(s) - 1

        while L < R:
            while L < R and c[L] not in vowels:
                L += 1
            
            while L < R and c[R] not in vowels:
                R -= 1

            # Swap the vowels
            c[L], c[R] = c[R], c[L]
            
            # Move pointers inward
            L += 1
            R -= 1

        return ''.join(c)