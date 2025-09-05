from collections import Counter
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # s = Counter(nums)
        length = len(nums)
        # res = [0] * length
        # if s[0] > 1:
        #     return res
        # elif s[0] == 1:
        #     total = 1
        #     for i in range(length):
        #         if nums[i] != 0:
        #             total *= nums[i]
        #         else:
        #             idz = i
        #     res[idz] = total
        #     return res
        # # no 0's
        res = [1] * length
        for i in range(1,length):
            res[i] *= nums[i-1] * res[i-1]
        runner = 1
        for i in range(length-2,-1,-1):
            runner *= nums[i+1]
            res[i] *= runner
        return res
        











        
        