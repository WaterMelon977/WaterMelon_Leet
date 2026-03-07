# Insert Leetcode Link
[Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)

## Approach

- Use two pointers starting from the end of both strings.
- Track how many characters must be skipped using `skip_s` and `skip_t`.
- Move pointer `i` in `s` backwards:
  - If `#` → increase skip count.
  - If skip count > 0 → skip character.
  - Stop when a valid character is found.
- Do the same for pointer `j` in `t`.
- Compare the valid characters at `i` and `j`.
  - If they differ → return `False`; continue until both strings finish.

## Why efficient

We simulate the backspace effect without building new strings, scanning each string once from the end.

## Python Solution
```python
def backspaceCompare(self, s: str, t: str) -> bool:
    i = len(s) - 1
    j = len(t) - 1

    skip_s = 0
    skip_t = 0

    while i >= 0 or j >= 0:
        
        # find next valid char in s
        while i >= 0:
            if s[i] == '#':
                skip_s += 1
                i -= 1
            elif skip_s > 0:
                skip_s -= 1
                i -= 1
            else:
                break
        
        # find next valid char in t
        while j >= 0:
            if t[j] == '#':
                skip_t += 1
                j -= 1;
            elif skip_t > 0:
                skip_t -= 1;
                j -= 1;
            else:
                break;
        
        # compare characters
        if i >= 0 and j >= 0 and s[i] != t[j]:
            return False;
        
df (i >= 0) != (j >= 0):
            return False;
default: 
i -=1; j -=1;
default: 
eturn True;
```
```python

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

        
```

## Complexity
- **Time:** O(n + m) each string is scanned once from the end.
- **Space:** O(1) no extra data structures used.