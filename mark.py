import re
import textwrap

def naive_text_to_md(text: str) -> str:
    lines = text.splitlines()
    md = []
    in_list = False

    for line in lines:
        line = line.rstrip()
        if not line:
            md.append("")
            in_list = False
            continue

        # Possible heading (all uppercase or ends with :)
        if line.isupper() or line.endswith(":"):
            md.append(f"## {line}")
            in_list = False
        # Numbered or bullet-like
        elif re.match(r"^\s*[-*•]|\d+[.)]\s", line):
            if not in_list:
                md.append("")  # space before list
            md.append(line)
            in_list = True
        else:
            # Just paragraph
            wrapped = textwrap.fill(line, width=88)
            md.append(wrapped)
            in_list = False

    return "\n".join(md)


# Test
plain = """**LeetCode Link**
[https://leetcode.com/problems/frequency-of-the-most-frequent-element/](https://leetcode.com/problems/frequency-of-the-most-frequent-element/)

**Approach**

* First **sort the array** so that we can increase smaller elements to match a larger element.
* Use a **sliding window** where the rightmost element `nums[right]` is the value we want all elements in the window to become.
* Maintain the **sum of the window** to calculate how many increments are required.
* To make all elements equal to `nums[right]`, required operations =
  `nums[right] * window_size - window_sum`.
* If required operations exceed `k`, shrink the window from the left until the cost becomes ≤ `k`.
* Track the maximum window size during the process.

**Key Insight**

When the array is sorted, the optimal strategy is always to **raise smaller elements to match the largest element in the window**.

**Why efficient**

Sorting takes `O(n log n)` and the sliding window runs in `O(n)`, avoiding brute-force checks of every subarray.

**Python Solution**

```python
class Solution:
    def maxFrequency(self, nums, k):
        nums.sort()
        
        left = 0
        window_sum = 0
        max_freq = 0
        
        for right in range(len(nums)):
            window_sum += nums[right]
            
            # cost to make all elements equal to nums[right]
            while nums[right] * (right - left + 1) - window_sum > k:
                window_sum -= nums[left]
                left += 1
            
            max_freq = max(max_freq, right - left + 1)
        
        return max_freq
```

**Explain any tricky part of the code**

**Cost formula**

To make every element in the window equal to `nums[right]`:

```
target_total = nums[right] * window_size
current_total = window_sum
operations_needed = target_total - current_total
```

If this exceeds `k`, we shrink the window.

Edge-case handling: sorting ensures `nums[right]` is always the **largest value in the window**, so we only perform **increment operations**, never decrements.

**Complexity**

Time: **O(n log n)** — sorting dominates, sliding window is linear.
Space: **O(1)** — only pointers and counters are used (ignoring sort space).
"""
print(naive_text_to_md(plain))