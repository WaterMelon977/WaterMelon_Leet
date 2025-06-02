class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_total=sum(nums[:k])
        total=max_total
        for i in range (k,len(nums)):
            total += nums[i]
            total -= nums[i-k]
            max_total = max(max_total,total)
        return max_total/k

        