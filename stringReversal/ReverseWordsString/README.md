# Deque (Double-Ended Queue) Approach to Reverse Words

Since you're ready to see the **Deque (Double-Ended Queue)** approach, this is actually a very elegant way to solve the problem. Instead of reversing the whole string twice, we build the result word-by-word and "push" each new word to the **front** of our collection.

This naturally reverses the order of the words while keeping the characters within each word in their original order.

## The Deque Strategy

1. **Find the word boundaries:** Use two pointers ($L$ and $R$) to skip leading/trailing spaces.
2. **Extract each word:** Iterate through the string. When you hit a character, start building a word. When you hit a space (or the end of the string), you've finished a word.
3. **Push to the front:** Add that word to the **left** side of your Deque.
4. **Join:** Convert the Deque back into a single string with spaces in between.

---

## The Implementation

```python
from collections import deque

class Solution:
    def reverseWords(self, s: str) -> str:
        L, R = 0, len(s) - 1
        
        # 1. Manually "trim" leading/trailing spaces
        while L <= R and s[L] == ' ':
            L += 1
        while L <= R and s[R] == ' ':
            R -= 1
            
        d = deque()
        word = []
        
        # 2. Iterate through the string
        while L <= R:
            if s[L] != ' ':
                # Build the current word
                word.append(s[L])
            elif word:
                # We hit a space and 'word' isn't empty, 
                # so we finished a word. Push it to the FRONT.
                d.appendleft("".join(word))
                word = []
            L += 1
            
        # 3. Don't forget the very last word!
        if word:
            d.appendleft("".join(word))
            
        # 4. Join with a single space
        return " ".join(d)
```

```python

class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Convert to list and remove extra spaces
        # We use a two-pointer approach to "shift" valid chars to the front
        n = len(s)
        ls = list(s)
        left, right = 0, n - 1
        
        # Manual trim (finding the real start and end)
        while left <= right and ls[left] == ' ': left += 1
        while left <= right and ls[right] == ' ': right -= 1
        
        # Extract words with single spaces
        output = []
        while left <= right:
            if ls[left] != ' ':
                output.append(ls[left])
            elif output[-1] != ' ': # Only add space if the previous char wasn't a space
                output.append(ls[left])
            left += 1
        
        # Step 2: Reverse the entire cleaned list
        self.reverse_range(output, 0, len(output) - 1)
        
        # Step 3: Reverse each individual word
        start = 0
        for end in range(len(output)):
            if output[end] == ' ':
                # Found a word boundary, reverse the word before the space
                self.reverse_range(output, start, end - 1)
                start = end + 1
            elif end == len(output) - 1:
                # Reached the very end, reverse the last word
                self.reverse_range(output, start, end)
                
        return "".join(output)

    def reverse_range(self, ls, i, j):
        """Helper to reverse a portion of the list in-place"""
        while i < j:
            ls[i], ls[j] = ls[j], ls[i]
            i += 1
            j -= 1
```
---

### Why this is a "Pro" Move:
* **One-Pass Logic:** You only traverse the string once ($O(N)$).
* **No Manual Reversals:** By using `appendleft()`, the Deque handles the "reversal" logic for you automatically as you discover words.
* **Space Management:** It inherently handles multiple spaces between words because the `elif word:` block only triggers if you've actually collected characters for a word.

