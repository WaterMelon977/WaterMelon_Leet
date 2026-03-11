# 2461. Maximum Sum of Distinct Subarrays With Length K

[LeetCode link](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/)

### Problem

Find the **maximum sum of a subarray of length `k` where all elements are distinct**.

---

### Idea

We use a **sliding window** that always maintains two conditions:

1. The window contains **only distinct elements**.
2. The window size is **at most `k`**.

A **set** (`seen`) is used to track elements currently inside the window.

When adding a new element would violate either condition (duplicate element or window exceeding size `k`), we **shrink the window from the left** until it becomes valid again.

While maintaining the window, we also track the **running sum** of elements inside it.

Whenever the window size becomes exactly `k`, we update the maximum sum.

---

### Algorithm Steps

1. Initialize:
   - `seen` â set to track elements in the window
   - `L` â left pointer of the window
   - `total` â running sum of the window
   - `max_sum` â result
2. Expand the window using pointer `R`.
3. Before adding `nums[R]`, shrink the window while:
   - The element already exists in the window, or
   - The window size would exceed `k`.
4. During shrinking:
   - remove `nums[L]` from the set
   - subtract it from the running sum
   - move `L` forward.
5. Add the new element to the window:
   - insert into `seen`
   - update `total`.
6. If the window size equals `k`, update `max_sum`.
7. Continue until the array is fully processed.

---

### Key Invariant
The window **always satisfies**:
- No duplicate elements 
- Window size â¤ k  
This guarantees that any window of size `k` automatically contains **distinct elements**.

---

### Code 
def maximumSubarraySum(self, nums: list[int], k: int) -> int:
def maximumSubarraySum(self, nums: list[int], k: int) -> int:
def maximumSubarraySum(self, nums: list[int], k: int) -> int:
def maximumSubarraySum(self, nums: list[int], k: int) -> int: