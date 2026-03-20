**LeetCode Link**
[https://leetcode.com/problems/serialize-and-deserialize-binary-tree/](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

**Approach**

* Use **preorder DFS** (node → left → right) for serialization.
* Represent null nodes with a marker (e.g., `#`) to preserve structure.
* Serialize as a comma-separated string.
* During deserialization:

  * Read values in order using an iterator.
  * If value is `#` → return `None`.
  * Otherwise create node and recursively build left and right.
* This ensures exact reconstruction of the tree.

**Key Insight**
Including **null markers** makes the traversal uniquely represent the tree structure.

**Why efficient**
Each node is processed exactly once in both serialize and deserialize.

**Python Solution**

```python
class Codec:

    def serialize(self, root):
        def dfs(node):
            if not node:
                return "#"
            
            return f"{node.val},{dfs(node.left)},{dfs(node.right)}"
        
        return dfs(root)

    def deserialize(self, data):
        values = iter(data.split(","))
        
        def dfs():
            val = next(values)
            
            if val == "#":
                return None
            
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            
            return node
        
        return dfs()
```

**Explain any tricky part of the code**

The iterator is key:

```python
values = iter(data.split(","))
```

It ensures we consume values **in exact preorder sequence** during reconstruction.

Edge-case handling: Null nodes (`#`) ensure structure is preserved, avoiding ambiguity.

**Complexity**
Time: O(n) — process each node once
Space: O(n) — recursion + serialized string


Good — this is the part that actually *builds your intuition*. Let’s break it down cleanly.

---

# 🔁 What are we given?

Serialized string (example):

```text
"1,2,#,#,3,4,#,#,5,#,#"
```

This came from **preorder traversal**:

```
node → left → right
```

---

# 🧠 Goal in deserialization

We want to **rebuild the exact same tree** from this sequence.

---

# 🔑 Core idea

We read values **in order**, and recursively rebuild:

```text
Read value → create node → build left → build right
```

---

# ⚙️ What does `iter()` do?

```python
values = iter(data.split(","))
```

### Without iter:

```python
["1","2","#","#","3","4","#","#","5","#","#"]
```

### With iter:

👉 It becomes a **stream** (like a pointer moving forward)

---

# ⚙️ What does `next(values)` do?

Every time you call:

```python
val = next(values)
```

👉 It gives the **next element** in sequence

Example flow:

```text
next → "1"
next → "2"
next → "#"
next → "#"
next → "3"
...
```

---

# 🌳 How tree is rebuilt

Let’s dry run:

```text
"1,2,#,#,3,#,#"
```

---

## Step 1:

```python
val = "1"
```

→ create node `1`

Now build:

```python
node.left = dfs()
node.right = dfs()
```

---

## Step 2 (build LEFT of 1):

```python
val = "2"
```

→ create node `2`

Again:

```python
node.left = dfs()
node.right = dfs()
```

---

## Step 3 (LEFT of 2):

```python
val = "#"
```

→ return `None`

---

## Step 4 (RIGHT of 2):

```python
val = "#"
```

→ return `None`

👉 Node 2 is complete:

```text
   2
  / \
 N   N
```

---

## Step 5 (build RIGHT of 1):

```python
val = "3"
```

→ create node `3`

---

## Step 6 (LEFT of 3):

```python
val = "#"
```

→ None

---

## Step 7 (RIGHT of 3):

```python
val = "#"
```

→ None

---

# ✅ Final tree:

```text
    1
   / \
  2   3
```

---

# 🔥 Key question you asked:

## ❓ How do we know what is left and right?

👉 Answer:
We don’t “figure it out” — we **follow preorder order strictly**

Rule:

```text
After reading a node:
    next value → left subtree
    next value → right subtree
```

---

# 🧠 Why this works

Because serialization was also:

```text
node → left → right
```

So deserialization mirrors it exactly.

---

# ⚠️ Why `#` is critical

Without `#`, we wouldn't know:

* where left subtree ends
* where right begins

---

# 🧩 One-line intuition

👉 The recursion itself keeps track of structure
👉 `iter + next()` ensures values are consumed **in exact order**

---

# 💡 Mental model (important)

Think of it like reading a sentence:

```text
"1 2 # # 3 # #"
```

You:

* read word
* recursively build left meaning
* recursively build right meaning

---

# 🚀 Final clarity

* `iter()` → turns list into a moving pointer
* `next()` → gives next value in order
* recursion → builds tree structure automatically
* preorder order → tells you exactly how to assign left/right

---

If you want, I can show a **visual stack trace of recursion calls** — that makes this 100% crystal clear.
