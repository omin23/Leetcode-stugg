class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #each row 
        check = set()
        for i in range(9):
            check.clear()
            for j in range(9):
                if board[i][j] in check:
                    return False
                elif board[i][j] != ".":
                    check.add(board[i][j])

        # #each col
        for i in range(9):
            check.clear()
            for j in range(9):
                if board[j][i] in check:
                    return False
                elif board[j][i] != ".":
                    check.add(board[j][i])

        #each 3 by 3
        for col in range(3):
            for row in range(3):
                check.clear()
                for i in range(3):
                    for j in range(3):
                        if board[(3*col) + i][(3*row) + j] in check:
                            return False
                        elif board[(3*col) + i][(3*row) + j] != ".":
                            check.add(board[(3*col) + i][(3*row) + j])
        return True
                        

        