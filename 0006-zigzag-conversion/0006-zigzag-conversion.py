class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        main = [[] for _ in range(numRows)]
        start = 0 
        change = 1
        for i in range(len(s)):
            main[start].append(s[i])
            if start == 0:
                change = 1
            elif start == numRows-1:
                change = -1
            start += change

        res = ""
        for i in main:
            res += ''.join(i)

        return res