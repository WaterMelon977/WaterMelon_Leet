class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        sett= set()
        n= len(nums)
        for i in range(min(n,k+1)):
            if nums[i] in sett:
                return True
            
            sett.add(nums[i])
        for i in range(k+1,n):
            sett.remove(nums[i-k-1])
            if nums[i] in sett:
                return True           
            sett.add(nums[i])
        return False

        
        
        