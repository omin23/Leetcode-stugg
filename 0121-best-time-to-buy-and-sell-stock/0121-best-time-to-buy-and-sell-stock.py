class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0 
        p1,p2 = 0,0
        maxl = len(prices) - 1
        while p2 != maxl:
            p2 +=1
            if prices[p1] < prices[p2]:
                curmax = prices[p2] - prices[p1]
                if curmax > maxp:
                    maxp = curmax
            # elif prices[p1] > prices[p2]:
            else:
                p1 = p2
        
        return maxp
                
            

