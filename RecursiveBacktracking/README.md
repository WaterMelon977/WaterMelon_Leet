Recursion
https://colab.research.google.com/drive/1qdUMlMleXTlObv-r-jdJj6tR2Vmes5AF?usp=sharing

# 🧠 Python Quick Review: Recursive Backtracking

Quick reference for solving Leetcode problems using backtracking in Python.

---

## 🔁 General Backtracking Template

```python
def backtrack(start, path):
    if base_case_condition:
        res.append(path[:])
        return
    for i in range(start, len(arr)):
        path.append(arr[i])
        backtrack(i + 1, path)
        path.pop()
```

---

## 🔹 Subsets

```python
def subsets(nums):
    res = []
    def backtrack(start, path):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return res
```

---

## 🔁 Permutations

```python
def permute(nums):
    res = []
    def backtrack(path, used):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used[i] = False
    backtrack([], [False] * len(nums))
    return res
```

---

## 🔢 Combinations

```python
def combine(n, k):
    res = []
    def backtrack(start, path):
        if len(path) == k:
            res.append(path[:])
            return
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()
    backtrack(1, [])
    return res
```

---

## 💰 Combination Sum

```python
def combinationSum(candidates, target):
    res = []
    def backtrack(start, path, total):
        if total == target:
            res.append(path[:])
            return
        if total > target:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, total + candidates[i])  # not i + 1 because reuse allowed
            path.pop()
    backtrack(0, [], 0)
    return res
```

---

## 📞 Letter Combinations of a Phone Number

```python
def letterCombinations(digits):
    if not digits:
        return []
    phone = {
        '2': 'abc', '3': 'def', '4': 'ghi',
        '5': 'jkl', '6': 'mno',
        '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    res = []
    def backtrack(index, path):
        if index == len(digits):
            res.append(''.join(path))
            return
        for char in phone[digits[index]]:
            path.append(char)
            backtrack(index + 1, path)
            path.pop()
    backtrack(0, [])
    return res
```

---

## 🧩 Generate Parentheses

```python
def generateParenthesis(n):
    res = []
    def backtrack(open_n, close_n, path):
        if len(path) == 2 * n:
            res.append(''.join(path))
            return
        if open_n < n:
            path.append('(')
            backtrack(open_n + 1, close_n, path)
            path.pop()
        if close_n < open_n:
            path.append(')')
            backtrack(open_n, close_n + 1, path)
            path.pop()
    backtrack(0, 0, [])
    return res
```

---

## 🔤 Word Search

```python
def exist(board, word):
    rows, cols = len(board), len(board[0])
    visited = set()

    def backtrack(r, c, i):
        if i == len(word):
            return True
        if (r < 0 or c < 0 or r >= rows or c >= cols or
            word[i] != board[r][c] or (r, c) in visited):
            return False

        visited.add((r, c))
        res = (backtrack(r+1, c, i+1) or backtrack(r-1, c, i+1) or
               backtrack(r, c+1, i+1) or backtrack(r, c-1, i+1))
        visited.remove((r, c))
        return res

    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True
    return False
```

---

## 📌 Notes

- Use **backtracking** to explore all potential solutions and undo the choice (pop) after exploring.
- For permutations, use a `used` boolean array.
- For subsets/combinations, control the index and avoid duplicates.
- Backtracking is essentially **DFS with undo (backtrack)** logic.
