import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = math.inf
        value = 0 
        l = 0 
        for i in range(len(nums)): 
            value += nums[i]
            while value >= target and l <= i:
                length = min(length,i-l+1) 
                value -= nums[l]
                l += 1
        if value >= target: length = min(length,i-l+1)
        if length == math.inf: return 0 
        return length
