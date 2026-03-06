class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]
        for num in nums:
            count[num] += 1
        for i in range(len(nums)):
            if i >= count[0] + count[1]:
                nums[i] = 2
            elif i < count[0]:
                nums[i] = 0
            else:
                nums[i] = 1
