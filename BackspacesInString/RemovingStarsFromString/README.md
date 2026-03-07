# Remove Stars from a String

[LeetCode Problem Link](https://leetcode.com/problems/removing-stars-from-a-string/)

## Approach

- Use a stack (list) to build the resulting string.
- Traverse the string character by character.
- If the character is not '*', push it onto the stack.
- If the character is '*', pop the last character from the stack (removes the closest left character).
- Continue until the entire string is processed.
- Join the stack to form the final string.

## Why Efficient?

Each character is pushed and popped at most once, so the algorithm processes the string in a single pass.

## Python Solution
```python
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == '*':
                stack.pop()  # remove closest character to the left
            else:
                stack.append(char)
        return "".join(stack)
```

## Complexity
- **Time:** O(n) — each character is processed once.
- **Space:** O(n) — stack stores remaining characters after removals.