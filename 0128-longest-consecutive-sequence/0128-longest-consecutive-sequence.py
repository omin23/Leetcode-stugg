from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        setplce = set(nums)
        longest = 0 
        for i in setplce: 
            if i-1 not in setplce:
                le = 0 
                j = i
                while j in setplce:
                    le += 1
                    j +=1
                longest = max(le,longest)
        return longest

