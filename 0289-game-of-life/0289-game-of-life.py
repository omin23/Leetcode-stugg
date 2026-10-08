class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        for i in range(len(board)):
            for j in range(len(board[0])):
                count = 0 
                for y,x in [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]:
                    cy = i + y 
                    cx = j + x
                    if cy > -1 and cy < len(board) and cx > -1 and cx < len(board[0]):
                        if board[cy][cx] != 0 and board[cy][cx] != 3: count +=1
                print(count)
                if board[i][j]:
                    if count < 2 or count > 3: board[i][j] = -1
                else: 
                    if count == 3: board[i][j] = 3
    
        print(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 3: board[i][j] = 1
                if board[i][j] == -1: board[i][j] = 0
        print(board)



        
        