class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lib = set()
        n = len(s)
        ml = l = 0
        for i in range(n):
            if s[i] in lib:
                while s[i] in lib:
                    lib.remove(s[l])
                    l+=1
                lib.add(s[i])
            else:
                lib.add(s[i])
            ml = max(ml,len(lib))
        return ml
            
