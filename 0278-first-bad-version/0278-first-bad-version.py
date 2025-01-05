# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r = 0, n
        if n == 1:
            return n
        while l < r:
            m = (l+r)//2
            if isBadVersion(m) == True:
                r = m
            else:
                l = m+1   
        return l


        