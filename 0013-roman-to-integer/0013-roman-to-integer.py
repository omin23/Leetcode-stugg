class Solution:
    def romanToInt(self, s: str) -> int:
        hash  = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        total = 0 
        for i in range(len(s)-1,-1,-1): 
            total += hash[s[i]]
            print(total)
            if s[i] in ("V","X") and s[i-1] == "I" and i > 0:
                total -=2
            if s[i] in ("L","C") and s[i-1] == "X" and i > 0:
                total -=20
            if s[i] in ("D","M") and s[i-1] == "C" and i > 0:
                total -= 200
        return total 
            
            
        