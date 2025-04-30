class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        counter=Counter(s)
        countert = Counter(t)
        return counter==countert


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        counter=Counter(s)
       
        for char in t:
            if char not in counter:
                return False
            else:
                counter[char]-=1
                if counter[char]==0:
                    del counter[char]
                
        return counter == {} 