class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        lib = {}
        jlen = len(jewels)
        slen = len(stones)

        for i in range(slen):
            lib[stones[i]] = lib.get(stones[i], 0) + 1
        total = 0 
        for i in range(jlen):
            total += lib.get(jewels[i],0)

        return total 