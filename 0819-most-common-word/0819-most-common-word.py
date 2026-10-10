from collections import defaultdict
class Solution:
    def mostCommonWord(self, p: str, banned: List[str]) -> str:
        hashb = set(banned)
        p = p.lower()
        cleaned = "".join(char if char.isalnum() else " " for char in p).replace("  "," ").split(" ")
        # print(cleaned)
        clean = [x for x in cleaned if x not in hashb]
        count = Counter(clean)
        del count['']
        counts = sorted(count.items(), reverse=True, key=lambda x: x[1])
        return counts[0][0]


