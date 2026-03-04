class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        last_nonZero_index = -1

        for i in range(n):
            if nums[i] != 0:
                last_nonZero_index += 1
                nums[last_nonZero_index] = nums[i]

        for i in range(last_nonZero_index + 1, n):
            nums[i] = 0
