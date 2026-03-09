class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,total=0,0
        n=len(nums)
        min_length=float('inf')

        for right in range(n):
            total+=nums[right]
            while total>=  target:
                min_length=min(min_length,right-left+1)
                total-=nums[left]
                left+=1
        return min_length if min_length != float('inf') else 0


        