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


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            m = (l + r) // 2
            
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m

        if nums[m] < target:
            return m + 1
        else:
            return m

# Time Complexity: O(log n)
# Space Complexity: O(1)
