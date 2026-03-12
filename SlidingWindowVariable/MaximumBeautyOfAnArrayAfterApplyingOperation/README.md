# 2779. Maximum Beauty of an Array After Applying Operation

[LeetCode link](https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/)

# LeetCode Link
[Maximum Beauty of an Array After Applying Operation](https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/)

## Approach

- Each element `nums[i]` can be changed to any value in the range `[nums[i] - k, nums[i] + k]`.
- Two elements can become equal if their ranges **overlap**.
- Sort the array so we can analyze ranges in increasing order.
- Use a **sliding window**: if `nums[right] - nums[left] â¤ 2k`, their adjustable ranges overlap and they can be made equal.
- If the difference becomes greater than `2k`, move `left` forward to restore validity.
- Track the maximum window size during traversal.

## Key Insight

Two numbers can be converted to the same value if the distance between them is **at most `2k`**, because each can move by `k`.

## Why efficient

Sorting allows us to apply a linear sliding window instead of comparing every pair of elements.

## Python Solution

```python
def maximumBeauty(self, nums, k):
    nums.sort()
    
    left = 0
    max_beauty = 0
    
    for right in range(len(nums)):
        while nums[right] - nums[left] > 2 * k:
            left += 1
        max_beauty = max(max_beauty, right - left + 1)
    return max_beauty
```

## Explain any tricky part of the code
The condition:
```python
diff = nums[right] - nums[left]
diff <= 2 * k
theoretically ensures that the **adjustment ranges overlap**:

``` 
```python

[nums[left] - k, nums[left] + k]
[nums[right] - k, nums[right] + k]
```
If these intervals overlap, both values can be changed to a **common value**.
Edge-case handling: sorting ensures the window only expands forward and shrinking restores validity efficiently.

## Complexity
- Time: **O(n log n)** â due to sorting; the sliding window itself is `O(n)`.
- Space: **O(1)** â only pointers are used (ignoring sort space).