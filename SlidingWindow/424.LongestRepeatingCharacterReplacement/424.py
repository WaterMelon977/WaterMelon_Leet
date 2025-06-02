class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        max_freq=0
        n=len(s)
        count=Counter()
        longest=0


        for right in range(n):
            count[s[right]]+=1
            max_freq=max(max_freq,count[s[right]])
            while (right-left+1) - max_freq > k:
                count[s[left]]-=1
                left+=1
            longest=max(longest,right-left+1)
        return longest



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        counts = [0] * 26

        for r in range(len(s)):
            counts[ord(s[r]) - 65] += 1

            while (r - l + 1) - max(counts) > k:
                counts[ord(s[l]) - 65] -= 1
                l += 1

            longest = max(longest, (r - l + 1))

        return longest

# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        max_freq=0
        n=len(s)
        count=Counter()
        


        for right in range(n):
            count[s[right]]+=1
            max_freq=max(max_freq,count[s[right]])
            if (right-left+1) - max_freq > k:
                count[s[left]]-=1
                left+=1
            
        return right-left+1
