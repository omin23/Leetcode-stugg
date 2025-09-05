from collections import Counter
# import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       freqk = Counter(nums)
       items = sorted(freqk.items(), key = lambda x: x[1],reverse=True)
       return [items[i][0] for i in range(k)]



