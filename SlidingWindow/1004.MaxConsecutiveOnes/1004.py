class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        L=0
        n=len(nums)
        max_ones=0
        for R in range(n):
            if nums[R] == 0:
                k-=1
            while k<0:
                if nums[L] == 0:
                    k += 1
                L += 1
            max_ones= max(max_ones,R-L+1)
        return max_ones
            
            


def longestOnes(nums, k):
    left = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            k -= 1
        if k < 0:
            if nums[left] == 0:
                k += 1
            left += 1
    return right - left + 1        