class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        small = strs[0]
        for i in strs[1:]:
            if len(i) < len(small):
                small = i 
        
        # print(small)
        test = ""
        for i in range(0,len(small)):
            test = small[:i+1]
            # print("new", test)
            for j in strs:
                if test != j[:i+1]: 
                    # print(test)
                    return test[:i]

        return test
             

        
    
            
        