class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ret,sol = [],[]

        def backtrack(i):
            if i ==n :
                ret.append(sol[:])
                return
            
            backtrack(i+1)
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

        backtrack(0)

        return ret

# Time Complexity: O(2^n)
# Space Complexity: O(n)
