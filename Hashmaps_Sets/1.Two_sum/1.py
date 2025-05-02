class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, x in enumerate(nums):
            y = target - x
            if y in h:
                return [i, h[y]]
            else:
                h[x] = i