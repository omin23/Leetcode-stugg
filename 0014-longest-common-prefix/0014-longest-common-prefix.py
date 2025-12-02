class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        small = strs[0]
        for i in strs[1:]:
            if len(i) < len(small):
                small = i 
        
        # print(small)
        for i in strs: 
            while not i.startswith(small):
                small = small[:-1]
                if not small: return ""
        return small
             

        
    
            
        