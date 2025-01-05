class Solution:
    def isPalindrome(self, s: str) -> bool:
        d = "".join([x for x in s.lower() if x.isalnum()])
        
        if(len(d) == 1):
            return True

        p1,p2 = 0,len(d)-1
        for j in range(len(d)):
            if(d[p1] != d[p2]):
                return False
            else:
                p1 += 1
                p2 -= 1 
        return True
                
                
        