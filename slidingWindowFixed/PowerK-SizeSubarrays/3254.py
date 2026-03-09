
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # Edge case: If k is 1, every element is its own valid subarray
        if k == 1:
            return nums
            
        n = len(nums)
        result = []

        streak = 1

        for i in range(1, n):
            if nums[i] == nums[i-1] + 1:
                streak += 1
            else:
                streak = 1

            if i >= k - 1:
                if streak >= k:
                    result.append(nums[i])
                else:
                    result.append(-1)

        return result