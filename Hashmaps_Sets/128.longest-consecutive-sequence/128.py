class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0


        s=set(nums)
        max_total=1

        

        for num in s:
            if num-1 not in s:
                total=1
                while num+1 in s:
                    total+=1
                    num+=1
                max_total=max(max_total,total)
                
                
        
        return max_total