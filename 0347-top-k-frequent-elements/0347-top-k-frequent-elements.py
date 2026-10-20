from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        listed = sorted(count.items(), reverse=True, key=lambda x: x[1])[:k]
        return [i[0] for i in listed]
        


