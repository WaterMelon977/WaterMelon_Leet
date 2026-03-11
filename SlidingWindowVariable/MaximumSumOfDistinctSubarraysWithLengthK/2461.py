class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        seen = set()
        L = 0
        max_sum = 0
        total = 0

        for R in range(len(nums)):
            # Shrink the window if the current number is a duplicate 
            # OR if adding the current number makes the window bigger than k
            while nums[R] in seen or (R - L + 1) > k:
                seen.remove(nums[L])
                total -= nums[L]
                L += 1
            
            # Now the window is guaranteed to be valid, so we add the new element
            seen.add(nums[R])
            total += nums[R]

            # If the window is exactly size k, check if it's our new max
            if R - L + 1 == k:
                max_sum = max(max_sum, total)
        
        return max_sum