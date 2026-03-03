# Two Sum II - Input Array Is Sorted

[Problem Link](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

Given a **1-indexed array** of integers `numbers` that is already sorted in **non-decreasing order**, find two numbers such that they add up to a specific target number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers `index1` and `index2`, each incremented by one, as an integer array `[index1, index2]` of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only **constant extra space**.

## Examples:

### Example 1:
- **Input:**
```plaintext
numbers = [2,7,11,15], target = 9
```
- **Output:**
```plaintext
[1, 2]
```
- **Explanation:** The sum of 2 and 7 is 9. Therefore, `index1 = 1`, `index2 = 2`. We return `[1, 2]`.

### Example 2:
- **Input:**
```plaintext
numbers = [2,3,4], target = 6
```
- **Output:**
```plaintext
[1, 3]
```
- **Explanation:** The sum of 2 and 4 is 6. Therefore, `index1 = 1`, `index2 = 3`. We return `[1, 3]`.

### Example 3:
- **Input:**
```plaintext
numbers = [-1,0], target = -1
```
- **Output:**
```plaintext
[1, 2]
```
- **Explanation:** The sum of -1 and 0 is -1. Therefore, `index1 = 1`, `index2 = 2`. We return `[1, 2]`.

--------------
# Solution


## 1. Core idea
Use two pointers on the sorted array: one at the start, one at the end. Compute their sum; if it equals target, return indices (1-based). If sum < target, move left forward; if sum > target, move right backward. Repeat until found.

## 2. Why optimal (time/space intuition)
Sorted order allows deterministic pointer movement without backtracking. Each step eliminates one candidate pair, so the array is scanned once. No extra data structures needed.

## 3. Python code

```python
class Solution:
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            if s < target:
                l += 1
            else:
                r -= 1
```

## 4. Time & Space: O(n) / O(1)