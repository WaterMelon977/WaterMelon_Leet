from collections import Counter

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        result = []

        for i in range(n - k + 1):

            if i == 0:
                freq = Counter(nums[:k])
            else:
                # add new element entering window
                freq[nums[i+k-1]] += 1

                # remove element leaving window
                freq[nums[i-1]] -= 1
                if freq[nums[i-1]] == 0:
                    del freq[nums[i-1]]

            # sort by frequency desc, value desc
            sorted_items = sorted(freq.items(), key=lambda item: (-item[1], -item[0]))

            total = 0
            count = 0

            for value, f in sorted_items:
                total += value * f
                count += 1
                if count == x:
                    break

            result.append(total)

        return result