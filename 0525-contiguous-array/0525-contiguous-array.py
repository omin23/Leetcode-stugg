class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hash = {0:-1}
        t = 0
        maxl = 0
        for i in range(len(nums)):
            if nums[i] == 0: t -= 1
            else: t += 1
            if t in hash.keys(): maxl = max(maxl,i-hash[t])
            else: hash[t] = i
        return maxl
