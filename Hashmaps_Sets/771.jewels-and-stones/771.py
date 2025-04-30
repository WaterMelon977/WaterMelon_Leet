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
