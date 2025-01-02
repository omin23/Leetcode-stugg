class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        so = len(word1)
        st = len(word2)
        maxl = max(so,st)
        res = "".join(
            (word1[i] if i < so else "") + (word2[i] if i < st else "")
            for i in range(maxl))
        return res


        # def mergeAlternately(self, word1, word2):
        # result = []
        # n = max(len(word1), len(word2))
        # for i in range(n):
        #     if i < len(word1):
        #         result += word1[i]
        #     if i < len(word2):
        #         result += word2[i]

        # return "".join(result)