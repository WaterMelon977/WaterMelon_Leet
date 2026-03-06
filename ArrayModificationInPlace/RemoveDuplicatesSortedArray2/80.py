

class Solution:
    def removeDuplicates(self, nums):
        # position where next valid element should be placed
        insert_pos = 0
        
        for i in range(len(nums)):
            # allow first two elements or ensure no more than 2 duplicates
            if insert_pos < 2 or nums[i] != nums[insert_pos - 2]:
                nums[insert_pos] = nums[i]
                insert_pos += 1
        
        return insert_pos


