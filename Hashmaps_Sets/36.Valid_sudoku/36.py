class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size=len(board)


        # checking rows
        for row in board:
            s=set()
            for char in row:
                if char !=".":
                    if char not in s:
                        s.add(char)
                    else:
                        return False
        
        j=0


    # checking coloumns
        while j< size:
            s=set()
            for i in range(size):
                if board[i][j] !=".":
                    if board[i][j] not in s:
                        s.add(board[i][j])
                    else:
                        return False
            j+=1
        
        
        i,j=0,0

        for x,y in [(0,0),(3,0),(6,0),(0,3),(3,3),(6,3),(0,6),(3,6),(6,6)]:
            s=set()
            for j in range(3):
                for i in range(3):
                    if board[x+i][y+j] != ".":
                        if board[x+i][y+j] not in s :
                            s.add(board[x+i][y+j])
                        else:
                            return False
                    
        return True



        
            
        