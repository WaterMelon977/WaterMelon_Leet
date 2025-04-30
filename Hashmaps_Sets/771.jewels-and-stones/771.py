class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict={}
        
        for char in stones:
            if char not in dict:
                dict[char]=1
            else:
                dict[char]+=1
        total=0
        
        for char in jewels:
            if char in stones:
                total+=dict[char]
        
        return total

class Solution:
    def numJewelsInStones (self, jewels: str, stones: str) -> int:
        # O(n + m)
        s = set(jewels)
        count = 0
        for stone in stones:
            if stone in s:
                count += 1
        return count

# Time Complexity: O(n + m)
# Space Complexity: O(n)