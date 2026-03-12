"""
LeetCode #1696: Jump Game VI

https://leetcode.com/problems/jump-game-vi/
"""

class Solution:
    def maxResult(self, nums, k):
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        # maxDeque
        maxDeque = deque([0])  # store indices of dp

        for i in range(1, n):

            # remove indices out of window
            while maxDeque and maxDeque[0] < i - k:
                maxDeque.popleft()

            dp[i] = nums[i] + dp[maxDeque[0]]

            # maintain decreasing deque
            while maxDeque and dp[maxDeque[-1]] <= dp[i]:
                maxDeque.pop()

            maxDeque.append(i)

        return dp[-1]

