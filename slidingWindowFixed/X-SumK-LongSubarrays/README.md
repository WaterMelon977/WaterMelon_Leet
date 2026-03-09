# Find X Sum of All K-Length Subarrays

[LeetCode Problem Link](https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/)

## Approach

- Use a sliding window of size `k` and maintain a frequency map of elements in the window.
- For the first window, build the frequency map using `Counter`.
- For each subsequent window:
  - Add the new element entering the window.
  - Decrease the frequency of the element leaving the window and remove it if the count becomes zero.
- Convert the frequency map into `(value, frequency)` pairs.
- Sort pairs by frequency descending, and if tied, by value descending.
- Take the top `x` elements and compute `value * frequency` for each, summing them to get the **x-sum**.

## Key Insight

Instead of rebuilding the frequency map for every window, maintain it with sliding window updates. This reduces repeated work and keeps the solution efficient.

## Why Efficient?

The sliding window ensures we update frequencies in constant time per step, while sorting only the unique elements of the window.

## Python Solution
```python
from collections import Counter

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        result = []

        for i in range(n - k + 1):
            if i == 0:
                freq = Counter(nums[:k])
            else:
                # add new element entering window
                freq[nums[i+k-1]] += 1
                # remove element leaving window
                freq[nums[i-1]] -= 1
                if freq[nums[i-1]] == 0:
                    del freq[nums[i-1]]
            # sort by frequency desc, value desc
            sorted_items = sorted(freq.items(), key=lambda item: (-item[1], -item[0]))
            total = 0
            count = 0
            for value, f in sorted_items:
                total += value * f
                count += 1
                if count == x:
                    break
            result.append(total)
        return result```

## Complexity Analysis 
- **Time:** O(n · u log u), where `u` is the number of unique elements in a window (sorting them each step).
- **Space:** O(k), as the frequency map stores at most `k` elements in the window.