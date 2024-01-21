class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        d = ""
        for i in s:
            if i.isalnum():
                d = d + i
        
        
        if(len(d) == 1):
            return True
        p1,p2 = 0,len(d)-1
        for j in range(len(d)):
            if(d[p1] == d[p2]):
                p1 += 1
                p2 -= 1
            elif(d[p1] != d[p2]):
                print(1,d[p1])
                print(2,d[p2])
                return False

        return True
                
                
        