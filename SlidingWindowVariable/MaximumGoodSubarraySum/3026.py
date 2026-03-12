"""
LeetCode #3026: Maximum Good Subarray Sum

https://leetcode.com/problems/maximum-good-subarray-sum/
"""

class Solution:
    def maximumSubarraySum(self, nums, k):
        prefix = 0
        best_prefix = {}
        ans = float("-inf")

        for num in nums:
            prefix += num

            if num - k in best_prefix:
                ans = max(ans, prefix - best_prefix[num - k])

            if num + k in best_prefix:
                ans = max(ans, prefix - best_prefix[num + k])

            if num not in best_prefix:
                best_prefix[num] = prefix - num
            else:
                best_prefix[num] = min(best_prefix[num], prefix - num)

        return ans if ans != float("-inf") else 0
