from typing import List
from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = Counter()
        L = 0
        
        for R in range(len(fruits)):
            count[fruits[R]] += 1
            
            # Notice this is an 'if', not a 'while'!
            if len(count) > 2:
                count[fruits[L]] -= 1
                if count[fruits[L]] == 0:
                    del count[fruits[L]]
                L += 1  # Shift the left pointer once
                
        # The maximum window size is exactly the distance 
        # between L and the end of the array.
        return len(fruits) - L