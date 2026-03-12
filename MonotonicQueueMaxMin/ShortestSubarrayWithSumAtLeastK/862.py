"""
LeetCode #862: Shortest Subarray with Sum at Least K

https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
"""

class Solution:
    def shortestSubarray(self, nums, k):
        n = len(nums)

        # prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        minDeque = deque()
        ans = float("inf")

        for j in range(n + 1):

            # check if we found a valid subarray
            while minDeque and prefix[j] - prefix[minDeque[0]] >= k:
                ans = min(ans, j - minDeque.popleft())

            # maintain increasing prefix sums
            while minDeque and prefix[j] <= prefix[minDeque[-1]]:
                minDeque.pop()

            minDeque.append(j)

        return ans if ans != float("inf") else -1
