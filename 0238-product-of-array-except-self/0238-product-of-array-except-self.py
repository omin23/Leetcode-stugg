from collections import Counter 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        # oc = Counter(nums)
        # if oc[0] > 1:
        #     res = [0 for i in range(length)]
        #     return res
        # elif oc[0] == 1: 
        #     res = [0 for i in range(length)]
        #     num = 1
        #     for i in nums: 
        #         if i != 0: 
        #             num *= i
        #     res[nums.index(0)] = num
        #     return res

        res = [1 for i in range(length)]
        pre = 1
        for i in range(1,length):
            pre *= nums[i-1]
            res[i] = pre
        post = 1
        for i in range(length-2,-1,-1):
            post*=nums[i+1]
            res[i] *= post

        return res 








            

    
    
        
        
        
        
        
        
        
        
        
        
        
        # length = len(nums)
        # res = [1] * length
        # # print(res)
        # num_zeros = 0
        # mapped = Counter(nums)

        # # zero_loc = 0
        # # for i in range(length):
        # #     if nums[i] == 0:
        # #         zero_loc = i 
        # #         num_zeros += 1
        
        # if mapped[0] > 1:
        #     return [0] * length
        
        # # if num_zeros == 1:
        # #     total = 1
        # #     for i in nums:
        # #         if i != 0:
        # #             total *= i
        # #     res[zero_loc] = total
        # #     return res

        # for i in range(1,length):
        #     res[i] = res[i-1] * nums[i-1]
        # # print(res)
        # suffix = 1 
        # for i in range(length-1,0,-1):
        #     # print(i)
        #     suffix *= nums[i]
        #     res[i-1] *= suffix
        # # print(res)
        # return res


        