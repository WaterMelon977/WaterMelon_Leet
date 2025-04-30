## 🧮 HASHMAP METHODS

### `put(key, value)` and `get(key)`
```java
Map<Character, Integer> map = new HashMap<>();
map.put('a', 1);
map.get('a'); // 1
```

### `getOrDefault(key, default)`
```java
map.getOrDefault('b', 0); // 0
```

### `containsKey(key)` and `containsValue(value)`
```java
map.containsKey('a');    // true
map.containsValue(1);    // true
```

### Iterating over entries
```java
for (Map.Entry<Character, Integer> entry : map.entrySet()) {
    char k = entry.getKey();
    int v = entry.getValue();
}
```

### Frequency count
```java
for (char c : "aabbc".toCharArray()) {
    map.put(c, map.getOrDefault(c, 0) + 1);
} // {a=2, b=2, c=1}
```

---

## ⛏️ HASHSET METHODS

### `add()`, `remove()`, `contains()`
```java
Set<Integer> set = new HashSet<>();
set.add(10);
set.contains(10);  // true
set.remove(10);
```

### Use to detect duplicates
```java
for (int num : nums) {
    if (!set.add(num)) {
        // duplicate found
    }
}
```

---

## 📚 ARRAY + STRING TRICKS

### `toCharArray()` and `charAt()`
```java
String s = "abc";
char[] chars = s.toCharArray();
char first = s.charAt(0); // 'a'
```

### `substring()`, `length()`
```java
s.substring(0, 3);  // "abc"
s.length();        // 3
```

### `equals()`, `equalsIgnoreCase()`, `contains()`
```java
s.equals("abc");        // true
s.contains("a");        // true
s.equalsIgnoreCase("ABC"); // true
```

### Sorting characters (for anagram problems)
```java
char[] ch = s.toCharArray();
Arrays.sort(ch);
String sorted = new String(ch);
```

---

## 🔃 GROUPING + ANAGRAMS

### Grouping by sorted string key
```java
Map<String, List<String>> map = new HashMap<>();
for (String word : words) {
    char[] ch = word.toCharArray();
    Arrays.sort(ch);
    String key = new String(ch);
    map.computeIfAbsent(key, k -> new ArrayList<>()).add(word);
}
```

---

## 🧩 LIST + ENUM

### `add()`, `get()`, `size()`
```java
List<Integer> list = new ArrayList<>();
list.add(10);
int x = list.get(0); // 10
list.size();         // 1
```

### `for (int i = 0; i < list.size(); i++)` and `for-each`
```java
for (int i = 0; i < list.size(); i++) {
    int val = list.get(i);
}
for (int val : list) {
    // val
}
```

---

## 🧠 TWO SUM HASHMAP TRICK
```java
Map<Integer, Integer> map = new HashMap<>();
for (int i = 0; i < nums.length; i++) {
    int complement = target - nums[i];
    if (map.containsKey(complement)) {
        // return new int[] {map.get(complement), i};
    }
    map.put(nums[i], i);
}
```

---

## ✅ VALIDITY CHECKS (SUDOKU etc.)

### Use set to track seen values
```java
Set<String> seen = new HashSet<>();
if (!seen.add("row" + r + val)) {
    // duplicate in row
}
```

### Combine row, col, box logic
```java
seen.add("row" + r + val);
seen.add("col" + c + val);
seen.add("box" + (r/3) + (c/3) + val);
```

---

## 🧊 LONGEST CONSECUTIVE SEQUENCE
```java
Set<Integer> set = new HashSet<>();
for (int n : nums) set.add(n);
int maxLen = 0;
for (int n : set) {
    if (!set.contains(n - 1)) {
        int curr = n, len = 1;
        while (set.contains(curr + 1)) {
            curr++;
            len++;
        }
        maxLen = Math.max(maxLen, len);
    }
} // maxLen is the answer
```

---

## 📐 MISC TRICKS

### Convert string to frequency array
```java
int[] freq = new int[26];
for (char c : s.toCharArray()) {
    freq[c - 'a']++;
}
```

### Compare two frequency arrays
```java
Arrays.equals(freq1, freq2); // true if anagrams
```

### StringBuilder reverse
```java
StringBuilder sb = new StringBuilder("abc");
sb.reverse(); // "cba"
```

### `Math.max()`, `Math.min()`, `Math.abs()`
```java
Math.max(3, 5); // 5
Math.min(2, 8); // 2
Math.abs(-4);  // 4
```

