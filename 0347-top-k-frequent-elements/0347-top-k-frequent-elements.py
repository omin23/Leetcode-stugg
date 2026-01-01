from collections import defaultdict, Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        listed = sorted(count.items(), key=lambda item: item[1], reverse=True)[:k]
        return [i[0] for i in listed]


