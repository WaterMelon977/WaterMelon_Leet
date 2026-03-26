"""
LeetCode #542: 01 Matrix

https://leetcode.com/problems/01-matrix/
"""

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i,j))
                else :
                    mat[i][j] = float('inf')
        directions = [(1,0),(-1,0),(0,1),(0,-1)]


        while queue:
            i,j = queue.popleft()
            for di , dj in directions:
                ni,nj = i+di, j+dj
                if  0 <= ni< rows and 0 <= nj < cols and  mat[ni][nj] > mat[i][j] + 1:
                    mat[ni][nj] = mat[i][j] + 1
                    queue.append((ni,nj))
        return mat

            

                

        

        