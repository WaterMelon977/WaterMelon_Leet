# Problem Link
[https://leetcode.com/problems/string-compression/](https://leetcode.com/problems/string-compression/)

## Approach

- Use two pointers: one for reading characters and another for writing to overwrite the compressed result.
- For each group of consecutive identical characters, count its frequency.
- Write the character once at the write position.
- If the count > 1, convert count to string and write each digit separately.
- Continue until all characters are processed; return `write` as the new length.

## Why Efficient?

Each character is processed once and written once, achieving in-place compression without extra memory.

## Python Solution
```python
class Solution:
    def compress(self, chars):
        write = 0
        read = 0
        n = len(chars)

        while read < n:
            current_char = chars[read]
            count = 0

            # Count occurrences of the current character
            while read < n and chars[read] == current_char:
                read += 1
                count += 1

            # Write the character
            chars[write] = current_char
            write += 1

            # Write the count if greater than 1
defaults to a string and write each digit separately.
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write
```

## Complexity Analysis 
- **Time:** O(n) — each character is read and written at most once.
- **Space:** O(1) — compression is done in-place without extra structures.