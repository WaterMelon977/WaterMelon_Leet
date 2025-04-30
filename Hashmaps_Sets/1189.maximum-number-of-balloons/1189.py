class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:        
        dict= defaultdict(int)

        for char in text:
            if char in "balon":
                dict[char]+=1
        
        b=dict['b']
        a=dict['a']
        l=dict['l']//2
        o=dict['o']//2
        n=dict['n']
        
        return min(b,a,l,o,n)


    
