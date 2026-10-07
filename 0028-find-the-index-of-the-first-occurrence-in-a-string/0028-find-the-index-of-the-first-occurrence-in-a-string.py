class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack): return -1
        hashs = {needle}
        check = len(haystack) - len(needle) +1
        for i in range(0,check):
            if haystack[i:(i+len(needle))] in hashs: return i 
        return -1