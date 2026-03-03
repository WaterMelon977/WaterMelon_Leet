class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        
        for i in range(n - 3):
            # Skip duplicate for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            for j in range(i + 1, n - 2):
                # Skip duplicate for j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                L = j + 1
                R = n - 1
                
                # You need a while loop here to exhaust all L, R pairs
                while L < R:
                    total = nums[i] + nums[j] + nums[L] + nums[R]
                    
                    if total == target:
                        ans.append([nums[i], nums[j], nums[L], nums[R]])
                        
                        # Move pointers and skip duplicates for L and R
                        while L < R and nums[L] == nums[L + 1]:
                            L += 1
                        while L < R and nums[R] == nums[R - 1]:
                            R -= 1
                        
                        L += 1
                        R -= 1
                    elif total < target:
                        L += 1
                    else:
                        R -= 1
        return ans