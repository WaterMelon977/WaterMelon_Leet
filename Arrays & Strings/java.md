// JAVA QUICK REVIEW NOTES (For Selected Leetcode Problems)

// 🔤 STRING METHODS

// .charAt(i) - Access character at index
temp.charAt(0);

// .substring(start, end) - Substring from start to end-1
String s = "leetcode";
s.substring(0, 4);  // "leet"

// .equals(str) vs. ==
"abc".equals("abc");  // true

// .toCharArray() - Convert string to character array
char[] arr = s.toCharArray();

// .split(delimiter)
String[] parts = "a,b,c".split(",");

// .toLowerCase(), .toUpperCase()
s.toLowerCase();

// .contains(), .indexOf(), .startsWith(), .endsWith()
s.contains("lee");
s.indexOf("t");
s.startsWith("leet");
s.endsWith("code");


// 📚 ARRAY METHODS

// Arrays.sort(arr)
import java.util.Arrays;
Arrays.sort(arr);

// Arrays.copyOfRange(arr, start, end)
int[] sub = Arrays.copyOfRange(arr, 1, 4); // index 1 to 3

// Reversing array (manual)
for (int i = 0, j = arr.length - 1; i < j; i++, j--) {
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

// Convert List to array
List<Integer> list = new ArrayList<>();
Integer[] a = list.toArray(new Integer[0]);


// 📏 LIST METHODS

// list.add(x), list.get(i), list.set(i, x), list.remove(i)
List<Integer> list = new ArrayList<>();
list.add(10);
list.get(0);
list.set(0, 20);
list.remove(0);

// list.contains(x), list.indexOf(x)
list.contains(10);
list.indexOf(10);


// 🧮 MAP / HASHMAP METHODS

import java.util.HashMap;
Map<String, Integer> map = new HashMap<>();

map.put("a", 1);
map.get("a");
map.getOrDefault("b", 0);
map.containsKey("a");
map.keySet();
map.values();
map.entrySet();

// Count frequencies
for (char c : s.toCharArray()) {
    map.put(c, map.getOrDefault(c, 0) + 1);
}


// 🧵 ZIP-LIKE & ENUMERATION

// Parallel iteration with index
for (int i = 0; i < Math.min(a.length(), b.length()); i++) {
    char x = a.charAt(i);
    char y = b.charAt(i);
}

// Enumerate style
for (int i = 0; i < list.size(); i++) {
    int val = list.get(i);
}


// 📐 MATH METHODS

Math.abs(x);          // absolute value
Math.min(a, b);       // minimum
Math.max(a, b);       // maximum


// 📎 2D ARRAY TRICKS

// Matrix rotation (90 degrees clockwise)
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

// Flatten matrix
for (int[] row : matrix) {
    for (int val : row) {
        list.add(val);
    }
}


// 🧪 UTILS

// Convert list of strings to joined string
String.join("-", Arrays.asList("a", "b"));  // "a-b"

// StringBuilder for efficient concatenation
StringBuilder sb = new StringBuilder();
sb.append("abc");
sb.reverse();
sb.toString();

// Convert char to int
char c = '3';
int digit = c - '0';


// ⛏️ SET METHODS

Set<Integer> set = new HashSet<>();
set.add(10);
set.contains(10);
set.remove(10);

// Convert array to set
Set<Integer> s = new HashSet<>(Arrays.asList(1,2,3));
