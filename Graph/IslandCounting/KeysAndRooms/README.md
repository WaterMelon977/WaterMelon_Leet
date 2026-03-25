**LeetCode Link**
[https://leetcode.com/problems/keys-and-rooms/](https://leetcode.com/problems/keys-and-rooms/)

**Approach**

* Treat rooms as a graph where each room contains keys to other rooms.
* Start from room `0` (only unlocked room initially).
* Use DFS/BFS to visit all reachable rooms using available keys.
* Maintain a `visited` set to avoid revisiting rooms.
* Traverse all keys found in each visited room.
* At the end, check if number of visited rooms == total rooms.

**Key Insight**
This reduces to checking if all nodes are reachable from node `0` in a directed graph.

**Why efficient**
Each room and key is processed once → linear traversal.

**Python Solution**

```python id="6c3l3s"
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        
        def dfs(room):
            visited.add(room)
            
            for key in rooms[room]:
                if key not in visited:
                    dfs(key)
        
        dfs(0)
        
        return len(visited) == len(rooms)
```

**Explain any tricky part of the code**

* We only start from room `0`, so unreachable rooms indicate disconnected graph.

Edge-case handling: If `rooms = [[]]` → only one room → already visited → return True.

**Complexity**
Time: O(n + e) — each room and key processed once
Space: O(n) — visited set + recursion stack
