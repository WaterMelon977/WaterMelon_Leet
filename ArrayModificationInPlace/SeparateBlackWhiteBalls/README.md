# Insert LeetCode Link
[Separate Black and White Balls](https://leetcode.com/problems/separate-black-and-white-balls/)

## Approach

**Goal:** Move all `0` (white balls) to the left and `1` (black balls) to the right.

- Traverse the string while tracking the next position where a white ball should go (`white_pos`).
- When encountering a `0` at index `i`, calculate swaps needed to move it to `white_pos`.
- Number of swaps required = `i - white_pos`.
- Add this to the total swaps and increment `white_pos`.

This effectively counts how many black balls each white ball must cross.

## Why Efficient?
Instead of simulating swaps, we count how far each white ball must move, achieving the result in one pass.

## Python Solution
```python
class Solution:
    def minimumSteps(self, s: str) -> int:
        swaps = 0
        white_pos = 0  # next position where a white ball should be

        for i in range(len(s)):
            if s[i] == '0':
                swaps += i - white_pos
                white_pos += 1

        return swaps
```

## Alternate

```python
class Solution:
    def minimumSteps(self, s: str) -> int:
        n=len(s)

        moves=0
        one_count=0

        for i in range(n):
            if s[i] == '1':
                one_count += 1
            else:
                moves += one_count
        return moves
```

## Complexity
- **Time:** O(n) — single traversal through the string.
- **Space:** O(1) — only constant variables used to track swaps and position.