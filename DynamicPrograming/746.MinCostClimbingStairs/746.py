class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        
        if n<=1:
            return 0

        dp=[0]*(n)
        dp[n-1]=cost[n-1]
        dp[n-2]=cost[n-2]

        for i in range (n-3,-1,-1):
            dp[i]=cost[i] + min(dp[i+1],dp[i+2])

        return min(dp[0],dp[1])


        

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        
        if n<=1:
            return 0

        
        prev=cost[n-1]
        cur=cost[n-2]

        for i in range (n-3,-1,-1):
            # dp[i]=cost[i] + min(dp[i+1],dp[i+2])
            prev,cur=cur ,cost[i]+ min(prev,cur)


        return min(prev,cur)