from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        res = 0
        count = l = 0
        for r in range(len(s)):
            d[s[r]] += 1
            count = max(count,d[s[r]])
            while (r-l+1) - count > k:
                d[s[l]] -= 1
                l +=1
            res = max(res, r-l+1)
        return res