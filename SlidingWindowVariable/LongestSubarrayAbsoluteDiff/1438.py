from collections import deque

class Solution:
    def longestSubarray(self, nums, limit):
        max_deque = deque()  # decreasing -> front is max
        min_deque = deque()  # increasing -> front is min
        
        left = 0
        max_length = 0
        
        for right in range(len(nums)):
            
            # maintain decreasing max deque
            while max_deque and nums[max_deque[-1]] < nums[right]:
                max_deque.pop()
            max_deque.append(right)
            
            # maintain increasing min deque
            while min_deque and nums[min_deque[-1]] > nums[right]:
                min_deque.pop()
            min_deque.append(right)
            
            # shrink window if invalid
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                
                if max_deque[0] == left:
                    max_deque.popleft()
                if min_deque[0] == left:
                    min_deque.popleft()
                
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length