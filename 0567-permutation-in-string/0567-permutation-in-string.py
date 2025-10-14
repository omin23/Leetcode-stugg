from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        checker = Counter(s1)
        needed = len(checker)
        ws = len(s1)

        for i in range(len(s2)):
            checker[s2[i]] -= 1
            if checker[s2[i]] == 0: needed -=1
            if i >= ws: 
                checker[s2[i-ws]] += 1
                if checker[s2[i-ws]] == 1:needed +=1
            if needed == 0: return True 
        return False 




        