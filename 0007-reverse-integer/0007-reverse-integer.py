class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0 

        cur = 1
        start = -1
        flip = 1
        INT_MAX = (2**31) - 1
        INT_MIN = (2**31)
        # print(INT_MAX,INT_MIN)
        if x < 0:
            x = -x
            flip = -1
        
        while x:
            new = x % 10 
            x = x // 10
            if not new and start == -1:continue 
            print(INT_MAX - new)
            if (INT_MAX - new) // 10 < cur: return 0
            if start != -1: cur = cur*10 + new
            else: cur,start = new,0
        
        cur = cur * flip
        return cur

