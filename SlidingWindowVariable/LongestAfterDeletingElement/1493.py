class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        L = 0
        k = 1

        for R in range(len(nums)):
            if nums[R] == 0:
                k -= 1
            if k < 0:
                if nums[L] == 0:
                    k += 1
                L += 1
            
        
        return R-L