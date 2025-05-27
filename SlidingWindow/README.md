## 🔺 SLIDING WINDOW IN PYTHON - QUICK REVIEW

---

## ⚙️ BASIC SLIDING WINDOW TEMPLATE

### Fixed-size window:

```python
def fixed_window(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum
```

Used in: **Maximum Average Subarray I**

### Variable-size window:

```python
def variable_window(s):
    left = 0
    for right in range(len(s)):
        # Expand window [left, right]
        # Shrink when needed (based on condition)
        while invalid_condition:
            left += 1
        # update answer
```

Used in: **Minimum Size Subarray Sum**, **Longest Substring Without Repeating Characters**, etc.

---

## ⭐ Maximum Average Subarray I (Leetcode 643)

```python
def findMaxAverage(nums, k):
    curr_sum = sum(nums[:k])
    max_sum = curr_sum
    for i in range(k, len(nums)):
        curr_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, curr_sum)
    return max_sum / k
```

---

## 1 Max Consecutive Ones III (Leetcode 1004)

```python
def longestOnes(nums, k):
    left = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            k -= 1
        if k < 0:
            if nums[left] == 0:
                k += 1
            left += 1
    return right - left + 1
```

---

## 🔑 Longest Substring Without Repeating Characters (Leetcode 3)

```python
def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len
```

---

## 🔢 Longest Repeating Character Replacement (Leetcode 424)

```python
from collections import Counter

def characterReplacement(s, k):
    count = Counter()
    max_freq = 0
    left = 0
    for right in range(len(s)):
        count[s[right]] += 1
        max_freq = max(max_freq, count[s[right]])
        if (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1
    return right - left + 1
```

---

## 🌊 Minimum Size Subarray Sum (Leetcode 209)

```python
def minSubArrayLen(target, nums):
    left = 0
    total = 0
    min_len = float('inf')
    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            min_len = min(min_len, right - left + 1)
            total -= nums[left]
            left += 1
    return min_len if min_len != float('inf') else 0
```

---

## 🔍 Permutation in String (Leetcode 567)

```python
from collections import Counter

def checkInclusion(s1, s2):
    if len(s1) > len(s2): return False

    s1_count = Counter(s1)
    window_count = Counter(s2[:len(s1)])

    if s1_count == window_count:
        return True

    for i in range(len(s1), len(s2)):
        window_count[s2[i]] += 1
        window_count[s2[i - len(s1)]] -= 1
        if window_count[s2[i - len(s1)]] == 0:
            del window_count[s2[i - len(s1)]]
        if s1_count == window_count:
            return True
    return False
```

---

## 📌 NOTES

- Use **fixed window** when size is known (e.g., max average subarray)
- Use **sliding/variable window** when we need to **shrink** or **expand** dynamically (e.g., substring problems)
- Use a **set** for unique characters, **dict/Counter** for frequency counts
- Problems often involve: **max length**, **min length**, or **inclusion check**
- Pay attention to conditions inside the loop to shrink the window correctly
- Initialize `left = 0`, `right` expands in for loop

---
