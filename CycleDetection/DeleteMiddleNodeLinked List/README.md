# 1. Core idea
Use slow/fast pointers to locate the middle node. Maintain a `prev` pointer behind `slow`. When `fast` reaches the end, `slow` is at the middle; delete it by linking `prev.next = slow.next`. Handle single-node edge case separately.

# 2. Why optimal (time/space intuition)
Single traversal finds the middle in **O(n)**. No extra data structures are used. This is the minimal linear-time, constant-space approach.

# 3. Python code
```python
class Solution:
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None
        
        slow = fast = head
        prev = None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = slow.next
        return head
```

# 4. Time & Space: O(n) / O(1)