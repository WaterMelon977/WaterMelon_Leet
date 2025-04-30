# PYTHON QUICK REVIEW NOTES (For Selected Leetcode Problems)

## 🔤 STRING METHODS

### `str.isdigit()`
- Checks if all characters are digits.
```python
"123".isdigit()  # True
"12a".isdigit()   # False
```

### `str.isalpha()`
- Checks if all characters are alphabetic.
```python
"abc".isalpha()  # True
"abc1".isalpha() # False
```

### `str.lower()` / `str.upper()`
- Converts string to lower or upper case.
```python
"ABC".lower()  # 'abc'
"abc".upper()  # 'ABC'
```

### `str.strip()` / `str.lstrip()` / `str.rstrip()`
- Removes leading/trailing spaces or characters.
```python
" abc ".strip()  # 'abc'
"abc\n".rstrip()   # 'abc'
```

### `str.split(sep)` / `str.join()`
- Splits/join strings.
```python
"a,b,c".split(',')     # ['a', 'b', 'c']
"-".join(['a','b'])    # 'a-b'
```

### `str[::-1]`
- Reverses a string.
```python
"abc"[::-1]  # 'cba'
```

## 📚 LIST METHODS (ARRAYS)

### `list.append(x)`
- Adds element to end.
```python
arr = [1,2]
arr.append(3)  # [1,2,3]
```

### `list.pop([i])`
- Removes and returns item at index.
```python
arr = [1,2,3]
arr.pop()    # 3
arr.pop(0)   # 1
```

### `list.sort()` / `sorted(list)`
- Sorts list in-place or returns new sorted list.
```python
arr = [3,1,2]
sorted(arr)      # [1,2,3]
arr.sort(reverse=True) # [3,2,1]
```

### `list.insert(i, x)`
- Inserts `x` at position `i`.
```python
arr = [1,3]
arr.insert(1,2)  # [1,2,3]
```

### `list.extend(iterable)`
- Extends list by appending elements from iterable.
```python
arr = [1,2]
arr.extend([3,4])  # [1,2,3,4]
```

### `reversed(list)`
- Returns a reversed iterator.
```python
list(reversed([1,2,3]))  # [3,2,1]
```

## 📏 LIST SLICING
```python
arr = [1,2,3,4,5]
arr[1:4]   # [2,3,4]
arr[::-1]  # [5,4,3,2,1]
```

## 🧮 DICTIONARY METHODS

### `dict.get(key, default)`
- Safe key access.
```python
d = {'a': 1}
d.get('a')     # 1
d.get('b', 0)  # 0
```

### `dict.items()` / `dict.keys()` / `dict.values()`
```python
d = {'a': 1, 'b': 2}
list(d.items())   # [('a', 1), ('b', 2)]
list(d.keys())    # ['a', 'b']
list(d.values())  # [1, 2]
```

### `collections.defaultdict()`
- Automatically initializes missing keys.
```python
from collections import defaultdict
d = defaultdict(int)
d['a'] += 1  # {'a': 1}
```

### `collections.Counter()`
```python
from collections import Counter
Counter("aabcc")  # {'a': 2, 'b': 1, 'c': 2}
```

## 🧵 ZIP & ENUMERATE

### `zip()`
- Combines multiple iterables.
```python
zip("abc", "123")  # [('a','1'), ('b','2'), ('c','3')]
```

### `enumerate()`
- Index-value pairs.
```python
for i, val in enumerate([10,20]):
    print(i, val)
```

## 📐 MATH & LOGIC

### `abs(x)`
- Absolute value.
```python
abs(-5)  # 5
```

### `min()` / `max()`
```python
min([1,2,3])  # 1
max([1,2,3])  # 3
```

### `sum()`
```python
sum([1,2,3])  # 6
```

## 📎 2D MATRIX TRICKS

### Transpose
```python
matrix = [[1,2],[3,4]]
zip(*matrix)  # [(1,3), (2,4)]
```

### Rotate Matrix 90°
```python
matrix[:] = zip(*matrix[::-1])
```

### Flatten 2D list
```python
flat = [val for row in matrix for val in row]
```

## 🧪 COMPARISONS

### `in` keyword
```python
3 in [1,2,3]        # True
"a" in "cat"        # True
"ab" in "abc"       # True
```

### `any()` / `all()`
```python
any([0,1,0])  # True
all([1,1,1])  # True
```

---
These are the most-used Python tricks/functions for problems involving arrays, strings, matrices, and intervals like those in your list.

Use this to quickly recall helpful tools during interview prep!
