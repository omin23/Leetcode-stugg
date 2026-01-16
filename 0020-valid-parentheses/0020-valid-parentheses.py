class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) & 0b1: 
            return False 
        d = {")":"(","]":"[","}":"{"}
        check = []
        for i in s:
            if i in d.keys():
                if not check: return False
                if d[i] == check[-1]: check.pop()
                else: return False
            else: check.append(i)
        
        if check: return False
        return True 



        
        
        
        
        
        
        
        # if len(s)%2 ==1: return False
        # cd = {
        #     ')':'(',
        #     '}':'{',
        #     ']':'['
        # }

        # storage = []

        # for i in s: 
        #     if i in cd.keys():
        #         if not storage: return False
        #         if cd[i] == storage[-1]: storage.pop()
        #         else: return False
        #     else: storage.append(i)

        # if not storage: return True
        # return False