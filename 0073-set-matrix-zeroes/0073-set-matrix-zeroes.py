class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        xset = set()
        yset = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0: 
                    xset.add(j)
                    yset.add(i)
        print(xset)
        print(yset)
        for x in xset:
            for y in range(len(matrix)):
                matrix[y][x] = 0 
        for y in yset:
            for x in range(len(matrix[0])):
                matrix[y][x] = 0 
        
            

        