// JAVA QUICK REVIEW NOTES (For Selected Leetcode Problems)

// 🔤 STRING METHODS

// .charAt(i) - Access character at index
String temp = "abc";
temp.charAt(0);  // 'a'

// .substring(start, end) - Substring from start to end-1
String s = "leetcode";
s.substring(0, 4);  // "leet"

// .equals(str) vs. ==
"abc".equals("abc");  // true

// .toCharArray() - Convert string to character array
char[] arr = s.toCharArray();  // ['l','e','e','t','c','o','d','e']

// .split(delimiter)
String[] parts = "a,b,c".split(",");  // ["a", "b", "c"]

// .toLowerCase(), .toUpperCase()
s.toLowerCase();  // "leetcode"
s.toUpperCase();  // "LEETCODE"

// .contains(), .indexOf(), .startsWith(), .endsWith()
s.contains("lee");  // true
s.indexOf("t");      // 3
s.startsWith("leet");  // true
s.endsWith("code");    // true


// 📚 ARRAY METHODS

// Arrays.sort(arr)
import java.util.Arrays;
int[] nums = {3, 1, 2};
Arrays.sort(nums);  // [1, 2, 3]

// Arrays.copyOfRange(arr, start, end)
int[] sub = Arrays.copyOfRange(nums, 0, 2); // [1, 2]

// Reversing array (manual)
for (int i = 0, j = nums.length - 1; i < j; i++, j--) {
    int tempVal = nums[i];
    nums[i] = nums[j];
    nums[j] = tempVal;
}  // reversed nums: [3, 2, 1]

// Convert List to array
import java.util.*;
List<Integer> list = new ArrayList<>();
list.add(1); list.add(2);
Integer[] a = list.toArray(new Integer[0]);  // [1, 2]


// 📏 LIST METHODS

list.add(10);           // [1, 2, 10]
list.get(0);            // 1
list.set(0, 20);        // [20, 2, 10]
list.remove(0);         // [2, 10]

list.contains(10);      // true
list.indexOf(10);       // 1


// 🧮 MAP / HASHMAP METHODS

import java.util.HashMap;
Map<String, Integer> map = new HashMap<>();

map.put("a", 1);
map.get("a");             // 1
map.getOrDefault("b", 0);  // 0
map.containsKey("a");     // true
map.keySet();              // ["a"]
map.values();              // [1]
map.entrySet();            // [a=1]

// Count frequencies
String example = "aabbc";
for (char c : example.toCharArray()) {
    map.put(String.valueOf(c), map.getOrDefault(String.valueOf(c), 0) + 1);
}  // map: {a=2, b=2, c=1}


// 🧵 ZIP-LIKE & ENUMERATION

String aStr = "abc", bStr = "123";
for (int i = 0; i < Math.min(aStr.length(), bStr.length()); i++) {
    char x = aStr.charAt(i);
    char y = bStr.charAt(i);
    // x and y: (a,1), (b,2), (c,3)
}

for (int i = 0; i < list.size(); i++) {
    int val = list.get(i);  // val = 2, 10
}


// 📐 MATH METHODS

Math.abs(-5);          // 5
Math.min(3, 8);        // 3
Math.max(3, 8);        // 8


// 📎 2D ARRAY TRICKS

// Matrix rotation (90 degrees clockwise)
int[][] matrix = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};
int N = matrix.length;
for (int i = 0; i < N / 2; i++) {
    for (int j = i; j < N - i - 1; j++) {
        int tempVal = matrix[i][j];
        matrix[i][j] = matrix[N - j - 1][i];
        matrix[N - j - 1][i] = matrix[N - i - 1][N - j - 1];
        matrix[N - i - 1][N - j - 1] = matrix[j][N - i - 1];
        matrix[j][N - i - 1] = tempVal;
    }
}  // rotated matrix: {
   //  {7, 4, 1},
   //  {8, 5, 2},
   //  {9, 6, 3}
   //}

// Flatten matrix
List<Integer> flatList = new ArrayList<>();
for (int[] row : matrix) {
    for (int val : row) {
        flatList.add(val);
    }
}  // flatList: [7,4,1,8,5,2,9,6,3]


// 🧪 UTILS

String joined = String.join("-", Arrays.asList("a", "b"));  // "a-b"

StringBuilder sb = new StringBuilder();
sb.append("abc");
sb.reverse();         // "cba"
sb.toString();        // "cba"

char c = '3';
int digit = c - '0';  // 3


// ⛏️ SET METHODS

Set<Integer> set = new HashSet<>();
set.add(10);          // [10]
set.contains(10);     // true
set.remove(10);       // []

Set<Integer> s = new HashSet<>(Arrays.asList(1, 2, 3));  // [1, 2, 3]
