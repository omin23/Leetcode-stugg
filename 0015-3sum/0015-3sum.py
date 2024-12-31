class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
      
        nums = sorted(nums)
        print(nums)
        res = []
        for i,a in enumerate(nums):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            

            # implement 2 sum 
            l = i+1
            r = len(nums)-1
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r-=1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
            
        return res  
        





        