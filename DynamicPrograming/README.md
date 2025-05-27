# Dynamic Programming Interview Patterns

This document provides Python solutions and core algorithms for key Dynamic Programming problems from Leetcode. These are ideal for revising common DP patterns used in coding interviews.

---

## 1. Fibonacci Number

**Leetcode:** [https://leetcode.com/problems/fibonacci-number/](https://leetcode.com/problems/fibonacci-number/)

**Pattern:** DP with memoization or bottom-up tabulation

### Algorithm

- Base cases: F(0) = 0, F(1) = 1
- Recurrence: F(n) = F(n-1) + F(n-2)

### Python Code (Bottom-Up)

```python
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
```

---

## 2. Climbing Stairs

**Leetcode:** [https://leetcode.com/problems/climbing-stairs/](https://leetcode.com/problems/climbing-stairs/)

**Pattern:** DP, Fibonacci variation

### Algorithm

- Ways to reach step `n` is sum of ways to reach `n-1` and `n-2`
- Recurrence: dp\[n] = dp\[n-1] + dp\[n-2]

### Python Code (Bottom-Up)

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
```

---

## 3. Min Cost Climbing Stairs

**Leetcode:** [https://leetcode.com/problems/min-cost-climbing-stairs/](https://leetcode.com/problems/min-cost-climbing-stairs/)

**Pattern:** DP with minimal path sum

### Algorithm

- Start from index 2 and update minimum cost from either of the previous two steps.
- Recurrence: dp\[i] = cost\[i] + min(dp\[i-1], dp\[i-2])

### Python Code

```python
class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        for i in range(2, n):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return min(cost[-1], cost[-2])
```

---

## 4. House Robber

**Leetcode:** [https://leetcode.com/problems/house-robber/](https://leetcode.com/problems/house-robber/)

**Pattern:** DP, choose or skip

### Algorithm

- Either rob this house and add to dp\[i-2], or skip it and take dp\[i-1]
- Recurrence: dp\[i] = max(dp\[i-1], dp\[i-2] + nums\[i])

### Python Code

```python
class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]
```

---

## 5. Unique Paths

**Leetcode:** [https://leetcode.com/problems/unique-paths/](https://leetcode.com/problems/unique-paths/)

**Pattern:** Grid DP

### Algorithm

- Only right or down moves allowed
- Recurrence: dp\[i]\[j] = dp\[i-1]\[j] + dp\[i]\[j-1]

### Python Code

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
```

---

## 6. Maximum Subarray (Kadane's Algorithm)

**Leetcode:** [https://leetcode.com/problems/maximum-subarray/](https://leetcode.com/problems/maximum-subarray/)

**Pattern:** Kadane’s Algorithm (Greedy + DP)

### Algorithm

- At each step, either extend the current subarray or start a new one.
- Recurrence: current = max(num, current + num)

### Python Code

```python
class Solution:
    def maxSubArray(self, nums):
        max_sum = current = nums[0]
        for num in nums[1:]:
            current = max(num, current + num)
            max_sum = max(max_sum, current)
        return max_sum
```

---

## 7. Jump Game

**Leetcode:** [https://leetcode.com/problems/jump-game/](https://leetcode.com/problems/jump-game/)

**Pattern:** Greedy / DP

### Algorithm

- Keep track of the maximum reachable index.
- If at any index, max_reach < index, return False.

### Python Code

```python
class Solution:
    def canJump(self, nums):
        max_reach = 0
        for i, num in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + num)
        return True
```

---

## 8. Coin Change

**Leetcode:** [https://leetcode.com/problems/coin-change/](https://leetcode.com/problems/coin-change/)

**Pattern:** DP - Unbounded Knapsack

### Algorithm

- dp\[x] = min(dp\[x], dp\[x - coin] + 1)
- Initialize dp\[0] = 0, rest = inf

### Python Code

```python
class Solution:
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
```

---

## 9. Longest Increasing Subsequence

**Leetcode:** [https://leetcode.com/problems/longest-increasing-subsequence/](https://leetcode.com/problems/longest-increasing-subsequence/)

**Pattern:** DP

### Algorithm

- For each element, check all previous elements to update the LIS length.

### Python Code

```python
class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
```

---

## 10. Longest Common Subsequence

**Leetcode:** [https://leetcode.com/problems/longest-common-subsequence/](https://leetcode.com/problems/longest-common-subsequence/)

**Pattern:** DP - 2D table

### Algorithm

- If chars match: dp\[i]\[j] = 1 + dp\[i-1]\[j-1]
- Else: dp\[i]\[j] = max(dp\[i-1]\[j], dp\[i]\[j-1])

### Python Code

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]
```

---

These problems cover essential DP patterns: bottom-up tabulation, greedy strategies, and classic DP table fills. Mastering them is key to acing coding interviews involving dynamic programming.
