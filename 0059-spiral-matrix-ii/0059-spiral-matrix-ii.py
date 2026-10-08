class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        mat = [[0 for i in range(n)] for j in range(n)]
        rl = n 
        up = n-1
        cont = 1 
        xval = -1
        yval = 0 
        while cont <= n*n:
            print(cont)
            for i in range(rl): 
                xval += 1
                mat[yval][xval] = cont
                print(xval,yval,cont)
                cont += 1
            rl -=1
            for i in range(up): 
                yval += 1
                mat[yval][xval] = cont
                print(xval,yval,cont)
                cont += 1
            up -=1
            for i in range(rl):
                xval -= 1
                mat[yval][xval] = cont
                print(xval,yval,cont)
                cont += 1
            rl -= 1
            for i in range(up):  
                yval -= 1
                mat[yval][xval] = cont
                print(xval,yval,cont)
                cont += 1
            up -=1
        return mat







            


