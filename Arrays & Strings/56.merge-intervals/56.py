class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<2:
            return intervals
        intervals.sort(key=lambda x: x[0])
        ls=[intervals[0]]
        for interval in intervals[1:]:
            if ls[-1][1] >= interval[0]:
                ls[-1][1] = max(interval[1],ls[-1][1])
            else:
                ls.append(interval)

        return ls 

