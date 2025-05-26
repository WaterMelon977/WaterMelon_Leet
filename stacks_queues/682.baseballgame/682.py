class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk=[]
        for item in operations:
            if item == "C":
                stk.pop()
            elif item == "D":
                x=stk[-1]
                stk.append(2*x)
            elif item =="+":
                x=stk[-1]
                y=stk[-2]
                stk.append(x+y)
            else:
                stk.append(int(item))

        return sum(stk)
    
    # time O(n) space: O(n)