class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        R,L=[],[]
        L.append(1)
        R.append(1)
        for i in range(1,len(nums)):
            L.append(L[i-1]*nums[i-1])
            R.append(R[i-1]*nums[len(nums)-i])
        
        for i in range(len(nums)):
            nums[i]=L[i]*R[len(nums)-i-1]

        return nums

            
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mult = 1
        r_mult = 1
        n = len(nums)
        l_arr = [0] * n
        r_arr = [0] * n
        
        for i in range(n): 
            j = -i -1
            l_arr[i] = l_mult
            r_arr[j] = r_mult
            l_mult *= nums[i]
            r_mult *= nums[j]

        return [l*r for l, r in zip(l_arr, r_arr)]            
        