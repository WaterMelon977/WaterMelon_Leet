# 3026. Maximum Good Subarray Sum

[LeetCode link](https://leetcode.com/problems/maximum-good-subarray-sum/)

# LeetCode Link
[https://leetcode.com/problems/maximum-good-subarray-sum/](https://leetcode.com/problems/maximum-good-subarray-sum/)

## Approach

- A subarray is **good** if `|nums[i] - nums[j]| = k` for the **first and last elements** of the subarray.
- Let `prefix_sum[i]` be the sum of elements up to index `i`.
- For a subarray ending at index `r`, we want a previous index `l` such that `nums[l] = nums[r] Â± k`.
- The subarray sum from `l..r` is `prefix[r] - prefix[l] + nums[l]`.
- To maximize this, store the **minimum prefix sum before each value** in a hashmap.
- For each `nums[r]`, check if `nums[r] - k` or `nums[r] + k` exists in the map and compute candidate sums.
- Update the map with the smallest prefix sum seen for the current value.

## Key Insight

Fix the **right endpoint** and search for a previous element whose value differs by `k`. Using **prefix sums + hashmap**, we can compute the best subarray sum in constant time.

## Why efficient

Instead of checking every pair of indices (`O(nÂ²)`), we reduce the search to **constant-time lookups** using a hashmap.

## Python Solution
```python
def maximumSubarraySum(self, nums, k):
    prefix = 0
    best_prefix = {}
    ans = float('-inf')
    
    for num in nums:
        prefix += num
        
        if num - k in best_prefix:
            ans = max(ans, prefix - best_prefix[num - k])
        
        if num + k in best_prefix:
            ans = max(ans, prefix - best_prefix[num + k])
        
        if num not in best_prefix:
            best_prefix[num] = prefix - num
        else:
            best_prefix[num] = min(best_prefix[num], prefix - num)
    
    return ans if ans != float('-inf') else 0
```

## Explain any tricky part of the code
The value stored in the hashmap is:
```plaintext
prefix_before_index = prefix - num
```
This represents the **prefix sum just before the subarray starts**, allowing us to compute:
```plaintext
subarray_sum = prefix[r] - prefix_before_l
```
Edge-case handling: if no valid good subarray exists, the answer remains `-inf`, so we return `0`.

## Complexity
- Time: **O(n)** â one pass through the array with constant-time hashmap operations.
- Space: **O(n)** â hashmap stores prefix information for seen values.