class Solution:
    def isValid(self, s: str) -> bool:
        start =[]
        
            

        for char in s:
            if char in  ('(' , '[', '{'):
                start.append(char)
            else:
                try:
                    opening=start.pop()
                except IndexError:
                    return False

                if opening == '(' and char != ')':
                    return False
                if opening == '[' and char != ']':
                    return False
                if opening == '{' and char != '}':
                    return False
        
        return not start

        
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in hash:
                if stack and stack[-1] == hash[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack