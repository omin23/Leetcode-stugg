class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
    # nlogn meathod,
    #  maybe there is a better way ?   
        # for s in range(len(nums)):
        #     nums[s] *= nums[s]
        # return sorted(nums)
        # res = []
        # l,r = 0,len(nums)-1
        # while l < r:
        #     if abs(nums[l]) > abs(nums[r]):
        #         res.append(nums[l]*nums[l])
        #         l += 1
        #     else:
        #         res.append(nums[r]*nums[r])
        #         r-=1
        # res.append(nums[r]*nums[r])
        # return res[::-1]
        return sorted([i*i for i in nums])


            


    
        