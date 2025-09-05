from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        scounter = Counter(s)
        tcounter = Counter(t)
        return scounter == tcounter

