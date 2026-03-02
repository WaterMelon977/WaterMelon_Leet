class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n= len(nums)
        nums.sort()
        ans= nums[0]+nums[1]+nums[2]
        

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L=i+1
            R=n-1
            
            while  L<R :
                if nums[i] > 0 and nums[i]>target:
                    return ans
                add =nums[L] +nums[R] +nums[i]
                if add == target:
                    return target
                if  abs(add- target) < abs(ans -target):
                    ans=add 
                if add > target :
                    R-=1
                else:
                    L+=1
        return ans
                 

        