"""
LeetCode #2762: Continuous Subarrays

https://leetcode.com/problems/continuous-subarrays/
"""

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        L, totalSubArrays = 0, 0
        n = len(nums)
        minDeque = deque()
        maxDeque = deque()

        for R in range(n):
            while maxDeque and nums[R] > maxDeque[-1]:
                maxDeque.pop()
            maxDeque.append(nums[R])

            while minDeque and nums[R] < minDeque[-1]:
                minDeque.pop()
            minDeque.append(nums[R])

            while maxDeque[0] - minDeque[0] > 2:
                if maxDeque[0] == nums[L]:
                    maxDeque.popleft()
                elif minDeque[0] == nums[L]:
                    minDeque.popleft()
                L += 1
            totalSubArrays += R - L + 1
        return totalSubArrays
