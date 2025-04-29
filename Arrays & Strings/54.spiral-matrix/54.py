class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ls=[]
        m=len(matrix)
        n=len(matrix[0])
        
        left_wall,right_wall,top_wall,bottom_wall=0,n,0,m

        RIGHT,DOWN,LEFT,UP = 0,1,2,3
        i,j,move=0,0,0

        while (len(ls)<m*n):
            if move==RIGHT:
                while j<right_wall:
                    ls.append(matrix[i][j])
                    j+=1
                top_wall+=1
                i+=1
                j-=1
                move=DOWN
            
            elif move==DOWN:
                while i<bottom_wall:
                    ls.append(matrix[i][j])
                    i+=1
                right_wall-=1
                i-=1
                j-=1
                move=LEFT
            
            elif move==LEFT:
                while j>=left_wall:
                    ls.append(matrix[i][j])
                    j-=1
                j+=1
                bottom_wall-=1
                i-=1
                move=UP
            
            elif move==UP:
                while i>=top_wall:
                    ls.append(matrix[i][j])
                    i-=1
                i+=1
                left_wall+=1
                j+=1
                move=RIGHT
        
        return ls




        