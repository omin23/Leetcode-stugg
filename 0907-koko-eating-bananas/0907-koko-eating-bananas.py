class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(i,h,piles): return sum([ceil(j/i) for j in piles]) <= h
        maxnum = max(piles)
        l,r = 1,maxnum
        worked = maxnum
        while l <= r: 
            m = (l+r)//2
            # print(m)
            if check(m,h,piles):
                worked = min(worked,m)
                r = m - 1
            else: 
                l = m + 1
        if check(m,h,piles): return m
        return worked



        # new = sorted(piles)
