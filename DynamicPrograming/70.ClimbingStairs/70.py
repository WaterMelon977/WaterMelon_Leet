class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=2:
            return n
        prev=1
        cur=2

        for _ in range(3,n+1):
            prev,cur=cur,prev+cur
        
        return cur
        