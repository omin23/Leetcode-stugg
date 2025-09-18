class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        counter = 0
        h,w = len(mat),len(mat[0])
        total = h * w
        res = [] 
        cx, cy = 0,0
        test = (cy,cx)
        i = 0 
        while i < total: 
            i += 1
            # go up right
            while (0 <= test[0] and test[0] < h) and (0 <= test[1] and test[1] < w):
                cy , cx = test
                counter += 1
                # print(mat[cy][cx], test,counter)
                res.append(mat[cy][cx])
                test = (cy-1,cx+1)
            test = (test[0]+1,test[1]-1)
            # print("cor: ",test)
            # check right then down
            if counter == total: 
                return res

            if ((test[1] + 1) < w):
                test = (test[0],test[1]+1)
            else: 
                test = (test[0]+1,test[1])

            # print("up to down",test)

            # go down left
            while (0 <= test[0] and test[0] < h) and (0 <= test[1] and test[1] < w):
                cy , cx = test
                counter += 1
                res.append(mat[cy][cx])
                # print(mat[cy][cx],test,counter)
                test = (cy+1,cx-1)
            
            test = (test[0]-1,test[1]+1)
            # check down then right
            if counter == total: 
                return res

            if ((test[0] + 1) < h): 
                test = (test[0]+1,test[1])
            else: 
                test = (test[0],test[1]+1)

    
        return res