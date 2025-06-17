class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol, ret= [],[]

        def backtrack(x):
            if len(sol)==k:
                ret.append(sol[:])
                return 
            
            left=x
            used=len(sol)

            if left > k-used:
                backtrack(x-1)
            sol.append(x)
            backtrack(x-1)
            sol.pop()

        backtrack(n)
        return ret

            

# Time Complexity: O(n choose k)
# Space Complexity: O(n)
        