class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r =0, len(nums)-1
        while l < r:
            m = (l+r)//2
            print(l,m,r)
            if nums[m] > target:
                r = m
            elif nums[m] < target:
                l = m + 1
            elif nums[m] == target:
                return m
        m = (l+r)//2
        if m == len(nums)-1:
            if target <= nums[len(nums)-1]:
                return m
            else:
                return len(nums)
        return m 