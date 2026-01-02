class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = set()
        nums = sorted(nums)
        leng = len(nums)
        for i in range(leng):
            if i>0 and nums[i] == nums[i-1]: continue
            l,r = i+1,leng-1
            while r>l:
                cur = nums[i] + nums[l] + nums[r]  
                if cur == 0:
                    sol.add(tuple([nums[i],nums[r],nums[l]]))
                    l+=1
                    r-=1
                    while l < r and nums[l-1] == nums[l]: l+=1
                    while l < r and nums[r+1] == nums[r]: r-=1
                elif cur > 0: r-=1
                else: l+=1
        return list(sol)





        
        