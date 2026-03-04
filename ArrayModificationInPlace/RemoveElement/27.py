class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        Last_not_val_index = -1

        for i in range(n):
            if nums[i] != val:
                Last_not_val_index += 1
                nums[Last_not_val_index] = nums[i]
        return Last_not_val_index + 1
