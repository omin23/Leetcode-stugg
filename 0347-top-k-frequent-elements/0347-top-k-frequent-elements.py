from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # mapper = Defaultdict(int)
        mapper = {}
        for i in nums: 
            mapper[i] = mapper.get(i,0) + 1
        
        new = (sorted(mapper.items(),key=lambda mappe: mappe[1], reverse =True))
        res = [x[0] for x in new][:k]
        return res


