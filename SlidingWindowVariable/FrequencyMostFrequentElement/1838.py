class Solution:
    def maxFrequency(self, nums, k):
        nums.sort()
        
        left = 0
        window_sum = 0
        max_freq = 0
        
        for right in range(len(nums)):
            window_sum += nums[right]
            
            # cost to make all elements equal to nums[right]
            while nums[right] * (right - left + 1) - window_sum > k:
                window_sum -= nums[left]
                left += 1
            
            max_freq = max(max_freq, right - left + 1)
        
        return max_freq