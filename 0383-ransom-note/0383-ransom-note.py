from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # maglib = defaultdict(int)
        # for i in magazine:
        #     maglib[i] += 1 
        # for i in (ransomNote):
        #     if i not in maglib:
        #         return False 
        #     maglib[i] -= 1 
        #     if maglib[i] == -1:
        #         return False
        # return True 
        countmag = Counter(magazine)
        countran = Counter(ransomNote)
        for i in countran:
            if countran[i] > countmag[i]:
                return False
        return True
