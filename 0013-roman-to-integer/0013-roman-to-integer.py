class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0 
        def get(s):
            match s:
                case "M": 
                    return 1000
                case "D": 
                    return 500
                case "C": 
                    return 100 
                case "L": 
                    return 50 
                case "X": 
                    return 10 
                case "V": 
                    return 5
                case "I": 
                    return 1
            return 0 
        skip = False
        for i in range(len(s)):
            if skip == True:
                skip = False
                continue

            if s[i] == "I" and i < len(s)-1:
                if s[i+1] == "V": 
                    res += 4
                    skip = True
                elif s[i+1] == "X":
                    res += 9
                    skip = True
                else:
                    res += get(s[i])
        
            elif s[i] == "X" and i < len(s)-1:
                if s[i+1] == "L": 
                    res += 40
                    skip = True
                elif s[i+1] == "C":
                    res += 90
                    skip = True
                else:
                    res += get(s[i])
            elif s[i] == "C" and i < len(s)-1:
                if s[i+1] == "D": 
                    res += 400
                    skip = True
                elif s[i+1] == "M":
                    res += 900  
                    skip = True 
                else:
                    res += get(s[i])
            else:
                res += get(s[i])
        return res 