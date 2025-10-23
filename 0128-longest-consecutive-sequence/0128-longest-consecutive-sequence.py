from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        setplce = set(nums)
        mapper = defaultdict(int)
        for i in setplce: 
            if i-1 not in setplce:
                j = i
                while j in setplce:
                    mapper[i] += 1
                    j +=1

        return max(mapper.values())

