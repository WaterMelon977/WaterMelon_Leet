https://colab.research.google.com/drive/1djJOXslserp8IerjT4kfp7DXX5s-tdgh?usp=sharing#scrollTo=xMM84zW-VHw5

## 🥞 STACK METHODS & USAGE

### Using `list` as a stack

```python
stack = []
stack.append(5)    # push
stack.pop()        # pop (last in)
stack[-1]          # peek (top element)
not stack          # check if empty
```

### Example: Valid Parentheses

```python
stack = []
for c in s:
    if c in '([{':
        stack.append(c)
    else:
        if not stack or stack[-1] != matching[c]:
            return False
        stack.pop()
return not stack
```

### Example: Min Stack logic

Keep track of current min with each value

```python
stack = []
min_stack = []

stack.append(val)
min_stack.append(min(val, min_stack[-1] if min_stack else val))

stack.pop()
min_stack.pop()

min_stack[-1]  # getMin()
```

---

## 📈 MONOTONIC STACK (e.g., Daily Temperatures)

### Maintain decreasing stack of indices

```python
res = [0] * len(temps)
stack = []  # stores indices

for i, temp in enumerate(temps):
    while stack and temps[i] > temps[stack[-1]]:
        prev = stack.pop()
        res[prev] = i - prev
    stack.append(i)
```

Used for: Next greater element, Daily Temperatures

---

## 🔁 REVERSE POLISH NOTATION (RPN)

### Evaluate postfix expression using stack

```python
stack = []
for token in tokens:
    if token in '+-*/':
        b = stack.pop()
        a = stack.pop()
        if token == '+': stack.append(a + b)
        elif token == '-': stack.append(a - b)
        elif token == '*': stack.append(a * b)
        else: stack.append(int(a / b))  # truncate toward zero
    else:
        stack.append(int(token))
return stack[0]
```

---

## ⚾ BASEBALL GAME

### Apply stack operations based on symbols

```python
stack = []
for op in ops:
    if op == "+":
        stack.append(stack[-1] + stack[-2])
    elif op == "D":
        stack.append(2 * stack[-1])
    elif op == "C":
        stack.pop()
    else:
        stack.append(int(op))
return sum(stack)
```

---

## 📬 QUEUE METHODS & USAGE

### Using `collections.deque`

```python
from collections import deque
queue = deque()

queue.append(10)     # enqueue
queue.popleft()      # dequeue
queue[0]             # peek
not queue            # empty check
```

### Can also use `deque` as stack

```python
stack = deque()
stack.append(5)      # push
stack.pop()          # pop
```

---

## 🧠 STACK/QUEUE DESIGN PATTERNS

- **Valid Parentheses**: use stack to match brackets.
- **Min Stack**: track minimum with auxiliary stack.
- **RPN**: stack to evaluate postfix operations.
- **Monotonic Stack**: solve span/next greater element problems.
- **Baseball Game**: interpret operations as stack manipulations.
- **Queue with Max/Min**: use deque for sliding window (not required here but good to know).

---

## 📌 NOTES

- Stack is **LIFO** (Last-In, First-Out)
- Queue is **FIFO** (First-In, First-Out)
- Use `deque` from `collections` for both stacks and queues efficiently
- Use auxiliary stacks for tracking min/max in stack design problems
- Monotonic stacks help answer range-based queries efficiently
