# Core idea
Sort the array and use two pointers: lightest (left) and heaviest (right). Always try to pair the heaviest person with the lightest; if their sum ≤ limit, move both pointers. Otherwise, send the heaviest alone. Each iteration uses one boat.

# Why optimal (time/space intuition)
Greedy works because pairing the heaviest with the lightest maximizes utilization while preserving feasibility. If the lightest cannot pair with the heaviest, no one can. Sorting dominates time; two-pointer scan is linear.

# Python code
```python
class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            boats += 1
        return boats
```

# Time & Space Complexity
- Time: O(n log n)
- Space: O(1)