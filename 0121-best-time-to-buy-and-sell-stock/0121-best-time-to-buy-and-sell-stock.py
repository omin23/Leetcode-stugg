class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0 
        p1,p2 = 0,1
        maxl = len(prices)
        while p2 < maxl:
            if prices[p1] < prices[p2]:
                maxp = max(maxp , prices[p2] - prices[p1])
            else:
                p1 = p2
            p2 +=1
        return maxp
                
            

