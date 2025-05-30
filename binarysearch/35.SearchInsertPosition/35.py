class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L,R = 0,len(nums)-1
        while L<R:
            M=L+((R-L)//2)
            if target == nums[M]:
                return M
            elif nums[M] > target:
                R=M
            else:
                L=M+1
        if L != len(nums)-1:
            return L  
        else:
            if target > nums[-1]:
                return L+1
            else:
                return L