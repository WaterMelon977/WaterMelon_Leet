"""
LeetCode #239: Sliding Window Maximum

https://leetcode.com/problems/sliding-window-maximum/
"""

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        result = []
        
        for right in range(len(nums)):
            
            # maintain decreasing deque
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            
            dq.append(right)
            
            # remove indices outside window
            if dq[0] < right - k + 1:
                dq.popleft()
            
            # record max when window formed
            if right >= k - 1:
                result.append(nums[dq[0]])
        
        return result