import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlenm = float("inf")
        l = 0
        total = 0 
        for r in range(len(nums)):
            total += nums[r]
            if total >= target:
                minlenm = min(minlenm,r-l+1)
                while total >= target:
                    minlenm = min(minlenm,r-l+1)
                    total -= nums[l]
                    l +=1
        return (minlenm if (minlenm < float("inf")) else 0)
                



