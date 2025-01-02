class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sec_row = [1]*(n)
        mult = 1
        for i in range(1,n):
            mult *= nums[i-1]
            sec_row[i] = mult
        print(sec_row)
        mult = 1
        for i in range((n-2),-1,-1):
            mult *= nums[i+1]
            sec_row[i] *= mult
        return sec_row




        
        