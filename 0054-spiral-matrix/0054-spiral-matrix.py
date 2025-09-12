class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l,r = -1,len(matrix[0])
        b,t = 0,len(matrix)
        done = r * t

        res = []
        x,y = 0,0
        print("top:",t,"bottom: ",b,"left: ",l,"right: ",r)
        spiral = False 
        while True: 
            # go right 
            print("spiral")
            if spiral:
                x +=1
            while x != r:
                print(x,y)
                res.append(matrix[y][x])
                x += 1
            x -= 1
            r -=1
            if len(res) == done:
                return res 
            # go down 
            y += 1
            while y != t:
                print(x,y,t)
                res.append(matrix[y][x])
                y +=1
            y -=1
            t -=1
            if len(res) == done:
                return res 
            
            # left 
            x -=1
            while x != l:
                print(x,y)
                res.append(matrix[y][x])
                x -=1
            x +=1
            l +=1
            if len(res) == done:
                return res 
            
            # up 
            y -=1
            while y != b:
                print(x,y)
                res.append(matrix[y][x])
                y -=1
            y +=1
            b +=1
            if len(res) == done:
                return res 
            spiral = True



            # # go right
            # for j in range(width): 
            #     x = j 
            #     res.append(matrix[y][x])
            # width -= 1 
            # height -= 1
            # if len(res) == done:
            #     return res
            # print(res,x,y)
            
            # # go down 
            # for j in range(1,height):
            #     y = j
            #     print(x,y)
            #     res.append(matrix[y][x])
            # height -= 1
            # width -= 1 
            # if len(res) == done:
            #     return res
            # print(res,x,y)

            # # go left 
            # for j in range(width):
            #     x -= 1
            #     res.append(matrix[y][x])
            # width -= 1 
            # if len(res) == done:
            #     return res
            # height -= 1
            # width -= 1 
            # print(res,x,y)
            
            # # go up 
            # for j in range(1,height):
            #     y -= 1
            #     res.append(matrix[y][x])
            # height -= 1
            # width -= 1 
            # if len(res) == done:
            #     return res
            # print(res,x,y)

        return ["huh"]