https://colab.research.google.com/drive/1spa5_AB-IXpdZjMeGZ6ARX_LEKRt6bBx?usp=sharing

## 🔗 LINKED LIST METHODS & ALGORITHMS IN PYTHON

---

### 🧱 Basic Node Definition

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

---

### 🔁 Traverse a Linked List

```python
cur = head
while cur:
    print(cur.val)
    cur = cur.next
```

---

### 🚫 Remove Duplicates from Sorted List (Leetcode 83)

```python
cur = head
while cur and cur.next:
    if cur.val == cur.next.val:
        cur.next = cur.next.next
    else:
        cur = cur.next
```

---

### 🔄 Reverse Linked List (Leetcode 206)

```python
prev = None
cur = head
while cur:
    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt
return prev
```

---

### 🔀 Merge Two Sorted Lists (Leetcode 21)

```python
dummy = ListNode(-1)
cur = dummy
while l1 and l2:
    if l1.val < l2.val:
        cur.next = l1
        l1 = l1.next
    else:
        cur.next = l2
        l2 = l2.next
    cur = cur.next
cur.next = l1 or l2
return dummy.next
```

---

### 🔁 Linked List Cycle (Leetcode 141) - Floyd’s Tortoise & Hare

```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True
return False
```

---

### ⚖️ Middle of the Linked List (Leetcode 876)

```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
return slow
```

---

### ➖ Remove Nth Node from End (Leetcode 19)

```python
dummy = ListNode(0, head)
slow = fast = dummy
for _ in range(n):
    fast = fast.next
while fast.next:
    slow = slow.next
    fast = fast.next
slow.next = slow.next.next
return dummy.next
```

---

### 🧬 Copy List with Random Pointer (Leetcode 138)

#### 3-step method:

1. Interweave original and copy nodes
2. Assign random pointers
3. Split into original and copied list

```python
# Step 1
cur = head
while cur:
    new = Node(cur.val, cur.next)
    cur.next = new
    cur = new.next

# Step 2
cur = head
while cur:
    if cur.random:
        cur.next.random = cur.random.next
    cur = cur.next.next

# Step 3
cur = head
copy_head = cur.next if head else None
while cur:
    copy = cur.next
    cur.next = copy.next
    if copy.next:
        copy.next = copy.next.next
    cur = cur.next
return copy_head
```

---

## 📌 TIPS

- Use **dummy node** to simplify head insert/delete cases
- Two-pointer approach (fast-slow) for middle/cycle
- Edge case: empty list, one node, two nodes
- In-place manipulation with O(1) space preferred when possible
- Use hashmap if you need extra data (like random pointers)

---

## ✅ COMMON INTERVIEW CHECKLIST

- Traversal (iterative/recursive)
- Cycle detection (Floyd's algo)
- Reverse and merge
- Two pointers for nth from end
- Deep copy using hashmaps or interleaving nodes
