class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) == 2 and s[0] == s[1]: return s
        elif len(s) < 3: return s[0]

        leng = len(s) - 1
        i = 0
        res = ""

        while i < leng:
            l,r = i,i
            while l > -1 and r < len(s) and s[l] == s[r]:
                l,r = l-1,r+1
            if len(res) < r-l: res = s[l+1:r]
            # print(s[l+1:r])
            l,r = i,i+1
            while l > -1 and r < len(s) and s[l] == s[r]:
                l,r = l-1,r+1
            if len(res) < r-l: res = s[l+1:r]
            # print(s[l+1:r])
            i+=1

        return res
        
            

