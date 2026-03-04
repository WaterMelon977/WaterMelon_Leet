class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd_index_to_replace = 0
        n= len(nums)

        for i in range(n):
            if nums[i]%2 == 0:
                c= nums[odd_index_to_replace]
                
                nums[odd_index_to_replace] =nums[i]
                nums[i]=c
                odd_index_to_replace += 1 

        return nums
            


