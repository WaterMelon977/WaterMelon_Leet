**LeetCode Link**
[https://leetcode.com/problems/subtree-of-another-tree/](https://leetcode.com/problems/subtree-of-another-tree/)

**Approach**

* Use **postorder DFS serialization** to convert each subtree into a string.
* Serialize both `root` and `subRoot` using:

  ```
  serial = "left,right,val"
  ```
* Include a **null marker (`#`)** to preserve structure.
* After serialization:

  * Check if `subRoot_serial` is a **substring** of `root_serial`.
* Postorder ensures structure is encoded uniquely.

**Key Insight**
Two trees are identical if their **postorder serialization strings match exactly** (including nulls).

**Why efficient**
Avoids repeated subtree comparisons → reduces from O(n·m) to near O(n + m).

**Python Solution**

```python
class Solution:
    def isSubtree(self, root, subRoot):
        
        def serialize(node):
            if not node:
                return "#"
            
            left = serialize(node.left)
            right = serialize(node.right)
            
            # postorder: left, right, node
            return f"{left},{right},{node.val}"
        
        root_serial = serialize(root)
        sub_serial = serialize(subRoot)
        
        return sub_serial in root_serial
```

**Explain any tricky part of the code**

The `"#"` null marker is critical:

```python
"#,#,1"
```

Without it, different structures could produce same string → false positives.

Edge-case handling: If `subRoot` is None → its serialization is `"#"` which is always found → correctly returns True.

**Complexity**
Time: O(n + m) — serialize both + substring check
Space: O(n + m) — storing serialized strings

----------------------------------------

Let’s do a **clean dry run** so you actually *see* how postorder serialization proves subtree match.

---

# 🌳 Example

### `root`

```text
        3
       / \
      4   5
     / \
    1   2
```

### `subRoot`

```text
      4
     / \
    1   2
```

---

# ✅ Step 1: Serialize using POSTORDER

Format:

```text
left, right, node
```

Null = `#`

---

## 🔹 Serialize `subRoot`

Start bottom-up:

### Node 1

```text
#,#,1
```

### Node 2

```text
#,#,2
```

### Node 4

```text
#,#,1,#,#,2,4
```

👉 Final:

```text
sub_serial = "#,#,1,#,#,2,4"
```

---

## 🔹 Serialize `root`

### Node 1

```text
#,#,1
```

### Node 2

```text
#,#,2
```

### Node 4

```text
#,#,1,#,#,2,4
```

### Node 5

```text
#,#,5
```

### Node 3

```text
#,#,1,#,#,2,4,#,#,5,3
```

👉 Final:

```text
root_serial = "#,#,1,#,#,2,4,#,#,5,3"
```

---

# 🔍 Step 2: Substring Check

Check:

```text
"#,#,1,#,#,2,4"  in  "#,#,1,#,#,2,4,#,#,5,3"
```

👉 YES ✅

---

# 🧠 Why this works

Because serialization includes:

* structure (`#`)
* values
* order (postorder)

So:

```text
identical subtree → identical substring
```

---

# ⚠️ Important Edge Case (why `#` matters)

Consider:

```text
Tree A:      Tree B:
   1            1
  /              \
 2                2
```

Without `#`, both serialize same ❌
With `#`:

```text
A → "#,#,2,#,1"
B → "#,#,#,2,1"
```

👉 Now different ✅

---

# 🔥 Final intuition

Postorder serialization turns each subtree into a **unique fingerprint**

So problem becomes:

```text
Is one fingerprint inside another?
```

---

If you want, I can show a case where this **fails without null markers** — that’s a very common interview trap.
