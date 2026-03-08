class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []

        for i in range(n - k + 1):
            is_consecutive = True

            for j in range(i, i + k - 1):
                if nums[j] + 1 != nums[j + 1]:
                    is_consecutive = False
                    break

            if is_consecutive:
                result.append(nums[i + k - 1])
            else:
                result.append(-1)

        return result