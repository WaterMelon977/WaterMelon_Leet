"""
LeetCode #2779: Maximum Beauty of an Array After Applying Operation

https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/
"""

class Solution:
    def maximumBeauty(self, nums, k):
        nums.sort()
        
        left = 0
        max_beauty = 0
        
        for right in range(len(nums)):
            
            while nums[right] - nums[left] > 2 * k:
                left += 1
            
            max_beauty = max(max_beauty, right - left + 1)
        
        return max_beauty