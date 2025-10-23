class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        # if r == 0:
        #     if nums[0] == target: return 0
        #     else: return -1
            
        while r >= l:
            m = (r+l)//2
            # print(l,m,r)
            if nums[m] == target: return m
            # if the left side sorted?
            if nums[m] >= nums[l]:
                if nums[l] <= target < nums[m]: r = m-1 
                else: l = m+1
            else:
                if nums[m] < target <= nums[r]: l = m + 1
                else: r = m-1
        
        return -1

