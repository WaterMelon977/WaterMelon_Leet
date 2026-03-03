# 1. Core idea
Sort the array. Fix two indices `i` and `j`, then solve the remaining 2-Sum problem using two pointers (`l`, `r`). Skip duplicates at every level to avoid repeated quadruplets. Collect valid combinations when the sum equals the target.

# 2. Why optimal (time/space intuition)
Sorting enables pruning and duplicate skipping. The outer two loops are **O(n²)**, and the inner two-pointer scan is **O(n)**, giving a total of **O(n³)**, which is optimal for *k=4* without extra heavy structures. Space complexity is only for output storage.

# 3. Python code
```python
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
                
                # Exhaust all L, R pairs with a while loop
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
```

# 4. Time & Space Complexity: O(n³) / O(1) (excluding output)