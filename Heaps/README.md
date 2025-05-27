https://colab.research.google.com/drive/1vUROF93_7r8hP3_Q9PjOWCgIEdiDpLae?usp=sharing

## 🐍 Python Interview Notes: Heaps (Priority Queues)

---

## 📚 `heapq` Module Basics

Python’s built-in module for heaps (min-heaps by default).

```python
import heapq
```

### Min Heap (default)

```python
heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 2)
heapq.heappop(heap)     # returns 2 (smallest)
heap[0]                 # peek (min element)
```

### Max Heap using Negation

```python
heap = []
heapq.heappush(heap, -val)
max_val = -heapq.heappop(heap)
```

---

## 📦 Last Stone Weight

Use a max heap (via negation) to simulate taking two heaviest stones repeatedly:

```python
stones = [-s for s in stones]
heapq.heapify(stones)

while len(stones) > 1:
    y = -heapq.heappop(stones)
    x = -heapq.heappop(stones)
    if y != x:
        heapq.heappush(stones, -(y - x))
return -stones[0] if stones else 0
```

---

## 🏆 Kth Largest Element in an Array

Maintain a **min-heap** of size k.

```python
heap = []
for num in nums:
    heapq.heappush(heap, num)
    if len(heap) > k:
        heapq.heappop(heap)
return heap[0]
```

---

## 🔝 Top K Frequent Elements

Use `Counter` and a min-heap of size k.

```python
from collections import Counter
count = Counter(nums)
heap = []

for num, freq in count.items():
    heapq.heappush(heap, (freq, num))
    if len(heap) > k:
        heapq.heappop(heap)

return [num for freq, num in heap]
```

---

## 📍 K Closest Points to Origin

Minimize `x² + y²` using max-heap to keep k closest.

```python
heap = []
for x, y in points:
    dist = -(x*x + y*y)
    heapq.heappush(heap, (dist, x, y))
    if len(heap) > k:
        heapq.heappop(heap)

return [(x, y) for dist, x, y in heap]
```

---

## 🔗 Merge K Sorted Linked Lists

Use a heap to store (value, list index, node) and pop smallest node.

```python
heap = []
for i, node in enumerate(lists):
    if node:
        heapq.heappush(heap, (node.val, i, node))

dummy = ListNode(0)
curr = dummy

while heap:
    val, i, node = heapq.heappop(heap)
    curr.next = node
    curr = curr.next
    if node.next:
        heapq.heappush(heap, (node.next.val, i, node.next))

return dummy.next
```

---

## 📌 Notes:

- Python heaps are **min-heaps**; use negation for max-heap behavior.
- Tuple comparison works naturally in `heapq` → `(priority, index, value)` ensures uniqueness.
- Use `heapq.heapify(list)` to build a heap in-place in O(n).
- Great for solving top-k, merging, and priority problems efficiently.

---
