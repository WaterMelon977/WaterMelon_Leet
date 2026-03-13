Yes — your intuition is close, but let’s make it precise.

`path` is **shared across recursive calls**. Without removing the last node, the path would keep growing and would contaminate the next branch.

### What actually happens

Suppose the tree is:

```
    1
   / \
  2   3
   \
    5
```

We traverse with DFS.

#### Step 1

Visit `1`

```
path = [1]
```

#### Step 2

Go left → visit `2`

```
path = [1,2]
```

#### Step 3

Go right → visit `5`

```
path = [1,2,5]
```

Leaf → store:

```
"1->2->5"
```

Now recursion returns.

### Why `path.pop()` is needed

After finishing node `5`, we must **remove it** before exploring other branches.

```
path.pop()
path = [1,2]
```

Return again to `2`.

Now we must remove `2` before exploring the right subtree of `1`.

```
path.pop()
path = [1]
```

Now DFS goes right:

```
path = [1,3]
```

Leaf → store `"1->3"`

### If we **did not** pop

The path would become:

```
[1,2,5,3]
```

which would produce incorrect paths.

### The mental model

Think of `path` as the **current route from root to the node you're standing on**.

* Going deeper → `append()`
* Going back up → `pop()`

That is exactly what **backtracking** means.

So your idea is partly right: we remove the node so that the **next branch starts from the correct parent path**, not from the previous child.
