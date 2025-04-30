## 🧮 DICTIONARY METHODS (`dict`)

### `dict.get(key, default)`
Returns the value if key exists, else default.
```python
freq = {}
freq.get('a', 0)  # 0
```

### `dict[key] = value`
Insert or update key-value pair.
```python
freq['a'] = 1
```

### Counting occurrences manually
```python
for c in "aabbc":
    freq[c] = freq.get(c, 0) + 1
# {'a': 2, 'b': 2, 'c': 1}
```

### `in` keyword
```python
"a" in freq  # True
```

### `dict.keys()`, `dict.values()`, `dict.items()`
```python
for key in freq.keys(): pass
for val in freq.values(): pass
for k, v in freq.items(): pass
```

### `collections.Counter`
```python
from collections import Counter
count = Counter("aabbc")
# Counter({'a': 2, 'b': 2, 'c': 1})
count['a']  # 2
```

---

## ⛏️ SET METHODS (`set`)

### Creating a set
```python
s = set([1, 2, 3])
```

### `in` keyword
```python
2 in s  # True
```

### `add()` and `remove()`
```python
s.add(4)
s.remove(3)
```

### Set operations
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1 & set2     # {3} (intersection)
set1 | set2     # {1, 2, 3, 4, 5} (union)
set1 - set2     # {1, 2} (difference)
```

---

## 🔃 SORTING AND GROUPING

### `sorted()` with key
```python
sorted(['abc', 'bca', 'cab'], key=sorted)
# ['abc', 'bca', 'cab']  (group anagrams logic)
```

### `defaultdict(list)`
```python
from collections import defaultdict
anagrams = defaultdict(list)
anagrams['a'].append("apple")
# {'a': ['apple']}
```

---

## 🔢 MATH + COUNTING TOOLS

### `max()` with key
```python
counts = {'a': 3, 'b': 5, 'c': 1}
max(counts, key=counts.get)  # 'b'
```

### Majority Element (Boyer-Moore style)
No library function, but common trick is count tracking using dictionary or variable.

---

## 📚 LIST + ENUMERATION

### `enumerate()`
```python
for idx, val in enumerate([10, 20, 30]):
    print(idx, val)  # (0,10), (1,20), ...
```

### `zip()`
```python
for a, b in zip("abc", "123"):
    print(a, b)  # (a,1), (b,2), (c,3)
```

---

## 🧪 UTILITY TRICKS

### `all()` / `any()`
```python
all([True, True])  # True
any([False, True]) # True
```

### Convert string to frequency count
```python
Counter("balloon")
# Counter({'l': 2, 'o': 2, 'b': 1, 'a': 1, 'n': 1})
```

### Checking character sufficiency (Ransom Note)
```python
from collections import Counter
note = Counter("aa")
magazine = Counter("aab")
note - magazine  # Counter() (empty => possible)
```

---

## 🧩 2D GRID / SUDOKU HELPERS

### Check for duplicates using set
```python
seen = set()
for r in board:
    for c in r:
        if c in seen:
            # duplicate
            pass
        seen.add(c)
```

### Coordinate-based set logic (for rows, cols, boxes)
```python
seen = set()
for r in range(9):
    for c in range(9):
        val = board[r][c]
        if val != ".":
            if (r, val) in seen or (val, c) in seen or (r//3, c//3, val) in seen:
                # duplicate
                pass
            seen.add((r, val))
            seen.add((val, c))
            seen.add((r//3, c//3, val))
```

---

## 🧵 STRING TRICKS

### `str.count()`
```python
"balloon".count("l")  # 2
```

### `ord()` and `chr()`
```python
ord('a')  # 97
chr(97)   # 'a'
```

### Sorting characters of a string
```python
sorted("cba")  # ['a', 'b', 'c']
```

---

## 🔗 TWO SUM / PAIRING

### Using hashmap to find complement
```python
nums = [2, 7, 11, 15]
target = 9
seen = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        # return [seen[complement], i]
        pass
    seen[num] = i
```

---

## 🧊 LONGEST CONSECUTIVE SEQUENCE

### Using set to check consecutive elements
```python
nums = [100, 4, 200, 1, 3, 2]
num_set = set(nums)
longest = 0
for n in num_set:
    if n - 1 not in num_set:
        length = 1
        while n + length in num_set:
            length += 1
        longest = max(longest, length)
# longest = 4 (sequence: 1, 2, 3, 4)
```

