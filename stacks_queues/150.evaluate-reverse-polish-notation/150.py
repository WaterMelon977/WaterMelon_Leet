class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token =="+":
                x=stack.pop()
                y=stack.pop()
                stack.append(int(x+y))
            elif token =="*":
                x=stack.pop()
                y=stack.pop()
                stack.append(int(x*y))
            elif token =="-":
                x=stack.pop()
                y=stack.pop()
                stack.append(int(y-x))
            elif token =="/":
                x=stack.pop()
                y=stack.pop()
                stack.append(int(y/x))
            else:
                stack.append(int(token))

        return stack.pop()
    


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        hashset = {'+', '-', '*', '/'}
        stack = []
        for i in tokens:
            if i in hashset:
                first = stack.pop()
                second = stack.pop()
                if i == "+":
                    res = second + first
                    stack.append(res)
                elif i == "-":
                    res = second - first
                    stack.append(res)
                elif i == "*":
                    res = second * first
                    stack.append(res)
                elif i == "/":
                    res = int(second / first)
                    stack.append(res)
            else:
                stack.append(int(i))
        return stack.pop()