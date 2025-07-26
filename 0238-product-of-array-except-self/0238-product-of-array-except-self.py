class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [0] * length
        print(res)
        num_zeros = 0
        zero_loc = 0
        for i in range(length):
            if nums[i] == 0:
                zero_loc = i 
                num_zeros += 1
        
        if num_zeros > 1:
            return res
        
        if num_zeros == 1:
            total = 1
            for i in nums:
                if i != 0:
                    total *= i
            res[zero_loc] = total
            return res
        
        total = 1
        for i in range(length):
            total *= nums[i]
        for i in range(length):
            new = total//nums[i]
            # print(i)
            res[i] = new
        return res


        