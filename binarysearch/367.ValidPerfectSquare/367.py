class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        L,R = 1,num

        while L<=R:
            M= L+ ((R-L)//2)
            if M*M == num:
                return True
            elif M*M > num :
                R= M-1
            else:
                L=M+1
        return False