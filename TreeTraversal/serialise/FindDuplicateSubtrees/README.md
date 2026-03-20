**LeetCode Link**
[https://leetcode.com/problems/find-duplicate-subtrees/](https://leetcode.com/problems/find-duplicate-subtrees/)

**Approach**

* Use **postorder DFS** to serialize each subtree.
* For each node, create a unique representation:

  ```
  serial = "val,left_serial,right_serial"
  ```
* Use a hashmap `count` to track frequency of each serialization.
* When a serialization appears **exactly twice**, add that node to result.
* Return serialization string to parent.

**Key Insight**
Two subtrees are identical **iff their serialized structure + values match**.

**Why efficient**
Each subtree is processed once and reused via hashing → avoids repeated comparisons.

**Python Solution**

```python
class Solution:
    def findDuplicateSubtrees(self, root):
        from collections import defaultdict
        
        count = defaultdict(int)
        result = []
        
        def dfs(node):
            if not node:
                return "#"  # marker for null
            
            left_serial = dfs(node.left)
            right_serial = dfs(node.right)
            
            # Serialize current subtree
            serial = f"{node.val},{left_serial},{right_serial}"
            
            count[serial] += 1
            
            # Add only when seen second time
            if count[serial] == 2:
                result.append(node)
            
            return serial
        
        dfs(root)
        return result
```

**Explain any tricky part of the code**

Using `"#"` for null ensures structure is preserved:

```python
serial = "1,#,#"   # leaf node
```

Without null markers, different trees could look identical.

Edge-case handling: Only add subtree when count == 2 to avoid duplicates in result list.

**Complexity**
Time: O(n) — each node serialized once
Space: O(n) — hashmap stores all subtree serializations
