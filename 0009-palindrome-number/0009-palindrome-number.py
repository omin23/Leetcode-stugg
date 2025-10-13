import math 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False 
        if x == 0 or (math.floor(math.log10(x)) + 1) == 1: return True 

        # chopdisthalf = math.log10(x) // 2
        # top  = x // (10 ** chopdisthalf) 
        # bottom = x - top * (10 ** chopdisthalf)
        # print(top, bottom)

        nulen = math.ceil(math.log10(x)) // 2
        newnum = 0
        # print(nulen)
        for i in range(nulen):
            get = x % 10
            x //= 10 
            newnum = newnum * 10 + get
        print(newnum)
        
        return newnum == x  or x//10 == newnum



