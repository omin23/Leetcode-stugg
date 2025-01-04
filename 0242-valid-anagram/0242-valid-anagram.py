from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
                return False

        cs = Counter(s)
        ct = Counter(t)
        if cs != ct:
            return False 
        return True 