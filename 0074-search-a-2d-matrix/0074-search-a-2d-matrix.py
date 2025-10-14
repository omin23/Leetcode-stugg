class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrow = len(matrix)
        ncol = len(matrix[0])
        l,r = 0, (nrow * ncol - 1)
        while l <= r:
            m = (r+l)//2
            row , col = m//ncol, m%ncol
            print(matrix[row][col])
            if matrix[row][col] < target: l = m+1
            elif matrix[row][col] > target: r = m-1
            else: return True
            print(m,l,r)
        return False

