class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        ls=[0]*n
        stack=[]
        stack.append((temperatures[0],0))
        for i in range(n):
            if not stack:
                stack.append((temperatures[i],i))

            else:
                while  stack and stack[-1][0] < temperatures[i]:
                    idx=stack[-1][1]
                    ls[idx]=i-idx
                    stack.pop()
                
                stack.append((temperatures[i],i))
        return ls
            

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = temperatures
        n = len(temps)
        answer = [0] * n
        stk = []

        for i, t in enumerate(temps):
            while stk and stk[-1][0] < t:
                stk_t, stk_i = stk.pop()
                answer[stk_i] = i - stk_i

            stk.append((t, i))
        return answer
        
# Time Complexity: O(n)
# Space Complexity: O(n)
            
class Solution:
    def dailyTemperatures(self, temps):
        results = [0] * len(temps)
        stack = []
        # UPVOTE !
        for i, temp in enumerate(temps):
            while stack and temps[stack[-1]] < temp:
                index = stack.pop()
                results[index] = i - index
            stack.append(i)

        return results

        