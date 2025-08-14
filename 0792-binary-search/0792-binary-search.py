class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while r >= l:
            mid = (l+r) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else: 
                r = mid - 1

        if len(nums) == 1 and nums[0] == target:
            return 0
        return -1
        