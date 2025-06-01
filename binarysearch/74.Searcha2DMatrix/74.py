class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L=0
        n=len(matrix[0])
        m=len(matrix)
        R=n*m-1


        while L<=R:
            M= L+ ((R-L)//2)
            i= M // n
            j= M % n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] <target:
                L=M+1
            else:
                R=M-1

        return False
