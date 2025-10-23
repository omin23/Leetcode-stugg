class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        smallest = float("inf") 
        while r >= l:
            if nums[l] < nums[r]: return nums[l]
            m = (r+l)//2
            smallest = min(nums[m],smallest)
            # print(nums[m])
            if nums[m] >= nums[l]: l = m+1
            else: r = m 

        return smallest