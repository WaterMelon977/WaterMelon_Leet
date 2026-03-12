**LeetCode Link**
[https://leetcode.com/problems/sliding-window-maximum/](https://leetcode.com/problems/sliding-window-maximum/)

**Approach**

* We need the **maximum element in every window of size `k`**.
* Use a **monotonic deque** that stores indices of elements in **decreasing order of values**.
* When expanding the window (`right`):

  * Remove elements from the back while their value is **smaller than the current element**, since they can never become the maximum.
* Remove elements from the front if they fall **outside the current window** (`index < right - k + 1`).
* The **front of the deque always holds the index of the current window’s maximum**.
* Once the first window is formed (`right ≥ k-1`), record the maximum.

**Key Insight**

Maintain a **decreasing deque** so the maximum element of the current window is always at the **front**.

**Why efficient**

Each element enters and leaves the deque at most once, giving a linear-time solution.

**Python Solution**

```python
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        result = []
        
        for right in range(len(nums)):
            
            # maintain decreasing deque
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            
            dq.append(right)
            
            # remove indices outside window
            if dq[0] < right - k + 1:
                dq.popleft()
            
            # record max when window formed
            if right >= k - 1:
                result.append(nums[dq[0]])
        
        return result
```

**Explain any tricky part of the code**

The deque stores **indices**, not values, so we can check if elements fall **outside the window** when `right` moves forward.

When a larger element enters the window, smaller elements at the back are removed because they **can never become the maximum again**.

Edge-case handling: results are recorded only after the first full window forms (`right ≥ k-1`).

**Complexity**

Time: O(n) — each element is pushed and popped from the deque at most once.
Space: O(k) — the deque stores indices of at most `k` elements.
