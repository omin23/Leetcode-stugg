import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == (0):
            return 0
        elif len(stones) == 1:
            return stones[0]
        
        stones = [-i for i in stones]
        
        heapq.heapify(stones)
        while len(stones) > 1:
            max1 = heapq.heappop(stones)
            max2 = heapq.heappop(stones)
            n = abs(max1 - max2)
            if n != 0:
                heappush(stones, -n)

        if len(stones) == (0):
            return 0
        return -stones[0]


