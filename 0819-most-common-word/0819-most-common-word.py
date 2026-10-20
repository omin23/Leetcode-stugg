from collections import Counter
class Solution:
    def mostCommonWord(self, p: str, banned: List[str]) -> str:
        p = re.findall("[a-z]+",p.lower())
        pc = Counter(p)
        for i in banned: del pc[i]
        spc = sorted(pc.items(), reverse=True, key=lambda x: x[1])[0]
        return spc[0]
            

