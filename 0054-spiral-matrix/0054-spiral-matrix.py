class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        sc = 0
        ypos = 0 
        xpos = 0
        ymax = len(matrix)-1
        xmax = len(matrix[0])-1
        total = (ymax+1)*(xmax+1)
        res = []
        res.append(matrix[ypos][xpos])
        while len(res) != total:
            # go accross to the right 
            while xpos < xmax-sc:
                xpos +=1
                res.append(matrix[ypos][xpos])
                if len(res) == total:
                    return res 
            # go down 
            while ypos < ymax-sc:
                ypos += 1
                res.append(matrix[ypos][xpos])
                if len(res) == total:
                    return res 
            # go to the left 
            while xpos > 0+sc:
                xpos -=1
                res.append(matrix[ypos][xpos])
                if len(res) == total:
                    return res 
            # go up 
            while ypos > 1+sc:
                ypos -=1
                res.append(matrix[ypos][xpos])
                if len(res) == total:
                    return res 
            sc+=1
        return res 


        