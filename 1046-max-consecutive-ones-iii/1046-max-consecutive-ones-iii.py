class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        tz = 0 
        maxl = 0 
        goal = len(nums)
        for r in range(goal): 
            if nums[r] == 0:
                tz += 1

            while tz > k:
                if nums[l] == 0:
                    tz -=1
                l+=1

            cur = r - l + 1    
            maxl = max(maxl,cur)
        return maxl


            
