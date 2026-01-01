from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        nums = list(check)
        mlen = 0 
        llen = len(check)
        i = 0 
        while i < llen: 
            if nums[i]-1 not in check: 
                tlen = 0
                new = nums[i]
                while new in check: 
                    tlen += 1
                    new += 1
                mlen = max(mlen,tlen)
            i += 1
        return mlen



