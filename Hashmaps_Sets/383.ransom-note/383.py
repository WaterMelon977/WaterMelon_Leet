class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_mag={}
        dict_rsm={}

        for char in magazine:
            if char in dict_mag:
                dict_mag[char]+=1
            else:
                dict_mag[char]=1
        

        for char in ransomNote:
            if char not in dict_mag:
                return False
            else:
                dict_mag[char]-=1
                if dict_mag[char]<0:
                    return False
        return True
    

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = Counter(magazine) # TC for Counter is O(n)

        for ch in ransomNote:
            if hashmap[ch] > 0:
                hashmap[ch]-=1
            else:
                return False
        return True