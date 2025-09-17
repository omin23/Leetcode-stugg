class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        length = len(s) 
        if not length:
            return 0
        seen = set()
        maxi = 1
        while r != length:
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
            else:
                maxi = max(maxi,len(seen))
                while s[r] in seen:
                    # print(r,l)
                    seen.remove(s[l])
                    l +=1

        maxi = max(maxi,len(seen))
        return maxi
                

