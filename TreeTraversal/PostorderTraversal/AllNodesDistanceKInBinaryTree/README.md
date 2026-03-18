**LeetCode Link**
[https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)

**Approach**

* Use postorder DFS to compute distance from each node → target.
* When target is found, collect all nodes `k` distance downward.
* While backtracking:

  * Compute current node’s distance to target.
  * If equal to `k`, add current node.
  * Otherwise, explore opposite subtree with remaining distance.
* Use helper `collect_downward()` for subtree traversal.
* Return `-1` when target not found in a subtree.

**Key Insight**
Each node learns its distance from target during DFS, enabling it to explore the opposite subtree with the remaining distance.

**Why efficient**
Single DFS traversal handles both distance calculation and node collection → avoids extra graph construction.

---

**Python Solution**

```python
class Solution:
    def distanceK(self, root, target, k):
        result = []
        
        # Collect all nodes 'distance' steps below this node
        def collect_downward(node, distance):
            if not node:
                return
            
            if distance == 0:
                result.append(node.val)
                return
            
            collect_downward(node.left, distance - 1)
            collect_downward(node.right, distance - 1)
        
        # Returns distance from current node to target
        # If target not in subtree → return -1
        def dfs_find_distance(current_node):
            if not current_node:
                return -1
            
            # Case 1: Found the target node
            if current_node == target:
                collect_downward(current_node, k)  # explore downward
                return 0  # distance to itself
            
            # Search left and right subtrees
            left_distance = dfs_find_distance(current_node.left)
            right_distance = dfs_find_distance(current_node.right)
            
            # Case 2: Target found in LEFT subtree
            if left_distance != -1:
                distance_from_current = left_distance + 1
                
                # If current node itself is k distance away
                if distance_from_current == k:
                    result.append(current_node.val)
                else:
                    # Explore RIGHT subtree (opposite side)
                    remaining_distance = k - (left_distance + 2)
                    collect_downward(current_node.right, remaining_distance)
                
                return distance_from_current
            
            # Case 3: Target found in RIGHT subtree
            if right_distance != -1:
                distance_from_current = right_distance + 1
                
                if distance_from_current == k:
                    result.append(current_node.val)
                else:
                    # Explore LEFT subtree (opposite side)
                    remaining_distance = k - (right_distance + 2)
                    collect_downward(current_node.left, remaining_distance)
                
                return distance_from_current
            
            # Case 4: Target not found in either subtree
            return -1
        
        dfs_find_distance(root)
        return result
```

---

**Explain any tricky part of the code**

### Distance propagation

* Child returns distance → parent adds `+1`
* This tells how far current node is from target

### `remaining_distance = k - (child_distance + 2)`

* `+1` → move from child → current node
* `+1` → move from current → opposite subtree
* So subtract **2**

---

Edge-case handling:
If `k = 0`, `collect_downward(target, 0)` directly adds the target node.

---

**Complexity**
Time: O(N) → each node processed once
Space: O(H) → recursion stack (tree height)



**LeetCode Link**
[https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)

**Approach**

* Convert tree into an undirected graph using adjacency list (parent ↔ child connections).
* Traverse tree once (DFS) to build graph.
* Perform BFS starting from target node.
* Track visited nodes to avoid revisiting (since graph has cycles).
* Stop BFS when distance == K and collect all nodes at that level.
* Return collected nodes.

**Key Insight**
Tree becomes a graph when parent links are added, enabling BFS from target in all directions (left, right, parent).

**Why efficient**
Single DFS to build graph + BFS traversal → avoids repeated subtree traversals.

**Python Solution**

```python
from collections import defaultdict, deque

class Solution:
    def distanceK(self, root, target, k):
        # Step 1: Build graph
        graph = defaultdict(list)
        
        def build_graph(node, parent):
            if not node:
                return
            if parent:
                graph[node].append(parent)
                graph[parent].append(node)
            build_graph(node.left, node)
            build_graph(node.right, node)
        
        build_graph(root, None)
        
        # Step 2: BFS from target
        queue = deque([(target, 0)])
        visited = set([target])
        result = []
        
        while queue:
            node, dist = queue.popleft()
            
            if dist == k:
                result.append(node.val)
            
            # Stop exploring deeper once we reach k
            if dist > k:
                break
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        
        return result
```

**Explain any tricky part of the code**

Turning tree into graph:

* We add both directions (`node ↔ parent`) so BFS can move upward as well.
* Without parent links, you cannot explore nodes above target.

BFS stopping logic:

* Once `dist == k`, we collect nodes but still process same level.
* We don’t expand further from those nodes.

Edge-case handling:
If `k = 0`, BFS immediately returns `[target.val]`.

**Complexity**
Time: O(N) → build graph + BFS over all nodes
Space: O(N) → adjacency list + visited set


Yes — and this is actually the **cleaner optimal approach without converting to a graph**.

You use **postorder traversal (DFS)** to compute distance from target and propagate it upward.

---

## **Approach (Postorder DFS)**

* Traverse tree using DFS.
* Return distance from current node → target:

  * `-1` → target not found in subtree
  * `>=0` → distance from current node to target
* When you find target:

  * Collect all nodes at distance `k` in its subtree.
* While backtracking:

  * If target found in left subtree:

    * Current node distance = `left_dist + 1`
    * Check:

      * If `left_dist + 1 == k` → add current node
      * Else → search right subtree for nodes at `k - left_dist - 2`
  * Same logic for right subtree.

---

## **Key Insight**

Each node returns its distance to target → allowing you to:

* Know how far target is
* Search opposite subtree for remaining distance

---

## **Python Solution**

```python 
class Solution:
    def distanceK(self, root, target, k):
        result = []
        
        # Helper to collect nodes at distance k downward
        def collect(node, dist):
            if not node:
                return
            if dist == 0:
                result.append(node.val)
                return
            collect(node.left, dist - 1)
            collect(node.right, dist - 1)
        
        def dfs(node):
            if not node:
                return -1
            
            # Found target
            if node == target:
                collect(node, k)
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # Target in left subtree
            if left != -1:
                if left + 1 == k:
                    result.append(node.val)
                else:
                    collect(node.right, k - left - 2)
                return left + 1
            
            # Target in right subtree
            if right != -1:
                if right + 1 == k:
                    result.append(node.val)
                else:
                    collect(node.left, k - right - 2)
                return right + 1
            
            return -1
        
        dfs(root)
        return result
```

---

## **Explain tricky part**

### `k - left - 2`

* `left` = distance from current node → target via left child
* `+1` → move to current node
* `+1` → move to right subtree root

So remaining distance =
👉 `k - (left + 2)`

---

## **Edge-case handling**

If `target` is root → only downward collection happens.

---

## **Complexity**

Time: **O(N)** → each node visited once
Space: **O(H)** → recursion stack (height of tree)

---

## Straight truth

If you're in an interview:

* Graph + BFS → easier to think
* Postorder DFS → more impressive and optimal in reasoning

Both are correct — but this one shows deeper understanding.
