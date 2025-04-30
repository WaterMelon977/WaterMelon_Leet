## 🔤 STRING METHODS

### `charAt(int index)`
Access character at a specific index.
```java
String temp = "abc";
temp.charAt(0);  // 'a'
```

### `substring(int start, int end)`
Extract substring from start (inclusive) to end (exclusive).
```java
String s = "leetcode";
s.substring(0, 4);  // "leet"
```

### `equals(String other)`
Compare string content.
```java
"abc".equals("abc");  // true
```

### `toCharArray()`
Convert string to a character array.
```java
char[] arr = s.toCharArray();  // ['l','e','e','t','c','o','d','e']
```

### `split(String delimiter)`
Split string by delimiter.
```java
"a,b,c".split(",");  // ["a", "b", "c"]
```

### `toLowerCase()` and `toUpperCase()`
Convert string to lowercase/uppercase.
```java
s.toLowerCase();  // "leetcode"
s.toUpperCase();  // "LEETCODE"
```

### `contains()`, `indexOf()`, `startsWith()`, `endsWith()`
Useful string checks.
```java
s.contains("lee");    // true
s.indexOf("t");       // 3
s.startsWith("leet"); // true
s.endsWith("code");   // true
```

---

## 📚 ARRAY METHODS

### `Arrays.sort()`
Sort an array.
```java
int[] nums = {3, 1, 2};
Arrays.sort(nums);  // [1, 2, 3]
```

### `Arrays.copyOfRange()`
Copy part of an array.
```java
int[] sub = Arrays.copyOfRange(nums, 0, 2);  // [1, 2]
```

### Manual reverse
```java
for (int i = 0, j = nums.length - 1; i < j; i++, j--) {
    int temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
}  // reversed: [3, 2, 1]
```

---

## 📏 LIST METHODS

### `add()`, `get()`, `set()`, `remove()`
```java
List<Integer> list = new ArrayList<>();
list.add(10);
list.get(0);        // 10
list.set(0, 20);     // [20]
list.remove(0);      // []
```

### `contains()` and `indexOf()`
```java
list.contains(10);  // true/false
list.indexOf(10);   // index or -1
```

---

## 🧮 MAP / HASHMAP METHODS

### `put()`, `get()`, `getOrDefault()`, `containsKey()`
```java
Map<String, Integer> map = new HashMap<>();
map.put("a", 1);
map.get("a");             // 1
map.getOrDefault("b", 0);  // 0
map.containsKey("a");     // true
```

### Count frequencies
```java
String example = "aabbc";
for (char c : example.toCharArray()) {
    map.put(String.valueOf(c), map.getOrDefault(String.valueOf(c), 0) + 1);
}  // map: {a=2, b=2, c=1}
```

---

## 🧵 ZIP-LIKE & ENUMERATION

### Iterate two strings in parallel
```java
for (int i = 0; i < Math.min(a.length(), b.length()); i++) {
    char x = a.charAt(i);
    char y = b.charAt(i);
    // (x, y): (a, 1), (b, 2), etc.
}
```

---

## 📐 MATH METHODS

```java
Math.abs(-5);    // 5
Math.min(3, 8);  // 3
Math.max(3, 8);  // 8
```

---

## 📎 2D ARRAY TRICKS

### Rotate matrix 90° clockwise
```java
int N = matrix.length;
for (int i = 0; i < N / 2; i++) {
    for (int j = i; j < N - i - 1; j++) {
        int temp = matrix[i][j];
        matrix[i][j] = matrix[N - j - 1][i];
        matrix[N - j - 1][i] = matrix[N - i - 1][N - j - 1];
        matrix[N - i - 1][N - j - 1] = matrix[j][N - i - 1];
        matrix[j][N - i - 1] = temp;
    }
}
```

### Flatten matrix
```java
for (int[] row : matrix) {
    for (int val : row) {
        list.add(val);
    }
}
```

---

## 🧪 UTILS

### `String.join()` and `StringBuilder`
```java
String.join("-", Arrays.asList("a", "b"));  // "a-b"

StringBuilder sb = new StringBuilder();
sb.append("abc");
sb.reverse();         // "cba"
sb.toString();        // "cba"
```

### Convert char to int
```java
char c = '3';
int digit = c - '0';  // 3
```

---

## ⛏️ SET METHODS

### `add()`, `contains()`, `remove()`
```java
Set<Integer> set = new HashSet<>();
set.add(10);
set.contains(10);  // true
set.remove(10);
```

### Convert array to set
```java
Set<Integer> s = new HashSet<>(Arrays.asList(1, 2, 3));
```

