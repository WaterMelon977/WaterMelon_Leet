class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj =nums[0]
        freq=1
        for num in nums[1:]:
            if num==maj:
                freq+=1
            else:
                freq-=1
                if freq<0:
                    freq=1
                    maj=num
        
        return maj
    # time complexity:O(n)

            


        