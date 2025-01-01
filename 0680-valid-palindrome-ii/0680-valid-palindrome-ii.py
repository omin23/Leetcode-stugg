class Solution:
    def validPalindrome(self, s: str) -> bool:
        def validP(s:str):
            l,r = 0, len(s)-1
            counter = 0
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        
        
        l,r = 0, len(s)-1
        counter = 0

        while l < r:
            if s[l] != s[r]:
                counter +=1
                if counter > 1:
                    return False
                if s[l] == s[r-1] and s[l+1] == s[r]:
                    Sone = validP(s[l:r])
                    Stwo = validP(s[(l+1):(r+1)])
                    return Sone or Stwo
                elif s[l] == s[r-1]:
                    r-=1
                elif s[l+1] == s[r]:
                    l+=1
                else:
                    return False
            l+=1
            r-=1



        return True 

