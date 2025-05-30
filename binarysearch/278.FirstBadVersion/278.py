# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        L,R = 0,n-1
        while L<=R:
            M= L+ ((R-L)//2)
            if isBadVersion(M) :
                R=M-1
            else:
                L=M+1
        return M if isBadVersion(M) else M+1
        