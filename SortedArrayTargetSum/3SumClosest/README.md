### The Core Idea: Sort & Squeeze

The most efficient way to solve this is the **Two-Pointer Technique**. Here is the logic:

1.  **Sort the array:** This allows us to move "up" or "down" the number scale predictably.
    
2.  **The Anchor:** Iterate through the array, fixing one number ($nums\[i\]$) as our starting point.
    
3.  **The Squeeze:** For the remaining part of the array, place one pointer at the start (left) and one at the end (right).
    
    *   If the current sum is **too small**, move the left pointer up to increase it.
        
    *   If the current sum is **too large**, move the right pointer down to decrease it.
        
4.  **The Record:** During every step, check if the current sum is closer to the target than your previous "best." If it is, update it.