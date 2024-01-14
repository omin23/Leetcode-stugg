class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
                return False
        s,t = sorted(s),sorted (t)
        for i in range(len(t)):
            if s[i] != t[i]:
                return False
        return True 