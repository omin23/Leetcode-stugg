class Solution:
    def validPalindrome(self, s: str) -> bool:
                
        l,r = 0, len(s)-1
        counter = 0

        while l < r:
            if s[l] != s[r]:
                counter +=1
                if counter > 1:
                    return False
                if s[l] == s[r-1] and s[l+1] == s[r]:
                    skipL = s[l:r]
                    skipR = s[(l+1):(r+1)]
                    return skipL == skipL[::-1] or skipR == skipR[::-1]
                elif s[l] == s[r-1]:
                    r-=1
                elif s[l+1] == s[r]:
                    l+=1
                else:
                    return False
            l+=1
            r-=1



        return True 

