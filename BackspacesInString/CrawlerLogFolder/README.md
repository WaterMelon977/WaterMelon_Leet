# Insert Leetcode Link
[https://leetcode.com/problems/crawler-log-folder/](https://leetcode.com/problems/crawler-log-folder/)

## Approach

- Maintain a variable `depth` representing the current folder depth.
- Iterate through each log entry.
- If log is `"../"` → move to parent folder → `depth -= 1` (but not below 0).
- If log is `"./"` → stay in current folder → do nothing.
- Otherwise (`"x/"`) → move into a child folder → `depth += 1`.

Return `depth`, which equals the minimum operations needed to return to the main folder.

## Why efficient?
We simulate the folder navigation using a single counter instead of an actual stack, making the solution linear and memory efficient.

## Python Solution
```python
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for log in logs:
            if log == "../":
                if depth > 0:
                    depth -= 1
            elif log == "./":
                continue
            else:
                depth += 1
        return depth
```

## Complexity
- **Time:** O(n) — iterate through all log operations once.
- **Space:** O(1) — only a counter is used to track directory depth.