class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        L,R=0,len(nums)-1
        ls=[]

        while L<=R:
            if abs(nums[L])>abs(nums[R]):
                ls.append(nums[L]**2)
                L+=1
            else:
                ls.append(nums[R]**2)
                R-=1
        
        ls.reverse()

        return ls




# time complexity: O(n)