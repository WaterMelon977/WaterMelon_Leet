## 🥞 STACK METHODS & USAGE IN JAVA

### Using `Stack` class

```java
Stack<Integer> stack = new Stack<>();
stack.push(5);         // push
stack.pop();           // pop
stack.peek();          // peek (top element)
stack.isEmpty();       // check if empty
```

### Example: Valid Parentheses

```java
Stack<Character> stack = new Stack<>();
Map<Character, Character> map = Map.of(')', '(', ']', '[', '}', '{');
for (char c : s.toCharArray()) {
    if (map.containsValue(c)) {
        stack.push(c);
    } else {
        if (stack.isEmpty() || stack.pop() != map.get(c)) {
            return false;
        }
    }
}
return stack.isEmpty();
```

### Min Stack logic

Keep track of current min with auxiliary stack

```java
Stack<Integer> stack = new Stack<>();
Stack<Integer> minStack = new Stack<>();

stack.push(val);
if (minStack.isEmpty()) {
    minStack.push(val);
} else {
    minStack.push(Math.min(val, minStack.peek()));
}

stack.pop();
minStack.pop();

minStack.peek();  // getMin
```

---

## 📈 MONOTONIC STACK (e.g., Daily Temperatures)

```java
int[] res = new int[temps.length];
Stack<Integer> stack = new Stack<>();  // stores indices

for (int i = 0; i < temps.length; i++) {
    while (!stack.isEmpty() && temps[i] > temps[stack.peek()]) {
        int prev = stack.pop();
        res[prev] = i - prev;
    }
    stack.push(i);
}
```

---

## ↻ REVERSE POLISH NOTATION (RPN)

```java
Stack<Integer> stack = new Stack<>();
for (String token : tokens) {
    if ("+-*/".contains(token)) {
        int b = stack.pop();
        int a = stack.pop();
        switch (token) {
            case "+": stack.push(a + b); break;
            case "-": stack.push(a - b); break;
            case "*": stack.push(a * b); break;
            case "/": stack.push(a / b); break;
        }
    } else {
        stack.push(Integer.parseInt(token));
    }
}
return stack.pop();
```

---

## ⚾ BASEBALL GAME

```java
Stack<Integer> stack = new Stack<>();
for (String op : ops) {
    switch (op) {
        case "+":
            stack.push(stack.get(stack.size() - 1) + stack.get(stack.size() - 2));
            break;
        case "D":
            stack.push(2 * stack.peek());
            break;
        case "C":
            stack.pop();
            break;
        default:
            stack.push(Integer.parseInt(op));
            break;
    }
}
return stack.stream().mapToInt(Integer::intValue).sum();
```

---

## 📬 QUEUE METHODS & USAGE IN JAVA

### Using `Queue` with `LinkedList`

```java
Queue<Integer> queue = new LinkedList<>();

queue.offer(10);       // enqueue
queue.poll();          // dequeue
queue.peek();          // front
queue.isEmpty();       // check if empty
```

### Using `Deque` as Stack

```java
Deque<Integer> stack = new ArrayDeque<>();
stack.push(5);         // push
stack.pop();           // pop
stack.peek();          // peek
```

---

## 🧐 STACK/QUEUE DESIGN PATTERNS

- **Valid Parentheses**: use stack to match brackets.
- **Min Stack**: use two stacks to track min.
- **RPN**: stack to evaluate postfix operations.
- **Monotonic Stack**: maintain increasing or decreasing order of indices.
- **Baseball Game**: simulate stack operations.
- **Queue**: `LinkedList` or `ArrayDeque` for FIFO processing.

---

## 📌 NOTES

- Stack is **LIFO** (Last-In, First-Out)
- Queue is **FIFO** (First-In, First-Out)
- Use `ArrayDeque` for better performance than `Stack` class
- Use two stacks to simulate getMin() and track min values efficiently
- Monotonic stack helps in range-based questions like next greater element
