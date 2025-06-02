class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canDo(k):
            return sum((pile +k-1) // k for pile in piles) <= h
        
        L,R=1,max(piles)

        while L<R:
            M= L+ ((R-L)//2)

            if canDo(M):
                R=M
            else:
                L=M+1

        return L