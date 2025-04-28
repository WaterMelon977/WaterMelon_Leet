class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ls=[]
        i=0

        while i<len(nums):
            start_index= i
            if i== len(nums)-1:
                ls.append(f"{nums[i]}")
                return ls
            while nums[i+1] == nums[i]+1 :
                i=i+1
                if i== len(nums)-1:
                    break
            if i != start_index:
                s=f"{nums[start_index]}->{nums[i]}"
                ls.append(s)
            else:
                ls.append(f"{nums[i]}")
            i=i+1
        
        
        return ls


        