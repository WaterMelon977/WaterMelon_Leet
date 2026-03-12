**LeetCode Link**
[https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/)

**Approach**

* Since the array may contain **negative numbers**, a normal sliding window does not work.
* Use **prefix sums** where `prefix[i]` represents the sum of the first `i` elements.
* We want the smallest `j - i` such that:
  `prefix[j] - prefix[i] ≥ k`.
* Maintain a **monotonic deque of prefix indices** where prefix values are **increasing**.
* For each new prefix `prefix[j]`:

  * While the difference with the **front of the deque** satisfies the condition (`≥ k`), update the minimum length and pop from the front.
  * While the **current prefix is smaller than the back**, pop from the back to maintain increasing order.
* Push the current index into the deque.

**Key Insight**

The deque maintains candidate starting points with **increasing prefix sums**, allowing us to efficiently find valid subarrays and discard worse candidates.

**Why efficient**

Each prefix index enters and leaves the deque at most once, giving a linear-time algorithm.

**Python Solution**

```python
from collections import deque

class Solution:
    def shortestSubarray(self, nums, k):
        n = len(nums)
        
        # prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        dq = deque()
        ans = float('inf')
        
        for j in range(n + 1):
            
            # check if we found a valid subarray
            while dq and prefix[j] - prefix[dq[0]] >= k:
                ans = min(ans, j - dq.popleft())
            
            # maintain increasing prefix sums
            while dq and prefix[j] <= prefix[dq[-1]]:
                dq.pop()
            
            dq.append(j)
        
        return ans if ans != float('inf') else -1
```

**Explain any tricky part of the code**

The second loop maintains **monotonic prefix sums**:

```python
while dq and prefix[j] <= prefix[dq[-1]]:
    dq.pop()
```

If a later prefix is **smaller**, it is always a better starting point for future subarrays.

Edge-case handling: if no valid subarray exists, `ans` remains `inf`, so the function returns `-1`.

**Complexity**

Time: **O(n)** — each prefix index enters and leaves the deque once.
Space: **O(n)** — prefix array and deque storage.
