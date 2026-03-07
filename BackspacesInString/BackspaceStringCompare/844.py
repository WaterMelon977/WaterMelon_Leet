class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack=[]
        t_stack=[]

        for ch in s:
            if ch == '#' and s_stack:
                s_stack.pop()
            elif ch != '#':
                s_stack.append(ch)

        for ch in t:
            if ch == '#' and t_stack:
                t_stack.pop()
            elif ch != '#':
                t_stack.append(ch)

        return s_stack == t_stack

        