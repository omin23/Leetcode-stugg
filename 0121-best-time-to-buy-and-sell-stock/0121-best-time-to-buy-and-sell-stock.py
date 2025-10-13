class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        minp = prices[0]
        for i in range(len(prices)):
            minp = min(prices[i],minp)
            maxp = max(maxp,prices[i] - minp)
        return maxp   
