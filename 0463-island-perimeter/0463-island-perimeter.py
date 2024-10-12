class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        overall = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(0,len(grid)): 
            for j in range(0,len(grid[i])):
                if grid[i][j] == 1:
                    sum = 4
                    #up
                    if ((i-1 > -1) and (grid[i-1][j] == 1)):
                        sum = sum - 1
                    #down 
                    if( (i+1 < row) and (grid[i+1][j] == 1)):
                        sum = sum - 1
                    #left
                    if( (j-1 > -1) and (grid[i][j-1] == 1)):
                        sum = sum - 1
                    if( (j+1 < col) and (grid[i][j+1] == 1)):
                        sum = sum - 1
                    print(sum)
                    overall += sum
        return overall