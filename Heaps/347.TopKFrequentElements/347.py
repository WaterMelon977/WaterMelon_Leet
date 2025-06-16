class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=Counter(nums)
        heap=[]
        for (key,freq) in counter.items():
            if len(heap)<k:
                heapq.heappush(heap,(freq,key))
            else:
                heapq.heappushpop(heap,(freq,key))
        print(heap)

        stk=[]
        while heap:
            (freq,key)=heapq.heappop(heap)
            stk.append(key)
        return stk
    

'''

⏱️ Time Complexity Breakdown
Let:

n = number of elements in nums

m = number of unique elements in nums

k = number of top frequent elements to return

1. Counter(nums)
Time: O(n)
→ Single pass to count each element.

2. Heap Construction
python
Copy
Edit
for (key, freq) in counter.items():
You're iterating over m unique elements.

In each iteration:

Heap operation (heappush or heappushpop) = O(log k) (since heap size is at most k).

Total Time: O(m x log k)

Note: You maintain the heap size at k, not more. So heap operations stay fast.

3. Heap Pop to Result
python
Copy
Edit
while heap:
    stk.append(heapq.heappop(heap)[1])
You pop k elements from the heap.

Each pop = O(log k)

Total Time: O(k x log k)

 Total Time Complexity
plaintext
Copy
Edit
O(n)             # for Counter
+ O(m x log k)   # for heap insertion
+ O(k x log k)   # for extracting k elements
🔍 Simplified:
If m ≈ n (e.g., all elements are unique):
⟶ O(n log k)

If k is small, then:
⟶ Dominated by O(n)

📦 Space Complexity
Counter: O(m)

heap: O(k)

stk (result): O(k)

→ Total: O(m + k)

'''


from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = Counter(nums)
        buckets = [0] * (n + 1)
 
        for num, freq in counter.items():
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)
        
        ret = []
        for i in range(n, -1, -1):
            if buckets[i] != 0:
                ret.extend(buckets[i])
            if len(ret) == k:
                break
        
        return ret
 
# Time Complexity: O(n)
# Space Complexity: O(n)