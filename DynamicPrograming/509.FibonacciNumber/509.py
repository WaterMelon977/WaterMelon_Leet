# Simple Recursion
class Solution:
    def fib(self, n: int) -> int:
        if n <=1 :
            return n

        return self.fib(n-1)+self.fib(n-2)
    



# Top Down Memoization
# Time: O(n)
# Space: O(n)

class Solution:
    def fib(self, n: int) -> int:
        memo={0:0,1:1}

        def f(x):
            if x in memo:
                return memo[x]
            memo[x] = f(x-1)+f(x-2)
            return memo[x]
        
        return f(n)

        

# Bottom-Up / tabulation 
# Time: O(n)
# Space: O(n)
class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n 
        
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1

        for i in range(2,n+1):
            dp[i]= dp[i-1]+dp[i-2]
        
        return dp[n]        
      

# Constant Space
# time: O(n)
# space: O(1)
class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n 
        
        prev=0
        cur=1

        for _ in range(2,n+1):
            prev,cur=cur,prev+cur
        
        return cur
        