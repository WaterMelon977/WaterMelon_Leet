https://colab.research.google.com/drive/1eN3A8i88C641wlIdwTeahwoQLcthCGtD?usp=sharing

## 🔍 BINARY SEARCH METHODS & PATTERNS IN PYTHON

---

### ⚙️ Template 1: Basic Binary Search

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

Used in: `Binary Search`, `Search Insert Position`, `Search in Rotated Sorted Array`

---

### ⚖️ Template 2: Binary Search with Condition (e.g., finding boundary)

```python
def condition(mid):
    # define condition to narrow the search
    return True or False

def binary_search_custom(n):
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left
```

Used in: `First Bad Version`, `Koko Eating Bananas`, `Find Minimum` etc.

---

### ➡️ Search Insert Position (Leetcode 35)

```python
def searchInsert(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
```

---

### 🌟 First Bad Version (Leetcode 278)

```python
def firstBadVersion(n):
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left
```

---

### ■ Valid Perfect Square (Leetcode 367)

```python
def isPerfectSquare(num):
    left, right = 1, num
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == num:
            return True
        elif mid * mid < num:
            left = mid + 1
        else:
            right = mid - 1
    return False
```

---

### 🗺️ Search a 2D Matrix (Leetcode 74)

```python
def searchMatrix(matrix, target):
    if not matrix: return False
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    while left <= right:
        mid = (left + right) // 2
        val = matrix[mid // n][mid % n]
        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
```

---

### ♻️ Find Minimum in Rotated Sorted Array (Leetcode 153)

```python
def findMin(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]
```

---

### 🤕 Search in Rotated Sorted Array (Leetcode 33)

```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:  # Left half sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
```

---

### 🥜 Koko Eating Bananas (Leetcode 875)

```python
def minEatingSpeed(piles, h):
    def can_eat_all(k):
        return sum((pile + k - 1) // k for pile in piles) <= h

    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        if can_eat_all(mid):
            right = mid
        else:
            left = mid + 1
    return left
```

---

## 📌 NOTES & TIPS

- Binary search is O(log n) and optimal for sorted/monotonic data
- Use `while left <= right` for exact match
- Use `while left < right` for finding minimum/boundary
- Carefully handle integer overflow (Python handles large ints safely)
- 2D matrix can be treated like 1D array in binary search
- Good candidates: sorted arrays, rotated arrays, optimization with conditions
