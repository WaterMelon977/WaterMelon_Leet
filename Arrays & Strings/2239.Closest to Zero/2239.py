class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest=nums[0]
        for i in range(1,len(nums)):
            if abs(closest)>abs(nums[i]):
                closest=nums[i]
            elif abs(closest)==abs(nums[i]):
                closest=max(closest,nums[i])
            
        return closest
        