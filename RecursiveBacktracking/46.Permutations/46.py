class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n= len(nums)
        sol,ret =[],[]

        def backtrack():
            if len(sol)==n:
                ret.append(sol[:])
            
            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtrack()
                    sol.pop()
            
        backtrack()
        return ret

# Time Complexity: O(n!)
# Space Complexity: O(n)        