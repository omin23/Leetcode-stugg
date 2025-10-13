import math 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False 
        if x == 0 or (math.floor(math.log10(x)) + 1) == 1: return True 

        # chopdisthalf = math.log10(x) // 2
        # top  = x // (10 ** chopdisthalf) 
        # bottom = x - top * (10 ** chopdisthalf)
        # print(top, bottom)
        nulen = math.ceil(math.log10(x)) 
        newnum = -1
        grind = x
        # print(nulen)
        for i in range(nulen):
            get = grind % 10
            grind = grind // 10 
            # print(grind,get)

            if newnum == -1:
                if get != 0: newnum = get
                else: return False
            else:    
                newnum = newnum * 10 + get
        
        return newnum == x



