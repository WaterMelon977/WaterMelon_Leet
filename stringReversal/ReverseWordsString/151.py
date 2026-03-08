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