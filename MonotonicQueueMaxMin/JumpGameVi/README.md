**LeetCode Link**
[https://leetcode.com/problems/jump-game-vi/](https://leetcode.com/problems/jump-game-vi/)

**Approach**

* Define `dp[i]` as the **maximum score reachable when landing at index `i`**.
* Transition: from index `i`, we could have jumped from any `j` in `[i-k, i-1]`.
  So: `dp[i] = nums[i] + max(dp[j])` for `j ∈ [i-k, i-1]`.
* Naively computing the max each time costs `O(k)` per step → `O(nk)`.
* Use a **monotonic deque** to keep indices of `dp` values in **decreasing order** so the maximum is always at the front.
* Before computing `dp[i]`, remove indices outside the window (`i-k`).
* After computing `dp[i]`, remove smaller `dp` values from the back before inserting `i`.

**Key Insight**

We only need the **maximum `dp` value in the last `k` positions**, which can be maintained efficiently using a **monotonic deque**.

**Why efficient**

The deque maintains the sliding maximum in amortized `O(1)` time, avoiding the `O(k)` scan for each position.

**Python Solution**

```python
from collections import deque

class Solution:
    def maxResult(self, nums, k):
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        
        dq = deque([0])  # store indices of dp
        
        for i in range(1, n):
            
            # remove indices out of window
            while dq and dq[0] < i - k:
                dq.popleft()
            
            dp[i] = nums[i] + dp[dq[0]]
            
            # maintain decreasing deque
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
            
            dq.append(i)
        
        return dp[-1]
```

**Explain any tricky part of the code**

The deque stores indices whose `dp` values are in **decreasing order**.
When inserting `dp[i]`, we remove all smaller values at the back because they will **never be chosen as the maximum for future positions**.

Edge-case handling: indices that fall outside the jump range (`i - k`) are removed from the front before computing the current state.

**Complexity**

Time: **O(n)** — each index enters and leaves the deque at most once.
Space: **O(n)** — the `dp` array stores scores for each position.
