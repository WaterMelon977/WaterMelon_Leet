# Insert Leetcode Link
[Find the Power of K-Size Subarrays I](https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/)

## Approach

- For every subarray of size `k`, check whether it forms a strictly increasing sequence with difference = 1.
- Iterate starting index `i` from 0 to `n - k`.
- For each window `[i ... i+k-1]`, verify that `nums[j] + 1 == nums[j+1]` for all elements.
- If the condition holds for the entire window, the power is the last element of that subarray.
- Otherwise, append `-1`.
- Store results for all windows.

## Why Efficient?

Each window checks only `k` elements, giving a straightforward solution for the small constraints of this problem.

## Python Solution
```python
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []

        for i in range(n - k + 1):
            is_consecutive = True

            for j in range(i, i + k - 1):
                if nums[j] + 1 != nums[j + 1]:
                    is_consecutive = False
                    break

            if is_consecutive:
                result.append(nums[i + k - 1])
            else:
                result.append(-1)

        return result
```

## Complexity
- **Time:** O(n·k) — for each window, we check up to `k` elements.
- **Space:** O(n) — result array stores `n - k + 1` values.