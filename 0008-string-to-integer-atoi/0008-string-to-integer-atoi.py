class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        flipper = 1
        start = -1
        res = 0
        i = 0
        MAX_INT = 2**31 -1
        MIN_INT = -2**31

        if not s:
            return 0

        if s[0] == "-" : i,flipper = 1, -1
        elif s[0] == "+": i = 1

        while i < len(s) and s[i].isdigit():
            new = int(s[i])
            i += 1
            if start == -1 and new == 0:continue
            elif start == -1 and new !=0:res,start = new,1
            else: res = res*10 + new
        res = res * flipper

        if MAX_INT < res:
            res = MAX_INT
        elif res < MIN_INT:
            res = MIN_INT

        return res



        